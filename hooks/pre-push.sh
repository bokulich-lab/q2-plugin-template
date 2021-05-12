#!/bin/sh

STASH_NAME="pre-push-$(date +%s)"
git stash save --keep-index $STASH_NAME

make test
RESULT=$?

STASHES=$(git stash list)
if [[ $STASHES == *$STASH_NAME* ]]; then
  git stash pop
fi
[ $RESULT -ne 0 ] && exit 1
exit 0
