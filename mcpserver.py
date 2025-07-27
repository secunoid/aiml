server.py
# 1. Import FastMCP
from mcp. server.fastmcp import FastMCP
# 2. Initialize MCP Server
mcp = FastMCP(name="your-server-name", version="1.0.0")
# 3. TOOLS - Functions that DO things
# (Add your tool definitions here using @mcp. tool)
# 4. RESOURCES - Data endpoints
# (Add your resource definitions here using @mcp.resource())
# 5. PROMPTS - AI assistance templates
# (Add your prompt definitions here using @mcp.prompt())
# 6. Run the server
if _name__ == "__main_":
mcp. run (transport="stdio") # or "http"