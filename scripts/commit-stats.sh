#!/usr/bin/env bash
# Commit Statistics for Claude x Mauxx AI
set -e

cd "$(dirname "$0")/.."

echo "═══ Claude x Mauxx AI — Commit Statistics ═══"
echo ""

TOTAL=$(git log --oneline | wc -l)
AUTHORS=$(git log --format="%an <%ae>" | sort -u | head -5)

echo "Total commits:  $TOTAL"
echo ""
echo "═══ Breakdown ═══"
echo ""

echo "By convention:"
git log --format="%s" | sed -E 's/^([a-z]+).*/\1/' | sort | uniq -c | sort -rn | head -15
echo ""
echo "By file type:"
git log --name-only --pretty=format: | grep -v '^$' | sed -E 's/.*\.([a-z]+)$/\1/' | sort | uniq -c | sort -rn | head -10
echo ""
echo "═══ Progress to 1000 ═══"
echo "  $TOTAL / 1000 commits"
echo -n "  "
for ((i=0; i<$TOTAL/10; i++)); do echo -n "█"; done
for ((i=$TOTAL/10; i<100; i++)); do echo -n "░"; done
echo "  $((TOTAL*100/1000))%"
echo ""
echo "═══ Last 10 commits ═══"
git log --oneline -10
echo ""
