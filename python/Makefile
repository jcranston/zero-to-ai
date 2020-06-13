### Testing ###
.PHONY: clean clean-pyc lint test test-assign0

clean: docs-clean clean-pyc
	rm -fr coverage_html_report/
	rm -f .coverage
	rm -fr .cache
	rm -fr .mypy_cache

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	# find ../scripts -name '__pycache__' -exec rm -fr {} +

lint:
	flake8 ../python
	pylint ../python


test-assign0:
	pytest --cov-config .coveragerc --pyargs test/assign0 --cov=test/assign0 --cov-report term-missing

test-assign1:
	pytest --cov-config .coveragerc --pyargs test/assign1 --cov=test/assign1 --cov-report term-missing

test: test-assign0 test-assign1

### Documentation ###
.PHONY: docs-clean docs

docs-clean:
	make -C ../docs clean
	rm -df ../docs/_build

docs:
	SPHINXOPTS='-t runnb' make -C ../docs html
	@echo open ../docs/_build/html/index.html


