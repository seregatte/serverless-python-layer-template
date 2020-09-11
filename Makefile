all: package deploy

package:
	@docker run -v "${PWD}:/var/task" "lambci/lambda:build-python3.8" /bin/sh -c "pip install -r requirements.txt -t .pythonpath/python/lib/python3.8/site-packages/; exit"

deploy:
	@sls deploy