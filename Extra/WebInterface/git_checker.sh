#!/bin/bash
set -e && cd "$(dirname `realpath -s $0`)"

# mostly AI here

REPO_DIR="../../"
TMUX_SESSION_NAME="WASMoonHTTP"
COMMAND="☾ gen.☾"

check_for_updates() {
  cd "$REPO_DIR" || exit 1
  git fetch origin
  LOCAL=$(git rev-parse HEAD)
  RMOTE=$(git rev-parse origin)
  cd -
  if [ "$LOCAL" != "$RMOTE" ]; then
    return 0
  else
    return 1
  fi
}

reset_tmux() {
    echo "Killing existing session"
    tmux kill-session -t "$TMUX_SESSION_NAME" || :
    echo "Starting new session..."
    tmux new-session -d -s "$TMUX_SESSION_NAME" "$COMMAND"
}

reset_tmux
while :; do
  if check_for_updates; then
    echo "Update detected, pulling."
    git pull
    reset_tmux
  else
    echo "No update detected."
  fi
  sleep 300
done