# update_changelog.py

import subprocess
import sys
import re
from datetime import datetime

README_PATH = "README.md"

def append_to_changelog(message):
    """Append a new changelog entry to the README.md."""
    version_match = re.search(r"v(\d+\.\d+)", message)
    if not version_match:
        print("❌ Commit message must contain a version like v1.12")
        sys.exit(1)

    version = version_match.group(1)
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"### v{version} ({date_str})\n- {message.strip()}\n\n"

    with open(README_PATH, "r") as file:
        content = file.read()

    # Insert new entry after "## Change Log"
    pattern = r"(## Change Log\n\n)"
    if new_entry in content:
        print("⚠️ Changelog entry already exists.")
        return

    updated_content = re.sub(pattern, r"\1" + new_entry, content)

    with open(README_PATH, "w") as file:
        file.write(updated_content)

    print(f"✅ Added changelog entry for version {version}.")

def commit_and_push(commit_message):
    """Stage all, commit, and push to origin main."""
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("🚀 Changes committed and pushed to origin main.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_changelog.py \"v1.12 your commit message here\"")
        sys.exit(1)

    commit_message = sys.argv[1]
    append_to_changelog(commit_message)
    commit_and_push(commit_message)

if __name__ == "__main__":
    main()