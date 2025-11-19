#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

# Load environment variables from .env at root
if [ -f "$PROJECT_ROOT/.env" ]; then
  echo "Loading environment variables from .env..."
  set -a
  source "$PROJECT_ROOT/.env"
  set +a
fi

cd "$PROJECT_ROOT/apis"
./mvnw spring-boot:run
