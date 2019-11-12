#!/bin/bash
set -e

echo "Start docker in which environment? [dev/test/prod]:"
read stage
if [ "$stage" == "dev" ]; then
	sudo docker-compose -f docker-compose-dev.yml up --build
elif [ "$stage" == "test" ]; then
	sudo docker-compose -f docker-compose-test.yml up --build
else
	sudo docker-compose -f docker-compose-prod.yml up -d --build
fi
