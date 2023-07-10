# vtracer Docker image example for Runpod serverless

[VTracer](https://github.com/visioncortex/vtracer) is a popular Raster to Vector Graphics Converter

This example shows how to create and run a custom Docker image that provides VTracer for Runpod serverless

---

**Disclaimer:** sharing my playground, make sure you know what you are doing before using in any production environment

---

## Files

* **[.dockerignore](.dockerignore)**

  Specifies files which are excluded when building the docker image
* **[Dockerfile](Dockerfile)**

  Docker instructions for assembling the image
* **[handler.py](handler.py)**

  Handler that is exposed by the Runpod serverless infrastructure and that handles your Runpod API calls

  In this example it exposes access to vtracer

## Build instructions

1. download the latest [vtracer-linux](https://github.com/visioncortex/vtracer/releases/) release

1. build docker image

1. push to dockerhub

1. create and start new Runpod serverless instance using the dockerhub image

---

With ❤️ from [bytegold.com](https://bytegold.com)
