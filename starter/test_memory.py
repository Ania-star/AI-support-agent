from dotenv import load_dotenv
import os
from bedrock_agentcore.memory import MemoryClient

load_dotenv()

client = MemoryClient(region_name="us-east-1")

memories = client.retrieve_memories(
    memory_id=os.environ["MEMORY_ID"],
    namespace="cs_agent/CUST-123/preferences",
    query="email notifications SMS communication preference",
    top_k=10,
)

for memory in memories:
    print(memory)