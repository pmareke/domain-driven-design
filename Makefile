.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: build
build: ## Build the app
	docker build .

.PHONY: install
install: ## Install all dependencies
	poetry install

.PHONY: update
update: ## Update dependencies
	poetry update

.PHONY: up
up:    ## Run the app
	docker-compose up --build weather

.PHONY: down
down: ## Stop and remove all the Docker services, volumes and networks
	docker-compose down -v --remove-orphans

.PHONY: dev
dev:    ## Run the server in dev mode
	poetry run uvicorn weather_app.main:app --reload --host 0.0.0.0 --port 8080

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-format
check-format:
	poetry run yapf --diff --recursive weather_app/**/*.py

.PHONY: check-style
check-style:
	poetry run flake8 weather_app/
	poetry run pylint weather_app/**

.PHONY: reformat
reformat:  ## Format python code
	poetry run yapf --parallel --recursive -ir weather_app/
	poetry run pyupgrade --py310-plus **/*.py

.PHONY: test-unit
test-unit: ## Run all unit tests
	docker-compose run --rm --no-deps weather poetry run pytest -n auto weather_app/tests/unit -ra

.PHONY: test-integration
test-integration: ## Run all integration tests
	docker-compose run --rm weather poetry run pytest -n auto weather_app/tests/integration -ra

.PHONY: test-acceptance
test-acceptance: ## Run all acceptance tests
	docker-compose run --rm weather poetry run pytest -n auto weather_app/tests/acceptance -ra

.PHONY: test
test: test-unit test-integration test-acceptance

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test
