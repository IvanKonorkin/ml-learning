ifneq (,$(wildcard ./.env))
	include .env
	export
endif

load-data:
	curl ${STATS_URL} -o data/stats.json