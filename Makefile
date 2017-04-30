.PHONY: clean test retest release

install:
	pip install -e .

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

test:
	py.test -vvv

coverage:
	py.test --cov=flake8_imports

retest:
	py.test -vvv --lf

release:
	pip install twine wheel
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload -s dist/*
