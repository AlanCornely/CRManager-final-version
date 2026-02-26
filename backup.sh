#!/bin/bash

# Database Configuration
DB_HOST=${DB_HOST:-"localhost"}
DB_USER=${DB_USER:-"root"}
DB_PASS=${DB_PASSWORD:-"password"}
DB_NAME=${DB_NAME:-"crmanager"}

# Backup directory
BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FILENAME="$BACKUP_DIR/backup_$TIMESTAMP.sql"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

echo "Starting backup for database: $DB_NAME..."

# Execute backup
# Note: Using -p$DB_PASS (no space) is insecure for production scripts logged in history,
# but using .my.cnf or environment variables is safer. For this simple script, we assume env var usage or prompt.
# Since we are using variables from .env ideally, we will try to just run it.
# If password is set, use it.

if [ -z "$DB_PASS" ]; then
    mysqldump -h $DB_HOST -u $DB_USER $DB_NAME > $FILENAME
else
    # Be careful with password visibility
    export MYSQL_PWD=$DB_PASS
    mysqldump -h $DB_HOST -u $DB_USER $DB_NAME > $FILENAME
fi

if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $FILENAME"
else
    echo "Backup failed!"
    exit 1
fi
