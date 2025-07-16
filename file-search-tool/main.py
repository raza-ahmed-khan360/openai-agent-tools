import os
import asyncio
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, FileSearchTool

# Load API key
load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "Please set your OPENAI_API_KEY in .env"
assert os.getenv("VECTOR_STORE_ID"), "Please set your VECTOR_STORE_ID in .env"

# Replace this with your actual vector store ID from upload step
vector_store_id = os.getenv("VECTOR_STORE_ID")

# FileSearchTool setup
file_search_tool = FileSearchTool(
    vector_store_ids=[vector_store_id],
    max_num_results=3,
    include_search_results=True
)

# Define the agent
agent = Agent(
    name="doc_assistant",
    instructions=(
        "You are an assistant with access to a file-based knowledge base. "
        "Use the FileSearchTool to answer any question based on the uploaded content."
    ),
    tools=[file_search_tool],
    model="gpt-4o"
)

runner = Runner()

# CLI Entry Point
async def main():
    query = "Where is DUET located?"
    result = await runner.run(agent, query)
    print("📘 Answer:", result.final_output)

# Chainlit UI
@cl.on_chat_start
async def start_chat():
    await cl.Message(content="## 📄 Ask me anything from the uploaded documents!").send()

@cl.on_message
async def handle_message(msg: cl.Message):
    result = await runner.run(agent, msg.content.strip())
    await cl.Message(content=result.final_output).send()

# Run CLI if not in Chainlit
if __name__ == "__main__":
    asyncio.run(main())