#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
report_date=${1:-$(date +%F)}

cd "$script_dir"
git add -- data.json

if git diff --cached --quiet -- data.json; then
  echo "No data.json changes to push."
  exit 0
fi

git commit -m "sync: ${report_date} 最新数据"
git push origin main
