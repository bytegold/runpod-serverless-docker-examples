# rembg Docker image example for Runpod serverless

[rembg](https://github.com/danielgatis/rembg) is a popular tool to remove the background from images

This example shows how to create and run a custom Docker image that provides rembg for Runpod serverless

---

**Disclaimer:** sharing my playground, make sure you know what you are doing before using in any production environment

---

## Files

* **.dockerignore**

  Specifies files which are excluded when building the docker image
* **Dockerfile-serverless**

  Docker instructions for assembling the image
* **handler.py**

  Handler that is exposed by the Runpod serverless infrastructure and that handles your Runpod API calls

  In this example it exposes access to rembg

## Build instructions

1. clone [https://github.com/danielgatis/rembg](https://github.com/danielgatis/rembghttps:/)
2. copy these files into the *rembg* directory

   * [.dockerignore](.dockerignore)
   * [Dockerfile-serverless](Dockerfile-serverless)
   * [handler.py](handler.py)
3. build docker image

   make sure to use the [Dockerfile-serverless](Dockerfile-serverless) and not the rembg Dockerfile

   see [Readme.md](../README.md) on how to use the -f param when building a Docker image
4. push to dockerhub
5. create and start new Runpod serverless instance using the dockerhub image

---

With ❤️ from [bytegold.com](https://bytegold.com)