.PHONY: clean build install deploy
clean:
	rm dist/* || echo ''
	python3 setup.py clean
build: clean
	python3 setup.py build
install: build
	python3 -m pip install -r requirements.txt
	python3 setup.py install
test: install
	python3 -m pytest --cov=human_security --cov-report html:cov.html -v -s tests/
deploy: build
	#http://guide.python-distribute.org/creation.html
	python3 setup.py sdist
	twine upload dist/*