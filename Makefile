.SILENT:

all: help

up:
	docker compose up -d db
	@if [ "$(dev)" = "1" ]; then \
		pip install -r requirements.txt; \
		POSTGRES_HOST=localhost python manage.py migrate; \
		POSTGRES_HOST=localhost python manage.py setup; \
		POSTGRES_HOST=localhost python manage.py runserver 0.0.0.0:5555; \
	else \
		docker compose up -d api; \
	fi

reload:
	docker compose up -d --build
	@if [ "$(logs)" = "1" ]; then \
		docker logs -f health-ia-api; \
	fi

down:
	docker compose down

migrations:
	POSTGRES_HOST=localhost python manage.py makemigrations

check:
	pylint $$(git ls-files '*.py')

test:
	docker exec -it health-ia-api python manage.py test  

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
	echo "    test		 Run all tests directly in docker container"
	echo "    help       Show this help message"
	echo ""
