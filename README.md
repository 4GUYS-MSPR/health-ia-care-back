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
| Linux / MacOS     | `curl https://get.docker.com \| bash`<br>https://docs.docker.com/desktop/setup/install/windows-install/ |
| MacOS             | https://docs.docker.com/desktop/setup/install/mac-install/ |
| Windows           | https://docs.docker.com/desktop/setup/install/windows-install/ |

### HealthIA
Run project using `run` command.<br>
You can now available to use all commands.<br>
<span style="color: red">WARNING:</span><span style="color: grey"> *But don't use directly `python manage.py ...`, you are going to have database host invalid !*</span>

Prepare your database. Create your super user with `<base> createsuperuser`.<br>
Then seed static informations with `<base> seed`.

| Command             | Linux / macOS  | Windows (PowerShell)              |
|---------------------|----------------|-----------------------------------|
| up                  | `make up`      | `docker compose up -d`            |
| reload              | `make reload`  | `docker compose up -d --build`    |
| down                | `make down`    | `docker compose down`             |
| migrate             | `make migrate` | `docker exec -it health-ia-api python manage.py makemigrations app && docker exec -it health-ia-api python manage.py migrate` |
| run                 | `make run`     | `docker exec -it health-ia-api python manage.py <cmd>` |
| help                | `make help`    | /                                 |
