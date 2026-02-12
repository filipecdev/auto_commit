#!/usr/bin/env python3
import subprocess
import os
import sys
from datetime import datetime

COMMIT_MSG_PREFIX = "Auto-commit"

def run_git_command(repo_path, command):
    return subprocess.run(
        command,
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def main():
    if len(sys.argv) < 2:
        print("Uso: auto_commit.py <caminho_do_repositorio>")
        sys.exit(1)

    repo_path = sys.argv[1]

    if not os.path.isdir(repo_path):
        print(f"Diretório inválido: {repo_path}")
        sys.exit(1)

    status = run_git_command(repo_path, ["git", "status", "--porcelain"])

    if not status.stdout.strip():
        # Nenhuma alteração
        return

    run_git_command(repo_path, ["git", "add", "."])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"{COMMIT_MSG_PREFIX} - {timestamp}"

    commit = run_git_command(
        repo_path,
        ["git", "commit", "-m", commit_message]
    )

    if commit.returncode != 0:
        print(commit.stderr)

    run_git_command(repo_path, ["git", "push"])

if __name__ == "__main__":
    main()
