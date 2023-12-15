---
title: "Node JS Jokebot"
date: 2023-12-13T12:36:56Z
draft: false
tags: ['tech','code','nodejs','bot','mastodon']
categories: ['Geek','NodeJS',]
featured_image: "/nodejs.jpg"
---

# Learning Node JS

I've started playing about with Node JS to learn it enough to modify some legacy Lambda code.

One of the tasks I set myself was to write a Joke bot for Mastodon, which work out to be fairly easy with a couple of packages [got](https://www.npmjs.com/package/got) and [masto](https://www.npmjs.com/package/masto).

[Dad Joke Bot](https://github.com/alastairhm/dadjokesbot) the code is only 32 lines long, looking to expand it to be able to post images as well.

```javascript
import { createRestAPIClient } from "masto";
import got from "got";

function getJoke(apiUrl){
  got.get(apiUrl, { responseType: 'json' })
    .then(response => {
                  // If the request is successful, parse the response body as a JSON object
                  const data = response.body;
                        // console.log("Data Response,",data);
                        post(data.joke);
                            })
    .catch(error => {
                  // If the request fails, print out the error message
                  console.error(error.message);
                    });
}

async function post(myJoke){
  const newStatus = myJoke + " #dadjoke"
  console.log("Post Joke,",myJoke);
  const masto = createRestAPIClient({
              url: process.env.URL,
                  accessToken: process.env.TOKEN,
                    });
  const status = await masto.v1.statuses.create({
              status: newStatus,
                  visibility: "public",
                    });
  console.log(status.url);
}

getJoke("https://icanhazdadjoke.com/");
```

The resulting posts end up here, [https://mastodon.me.uk/@dadjokes](https://mastodon.me.uk/@dadjokes), I ended up running it via a Dockaer image with crontab.

Alastair Montgomery Dec 2023
