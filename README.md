# Example files for Docker images for Runpod serverless

**Disclaimer:** sharing my playground, make sure you know what you are doing before using in any production environment

## Examples

### rembg Docker image example for Runpod serverless

[rembg](https://github.com/danielgatis/rembg) is a popular tool to remove the background from images

This example shows how to create and run a custom Docker image that provides rembg for Runpod serverless

[See example](rembg)

---

### Stable Diffusion Docker image example for Runpod serverless

This example shows how to create and run a custom Docker image that provides a custom Stable Diffusion model through the [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) for Runpod serverless

[See example](stable-diffusion)

---

### vtracer Docker image example for Runpod serverless

[VTracer](https://github.com/visioncortex/vtracer) is a popular Raster to Vector Graphics Converter

This example shows how to create and run a custom Docker image that provides VTracer for Runpod serverless

[See example](vtracer)

---

## Docker cheatsheet

### Build docker image for dockerhub
DOCKER_BUILDKIT=1 docker build -t USERNAME/REPOSITORY:latest -f Dockerfile .


### Publish docker image to dockerhub
docker push USERNAME/REPOSITORY:latest


---

With ❤️ from [bytegold.com](https://bytegold.com)