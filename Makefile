# Use Docker if installed, otherwise fall back to Podman.
# Override with e.g. `make run-docker CONTAINER_ENGINE=podman`.
CONTAINER_ENGINE ?= $(shell command -v docker >/dev/null 2>&1 && echo docker || (command -v podman >/dev/null 2>&1 && echo podman))

build-blog:
	hugo

deploy-blog: build-blog
	hugo deploy

check-engine:
	@test -n "$(CONTAINER_ENGINE)" || { echo "Neither docker nor podman found in PATH" >&2; exit 1; }

build-docker: check-engine build-blog
	$(CONTAINER_ENGINE) build -t 0x32 .

run-docker: build-docker
	$(CONTAINER_ENGINE) run --rm --name "my-lighttpd" -p 8000:80 0x32

.PHONY: build-blog deploy-blog check-engine build-docker run-docker
