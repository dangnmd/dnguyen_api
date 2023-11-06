#!/bin/bash

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

SERVICE_NAME=${PROJECT_NAME}_${HOST_PORT}
echo $SERVICE_NAME

docker compose up -d

