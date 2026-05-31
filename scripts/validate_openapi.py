from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml


HTTP_METHODS = {"get", "post", "put", "delete", "patch", "options", "head", "trace"}


def fail(message: str) -> None:
    print(f"openapi validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    spec_path = Path("openapi.yaml")
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))

    if spec.get("openapi") != "3.1.0":
        fail("expected OpenAPI 3.1.0")

    paths = spec.get("paths")
    if not isinstance(paths, dict) or not paths:
        fail("paths must be a non-empty object")

    operation_ids: list[str] = []

    for path, path_item in paths.items():
        declared_path_params = set(re.findall(r"{([^}]+)}", path))

        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue

            location = f"{method.upper()} {path}"
            operation_id = operation.get("operationId")
            if not operation_id:
                fail(f"{location} is missing operationId")

            operation_ids.append(operation_id)

            responses = operation.get("responses")
            if not isinstance(responses, dict) or not responses:
                fail(f"{location} is missing responses")

            path_params = {
                parameter.get("name")
                for parameter in operation.get("parameters", [])
                if parameter.get("in") == "path"
            }
            if path_params != declared_path_params:
                fail(f"{location} path params mismatch: expected {declared_path_params}, got {path_params}")

    duplicates = sorted({item for item in operation_ids if operation_ids.count(item) > 1})
    if duplicates:
        fail(f"duplicate operationId values: {', '.join(duplicates)}")

    print(f"OK: {len(paths)} paths, {len(operation_ids)} operations")


if __name__ == "__main__":
    main()
