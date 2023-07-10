# Stable Diffusion Docker image example for Runpod serverless

This example shows how to create and run a custom Docker image that provides a custom Stable Diffusion model through the [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) for Runpod serverless

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

  In this example it exposes access to several functions of the Stable Diffusion web ui API in the image

* **[start.sh](start.sh)**

  Script that is started inside the docker image once it is spun up

## Build instructions

1. change MODELFILE in [Dockerfile](Dockerfile)

1. change MODELFILE in [.dockerignore](.dockerignore)

1. change MODELFILE in [start.sh](start.sh) to your model file (e.g. .ckpt, .safetensors)

1. build docker image

1. push to dockerhub

1. create and start new Runpod serverless instance using the dockerhub image

---

With ❤️ from [bytegold.com](https://bytegold.com)