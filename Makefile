requirements.txt: Pipfile.lock
	@pipenv run pip freeze > requirements.txt

build-docker:
	@docker build . -t hivdb/hivdb-cms-builder:latest

push-docker: build-docker
	@docker push hivdb/hivdb-cms-builder:latest

build: pages images
	@rm -rf build/
	@docker run \
		--mount type=bind,source=$(PWD),target=/app \
		--rm -it hivdb/hivdb-cms-builder:latest \
		python /app/build.py

deploy-localhost: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/localhost --delete

deploy-staging: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/staging --delete

deploy-staging2: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/staging2 --delete

deploy-prod: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/prod --delete

deploy-all: deploy-localhost deploy-staging deploy-staging2 deploy-prod


.PHONY: build-docker push-docker deploy-*
