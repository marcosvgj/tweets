SHELL=/bin/bash

delete-py-cache:
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

delete-wheel: delete-py-cache
	@find . -type d -name 'build' -exec rm -rf {} +
	@find . -type d -name 'dist' -exec rm -rf {} +
	@find . -type d -name '*.egg-info' -exec rm -rf {} +
	
build-wheel:
	@python3 setup.py sdist bdist_wheel

install-whell: build-wheel
	@pip3 install --use-wheel dist/*.whl

setup: install-whell
clean: delete-wheel
	
