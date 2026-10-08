#!/usr/bin/env bash
# Download the roster of one day and register its students.
# Usage: bash scripts/daily_roster.sh [YYYY-MM-DD]     (default: yesterday)
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -f .env ]]; then
    set -a
    # shellcheck disable=SC1091
    source .env
    set +a
fi

: "${ROSTER_URL:?ROSTER_URL is not set (see .env.example)}"
: "${ROSTER_TOKEN:?ROSTER_TOKEN is not set (see .env.example)}"

# GNU date (Linux, Git Bash) and BSD date (macOS) spell "yesterday" differently.
day="${1:-$(date -d yesterday +%F 2>/dev/null || date -v-1d +%F)}"
target="data/raw/${day}.csv"
mkdir -p data/raw

if [[ -s "$target" ]]; then
    echo "already downloaded: $target"
else
    curl --fail --silent --show-error \
        -H "Authorization: Bearer ${ROSTER_TOKEN}" \
        -o "${target}.part" \
        "${ROSTER_URL}/${day}.csv"
    mv "${target}.part" "$target"
    echo "saved: $target ($(wc -l < "$target") lines)"
fi

uv run greetings roster "$target"
