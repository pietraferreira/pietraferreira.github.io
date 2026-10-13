#!/usr/bin/env bash
# Sync the Machi vault into content/, then commit and push if anything changed.
# Pushing quartz-v5 triggers the GitHub Pages deploy workflow.
set -euo pipefail
cd "$(dirname "$0")/.."

git pull --ff-only --quiet origin quartz-v5
python3 scripts/sync-vault.py
git add content
if git diff --cached --quiet; then
  echo "nothing to publish"
  exit 0
fi
git commit --quiet -m "Sync vault $(date +%F)"
git push --quiet origin quartz-v5
echo "published: $(git log -1 --format=%h)"
