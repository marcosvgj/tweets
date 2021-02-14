SHELL=/bin/bash
PIP=`command -v pip3 || pip`

.PHONY: install clean build test start configure

configure:
	$(SHELL) credentials_setup/setup.sh

install-requirements:
	$(PIP) install -r requirements.txt

test:
	@python3 -m unittest -v

build:
	@python3 setup.py sdist bdist_wheel

copy-python-project:
	mkdir -p docker/airflow/libs/
	cp -f dist/*.whl docker/airflow/libs/
	cp -f requirements.txt docker/airflow/

install-python-project:
	$(PIP) install --use-wheel dist/*.whl

clean-pyc:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean-python-project:
	rm --force -- docker/airflow/requirements.txt

docker-compose-up:
	docker-compose kill
	docker-compose rm -f
	docker-compose pull
	docker-compose up --build --force-recreate -d

install: install-requirements test build install-python-project copy-python-project clean
clean: clean-pyc clean-build clean-python-project
start: install docker-compose-up
	






	
