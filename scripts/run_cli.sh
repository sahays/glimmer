#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

cd "$PROJECT_ROOT/cli"

echo "Building CLI..."
./mvnw clean package -DskipTests -q

java -jar target/cli-0.0.1-SNAPSHOT.jar "$@"
