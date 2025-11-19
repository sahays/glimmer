#!/bin/bash

# Load environment variables from .env
if [ -f .env ]; then
  echo "Loading environment variables from .env..."
  set -a
  source .env
  set +a
fi

# Navigate to api directory
cd apis

echo "Resetting Database (Clean + Migrate)..."
# Use -Dflyway.cleanDisabled=false to allow clean
./mvnw flyway:clean flyway:migrate \
    -Dflyway.url=jdbc:postgresql://${DB_HOST}:${DB_PORT}/${DB_NAME} \
    -Dflyway.user=${DB_USERNAME} \
    -Dflyway.password=${DB_PASSWORD} \
    -Dflyway.cleanDisabled=false

echo "Database reset complete."
