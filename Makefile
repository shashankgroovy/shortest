format:
	black shortest tests

lint:
	black shortest tests --check
	mypy shortest tests

run:
	uvicorn shortest.app:bootload --reload

server:
	gunicorn shortest.app:bootload --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

test:
	python -m pytest
