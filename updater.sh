#!/bin/bash
set -e
# definition
DOT_GIT=$1
WORK_TREE=$2
REMOTE=$3
BRANCH=$4

pull () {
  git --git-dir=$1/.git --work-tree=$2 pull $3 $4
}

SUCCESS=$(pull $DOT_GIT $WORK_TREE $REMOTE $BRANCH > /dev/null 2>&1 ; echo $?)

if [ $SUCCESS -gt 0 ]; then
  echo "success update"
else
  echo $SUCCESS
fi