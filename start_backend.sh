#!/bin/bash

# Load environment variables from .env if it exists
if [ -f .env ]; then
  echo "Loading environment variables from .env..."
  set -a
  source .env
  set +a
fi

# Navigate to the Java backend directory
cd apis

# Run the Spring Boot application
./mvnw spring-boot:run
