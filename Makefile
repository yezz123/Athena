help:
	@echo "Targets:"
	@echo "    make start"
	@echo "    make down"
	@echo "    make pull"
	@echo "    make build"
	@echo "    make lint"
	@echo "    make clean"

start:
	docker-compose up -d

down:
	docker-compose down

pull:
	docker-compose pull

build:
	docker-compose build

lint:
	docker-compose run --rm athena pre-commit run --all-files

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +