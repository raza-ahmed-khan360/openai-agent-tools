import asyncio, os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, WebSearchTool

# Load API key from .env
load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "Please set your OPENAI_API_KEY in .env"

# Create agent with WebSearchTool
agent = Agent(
    name="weather_bot",
    instructions="""
    You are a weather assistant. When a user asks about the weather,
    use the WebSearchTool to get current weather information.
    Do not guess. Respond with concise summaries.
    """,
    tools=[WebSearchTool()],
    model="gpt-4o"
)

runner = Runner()

# Optional CLI test
async def main():
    result = await runner.run(agent, "What's the weather in Karachi today?")
    print("CLI:", result.final_output)

# Chainlit UI
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="## 🌦️ Welcome! Ask me about the weather in any city (e.g., `Weather in Karachi`)."
    ).send()

@cl.on_message
async def on_user_message(message: cl.Message):
    result = await runner.run(agent, message.content.strip())
    await cl.Message(content=result.final_output).send()

if __name__ == "__main__":
    asyncio.run(main())
