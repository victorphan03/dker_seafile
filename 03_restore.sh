#!/bin/bash
# filepath: /home/x79/seafile/03_restore.sh

if [ -z "$1" ]; then
  echo "Usage: $0 backup_file.tar.gz"
  exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
  echo "Backup file '$BACKUP_FILE' not found!"
  exit 2
fi

# Remove existing data folder (optional, be careful!)
rm -rf ./data

# Extract backup
tar -xzvf "$BACKUP_FILE"

echo "Restore completed from $BACKUP_FILE"