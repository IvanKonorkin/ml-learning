ifneq (,$(wildcard ./.env))
	include .env
	export
endif

load-data:
	curl ${STATS_URL} -o data/stats.json

main:
	docker compose run ml python3 main.py

build:
	docker compose build
