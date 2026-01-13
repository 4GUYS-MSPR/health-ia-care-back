.SILENT:

all: help

up:
	docker compose up -d
	
reload:
	docker compose up -d --build
	@if [ "$(logs)" = "1" ]; then \
		docker logs -f health-ia-api; \
	fi

down:
	docker compose down

migrations:
	POSTGRES_HOST=localhost python manage.py makemigrations app

check:
	pylint $$(git ls-files '*.py')

run:
ifndef cmd
	$(error cmd must be set, make run cmd=cmd.gx)
else
	docker exec -it health-ia-api python manage.py $(cmd)
endif

help:
	echo "Usage: make <target>"
	echo ""
	echo "    up         Start docker-compose in detached mode"
	echo "    reload     Rebuild docker-compose in detached mode"
	echo "    down       Stop docker-compose"
	echo "    migrate    Run Django migrations inside container"
	echo "    check      Run pylint"
	echo "    run        Run arbitrary Django manage.py command (ex: make run cmd=createsuperuser)"
	echo "    help       Show this help message"
	echo ""
