build:
	docker compose build

clean:
	docker compose down --remove-orphans
	-docker rm shortest-api
	-docker rmi shortest:latest

docker-run: build
	docker run -p 8000:8000 --name shortest-api shortest:latest

format:
	black shortest tests

install:
	pip install poetry
	poetry install
	poetry shell

lint:
	black shortest tests --check
	mypy shortest tests

dev:
	uvicorn shortest.app:bootload --reload

run:
	gunicorn shortest.app:bootload --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

server: clean build
	docker compose up

test:
	python -m pytest
