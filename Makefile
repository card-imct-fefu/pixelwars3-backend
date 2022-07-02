CODE = pixelwars3
SRC = .

lint:
	flake8 --jobs 4 --statistics --show-source $(CODE) $(TEST)
	black --target-version py39 --skip-string-normalization --line-length=79 --check $(CODE) $(TEST)

pretty:
	isort $(CODE)
	black --target-version py39 --skip-string-normalization --line-length=79 $(CODE)

run: init_db
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --app-dir pixelwars3

init_db:
	poetry run alembic upgrade head
