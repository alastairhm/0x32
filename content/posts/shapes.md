---
title: "Shapes"
date: 2020-09-07T10:41:29+01:00
draft: false
tags: ['fractal','art','processing','generative']
categories: ['Creative']
featured_image: "https://live.staticflickr.com/65535/50315179791_56ab079828_w.jpg"
---

{{< flickr "Shapes"
           "Random Shapes"
           "https://www.flickr.com/photos/doodle_m/50315179791"
           "https://live.staticflickr.com/65535/50315179791_56ab079828_c.jpg" >}}

Code can be found at [Shapes](https://github.com/alastairhm/processing/tree/master/shapes)

```java
// Alastair Montgomery
// http://0x32.uk/

PShape s;  // The PShape object

void setup() {
  size(2000, 1000);
  background(128,128,128);

  int spacing = 25;
  float length = spacing * 0.95;

  strokeWeight(1);
  stroke(0);

  for (int y = 0; y < height; y=y+spacing) {
    for (int x = 0; x < width; x=x+spacing) {

      double selector = 4 * Math.random();
      if ( selector < 1) {
        shape11(x, y, length);
      }
      else if (selector > 1 && selector < 2){
        shape12(x, y, length);
      }
      else if (selector > 2 && selector < 3){
        shape13(x,y,length);
      }
      else {
        shape14(x,y,length);
      }
    }
  }
  save("Example/shape.png");
}

void shape11(int x, int y, float l) {
  s = createShape();
  s.beginShape();
  s.strokeJoin(ROUND);
  s.vertex(0, 0);
  s.vertex(l/2, 0);
  s.vertex(l/2, l/2);
  s.vertex(l, l/2);
  s.vertex(l,l);
  s.vertex(0,l);
  s.vertex(0,0);
  s.endShape(CLOSE);
  shape(s, x, y);
}

void shape12(int x, int y, float l) {
  s = createShape();
  s.beginShape();
  s.strokeJoin(ROUND);
  s.vertex(0, 0);
  s.vertex(0, l/2);
  s.vertex(l/2, l/2);
  s.vertex(l/2, l);
  s.vertex(l,l);
  s.vertex(l,0);
  s.endShape(CLOSE);
  shape(s, x, y);
}

void shape13(int x, int y, float l) {
  s = createShape();
  s.beginShape();
  s.strokeJoin(ROUND);
  s.vertex(l/2, 0);
  s.vertex(l, 0);
  s.vertex(l, l);
  s.vertex(0, l);
  s.vertex(0,l/2);
  s.vertex(l/2,l/2);
  s.endShape(CLOSE);
  shape(s, x, y);
}

void shape14(int x, int y, float l) {
  s = createShape();
  s.beginShape();
  s.strokeJoin(ROUND);
  s.vertex(0, 0);
  s.vertex(l, 0);
  s.vertex(l, l/2);
  s.vertex(l/2, l/2);
  s.vertex(l/2,l);
  s.vertex(0,l);
  s.endShape(CLOSE);
  shape(s, x, y);
}
```