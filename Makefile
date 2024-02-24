install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black --fast *.py ./config/*py
lint:
	# pylint
	pylint --disable=R,C \
	--generated-members=objects \
	--allow-global-unused-variables=y \
	*.py config/*.py
test:
	# test
deploy:
	# docker

all: install format lint test