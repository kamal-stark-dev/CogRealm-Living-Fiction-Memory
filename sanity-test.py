import asyncio
import sys

# This fixes a surprising number of asyncio/SSL issues on Windows.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import cognee
from cognee import SearchType

async def test():
    try:
        print("Adding data to Cognee...")
        await cognee.remember(
            "Naruto Uzumaki is a ninja from Konohagakure. His best friend is Sasuke Uchiha."
        )

        print("Cognifying...")
        await cognee.cognify()

        print("Searching...")
        response = await cognee.recall(
            query_type=SearchType.GRAPH_COMPLETION,
            query_text="Who is Naruto's best friend?"
        )

        print(response)
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(test())
