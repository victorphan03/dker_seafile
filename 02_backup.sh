#!/bin/bash
# filepath: /home/x79/seafile/backup.sh
docker compose down
TITLE=${1:-backup}
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="seafile_${TITLE}_${DATE}.tar.gz"

tar -czvf "$BACKUP_FILE" ./data

echo "Backup created: $BACKUP_FILE"
docker compose up -d