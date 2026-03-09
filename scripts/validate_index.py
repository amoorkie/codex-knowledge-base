from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "index.yaml"
CONTENT_DIRS = {
    "ai",
    "backend",
    "community",
    "data",
    "databases",
    "devops",
    "frontend",
    "security",
    "testing",
}
REQUIRED_METADATA_FIELDS = {
    "priority": {"high", "medium", "low"},
    "scope": {"core", "advanced", "operations", "security", "workflow", "ecosystem"},
    "stability": {"high", "medium", "low"},
    "trust": {"official", "spec", "reference", "community", "mixed"},
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("index.yaml must parse to a mapping")
    return data


def validate_top_level(data: dict, errors: list[str]) -> None:
    version = data.get("version")
    if not isinstance(version, int):
        errors.append("`version` must be an integer")

    updated = data.get("updated")
    if isinstance(updated, dt.date):
        pass
    elif isinstance(updated, str) and DATE_RE.match(updated):
        pass
    else:
        errors.append("`updated` must be a date or a string in YYYY-MM-DD format")

    metadata_fields = data.get("metadata_fields")
    if not isinstance(metadata_fields, dict):
        errors.append("`metadata_fields` must be a mapping")
        return

    for field_name, allowed_values in REQUIRED_METADATA_FIELDS.items():
        field = metadata_fields.get(field_name)
        if not isinstance(field, dict):
            errors.append(f"`metadata_fields.{field_name}` must be a mapping")
            continue
        values = field.get("values")
        if not isinstance(values, list) or set(values) != allowed_values:
            errors.append(
                f"`metadata_fields.{field_name}.values` must be {sorted(allowed_values)}"
            )


def validate_sections(data: dict, errors: list[str]) -> set[str]:
    sections = data.get("sections")
    if not isinstance(sections, list):
        errors.append("`sections` must be a list")
        return set()

    indexed_paths: set[str] = set()
    section_names: set[str] = set()

    for section_index, section in enumerate(sections, start=1):
        if not isinstance(section, dict):
            errors.append(f"Section #{section_index} must be a mapping")
            continue

        name = section.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"Section #{section_index} must have a non-empty `name`")
        elif name in section_names:
            errors.append(f"Duplicate section name `{name}`")
        else:
            section_names.add(name)

        files = section.get("files")
        if not isinstance(files, list):
            errors.append(f"Section `{name}` must have a `files` list")
            continue

        for file_index, item in enumerate(files, start=1):
            if not isinstance(item, dict):
                errors.append(f"Section `{name}` file #{file_index} must be a mapping")
                continue

            path_value = item.get("path")
            if not isinstance(path_value, str) or not path_value.endswith(".md"):
                errors.append(f"Section `{name}` file #{file_index} has invalid `path`")
                continue

            if path_value in indexed_paths:
                errors.append(f"Duplicate indexed path `{path_value}`")
            indexed_paths.add(path_value)

            path = ROOT / path_value
            if not path.exists():
                errors.append(f"Indexed file does not exist: `{path_value}`")

            topics = item.get("topics")
            if not isinstance(topics, list) or not topics or not all(
                isinstance(topic, str) and topic for topic in topics
            ):
                errors.append(f"`topics` must be a non-empty list of strings for `{path_value}`")

            for field_name, allowed_values in REQUIRED_METADATA_FIELDS.items():
                value = item.get(field_name)
                if value not in allowed_values:
                    errors.append(
                        f"`{field_name}` for `{path_value}` must be one of {sorted(allowed_values)}"
                    )

    return indexed_paths


def find_unindexed_markdown(indexed_paths: set[str]) -> list[str]:
    unindexed: list[str] = []
    for directory in sorted(CONTENT_DIRS):
        for path in sorted((ROOT / directory).glob("*.md")):
            relative = path.relative_to(ROOT).as_posix()
            if relative not in indexed_paths:
                unindexed.append(relative)
    return unindexed


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate index.yaml structure and coverage.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if content markdown files exist outside index.yaml coverage.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = load_yaml(INDEX_PATH)
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: failed to parse {INDEX_PATH.name}: {exc}")
        return 1

    validate_top_level(data, errors)
    indexed_paths = validate_sections(data, errors)

    unindexed = find_unindexed_markdown(indexed_paths)
    if unindexed:
        message = "Unindexed markdown files: " + ", ".join(unindexed)
        if args.strict:
            errors.append(message)
        else:
            warnings.append(message)

    if errors:
        print("Index validation failed:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")
        return 1

    print("Index validation passed.")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
