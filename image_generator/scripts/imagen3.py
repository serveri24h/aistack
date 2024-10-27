import torch
from diffusers import StableDiffusion3Pipeline
import os
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'

pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16, safety_checker = None)
pipe = pipe.to("cuda")
print("PIPE IS DONE")
image = pipe(
    "Pixel art city",
    negative_prompt="",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
print("IMAGE IS DONE", type(image))
image.save("testin.png")