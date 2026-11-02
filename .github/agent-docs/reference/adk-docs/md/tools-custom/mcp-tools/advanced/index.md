Skip to content 

**Released!** [ ADK TypeScript 2.0 GA ](/2.0/) is now available with graph workflows support! [Get started](/graphs/#typescript)

[ ](../../.. "Agent Development Kit \(ADK\)")

[ Agent Development Kit (ADK) ](../../.. "Agent Development Kit \(ADK\)")

Advanced configuration 

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
      * [ Service registration  ](../../../agents/service-registration/)
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

Gemini 
        * [ Deferred scheduling  ](../../../agents/models/google-gemini/deferred-schedule/)
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
        * Advanced configuration  [ Advanced configuration  ](./) Table of contents 
          * Advanced configuration patterns 
          * Dynamic authentication and per-user headers (header_provider) 
          * Human-in-the-loop and tool confirmations (require_confirmation) 
          * Real-time progress tracking (progress_callback) 
            * Option A: Global callback function 
            * Option B: Per-tool callback factory (Session-Aware) 
          * Standalone runner execution (Outside adk web) 
          * Name collisions and tool namespacing (tool_name_prefix) 
          * Bi-directional protocol hooks: sampling and elicitation 
          * Diagnostic logging and error streams (errlog) 
          * Render interactive UI widgets 
            * How it works 
          * Dynamic instructions with McpInstructionProvider 
          * Next Steps 
        * [ Deployment  ](../deployment/)
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
      * [ Architectures  ](../../../live/architectures/)

Architectures 
        * [ Speech-to-speech  ](../../../live/architectures/speech-to-speech/)
        * [ Cascade  ](../../../live/architectures/cascade/)
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

  * Advanced configuration patterns 
  * Dynamic authentication and per-user headers (header_provider) 
  * Human-in-the-loop and tool confirmations (require_confirmation) 
  * Real-time progress tracking (progress_callback) 
    * Option A: Global callback function 
    * Option B: Per-tool callback factory (Session-Aware) 
  * Standalone runner execution (Outside adk web) 
  * Name collisions and tool namespacing (tool_name_prefix) 
  * Bi-directional protocol hooks: sampling and elicitation 
  * Diagnostic logging and error streams (errlog) 
  * Render interactive UI widgets 
    * How it works 
  * Dynamic instructions with McpInstructionProvider 
  * Next Steps 



  1. [ Home  ](../../..)
  2. [ Components  ](../../../get-started/about/)
  3. [ Custom Tools  ](../../)
  4. [ MCP tools  ](../)

[ ](https://github.com/google/adk-docs/edit/main/docs/tools-custom/mcp-tools/advanced.md "Edit this page on GitHub") [ ](./index.md "View this page as Markdown")

# Advanced MCP configuration¶

Supported in ADKPython v0.1.0

This guide covers advanced integration patterns for the Model Context Protocol (MCP) in ADK. It provides production patterns for dynamic per-user authentication, human-in-the-loop approvals, long-running progress tracking, custom runtime execution, and enterprise cloud deployments.

## Advanced configuration patterns¶

Use the matrix below to select the right configuration mechanism for your production workload:

Developer Requirement | Recommended Mechanism | Primary API / Parameter | Typical Scenario  
---|---|---|---  
**Inject per-user credentials or dynamic session tokens** | Dynamic Header Provider | `header_provider=...` | Multi-tenant apps, per-user JWTs/OAuth tokens  
**Require approval before dangerous tool calls** | Tool Confirmation | `require_confirmation=...` | Database mutations, destructive shell/file ops  
**Stream real-time progress for long operations** | Progress Callback & Factory | `progress_callback=...` | Heavy SQL queries, web scraping, data indexing  
**Run agents in FastAPI / backend services without`adk web`** | Programmatic Runner Lifecycle | `Runner` \+ `await toolset.close()` | Custom microservices, CLI tools, worker queues  
**Resolve tool naming collisions across servers** | Tool Namespacing & Filtering | `tool_name_prefix`, `tool_filter` | Aggregating multiple MCP servers (DB + GitHub)  
**Handle server-requested sampling or auth challenges** | Bi-directional Protocol Callbacks | `sampling_callback`, `elicitation_callback` | Server-initiated LLM generation & auth prompts  
**Inspect raw STDERR diagnostic streams** | Diagnostic Stream Logging | `errlog=sys.stderr` | Troubleshooting MCP subprocess crashes  
**Render rich, interactive visual widgets in chat** | Experimental UI Rendering | `meta.ui.resourceUri` | Maps, charts, weather cards, or custom forms  
**Fetch agent instructions dynamically from an MCP server** | Dynamic Instruction Provider | `McpInstructionProvider` | Centralized prompt management via MCP servers  
  
* * *

## Dynamic authentication and per-user headers (`header_provider`)¶

In multi-tenant or user-facing systems, hardcoding credentials into connection parameters is insecure. `McpToolset` supports `header_provider`, an asynchronous or synchronous callable that receives the active `ReadonlyContext` to dynamically construct authentication headers on every tool invocation.
    
    
    from google.adk.agents import LlmAgent
    from google.adk.agents.readonly_context import ReadonlyContext
    from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
    
    async def extract_per_user_headers(context: ReadonlyContext) -> dict[str, str]:
        """Dynamically extracts session state or per-user token on every turn."""
        user_token = context.state.get("user_access_token", "ANONYMOUS_TOKEN")
        return {
            "Authorization": f"Bearer {user_token}",
            "X-User-ID": context.user_id,
            "X-Session-ID": context.session.id,  # Fixed: access session.id
        }
    
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://mcp-server.example.com/mcp",
            timeout=5,
            sse_read_timeout=300,
        ),
        header_provider=extract_per_user_headers,
    )
    

* * *

## Human-in-the-loop and tool confirmations (`require_confirmation`)¶

MCP servers can expose high-impact capabilities, for example: database schema modifications or record deletions. You can enforce confirmation globally across all tools in the toolset or conditionally via a predicate function that inspects tool arguments.
    
    
    from typing import Any
    from google.adk.agents import LlmAgent
    from google.adk.tools.mcp_tool import McpToolset
    from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
    from mcp import StdioServerParameters
    
    def should_require_approval(query: str = "", **kwargs) -> bool:
        query_str = str(query).lower()
        destructive_keywords = ["drop", "delete", "truncate", "alter", "update"]
        return any(keyword in query_str for keyword in destructive_keywords)
    
    toolset = McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/db"],
            ),
            timeout=5,
        ),
        require_confirmation=should_require_approval,  # Can also be a boolean (True)
    )
    
    root_agent = LlmAgent(
        model="gemini-flash-latest",
        name="db_administrator",
        instruction="Execute database queries safely with explicit approval for mutations.",
        tools=[toolset],
    )
    

* * *

## Real-time progress tracking (`progress_callback`)¶

Long-running MCP operations, such as scraping large websites or training jobs, send intermediate progress notifications over the `notifications/progress` channel.

### Option A: Global callback function¶

Assign a shared callback for simple logging or progress reporting:
    
    
    async def on_mcp_progress(progress: float, total: float | None, message: str | None) -> None:
        percentage = (progress / total * 100) if total else progress
        print(f"[MCP Progress] {percentage:.1f}% complete: {message or 'Working...'}")
    
    toolset = McpToolset(
        connection_params=...,
        progress_callback=on_mcp_progress,
    )
    

### Option B: Per-tool callback factory (Session-Aware)¶

Use `ProgressCallbackFactory` to inject tool-specific callbacks with write access to `ToolContext.state`:
    
    
    from google.adk.tools.tool_context import ToolContext
    
    def create_tool_progress_tracker(tool_name: str, callback_context: ToolContext, **kwargs):
        """Generates custom progress handlers and updates active agent session state."""
        async def progress_handler(progress: float, total: float | None, message: str | None):
            callback_context.state[f"{tool_name}_status"] = message
            callback_context.state[f"{tool_name}_progress"] = progress
        return progress_handler
    
    toolset = McpToolset(
        connection_params=...,
        progress_callback=create_tool_progress_tracker,
    )
    

* * *

## Standalone runner execution (Outside `adk web`)¶

When embedding ADK agents into custom FastAPI applications, background workers, or standalone CLI scripts, instantiate `Runner` and manage lifecycle teardown explicitly via `await toolset.close()`.
    
    
    import asyncio
    import os
    from google.genai import types
    from google.adk.agents import LlmAgent
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.adk.tools.mcp_tool import McpToolset
    from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
    from mcp import StdioServerParameters
    
    async def run_standalone_mcp_agent():
        # 1. Define McpToolset and Agent synchronously
        toolset = McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-filesystem", os.path.abspath("./data")],
                ),
                timeout=5,
            ),
            tool_filter=["list_directory", "read_file"],
        )
    
        agent = LlmAgent(
            model="gemini-flash-latest",
            name="filesystem_assistant",
            instruction="Assist users with file management.",
            tools=[toolset],
        )
    
        # 2. Setup Session and Runner
        session_service = InMemorySessionService()
        session = await session_service.create_session(
            app_name="standalone_mcp_app",
            user_id="user_001",
        )
    
        runner = Runner(
            app_name="standalone_mcp_app",
            agent=agent,
            session_service=session_service,
        )
    
        try:
            # 3. Stream agent execution
            user_message = types.Content(
                role="user",
                parts=[types.Part(text="List the files available in the directory.")],
            )
    
            async for event in runner.run_async(
                session_id=session.id,
                user_id=session.user_id,
                new_message=user_message,
            ):
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            print(part.text, end="", flush=True)
        finally:
            # 4. Gracefully terminate subprocesses and network connections
            print("\nTerminating MCP connection...")
            await toolset.close()
    
    if __name__ == "__main__":
        asyncio.run(run_standalone_mcp_agent())
    

* * *

## Name collisions and tool namespacing (`tool_name_prefix`)¶

When you connect to multiple MCP servers, tool names such as `query` or `search` can conflict. Use `tool_name_prefix` to automatically namespace discovered tools:
    
    
    from google.adk.tools.mcp_tool import McpToolset
    from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
    from mcp import StdioServerParameters
    
    postgres_toolset = McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/db"],
            )
        ),
        tool_name_prefix="pg_",  # Generates pg_query, pg_list_tables
    )
    
    github_toolset = McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-github"],
            )
        ),
        tool_name_prefix="gh_",  # Generates gh_search_repositories, gh_create_issue
    )
    

* * *

## Bi-directional protocol hooks: sampling and elicitation¶

The Model Context Protocol supports bi-directional interaction where servers can request actions from clients: \- **Sampling (`sampling_callback`)**: Allows the MCP server to ask the ADK host to generate an LLM completion. \- **Elicitation (`elicitation_callback`)**: Allows the MCP server to request out-of-band user interactions or authentication flows.
    
    
    from mcp import SamplingCapability
    from google.adk.tools.mcp_tool import McpToolset
    
    async def handle_server_sampling(params):
        """Processes server-initiated LLM generation requests."""
        return {
            "role": "assistant",
            "content": {"type": "text", "text": "Generated response from ADK"},
        }
    
    async def handle_server_elicitation(params):
        """Handles authentication or interactive challenges from the server."""
        print(f"Elicitation requested: {params}")
        return {"action": "approved"}
    
    toolset = McpToolset(
        connection_params=...,
        sampling_callback=handle_server_sampling,
        sampling_capabilities=SamplingCapability(),
        elicitation_callback=handle_server_elicitation,
    )
    

* * *

## Diagnostic logging and error streams (`errlog`)¶

By default, MCP subprocess errors are logged to standard error. You can redirect STDERR streams to an external file or diagnostic buffer for root-cause debugging:
    
    
    import sys
    from google.adk.tools.mcp_tool import McpToolset
    
    error_file = open("mcp_server_errors.log", "a")
    try:
        toolset = McpToolset(connection_params=..., errlog=error_file)
        # Run agent...
    finally:
        await toolset.close()
        error_file.close()
    

## Render interactive UI widgets¶

Standard MCP tools return plain text or JSON output. This feature enables MCP tools to return rich, interactive visual widgets, such as maps, charts, or forms, directly inside the chat interface.
    
    
    sequenceDiagram
        autonumber
        participant Tool as MCP Server Tool
        participant ADK as ADK Framework
        participant UI as Client UI (adk web / Frontend)
    
        Tool-->>ADK: Returns result + metadata (meta.ui.resourceUri = "ui://widgets/map")
        ADK->>ADK: Detects meta.ui.resourceUri annotation
        ADK-->>UI: Emits Event with UI rendering signal & Resource URI
        UI->>Tool: Fetches UI bundle from Resource URI
        UI-->>UI: Renders interactive widget in chat interface

### How it works¶

  1. **Tool Registration** : The MCP tool declares a UI resource link in its schema definition metadata during `tools/list`: `meta.ui.resourceUri = "ui://widgets/weather-card"`.
  2. **ADK Detection** : ADK reads the schema definition to detect `meta.ui.resourceUri` and knows this tool supports an interactive UI.
  3. **Client Display** : Upon tool execution, ADK signals the web UI (`adk web` or custom frontend) to fetch the UI resource and render an interactive widget instead of plain text.


    
    
    from mcp import types as mcp_types
    from mcp.server.lowlevel import Server
    
    app = Server("weather-mcp-server")
    
    
    @app.list_tools()
    async def list_mcp_tools() -> list[mcp_types.Tool]:
      """Declares the tool and attaches UI rendering metadata."""
      return [
          mcp_types.Tool(
              name="get_weather",
              description="Get weather forecast for a city.",
              inputSchema={
                  "type": "object",
                  "properties": {"city": {"type": "string"}},
                  "required": ["city"],
              },
              meta={"ui": {"resourceUri": "ui://widgets/weather-card"}},
          )
      ]
    
    
    @app.call_tool()
    async def call_mcp_tool(name: str, arguments: dict) -> list[mcp_types.Content]:
      """Executes the tool and returns standard text/data content."""
      if name == "get_weather":
        city = arguments.get("city", "Unknown")
        return [
            mcp_types.TextContent(
                type="text", text=f"Weather in {city}: 72°F Sunny"
            )
        ]
      return [
          mcp_types.TextContent(type="text", text=f"Unknown tool: '{name}'")
      ]
    

* * *

## Dynamic instructions with `McpInstructionProvider`¶

Supported in ADKPython v1.18.0

To manage agent instructions dynamically in Python, use `McpInstructionProvider`. This class fetches agent instructions from a Model Context Protocol (MCP) server.

Initialize `McpInstructionProvider` with MCP server connection parameters and the name of the prompt to fetch. Pass this instance to the `instruction` parameter of `LlmAgent`:
    
    
    from google.adk.agents import LlmAgent, McpInstructionProvider
    from google.adk.tools.mcp_tool import SseConnectionParams
    
    # Define the MCP connection parameters.
    mcp_connection_params = SseConnectionParams(
        url="https://mcp.example.com",
        headers={"Authorization": "Bearer YOUR_MCP_API_KEY"},
    )
    
    # Create an instance of the instruction provider.
    instruction_provider = McpInstructionProvider(
        connection_params=mcp_connection_params,
        prompt_name="my-agent-prompt",
    )
    
    # Use the instruction provider in the agent.
    my_agent = LlmAgent(
        model="gemini-2.0-flash",
        name="my_mcp_agent",
        instruction=instruction_provider,
    )
    

Caution

Instructions fetched from an MCP server directly control your agent's behavior. Only connect to MCP servers that you trust, and protect any credentials used in the connection parameters.

* * *

## Next Steps¶

  * Return to the [Model Context Protocol Overview](../) for basic setup.
  * Explore [Custom Function Tools](../../function-tools/) for in-process Python tools.
  * Read the [ADK Deployment Guide](../../../deploy/) for full cloud configuration options.



Back to top 

Copyright Google 2026  |  [License](//github.com/google/adk-docs/blob/main/LICENSE)  |  [Privacy](//policies.google.com/privacy)  |  Manage cookies

Made with [ Material for MkDocs ](https://squidfunk.github.io/mkdocs-material/)

#### Cookie consent

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better.

  * Google Analytics 
  * GitHub 



Accept Manage settings
