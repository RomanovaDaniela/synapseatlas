#!/usr/bin/env bash
set -euo pipefail
JITTER_MAX=1600
sleep $((RANDOM % JITTER_MAX))
set -a; [ -f "$HOME/.env" ] && . "$HOME/.env"; set +a
{
  echo "[$(date -Is)] DIAG: whoami=$(id -un) TOKEN_LEN=${#TELEGRAM_TOKEN} CHAT=${TELEGRAM_CHAT_ID:-<empty>}"
} >> /root/synapseatlas/cron.log
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd /root/synapseatlas
/usr/bin/python3 -m auto_updater.scheduler >> /root/synapseatlas/cron.log 2>&1
