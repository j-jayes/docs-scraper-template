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
    * [MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/)



  * Light 

  * Dark 

  * System 




On this page

  * Quickstart
  * Web
  * CLI
  * TUI
  * Inspecting published servers
  * npm package
  * PyPI package
  * Remote HTTP server
  * Launcher flags vs. client flags
  * Where to go next
  * Web client
  * CLI client
  * TUI client
  * Configuration and flags
  * Authorization
  * Protocol eras
  * mcpdo connection client
  * Security
  * Recipes
  * Debugging guide



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

MCP Inspector

# MCP Inspector

Source: [MCP d998c804](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/d998c8049b8850d49d1fe3389ebf0e4a63262ab5/docs/docs/2026-07-28/tools/inspector.mdx)

## Start with one question and one observable result

Use the Web client when you need to inspect individual requests or understand a server's capabilities interactively. Use the CLI when the result must be checked by a script, and the TUI when you want an interactive session without a browser. These are different clients for the same debugging task; starting all three does not provide three independent proofs that your server works.

Keep the first check narrow: discover a known server, list its tools, then call one harmless tool with valid arguments. Listing tools proves discovery, not successful execution. If the call fails, retain the method, transport, protocol era, and error category before changing configuration. Use synthetic inputs rather than production data.

Observation| Check next  
---|---  
The Web UI opens, but no server is connected| Inspect the target command or remote URL and transport; UI startup is not server startup  
Tools are listed, but a call fails| Check that tool's input schema, required arguments, permissions, and returned error  
An expected feature or tab is absent| Compare the selected protocol era and server capabilities before reinstalling  
An unattended CLI command waits for login| Use the documented stored-auth-only workflow for automation and provision credentials separately  
A local check succeeds but a remote check fails| Check routing, authorization, and the actual remotely reachable address before changing business logic  
  
Read the [CLI recipes](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/) for machine assertions, [protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/) for legacy/modern differences, and [security](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/) before sharing a listener. This guide is tied to the attributed documentation revision; it does not claim that whichever package `npx` resolves today was tested by this site.

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is the reference developer tool for testing and debugging [MCP servers](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/). It ships as a single package, `@modelcontextprotocol/inspector`, providing **three clients behind one binary** :

Client| Invocation| What it's for  
---|---|---  
**Web**| `npx @modelcontextprotocol/inspector`| A full graphical inspector in the browser. The default, and the richest surface.  
**CLI**| `npx @modelcontextprotocol/inspector --cli`| A scriptable, machine-readable client for CI, shell pipelines, and coding agents.  
**TUI**| `npx @modelcontextprotocol/inspector --tui`| An interactive terminal UI, for when a browser isn't available or wanted.  
  
All three are built on the same shared core, so a connection behaves identically across them: the same transports, the same configuration files, the same OAuth state on disk, and the same [protocol-era](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/) negotiation (legacy vs. modern 2026-07-28).

The package also installs **`mcpdo`** , an experimental [connection client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/) that connects to a server once and keeps it open across many commands, on the same core.

## Quickstart

The Inspector requires **Node 22.19.0 or newer** and runs directly through `npx`. No installation is required:

#### Web
    
    
    # Launch the web UI and connect to a local stdio server
    npx @modelcontextprotocol/inspector node path/to/server/index.js
    
    # Or launch with no target and add servers from the UI
    npx @modelcontextprotocol/inspector

The command prints a URL carrying a per-launch API token and opens it in your browser (set `MCP_AUTO_OPEN_ENABLED=false` to stop it opening). See [Web client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/).

#### CLI
    
    
    # List a server's tools and exit
    npx @modelcontextprotocol/inspector --cli node path/to/server/index.js --method tools/list
    
    # Call a tool and pipe the result into jq
    npx @modelcontextprotocol/inspector --cli https://api.example.com/mcp --transport http \
      --method tools/call --tool-name get_weather --tool-arg city=Boston --format json | jq .result

See [CLI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/).

#### TUI
    
    
    npx @modelcontextprotocol/inspector --tui node path/to/server/index.js

See [TUI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/tui/).

### Inspecting published servers

Pass the command that launches the server as the Inspector's arguments, or point it at a remote server with `--server-url`:

#### npm package
    
    
    npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ~/Desktop

#### PyPI package
    
    
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git

#### Remote HTTP server
    
    
    npx @modelcontextprotocol/inspector --server-url https://api.example.com/mcp --transport http

Always read a server's own README first, since every server requires different commands and arguments.

**The Inspector stores secrets (OAuth tokens, OAuth client secrets, and stdio`env:` values) in the OS keychain when one is available.** On a machine with no keychain (Linux without libsecret or a Secret Service, headless and SSH sessions, Termux, and containers with a mounted volume) they are saved to `~/.mcp-inspector/secrets.json` instead, **unencrypted unless you supply a key**. See [Where secrets are stored](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#where-secrets-are-stored) for how to get a keychain back, encrypt the file, or keep secrets in memory only.

## Launcher flags vs. client flags

`mcp-inspector`, the binary that `npx @modelcontextprotocol/inspector` runs, is a thin launcher. It owns only two things:

  1. **The mode flag:** `--web` (default), `--cli`, or `--tui`. At most one; passing two errors with `Specify at most one of --web, --cli, or --tui.`
  2. **`-h` / `--help`.**



Everything else (`--catalog`, `--config`, `--server-url`, `--transport`, `--method`, the OAuth flags) is defined by the _client_ , not the launcher, and the clients do not all define the same set. The [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/) page is organized that way, by owner.

Mode flags are recognized only at the front of the command line: the first token that isn't `--web` / `--cli` / `--tui` ends launcher parsing, and everything after it is forwarded to the client unchanged. That's what lets a literal `--cli` appear later as one of your server's own arguments:
    
    
    mcp-inspector --cli node server.js --cli   # mode is CLI; the trailing --cli goes to server.js

`--help` behaves differently with and without a mode flag. Without one, `-h`/`--help` anywhere on the command line (even after a server command) prints the launcher's help and exits. With a mode flag it is forwarded, so `mcp-inspector --cli --help` prints the CLI's full flag reference instead.

## Where to go next

### [Web client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/)

A tab-by-tab walkthrough of the graphical inspector.

### [CLI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)

Method reference, output formats, exit codes, and CI recipes.

### [TUI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/tui/)

Terminal navigation and keyboard reference.

### [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/)

Catalog vs. config files, the full per-client flag reference, and environment variables.

### [Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/)

The OAuth flow end to end, mid-session re-authorization, and loopback callbacks.

### [Protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/)

Legacy vs. modern (2026-07-28) operation, and how every tab changes between protocol eras.

### [mcpdo connection client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/)

Connect once, then run many commands against a named connection.

### [Security](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/)

The threat model: the web backend's token, Docker, secret storage, stdio servers, and the mcpdo daemon.

### [Recipes](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/)

Importing client configs, reviewing MCP Apps, Docker, and network hosting.

### [Debugging guide](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)

Broader debugging strategies beyond the Inspector.

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
