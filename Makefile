SHELL=/bin/bash
PIP=`command -v pip3 || pip`

.PHONY: install clean build test start

install-requirements:
	$(PIP) install -r requirements.txt

test:
	@python3 -m unittest -v

build:
	@python3 setup.py sdist bdist_wheel

copy-python-project:
	cp -f dist/*.whl docker/airflow/libs
	cp -f requirements.txt docker/airflow/

install-python-project:
	$(PIP) install --use-wheel dist/*.whl

clean-pyc:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

docker-compose-up:
	docker-compose kill
	docker-compose rm -f
	docker-compose pull
	docker-compose up --build --force-recreate -d

install: install-requirements test build install-python-project copy-python-project clean
clean: clean-pyc clean-build
start: install docker-compose-up
	






	
