#!/usr/bin/env bash
# Regenerate the Instructor Guide PDF from the HTML source.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PROFILE="$(mktemp -d /tmp/chrome-instructor-guide-XXXXXX)"
cleanup() { rm -rf "$PROFILE"; }
trap cleanup EXIT
timeout 90 google-chrome \
  --headless=new \
  --disable-gpu \
  --no-first-run \
  --no-default-browser-check \
  --user-data-dir="$PROFILE" \
  --no-pdf-header-footer \
  --virtual-time-budget=20000 \
  --print-to-pdf="$ROOT/complete-software-testing-instructor-guide.pdf" \
  "file://$ROOT/complete-software-testing-instructor-guide.html" || true
# Chrome sometimes hangs after writing PDF; accept success if file exists and is non-trivial
test -s "$ROOT/complete-software-testing-instructor-guide.pdf"
ls -la "$ROOT/complete-software-testing-instructor-guide.pdf"
