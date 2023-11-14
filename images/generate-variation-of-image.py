# Description: Generate a variation of an image
# Source: https://platform.openai.com/docs/guides/images

from openai import OpenAI
client = OpenAI()

# Create a variation of an image
response = client.images.create_variation(
  image=open("image.png", "rb"),
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
print(image_url)