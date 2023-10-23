run:
	uvicorn shortest.app:app --reload

format:
	black shortest tests

lint:
	black shortest tests --check
	mypy shortest tests

test:
	python -m pytest
