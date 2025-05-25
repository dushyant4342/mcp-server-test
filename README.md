# MCP Server

## Overview
MCP Server is a flexible and extensible server framework designed to expose programmable tools, APIs, and automation agents in a unified, discoverable, and secure way. MCP servers are ideal for integrating AI, automation, and custom business logic into applications, workflows, and developer tools.

---

## Use Cases
- **AI Agent Hosting:** Run AI-powered tools and assistants that can interact with users, data, or external APIs.
- **Automation Gateways:** Expose automation scripts and business logic as callable tools for integration with other systems.
- **Developer Productivity:** Provide code completion, code intelligence, and other developer tools via standardized interfaces.
- **Mock/Test Servers:** Quickly prototype and test tool integrations before deploying to production.
- **Custom API Aggregation:** Combine multiple APIs and tools into a single, discoverable endpoint.

---

## Features
- **Tool Registration:** Easily register Python functions as callable tools using decorators.
- **Async Support:** Native support for asynchronous tools and workflows.
- **Transport Flexibility:** Supports multiple transports (e.g., stdio, HTTP, sockets) for integration with various clients.
- **Secure and Isolated:** Tools can be sandboxed and permissions can be managed per tool.
- **Extensible:** Add new tools, transports, and integrations with minimal effort.
- **Discoverability:** Tools are self-describing and can be discovered by clients.

---

## Definitions
- **Tool:** A function or method exposed by the MCP server that can be called remotely.
- **Transport:** The mechanism by which clients communicate with the MCP server (e.g., stdio for CLI, HTTP for web).
- **Agent:** An AI or automation agent that can use tools to perform tasks.
- **Tool Decorator:** A Python decorator (`@mcp.tool()`) used to register a function as a tool.

---

## Example Tools
- `get_alerts(state: str)`: Returns weather alerts for a given state.
- `get_forecast(latitude: float, longitude: float)`: Returns weather forecasts for a specific location.

---

## Example: Weather MCP Server
```python
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
```

---

## MCP Server Architecture
- **Core Server:** Handles tool registration, request routing, and transport management.
- **Tool Layer:** User-defined Python functions registered as tools.
- **Transport Layer:** Supports various communication protocols.
- **Security Layer:** Manages authentication, authorization, and sandboxing.

---

## How to Use
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/dushyant4342/mcp-server-test.git
   cd mcp-server-test
   ```
2. **Install Requirements:**
   (Add requirements.txt as needed)
3. **Run the Example Server:**
   ```sh
   python weather.py
   ```

---

## More Information
For more details, see the code examples and comments in the repository, or open an issue for questions and suggestions.
