import requests
import os
from dotenv import load_dotenv
from PIL import Image
import random

load_dotenv()

api_key = os.environ.get("SEGMIND_API_KEY")
url = "https://api.segmind.com/v1/sdxl1.0-txt2img"

def get_img(prompt="A cute anime girl named Ren with dark purple hair looking at the viewer sitting under a tree in a beautiful garden, upper body, focus on face, high quality, high budget, anime, 4k, beautiful, cute, highly detailed",
            negative_prompt="ugly, bad fingers, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft",
            style="anime",
            samples=1,
            scheduler="UniPC",
            num_inference_steps=30,
            guidance_scale=8,
            strength=0.2,
            high_noise_fraction=0.8,
            seed=random.randint(0, 1000000),
            img_width=1024,
            img_height=2048,
            refiner=True,
            base64=False
            ):
        
    payload = {
        "prompt": prompt,
      "negative_prompt": negative_prompt,
      "style": style,
      "samples": samples,
      "scheduler": scheduler,
      "num_inference_steps": num_inference_steps,
      "guidance_scale": guidance_scale,
      "strength": strength,
      "high_noise_fraction": high_noise_fraction,
      "seed": seed,
      "img_width": img_width,
      "img_height": img_height,
      "refiner": refiner,
      "base64": base64

    }

    response = requests.post(url, json=data, headers={'x-api-key': api_key})
    print(response)
    return response.content



if __name__ == "__main__":
    # Request payload
    data = get_img()

    with open("output.jpeg", "wb") as image:
        image.write(data)

    img = Image.open("output.jpeg")
    img.show()
