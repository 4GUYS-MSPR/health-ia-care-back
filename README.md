# Health IA API

![Status](https://img.shields.io/badge/status-production-success)
![Version](https://img.shields.io/badge/version-0.1.2-green)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Django Version](https://img.shields.io/badge/django-6.0%2B-green)
![DRF](https://img.shields.io/badge/DRF-3.16%2B-red)
![Pydantic](https://img.shields.io/badge/data_validation-pydantic-white?logo=pydantic)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-important)

This repository houses the Django-based backend for HealthAI, a digital health platform providing AI-driven nutrition and fitness coaching. The core mission of this infrastructure is to serve as a reliable, high-performance data hub for multi-source wellness metrics.

## Summary
- [Introduction](#health-ia-api)
- [Summary](#summary)
- [Installation](#installation)
  - [Environment](#environment)
  - [Docker compose](#docker-compose)
  - [HealthIA](#healthia)
- [Commands](#commands)

## Installation

### Environment
After clone this repo, you have to rename `.env.example` as `.env` and fill it.

| System            | Command                                    |
|-------------------|--------------------------------------------|
| Linux / MacOS     | `mv .env.example .env`                     |
| Windows           | `ren .env.example .env`                    |

### Docker compose
You should have docker installed.
| System            | Lien / Command                             |
|-------------------|--------------------------------------------|
| Linux             | `curl https://get.docker.com \| bash`      |
| MacOS             | https://docs.docker.com/desktop/setup/install/mac-install/ |
| Windows           | https://docs.docker.com/desktop/setup/install/windows-install/ |

Then, juste run `up` command bellow.

### HealthIA

#### Default Credentials
| Identifier | Value   |
|------------|---------|
| Username   | `admin` |
| password   | `admin` |

⚠️ **Don't forget to change admin password !**<br>
⚠️ *Don't use directly `python manage.py ...`, you are going to have invalid database host error !*

## Commands

| Command             | Linux / MacOS        | Windows                           |
|---------------------|----------------------|-----------------------------------|
| up                  | `make up`            | `docker compose up -d`            |
| down                | `make down`          | `docker compose down`             |
| migrations          | `make migrations`    | `POSTGRES_HOST=localhost python manage.py makemigrations app` |
| lint                | `make check-lint`    | `pylint $(git ls-files '*.py')`   |
| test                | `make check-test`    | `POSTGRES_HOST=localhost pytest`  |
| run                 | `make run cmd=<cmd>` | `docker exec -it health-ia-api python manage.py <cmd>` |
| help                | `make help`          | /                                 |
