# Health IA API

<span style="color: grey">// Description</span>

## Summary
- [Introduction](#health-ia-api)
- [Summary](#summary)
- [Installation](#installation)
  - [Environment](#environment)
  - [Docker compose](#docker-compose)
  - [HealthIA](#healthia)
- [Usage](#usage)

## Installation

### Environment
After clone this repo, you have to rename & `.env.example` as `.env` and fill it.

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

<span style="color: gold">WARNING</span> : <span style="color: grey"> **Don't forget to change admin password !**</span><br>
<span style="color: gold">WARNING</span> : <span style="color: grey"> *Don't use directly `python manage.py ...`, you are going to have invalid database host error !*</span>

## Commands

| Command             | Linux / MacOS        | Windows                           |
|---------------------|----------------------|-----------------------------------|
| up                  | `make up`            | `docker compose up -d`            |
| reload              | `make reload`        | `docker compose up -d --build`    |
| down                | `make down`          | `docker compose down`             |
| migration           | `make migration`     | `POSTGRES_HOST=localhost python manage.py makemigrations app` |
| run                 | `make run cmd=<cmd>` | `docker exec -it health-ia-api python manage.py <cmd>` |
| help                | `make help`          | /                                 |
