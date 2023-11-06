#!/bin/bash

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

if [ -z "$IMAGE" ]
then
	IMAGE='registry.billbros.vn/cooky_python_api:python3_mssql'
fi

if [ -z "$NUM_WORKERS" ]
then
	NUM_WORKERS='multiprocessing.cpu_count() * 2 \+ 1'
fi

SERVICE_NAME=${PROJECT_NAME}_${HOST_PORT}

docker compose up -d

