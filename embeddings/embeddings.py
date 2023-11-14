# Description: Example of how to use the embeddings API
# Source: https://platform.openai.com/docs/guides/embeddings

from openai import OpenAI
client = OpenAI()

# Create an embedding from a prompt
response = client.embeddings.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)

print(response)