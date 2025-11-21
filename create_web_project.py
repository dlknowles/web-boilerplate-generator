from __future__ import annotations

import sys
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "templates" / "base"
VERSION = "0.1.0"


def create_web_project(project_name: str) -> None:
    target_dir = ROOT / project_name

    if target_dir.exists():
        raise FileExistsError(f"Target directory already exists: {target_dir}")

    # Copy all template files
    shutil.copytree(TEMPLATE_DIR, target_dir)

    # Replace tokens in key files
    project_title = project_name.replace("-", " ").title()

    replacements = {
        "__PROJECT_NAME__": project_name,
        "__PROJECT_TITLE__": project_title,
    }

    def replace_tokens(path: Path) -> None:
        text = path.read_text(encoding="utf-8")
        for token, value in replacements.items():
            text = text.replace(token, value)
        path.write_text(text, encoding="utf-8")

    for rel in ["package.json", "index.html", "src/main.ts"]:
        file_path = target_dir / rel
        if file_path.exists():
            replace_tokens(file_path)

    print(f"Created web project at: {target_dir}")
    print("Next steps:")
    print(f"  cd {project_name}")
    print("  npm install")
    print("  npm run dev")


def main(argv: list[str] | None = None) -> None:
    print(f"web-boilerplate-generator v{VERSION}")
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python create_web_project.py <project-name>")
        sys.exit(1)

    create_web_project(argv[0])


if __name__ == "__main__":
    main()
