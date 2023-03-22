build-blog:
	hugo

deploy-blog: build-blog
	hugo deploy

build-docker: build-blog
	docker build -t 0x32 .

run-docker: build-docker
	docker run --rm --name "my-lighttpd" --rm -p 8000:80 0x32
