install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black --fast *.py config/*.py tests/*.py
lint:
	# pylint
	pylint --disable=R,C \
	--generated-members=objects \
	--allow-global-unused-variables=y \
	*.py config/*.py tests/*.py
test:
	pytest tests/*.py
build:
	docker compose -f docker-compose.yaml up --build -d

all: install format lint test build