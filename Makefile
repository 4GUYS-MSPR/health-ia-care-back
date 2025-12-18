VENV = .venv/bin

.SILENT:

all: help

up:
	docker compose up -d --build

down:
	docker compose down

migrate:
	docker exec -it health-ia-api python manage.py makemigrations app
	docker exec -it health-ia-api python manage.py migrate

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
	echo "    down       Stop docker-compose"
	echo "    migrate    Run Django migrations inside container"
	echo "    run        Run arbitrary Django manage.py command (ex: make run cmd=createsuperuser)"
	echo "    help       Show this help message"
	echo ""
