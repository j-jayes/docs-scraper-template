[ Model Context Protocol （MCP） ](https://modelcontextprotocol.info/)[Home ](https://modelcontextprotocol.info/)[Get Started ](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)[Develop ](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)[Connect and Run ](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)[Protocol and Versions ](https://modelcontextprotocol.info/specification/)[Reference ](https://modelcontextprotocol.info/tools/)[Blog ](https://modelcontextprotocol.info/blog/)[About](https://modelcontextprotocol.info/about/)

`CTRL K`




`CTRL K`




  * [Get Started](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)

    * [What is MCP?](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)
    * [Architecture and roles](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/)
    * [Servers and primitives](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/)
    * [Hosts and clients](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/)

  * [Develop](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

    * [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)
    * [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)
    * [Choose an SDK](https://modelcontextprotocol.info/docs/2026-07-28/sdk/)
    * [Build with agent skills](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-with-agent-skills/)
    * [Node.js client: calls and failures without a model](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/)
    * [Design and check effective tools](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/)

  * [Connect and Run](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)

    * [Connect a local server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)
    * [Connect a remote server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)
    * [Authorization with OAuth 2.1](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/)
    * [Local server security defaults](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/)
    * [Security checklist before launch](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/)
    * [Host applications at scale](https://modelcontextprotocol.info/docs/2026-07-28/develop/clients/client-best-practices/)
    * [Troubleshoot connections and calls](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)
    * [Inspector: test a server interactively](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
    * [Inspector CLI: scripted checks and CI](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)
    * [Inspector recipes: transports, Docker, config import](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/)
    * [Inspector lab: reproducible calls and failure diagnosis](https://modelcontextprotocol.info/tools/inspector/)

  * [Protocol and Versions](https://modelcontextprotocol.info/specification/)

    * [Version negotiation rules](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)
    * [Revision and method matrix](https://modelcontextprotocol.info/specification/)
    * [Key changes in 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/changelog/)
    * [Deprecated features](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/)
    * [Legacy and modern protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/)
    * [Client extension support matrix](https://modelcontextprotocol.info/extensions/client-matrix/)

  * [Reference](https://modelcontextprotocol.info/tools/)

    * [Tools and Registry overview](https://modelcontextprotocol.info/tools/)
    * [Production checklist](https://modelcontextprotocol.info/docs/best-practices/)
    * [Client capability matrix](https://modelcontextprotocol.info/docs/clients/)
    * [Tools: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/tools/)
    * [Resources: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/resources/)
    * [Prompts: definitions and trade-offs](https://modelcontextprotocol.info/docs/concepts/prompts/)
    * [Sampling: deprecated server requests for client model calls](https://modelcontextprotocol.info/docs/concepts/sampling/)
    * [Current transports: stdio and Streamable HTTP](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/)
    * [Publish a server to the Registry](https://modelcontextprotocol.info/tools/registry/publishing/)
    * [Official SEP status index](https://modelcontextprotocol.info/seps/)
    * [SEP impact and method lifecycle guide](https://modelcontextprotocol.info/docs/reference/sep-impact-guide/)
    * [FAQ: revisions, authorization and failure handling](https://modelcontextprotocol.info/docs/faqs/)

  * In this section

    * [MCP Docs](https://modelcontextprotocol.info/docs/)
    * [Debugging](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/debugging/)



  * Light 

  * Dark 

  * System 




On this page

  * Debugging tools overview
  * Implementing logging
  * Server-side logging
  * Common issues
  * Working directory
  * Environment variables
  * Server startup
  * Connection problems
  * Debugging in Claude Desktop
  * Checking server status
  * Viewing logs
  * Using Chrome DevTools
  * Debugging workflow
  * Development cycle
  * Testing changes
  * Best practices
  * Logging strategy
  * Security considerations
  * Getting help
  * Next steps
  * MCP Inspector
  * Build an MCP server
  * Connect local servers



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

Debugging

# Debugging

Source: [MCP 89153404](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/891534049ae842de72190fe4af7ce9a0f7c045e6/docs/docs/2026-07-28/tools/debugging.mdx)

## Troubleshoot from the last successful step

A connection can fail while starting a process, parsing a message, negotiating a revision or executing a tool. Record the absolute executable, arguments, working directory, SDK package versions, actual protocol revision and last successful method. Keep only redacted error codes and correlation IDs; never attach credentials, a full environment dump or user files.

Last visible result| Check first| What it tells you  
---|---|---  
No process; `ENOENT`| Executable exists; GUI and shell PATH differ| Tool arguments cannot repair a process that never started  
Immediate process exit| Run the same command, inspect stderr and exit status; use absolute config paths| A successful terminal run does not establish the host's cwd  
stdout starts with `Server starting...`| Startup banners and dependency initialization output| A JSON-RPC parsing failure is not a version mismatch  
Discovery works; a call fails| Protocol error, `isError` tool result, timeout or closed connection| Treat input, application and transport failures separately  
Legacy works; modern fails| Peer support for `2026-07-28`, discovery and per-request `_meta`| An SDK package version is not a protocol revision  
  
### Reproduce a clean and a polluted stdout

Copy `inspector_smoke.py` and `sdk_server.py` from [the Inspector lab](https://modelcontextprotocol.info/tools/inspector/) into a practice environment with `mcp==2.3.0`:
    
    
    python3 inspector_smoke.py --call add --arg a=2 --arg b=3 --check-stdout -- python3 sdk_server.py stdio ok
    python3 inspector_smoke.py --check-stdout -- python3 sdk_server.py stdio banner
    python3 inspector_smoke.py --check-stdout -- python3 sdk_server.py stdio crash

On 2026-10-30, Inspector `2.12.0`, Node `24.18.0` and Python `3.11.12` reproduced all three: the clean server discovered tools, returned `5` and passed stdout validation; the pre-start banner failed stdout validation; the exiting server failed connection. The banner explicitly flushes so buffering cannot hide it. Do not infer that every print corrupts the stream: this SDK redirects prints inside a running tool, while pre-start output still needs control.

For HTTP, compare with a successful discovery request: local stubs returning 401, 403, 404 or HTML with status 200 all failed MCP connection. These are different causes, and HTML 200 is not protocol success; see [remote connections](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/). The actual SDK also rejected an unsupported revision with `-32022`. Do not infer one particular missing `_meta` field from `-32602` alone; inspect the request and error data.

This run did not open Claude Desktop or another host UI. Check the pinned source's menus, shortcuts and platform statements against your installed client and its help. Models, real remote login, the weather API and every language SDK were outside this test.

Effective debugging is essential when developing MCP servers or integrating them with applications. This guide covers the debugging tools and approaches available in the MCP ecosystem.

## Debugging tools overview

MCP provides several tools for debugging at different levels:

  1. **[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)** : interactive, transport-agnostic testing UI. Connect to stdio or Streamable HTTP servers, invoke [tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/), [prompts](https://modelcontextprotocol.info/specification/2026-07-28/server/prompts/), and [resources](https://modelcontextprotocol.info/specification/2026-07-28/server/resources/), and watch the notification stream. This should be your first stop.
  2. **Server logging** : structured logs to stderr (stdio transport) or via [OpenTelemetry](https://opentelemetry.io/) (all transports). [Logging](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/logging/) over the protocol (`notifications/message`) is deprecated as of protocol version `2026-07-28`.
  3. **Client developer tools** : most MCP clients expose logs and connection state. See Debugging in Claude Desktop below for one example, or consult your client's documentation.



## Implementing logging

### Server-side logging

When building a server that uses the local [stdio transport](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/stdio/), all messages logged to stderr (standard error) will be captured by the host application automatically.

Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation.

For servers using the [Streamable HTTP transport](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/), stderr is not captured by the client. Use your own server-side log aggregation or [OpenTelemetry](https://opentelemetry.io/) for logs, and standard HTTP tooling (curl, browser DevTools Network panel) to inspect requests and SSE streams.

The `notifications/message` mechanism below is deprecated as of protocol version `2026-07-28`. It remains available during the deprecation window.

For all [transports](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/), record what the server is doing as it runs:
    
    
    import logging
    
    from mcp.server import MCPServer
    
    logger = logging.getLogger(__name__)
    
    mcp = MCPServer("reports")
    
    
    @mcp.tool()
    async def fetch_report(report_id: str) -> str:
        """Fetch a report by id."""
        logger.info("Fetching report %s", report_id)
        return f"Report {report_id} is ready."
    
    
    await server.sendLoggingMessage({
      level: "info",
      data: "Server started successfully",
    });

MCP defines eight [RFC 5424 severity levels](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/logging/#log-levels) (`debug` through `emergency`). Clients opt in to log messages per request by setting the [`io.modelcontextprotocol/logLevel`](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/logging/#per-request-log-level) field in the request's `_meta`. Servers must not send `notifications/message` for requests that omit this field.

Important events to log:

  * Startup steps
  * Resource access
  * Tool execution
  * Error conditions
  * Performance metrics



## Common issues

The examples below use Claude Desktop's [`claude_desktop_config.json`](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/); the same principles apply to any stdio-based MCP client.

### Working directory

When an MCP client launches a stdio server:

  * The working directory for servers launched via the client's config may be undefined (like `/` on macOS) since the client could be started from anywhere
  * Always use absolute paths in your configuration and `.env` files to ensure reliable operation
  * For testing servers directly via command line, the working directory will be where you run the command



For example in `claude_desktop_config.json`, use:
    
    
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/Users/username/data"
          ]
        }
      }
    }

Instead of relative paths like `./data`

### Environment variables

MCP servers launched over stdio inherit only a limited subset of environment variables automatically (the exact set is platform-dependent).

To override the default variables or provide your own, you can specify an `env` key in `claude_desktop_config.json`:
    
    
    {
      "mcpServers": {
        "myserver": {
          "command": "mcp-server-myapp",
          "env": {
            "MYAPP_API_KEY": "some_key"
          }
        }
      }
    }

### Server startup

Common startup problems:

  1. **Path Issues**

     * Incorrect server executable path
     * Missing required files
     * Permission problems
     * Try using an absolute path for `command`
  2. **Configuration Errors**

     * Invalid JSON syntax
     * Missing required fields
     * Type mismatches
  3. **Environment Problems**

     * Missing environment variables
     * Incorrect variable values
     * Permission restrictions



### Connection problems

When servers fail to connect:

  1. Check client logs
  2. Verify server process is running
  3. Test standalone with [Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
  4. Verify [protocol compatibility](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/#negotiation): call [`server/discover`](https://modelcontextprotocol.info/specification/2026-07-28/server/discover/) to see which protocol versions the server supports. An `UnsupportedProtocolVersionError` (`-32022`) lists the server's supported versions in its `data` field
  5. Check the [per-request `_meta` fields](https://modelcontextprotocol.info/specification/2026-07-28/basic/#_meta): every request must carry `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities`, and clients should also include `io.modelcontextprotocol/clientInfo`. A request missing either required field is rejected with error `-32602` (Invalid params), the same code returned for many other malformed inputs. If the server needs a capability the request's `clientCapabilities` did not declare, such as [elicitation](https://modelcontextprotocol.info/specification/2026-07-28/client/elicitation/), it returns a `MissingRequiredClientCapabilityError` (`-32021`) naming the missing capabilities. Inspect the request's `_meta` and the [`server/discover`](https://modelcontextprotocol.info/specification/2026-07-28/server/discover/) response to verify both sides declared what you expect



## Debugging in Claude Desktop

Claude Desktop is one of many MCP clients. It is available on macOS, Windows, and Linux.

### Checking server status

Click the "Add files, connectors, and more" plus icon in the chat input, then hover over the **Connectors** menu to see connected servers and available tools.

### Viewing logs

Log files are written to:

  * macOS: `~/Library/Logs/Claude`
  * Windows: `%APPDATA%\Claude\logs`
  * Linux: `~/.config/Claude/logs`


    
    
    tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
    
    
    tail -n 20 -F ~/.config/Claude/logs/mcp*.log
    
    
    type "$env:AppData\Claude\logs\mcp*.log"

The logs capture:

  * Server connection events
  * Configuration issues
  * Runtime errors
  * Message exchanges



### Using Chrome DevTools

Access Chrome's developer tools inside Claude Desktop to investigate client-side errors:

  1. Create a `developer_settings.json` file with `allowDevTools` set to true:


    
    
    echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json
    
    
    '{"allowDevTools": true}' | Set-Content "$env:AppData\Claude\developer_settings.json"

  2. Open DevTools: `Command-Option-I` (macOS) or `Ctrl+Alt+I` (Windows)



Note: You'll see two DevTools windows:

  * Main content window
  * App title bar window



Use the Console panel to inspect client-side errors.

Use the Network panel to inspect:

  * Message payloads
  * Connection timing



## Debugging workflow

### Development cycle

  1. Initial Development

     * Use [Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/) for basic testing
     * Implement core functionality
     * Add logging points
  2. Integration Testing

     * Test in your target MCP client
     * Monitor logs
     * Check error handling



### Testing changes

To test changes efficiently:

  * **Configuration changes** : Restart the MCP client
  * **Server code changes** : Restart the client (for Claude Desktop, fully quit and reopen; closing the window is not enough)
  * **Quick iteration** : Use [Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/) during development



## Best practices

### Logging strategy

  1. **Structured Logging**

     * Use consistent formats
     * Include context
     * Add timestamps
     * Track request IDs
  2. **Error Handling**

     * Log stack traces
     * Include error context
     * Track error patterns
     * Monitor recovery
  3. **Performance Tracking**

     * Log operation timing
     * Monitor resource usage
     * Track message sizes
     * Measure latency



### Security considerations

When debugging:

  1. **Sensitive Data**

     * Sanitize logs
     * Protect credentials
     * Mask personal information
  2. **Access Control**

     * Verify permissions
     * Check authentication
     * Monitor access patterns



For a full treatment of MCP attack vectors and mitigations, see [Security Best Practices](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/).

## Getting help

When encountering issues:

  1. **First Steps**

     * Check server logs
     * Test with [Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
     * Review configuration
     * Verify environment
  2. **Support Channels**

     * [GitHub issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)
     * [GitHub discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions)
  3. **Providing Information**

     * Log excerpts
     * Configuration files
     * Steps to reproduce
     * Environment details



## Next steps

### [MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

Learn to use the MCP Inspector

### [Build an MCP server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

Walk through building a server from scratch

### [Connect local servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)

Full claude_desktop_config.json reference and troubleshooting

[Connect to remote MCP Servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/ "Connect to remote MCP Servers")[Local Server Security](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/ "Local Server Security")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
