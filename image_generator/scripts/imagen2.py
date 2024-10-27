import PIL.Image
import torch
import PIL
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-3-medium", torch_dtype=torch.float16, safety_checker = None)

pipe = pipe.to("cuda")

prompt = "red car"

image:PIL.Image.Image = pipe(prompt).images[0]
image.save("test_img.png")