
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

GATEWAY_URL = (
    "https://customersupportgateway-hh7q2whxua.gateway."
    "bedrock-agentcore.us-east-1.amazonaws.com/mcp"
)

async def main():
    async with streamable_http_client(GATEWAY_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            response = await session.call_tool(
                "refund-processor___get_return_label",
                arguments={"order_id": "ORD-001"}
            )
            print(response)

            for tool in result.tools:
                print(tool.name)

asyncio.run(main())
