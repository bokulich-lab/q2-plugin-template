#!/bin/sh

STASH_NAME="pre-commit-$(date +%s)"
git stash save --keep-index $STASH_NAME

make lint
RESULT=$?

STASHES=$(git stash list)
if [[ $STASHES == *$STASH_NAME* ]]; then
  git stash pop
fi
[ $RESULT -ne 0 ] && exit 1
exit 0
