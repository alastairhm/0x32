FROM ghcr.io/alastairhm/docker-hugo:main as builder

WORKDIR /mnt
COPY ./ /mnt/
RUN hugo

FROM ghcr.io/alastairhm/alpine-lighttpd:latest
COPY --from=builder /mnt/public/ /var/www/


