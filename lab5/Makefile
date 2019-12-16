STATES := app tests
REPO := prometej46297/lab_5

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

tests:
	@docker build -f Dockerfile.tests -t prometej46297/lab_5:tests .

app:
	@docker build -f Dockerfile.app -t prometej46297/lab_5:app .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

push:
	@docker push $(REPO):app
	@docker push $(REPO):tests

rm-images:
	@docker rmi -f $$(docker images -q)

pull:
	@docker pull $(REPO):app
	@docker pull $(REPO):tests
