from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as sessions:

            await sessions.initialize()

            tools = await sessions.list_tools()
            print(tools)

            result = await sessions.call_tool("add_two_numbers", arguments={"a":4,"b":5})
            print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())