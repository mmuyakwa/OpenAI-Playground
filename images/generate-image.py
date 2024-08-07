# Description: This script generates images with the image generator from OpenAI.
# Source: https://platform.openai.com/docs/guides/images
# Use the script as follows:
# python script-name.py "image-prompt"
# Created by: Michael Muyakwa, 2023-11-14

import urllib.request
import sys
from openai import OpenAI
from urllib.parse import urlparse

# Parameters:
# The image prompt that will be used to generate the images
image_prompt = "full body shot, A young woman dressed in a bodysuit dancing, highly detailed face, ultrarealistic, high resolution, 1024x1024"
# If debug is set to True, the response of the API calls will be printed.
debug = False


# Function to check if a URL is safe (uses http or https)
def is_safe_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https")


# Create an instance of the OpenAI client
client = OpenAI()

# When Parameters were given to the python call, use them as image prompt, otherwise use the default image prompt
if len(sys.argv) > 1:
    image_prompt = sys.argv[1]

# Use the "text-moderation-latest" model from OpenAI to check the text if OpenAI thinks it is offensive
moderation_response = client.moderations.create(
    model="text-moderation-latest", input=image_prompt
)

# Check the response to determine if the text is offensive
try:
    # Show the response of the moderation query, if debug = True
    if debug:
        print(moderation_response)

    # If the text is offensive, do not generate the image otherwise generate the image
    if moderation_response.results[0].flagged:
        # Inform the user that the image will not be generated
        print("The image will not be generated, because OpenAI thinks it is offensive.")
    else:
        # Generate images with the image generator from OpenAI
        print("The image is being generated.")

        try:
            image_response = client.images.generate(
                prompt=image_prompt, n=2, size="1024x1024"
            )

            # Show the response of the image generation, if debug = True
            if debug:
                print(image_response)

            # Generate the images and save them
            for i in range(len(image_response.data)):
                image_url = image_response.data[i].url
                if is_safe_url(image_url):
                    image_name = f"image{i+1}.png"
                    try:
                        urllib.request.urlretrieve(image_url, image_name)
                        print(f"Image {i+1} downloaded successfully.")
                    except Exception as e:
                        print(f"Error downloading image {i+1}: {e}")
                else:
                    print(
                        f"Skipping download from unsafe URL for image {i+1}: {image_url}"
                    )
        except Exception as e:
            # If an error occurs while generating the images, print it
            print(f"Error generating images: {e}")

# If an error occurs, print it
except Exception as e:
    print(f"Error in moderation check: {e}")
    print(moderation_response)
