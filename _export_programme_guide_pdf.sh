#!/usr/bin/env bash
# Regenerate the Student Programme Guide PDF from the HTML source.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PROFILE="$(mktemp -d /tmp/chrome-guide-XXXXXX)"
cleanup() { rm -rf "$PROFILE"; }
trap cleanup EXIT
google-chrome \
  --headless=new \
  --disable-gpu \
  --no-first-run \
  --no-default-browser-check \
  --user-data-dir="$PROFILE" \
  --no-pdf-header-footer \
  --virtual-time-budget=20000 \
  --print-to-pdf="$ROOT/complete-software-testing-student-programme-guide.pdf" \
  "file://$ROOT/complete-software-testing-student-programme-guide.html"
ls -la "$ROOT/complete-software-testing-student-programme-guide.pdf"
