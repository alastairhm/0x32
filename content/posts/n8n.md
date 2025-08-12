---
title: "N8N finally an IFTTT replacement"
date: 2025-08-12T15:13:19+01:00
draft: false
tags: ['tech','linux','automation','homelab']
featured_image: 'n8n-logo.png'
---

# N8N Self hosted IFTTT replacement

Found [N8N](https://n8n.io/) recently which is an open-source workflow automation tool that lets you connect various services and automate tasks.

Think IFTTT which you can host yourself locally.

I run it locally on my Debian Linux Server using this Docker compose file.

```
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    environment:
      - GENERIC_TIMEZONE=Europe/Amsterdam
      - NODE_ENV=production
      - N8N_SECURE_COOKIE=false
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    restart: unless-stopped

volumes:
  n8n_data:
    name: n8n_data
    external: true
```

You can use it do automate all sort of tasks, I am currently testing it posting RSS feed updated to a Discord Server.


![n8n example](https://live.staticflickr.com/65535/54716365473_307f56cec2_c.jpg "n8n rss")

There are a lot of other integrations you can use to automate to your hearts content.
