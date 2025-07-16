import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 1. Upload the file
file = openai.files.create(
    file=open("knowledge.txt", "rb"),
    purpose="assistants"
)

# 2. Create a vector store
vector_store = openai.vector_stores.create(name="My File Search Store")

# 3. Upload the file to the vector store (new syntax)
openai.vector_stores.files.create_and_poll(
    vector_store_id=vector_store.id,
    file_id=file.id
)

# 4. Print the result
print("✅ Uploaded to Vector Store ID:", vector_store.id)
