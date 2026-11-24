import os
from pathlib import Path

dir_paths=[
    Path("app/__init__.py"),
    Path("app/main.py"),
    Path("app/config.py"),
    Path("app/dependencies.py"),
    "applications/",
    "agents/",
    "tools/",
    "incident/",
    "rag/",
    "memory/",
    "database/",
    "api/",
    "evaluation/",
    "frontend/",
    "knowledge/",
    "infrastructure/",
    "tests/",
    "scripts/",
    ".env.example",
]


for path in dir_paths:
    dir,file_name = os.path.split(path)

    if dir:
        os.makedirs(dir,exist_ok=True)

    if file_name:
        file_path = os.path.join(dir,file_name)
        open(file_path,'a').close
