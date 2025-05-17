import asyncio
from langgraph.runtime_inmem import run_graph, GraphConfig
from ollama_deep_researcher.graph import graph
from dotenv import load_dotenv

load_dotenv()


async def main():
    cfg = GraphConfig(app_id="ollama_deep_researcher")
    result = await run_graph(graph, input={"topic": "future of generative AI"}, config=cfg)
    print(result["final_summary"])

if __name__ == "__main__":
    asyncio.run(main())
