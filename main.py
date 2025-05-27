from fastmcp import FastMCP
import os
from loguru import logger

# Simple test server
mcp = FastMCP(name="TestMCP")

@mcp.tool()
def test_tool() -> str:
    """Simple test tool"""
    return "Hello from Attio MCP!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting on port {port}")
    mcp.run(transport="sse", host="0.0.0.0", port=port)
