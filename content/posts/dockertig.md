---
title: "Docker Images Again"
date: 2022-07-06T12:07:22+01:00
draft: false
featured_image: "/devops.jpg"
tags: ['devops','docker','terraform','ssl']
---
## Devops Docker images again

Another Docker image with some tools useful for devops, this time includes the [TIG CLI utility](https://jonas.github.io/tig/).

### Tig

Tig Docker image [https://github.com/alastairhm/docker-tig](https://github.com/alastairhm/docker-tig)

To use run the following;

#### Directly on the CLI

```bash
docker run --rm -ti -v $(pwd):/mnt ghcr.io/alastairhm/docker-tig:latest
```


#### As an alias

```bash
alias tig='docker run --rm -ti -v $(pwd):/mnt ghcr.io/alastairhm/docker-tig:latest'

```

For full instructions on using TIG visit the [offical instructions page](https://jonas.github.io/tig/doc/manual.html).

