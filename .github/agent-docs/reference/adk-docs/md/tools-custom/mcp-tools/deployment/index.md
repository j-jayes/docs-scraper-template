Skip to content 

**Released!** [ ADK TypeScript 2.0 GA ](/2.0/) is now available with graph workflows support! [Get started](/graphs/#typescript)

[ ](../../.. "Agent Development Kit \(ADK\)")

[ Agent Development Kit (ADK) ](../../.. "Agent Development Kit \(ADK\)")

Deployment 

[ Python ](https://github.com/google/adk-python "adk-python on GitHub") [ JS ](https://github.com/google/adk-js "adk-js on GitHub") [ Go ](https://github.com/google/adk-go "adk-go on GitHub") [ Java ](https://github.com/google/adk-java "adk-java on GitHub") [ Kotlin ](https://github.com/google/adk-kotlin "adk-kotlin on GitHub")

  * [ Home ](../../..)
  * [ Build Agents ](../../../get-started/)
  * [ Run Agents ](../../../runtime/)
  * [ Components ](../../../get-started/about/)
  * [ Integrations ](../../../integrations/)
  * [ Reference ](../../../api-reference/)
  * [ Community ](../../../community/)
  * [ ADK 2.0 ](../../../2.0/)



[ Python ](https://github.com/google/adk-python "adk-python on GitHub") [ JS ](https://github.com/google/adk-js "adk-js on GitHub") [ Go ](https://github.com/google/adk-go "adk-go on GitHub") [ Java ](https://github.com/google/adk-java "adk-java on GitHub") [ Kotlin ](https://github.com/google/adk-kotlin "adk-kotlin on GitHub")

  * [ Home  ](../../..)
  * Build Agents  Build Agents 
    * [ Get Started  ](../../../get-started/)

Get Started 
      * [ Python  ](../../../get-started/python/)
      * [ TypeScript  ](../../../get-started/typescript/)
      * [ Go  ](../../../get-started/go/)
      * [ Java  ](../../../get-started/java/)
      * [ Kotlin  ](../../../get-started/kotlin/)
      * [ Agents CLI  ](../../../get-started/agents-cli/)
      * [ Installation  ](../../../get-started/installation/)
      * [ Google Cloud  ](../../../get-started/google-cloud/)
      * [ Migrate to ADK  ](../../../get-started/migrate/)
    * [ Build your Agent  ](../../../tutorials/)

Build your Agent 
      * [ Multi-tool agent  ](../../../tutorials/multi-tool-agent/)
      * [ Agent team  ](../../../tutorials/agent-team/)
      * [ Code with AI  ](../../../tutorials/coding-with-ai/)
      * [ Agent Config  ](../../../agents/config/)
    * [ Agents  ](../../../agents/)

Agents 
      * [ Simple agents  ](../../../agents/llm-agents/)
      * [ Managed agents  ](../../../agents/managed-agents/)
    * [ Graph Workflows  ](../../../graphs/)

Graph Workflows 
      * [ Graph routes  ](../../../graphs/routes/)
      * [ Data handling  ](../../../graphs/data-handling/)
      * [ Human input  ](../../../graphs/human-input/)
      * [ Dynamic workflows  ](../../../graphs/dynamic/)
    * [ Multi-Agent Workflows  ](../../../workflows/)

Multi-Agent Workflows 
      * [ Collaborative workflows  ](../../../workflows/collaboration/)
      * [ Template workflows  ](../../../agents/workflow-agents/)

Template workflows 
        * [ Sequential workflow  ](../../../agents/workflow-agents/sequential-agents/)
        * [ Loop workflow  ](../../../agents/workflow-agents/loop-agents/)
        * [ Parallel workflow  ](../../../agents/workflow-agents/parallel-agents/)
        * [ Custom template workflows  ](../../../agents/custom-agents/)
      * [ Agent routing  ](../../../agents/routing/)
      * [ Workflow patterns  ](../../../workflows/patterns/)
    * [ Models for Agents  ](../../../agents/models/)

Models for Agents 
      * [ Gemini  ](../../../agents/models/google-gemini/)
      * [ Gemma  ](../../../agents/models/google-gemma/)
      * [ Claude  ](../../../agents/models/anthropic/)
      * [ Agent Platform hosted  ](../../../agents/models/agent-platform/)
      * [ Apigee AI Gateway  ](../../../agents/models/apigee/)
      * [ Model routing  ](../../../agents/models/routing/)
      * [ OpenAI  ](../../../agents/models/openai/)
      * [ Ollama  ](../../../agents/models/ollama/)
      * [ vLLM  ](../../../agents/models/vllm/)
      * [ LiteLLM  ](../../../agents/models/litellm/)
      * [ LiteRT-LM  ](../../../agents/models/litert-lm/)
  * Run Agents  Run Agents 
    * [ Agent Runtime  ](../../../runtime/)

Agent Runtime 
      * [ Web Interface  ](../../../runtime/web-interface/)

Web Interface 
        * [ Visual Builder  ](../../../visual-builder/)
      * [ Command Line  ](../../../runtime/command-line/)
      * [ API Server  ](../../../runtime/api-server/)
      * [ Ambient Agents  ](../../../runtime/ambient-agents/)
      * [ Resume Agents  ](../../../runtime/resume/)
      * [ Cancel Agent Runs  ](../../../runtime/cancel/)
      * [ Runtime Config  ](../../../runtime/runconfig/)
      * [ Event Loop  ](../../../runtime/event-loop/)
    * [ Deployment  ](../../../deploy/)

Deployment 
      * [ Agent Runtime  ](../../../deploy/agent-runtime/)

Agent Runtime 
        * [ Standard deployment  ](../../../deploy/agent-runtime/deploy/)
        * [ agents-cli  ](../../../deploy/agent-runtime/agents-cli/)
        * [ Test deployed agents  ](../../../deploy/agent-runtime/test/)
      * [ Cloud Run  ](../../../deploy/cloud-run/)
      * [ GKE  ](../../../deploy/gke/)
    * [ Observability  ](../../../observability/)

Observability 
      * [ Logging  ](../../../observability/logging/)
      * [ Metrics  ](../../../observability/metrics/)
      * [ Traces  ](../../../observability/traces/)
    * [ Evaluation  ](../../../evaluate/)

Evaluation 
      * [ Criteria  ](../../../evaluate/criteria/)
      * [ User Simulation  ](../../../evaluate/user-sim/)
      * [ Environment Simulation  ](../../../evaluate/environment_simulation/)
      * [ Custom Metrics  ](../../../evaluate/custom_metrics/)
      * [ Optimization  ](../../../optimize/)
    * [ Safety and Security  ](../../../safety/)

Safety and Security 
  * Components  Components 
    * [ Technical Overview  ](../../../get-started/about/)
    * [ Custom Tools  ](../../)

Custom Tools 
      * Function tools  Function tools 
        * [ Overview  ](../../function-tools/)
        * [ Tool performance  ](../../performance/)
        * [ Action confirmations  ](../../confirmation/)
      * [ MCP tools  ](../)

MCP tools 
        * [ Advanced configuration  ](../advanced/)
        * Deployment  [ Deployment  ](./) Table of contents 
          * Critical Deployment Requirement: Synchronous Agent Definition 
          * Quick Deployment Commands 
            * Agent Runtime 
            * Cloud Run 
          * Deployment Patterns 
            * Pattern 1: Self-Contained Stdio MCP Servers 
            * Pattern 2: Remote MCP Servers (Streamable HTTP) 
            * Pattern 3: Sidecar MCP Servers (GKE) 
          * Connection management considerations 
            * Stdio connections 
            * SSE/HTTP connections 
          * Production deployment guidelines 
            * Connection lifecycle 
            * Resource management 
            * Security 
            * Monitoring and observability 
        * [ Agent as MCP server  ](../agent-as-server/)
        * [ Sub-agent delegation  ](../agent-managed/)
      * [ OpenAPI tools  ](../../openapi-tools/)
      * [ Authentication  ](../../authentication/)
      * [ Tool limitations  ](../../../tools/limitations/)
    * [ Artifacts  ](../../../artifacts/)

Artifacts 
    * [ Skills for Agents  ](../../../skills/)

Skills for Agents 
    * [ App management  ](../../../apps/)

App management 
      * [ Callbacks  ](../../../callbacks/)

Callbacks 
        * [ Types of callbacks  ](../../../callbacks/types-of-callbacks/)
        * [ Callback patterns  ](../../../callbacks/design-patterns-and-best-practices/)
      * [ Plugins  ](../../../plugins/)
    * [ Agent context  ](../../../context/)

Agent context 
      * [ Conversational context  ](../../../sessions/)
      * [ Sessions  ](../../../sessions/session/)

Sessions 
        * [ Rewind sessions  ](../../../sessions/session/rewind/)
        * [ Migrate sessions  ](../../../sessions/session/migrate/)
      * [ State  ](../../../sessions/state/)
      * [ Events  ](../../../events/)
      * [ Memory  ](../../../sessions/memory/)
      * [ Context compression  ](../../../context/compaction/)
      * [ Model context caching  ](../../../context/caching/)
    * [ A2A Protocol  ](../../../a2a/)

A2A Protocol 
      * [ Introduction to A2A  ](../../../a2a/intro/)
      * A2A Quickstart (Exposing)  A2A Quickstart (Exposing) 
        * [ Python  ](../../../a2a/quickstart-exposing/)
        * [ Go  ](../../../a2a/quickstart-exposing-go/)
        * [ Java  ](../../../a2a/quickstart-exposing-java/)
      * A2A Quickstart (Consuming)  A2A Quickstart (Consuming) 
        * [ Python  ](../../../a2a/quickstart-consuming/)
        * [ Go  ](../../../a2a/quickstart-consuming-go/)
        * [ Java  ](../../../a2a/quickstart-consuming-java/)
        * [ Kotlin  ](../../../a2a/quickstart-consuming-kotlin/)
      * [ A2A Extension  ](../../../a2a/a2a-extension/)
    * [ Live and Voice Agents  ](../../../live/)

Live and Voice Agents 
      * [ Get started  ](../../../live/get-started/)

Get started 
        * [ Python  ](../../../live/get-started/streaming-python/)
        * [ Java  ](../../../live/get-started/streaming-java/)
      * Building  Building 
        * [ Workflows  ](../../../live/workflows/)
        * [ Tools  ](../../../live/tools/)
        * [ Sessions  ](../../../live/sessions/)
        * [ Events  ](../../../live/events/)
        * [ Audio and video  ](../../../live/audio-video/)
        * [ Configuration  ](../../../live/configuration/)
      * Production  Production 
        * [ Guardrails  ](../../../live/guardrails/)
        * [ Evaluation  ](../../../live/evaluation/)
        * [ Build a custom server  ](../../../live/custom-server/)
      * [ Supported models  ](../../../live/models/)
    * [ Grounding  ](../../../grounding/)

Grounding 
      * [ Google Search Grounding  ](../../../grounding/google_search_grounding/)
      * [ Grounding with Search  ](../../../grounding/grounding_with_search/)
  * [ Integrations  ](../../../integrations/)

Integrations 
  * Reference  Reference 
    * [ API Reference  ](../../../api-reference/)

API Reference 
      * [ Python ADK  ](../../../api-reference/python/)
      * [ TypeScript ADK  ](../../../api-reference/typescript/)
      * Go ADK  Go ADK 
        * [ Go v2.x  ](https://pkg.go.dev/google.golang.org/adk/v2)
        * [ Go v1.x  ](https://pkg.go.dev/google.golang.org/adk)
      * [ Java ADK  ](../../../api-reference/java/)
      * [ Kotlin ADK  ](../../../api-reference/kotlin/)
      * [ CLI Reference  ](../../../api-reference/cli/)
      * [ Agent Config Reference  ](../../../api-reference/agentconfig/)
      * [ REST API  ](../../../api-reference/rest/)
    * [ Release Notes  ](../../../release-notes/)
  * [ Community  ](../../../community/)

Community 
    * [ Contributing Guide  ](../../../community/contributing-guide/)
  * [ ADK 2.0  ](../../../2.0/)

ADK 2.0 



Table of contents 

  * Critical Deployment Requirement: Synchronous Agent Definition 
  * Quick Deployment Commands 
    * Agent Runtime 
    * Cloud Run 
  * Deployment Patterns 
    * Pattern 1: Self-Contained Stdio MCP Servers 
    * Pattern 2: Remote MCP Servers (Streamable HTTP) 
    * Pattern 3: Sidecar MCP Servers (GKE) 
  * Connection management considerations 
    * Stdio connections 
    * SSE/HTTP connections 
  * Production deployment guidelines 
    * Connection lifecycle 
    * Resource management 
    * Security 
    * Monitoring and observability 



  1. [ Home  ](../../..)
  2. [ Components  ](../../../get-started/about/)
  3. [ Custom Tools  ](../../)
  4. [ MCP tools  ](../)

[ ](https://github.com/google/adk-docs/edit/main/docs/tools-custom/mcp-tools/deployment.md "Edit this page on GitHub") [ ](./index.md "View this page as Markdown")

# Deploy Agents with MCP Tools¶

When deploying ADK agents that use MCP tools to production environments like Cloud Run, GKE, or Agent Runtime, you need to consider how MCP connections will work in containerized and distributed environments.

## Critical Deployment Requirement: Synchronous Agent Definition¶

Warning

When deploying agents with MCP tools, the agent and its McpToolset must be defined **synchronously** in your `agent.py` file. While `adk web` allows for asynchronous agent creation, deployment environments require synchronous instantiation.
    
    
    # CORRECT: Synchronous agent definition for deployment
    import os
    from google.adk.agents.llm_agent import LlmAgent
    from google.adk.tools.mcp_tool import McpToolset
    from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
    from mcp import StdioServerParameters
    
    _allowed_path = os.path.dirname(os.path.abspath(__file__))
    
    root_agent = LlmAgent(
        model='gemini-flash-latest',
        name='enterprise_assistant',
        instruction=f'Help user accessing their file systems. Allowed directory: {_allowed_path}',
        tools=[
            McpToolset(
                connection_params=StdioConnectionParams(
                    server_params=StdioServerParameters(
                        command='npx',
                        args=['-y', '@modelcontextprotocol/server-filesystem', _allowed_path],
                    ),
                    timeout=5,  # Configure appropriate timeouts
                ),
                # Filter tools for security in production
                tool_filter=[
                    'read_file', 'read_multiple_files', 'list_directory',
                    'directory_tree', 'search_files', 'get_file_info',
                    'list_allowed_directories',
                ],
            )
        ],
    )
    
    
    
    # WRONG: Asynchronous patterns don't work in deployment
    async def get_agent():  # This won't work for deployment
        toolset = await create_mcp_toolset_async()
        return LlmAgent(tools=[toolset])
    

## Quick Deployment Commands¶

### Agent Runtime¶
    
    
    uv run adk deploy agent_engine \
      --project=<your-gcp-project-id> \
      --region=<your-gcp-region> \
      --display_name="My MCP Agent" \
      ./path/to/your/agent_directory
    

### Cloud Run¶
    
    
    uv run adk deploy cloud_run \
      --project=<your-gcp-project-id> \
      --region=<your-gcp-region> \
      --service_name=<your-service-name> \
      ./path/to/your/agent_directory
    

## Deployment Patterns¶

### Pattern 1: Self-Contained Stdio MCP Servers¶

For MCP servers that can be packaged as npm packages or Python modules (like `@modelcontextprotocol/server-filesystem`), you can include them directly in your agent container:

**Container Requirements:**
    
    
    # Example for npm-based MCP servers
    FROM python:3.13-slim
    
    # Install Node.js and npm for MCP servers
    RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
    
    # Install your Python dependencies
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    
    # Copy your agent code
    COPY . .
    
    # Your agent can now use StdioConnectionParams with 'npx' commands
    CMD ["python", "main.py"]
    

**Agent Configuration:**
    
    
    # This works in containers because npx and the MCP server run in the same environment
    McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command='npx',
                args=["-y", "@modelcontextprotocol/server-filesystem", "/app/data"],
            ),
        ),
    )
    

### Pattern 2: Remote MCP Servers (Streamable HTTP)¶

For production deployments requiring scalability, deploy MCP servers as separate services and connect via Streamable HTTP:

**MCP Server Deployment (Cloud Run):**
    
    
    # deploy_mcp_server.py - Separate Cloud Run service using Streamable HTTP
    import contextlib
    import logging
    from collections.abc import AsyncIterator
    from typing import Any
    
    import mcp.types as types
    from mcp.server.lowlevel import Server
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
    from starlette.applications import Starlette
    from starlette.routing import Mount
    from starlette.types import Receive, Scope, Send
    
    logger = logging.getLogger(__name__)
    
    def create_mcp_server():
        """Create and configure the MCP server."""
        app = Server("adk-mcp-streamable-server")
    
        @app.call_tool()
        async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.ContentBlock]:
            """Handle tool calls from MCP clients."""
            # Example tool implementation - replace with your actual ADK tools
            if name == "example_tool":
                result = arguments.get("input", "No input provided")
                return [
                    types.TextContent(
                        type="text",
                        text=f"Processed: {result}"
                    )
                ]
            else:
                raise ValueError(f"Unknown tool: {name}")
    
        @app.list_tools()
        async def list_tools() -> list[types.Tool]:
            """List available tools."""
            return [
                types.Tool(
                    name="example_tool",
                    description="Example tool for demonstration",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "input": {
                                "type": "string",
                                "description": "Input text to process"
                            }
                        },
                        "required": ["input"]
                    }
                )
            ]
    
        return app
    
    def main(port: int = 8080, json_response: bool = False):
        """Main server function."""
        logging.basicConfig(level=logging.INFO)
    
        app = create_mcp_server()
    
        # Create session manager with stateless mode for scalability
        session_manager = StreamableHTTPSessionManager(
            app=app,
            event_store=None,
            json_response=json_response,
            stateless=True,  # Important for Cloud Run scalability
        )
    
        async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:
            await session_manager.handle_request(scope, receive, send)
    
        @contextlib.asynccontextmanager
        async def lifespan(app: Starlette) -> AsyncIterator[None]:
            """Manage session manager lifecycle."""
            async with session_manager.run():
                logger.info("MCP Streamable HTTP server started!")
                try:
                    yield
                finally:
                    logger.info("MCP server shutting down...")
    
        # Create ASGI application
        starlette_app = Starlette(
            debug=False,  # Set to False for production
            routes=[
                Mount("/mcp", app=handle_streamable_http),
            ],
            lifespan=lifespan,
        )
    
        import uvicorn
        uvicorn.run(starlette_app, host="0.0.0.0", port=port)
    
    if __name__ == "__main__":
        main()
    

**Agent Configuration for Remote MCP:**

PythonJavaKotlin
    
    
    # Your ADK agent connects to the remote MCP service via Streamable HTTP
    McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://your-mcp-server-url.run.app/mcp",
            headers={"Authorization": "Bearer your-auth-token"}
        ),
    )
    
    
    
    import java.util.Map;
    import com.google.adk.tools.mcp.StreamableHttpServerParameters;
    import com.google.adk.tools.mcp.McpToolset;
    
    // Your ADK agent connects to the remote MCP service via Streamable HTTP
    StreamableHttpServerParameters streamableParams = StreamableHttpServerParameters.builder()
            .url("https://your-mcp-server-url.run.app/mcp")
            .headers(Map.of("Authorization", "Bearer your-auth-token"))
            .build();
    
    McpToolset toolset = new McpToolset(streamableParams);
    
    
    
    import com.google.adk.kt.tools.mcp.McpConnectionParameters
    import com.google.adk.kt.tools.mcp.McpToolset
    
    // Your ADK agent connects to the remote MCP service via Streamable HTTP
    // headerProvider is suspend, so fetchToken() can await a fresh token per request;
    // it also disables session reuse, so use StreamableHttp(headers = ...) for a fixed one.
    val toolset =
        McpToolset.McpToolsetConfig(
            streamableHttpConnectionParams =
                McpConnectionParameters.StreamableHttp(
                    url = "https://your-mcp-server-url.run.app/mcp",
                ),
        ).toToolset(headerProvider = { mapOf("Authorization" to "Bearer ${fetchToken()}") })
    

### Pattern 3: Sidecar MCP Servers (GKE)¶

In Kubernetes environments, you can deploy MCP servers as sidecar containers:
    
    
    # deployment.yaml - GKE with MCP sidecar
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: adk-agent-with-mcp
    spec:
      template:
        spec:
          containers:
          # Main ADK agent container
          - name: adk-agent
            image: your-adk-agent:latest
            ports:
            - containerPort: 8080
            env:
            - name: MCP_SERVER_URL
              value: "http://localhost:8081"
    
          # MCP server sidecar
          - name: mcp-server
            image: your-mcp-server:latest
            ports:
            - containerPort: 8081
    

## Connection management considerations¶

Choose your connection type based on your scaling and infrastructure needs. 

### Stdio connections¶

  * **Pros:** Simple setup, process isolation, and works well in containers.
  * **Cons:** Process overhead; not suitable for high-scale deployments.
  * **Best for:** Development, single-tenant deployments, and simple MCP servers.



### SSE/HTTP connections¶

  * **Pros:** Network-based, scalable, and handles multiple clients.
  * **Cons:** Requires network infrastructure and authentication complexity.
  * **Best for:** Production deployments, multi-tenant systems, external MCP services, and high-volume traffic.



## Production deployment guidelines¶

Follow these core guidelines when deploying agents with MCP tools to production environments.

### Connection lifecycle¶

  * Clean up MCP connections properly using standard exit stack patterns.
  * Configure appropriate timeouts for connection establishment and requests.
  * Implement retry logic to handle transient connection failures gracefully.



### Resource management¶

  * Monitor memory usage closely for stdio MCP servers, as each connection spawns a new process.
  * Configure appropriate CPU and memory limits for MCP server processes.
  * Implement connection pooling for remote MCP servers to optimize resource consumption.



### Security¶

Security Best Practices

  * Use strict authentication headers for all remote MCP connections.
  * Restrict network access tightly between ADK agents and MCP servers.
  * Filter MCP tools using `tool_filter` to strictly limit exposed functionality.
  * Validate all MCP tool inputs to prevent prompt or command injection attacks.
  * Use restrictive, absolute file paths for filesystem MCP servers (for example, `os.path.dirname(os.path.abspath(__file__))`).
  * Apply read-only tool filters in production environments whenever possible.



### Monitoring and observability¶

  * Log all MCP connection establishment and teardown events.
  * Monitor MCP tool execution times and overall success rates.
  * Set up automated alerts for recurring MCP connection failures.



Back to top 

Copyright Google 2026  |  [License](//github.com/google/adk-docs/blob/main/LICENSE)  |  [Privacy](//policies.google.com/privacy)  |  Manage cookies

Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)

#### Cookie consent

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better.

  * Google Analytics 
  * GitHub 



Accept Manage settings
