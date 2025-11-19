#!/bin/bash

echo "Building CLI..."
# cd cli
./mvnw clean package -DskipTests -q

if [ $? -eq 0 ]; then
  echo "Starting CLI..."
  java -jar target/cli-0.0.1-SNAPSHOT.jar
else
  echo "Build failed."
  exit 1
fi
