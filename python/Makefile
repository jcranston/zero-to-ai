### project constants ###
ZERO2AIHOME ?= ${HOME}/sandbox/zero-to-ai

.FORCE:

### python versioning ###
export PYTHONPATH=$(ZERO2AIHOME)/python
PYVERS:= 3.7
MY_PTH_FILES:=$(patsubst %,~/.local/lib/python%/site-packages/my.pth,$(PYVERS))

%.pth: .FORCE
	mkdir -p $(@D)
	echo "$(ZERO2AIHOME)/python" > $@

make-pth: $(MY_PTH_FILES)

VARS:=              \
  ZERO2AIHOME       \
  PYVERS            \
  MY_PTH_FILES      \

set-vars: $(VARS:%=set.%)

set.%: .FORCE
	@if [[ "$(words $($*))" == "0" ]]; then \
	  echo "unset $*"; \
	elif [[ "$(words $($*))" == "1" ]]; then \
	  echo "export $*='$($*)'"; \
	else \
	  echo "export $*=($($*:%='%'))"; \
	fi

show-vars: $(VARS:%=show.%)
show.%: .FORCE
	@printf '%-15s: %s\n' "$*" "$($*)"

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

# usage: `make conda-env-assignN` for assignN
conda-env-%:
	conda env create --force -f conf/$*-deps.yml

lint:
	flake8 ../python
	pylint ../python

test-assign0:
	pytest --tb=line -s -vv --cov-config .coveragerc --pyargs test/assign0 --cov=test/assign0 --cov-report term-missing

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
