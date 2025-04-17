import sys
#sys.stdout.reconfigure(line_buffering=True)  # Ensures Cursor reads stdio live

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_alerts(state: str) -> str:
    return f"🚨 Mock alert for state: {state}"

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    return f"🌤️ Mock forecast at lat: {latitude}, lon: {longitude}"

if __name__ == "__main__":
    print("✅ MCP Weather Server Started")
    mcp.run(transport="stdio")
