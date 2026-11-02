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

    * [MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
    * [TUI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/tui/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/tui/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/tui/)



  * Light 

  * Dark 

  * System 




On this page

  * Choosing servers
  * Tabs
  * Navigation
  * Authorizing an HTTP server
  * Requirements



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

TUI client

# TUI client

Source: [MCP d998c804](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/d998c8049b8850d49d1fe3389ebf0e4a63262ab5/docs/docs/2026-07-28/tools/inspector/tui.mdx)

## A missing tab is usually a fact about the connection, not a bug

TUI shows tabs by applicability; a missing tab normally reflects connection properties:

Missing tab| Meaning| Next step  
---|---|---  
Auth / Network| The connection is stdio| Expected; appears for HTTP/SSE servers  
Console| The connection is HTTP/SSE| Expected  
Subscriptions / Skills / Tasks| The server doesn't declare that capability/extension| Check Info for capabilities, Protocol for the initialize handshake  
  
Three common OAuth stalls: the 6276 callback port taken by a concurrent flow (EADDRINUSE — switch via -callback-url to another fixed port or 127.0.0.1:0); a redirect URI that doesn't match the registration (localhost and 127.0.0.1 are different URIs); the callback port not forwarded when your browser runs on another machine. In headless environments (CI, no-TTY hosts) use the CLI instead.

The TUI is the Inspector's terminal interface, with the same interactive exploration of tools, resources, and prompts as the web client. Use it on a remote host over SSH, in a locked-down environment, or when you prefer to stay in the terminal.
    
    
    npx @modelcontextprotocol/inspector --tui node build/index.js   # with an ad-hoc stdio server

## Choosing servers

Unlike the CLI, the TUI has no `--server <name>` flag for picking one entry: it reads its servers from a catalog or config file, loads every server in it, and lets you pick from an on-screen list:
    
    
    mcp-inspector --tui --catalog mcp.json   # writable catalog, seeded empty if missing
    mcp-inspector --tui --config mcp.json    # read-only session, errors if absent

With neither `--catalog` nor `--config`, and no [ad-hoc target](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#ad-hoc-targets), it uses the default writable catalog `~/.mcp-inspector/mcp.json`. See [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/).

The TUI also takes the [shared server-selection flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#shared-server-selection-flags) (`--server-url`, `--transport`, `--header`, `-e`, `--cwd`) plus `--protocol-era` for an ad-hoc server, and the [OAuth client flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#cli-and-tui-oauth-client-flags) (`--client-id`, `--client-secret`, `--client-metadata-url`, `--client-config`, `--callback-url`).

## Tabs

Tab| Key| What it shows  
---|---|---  
**Info**| `i`| Server configuration, name, version and instructions, plus the roots the client advertises (press `e` to edit them).  
**Auth**| `a`| OAuth state for the selected HTTP or SSE server, plus a **Clear OAuth State** action (`s`), which also disconnects a live connection.  
**Resources**| `r`| Browse and read resources.  
**Subscriptions**| `u`| Subscribe to and unsubscribe from resources (servers that support resource subscriptions).  
**Prompts**| `m`| List prompts and render them with arguments.  
**Skills**| `k`| List a server's skills and verify their digests and frontmatter (servers that declare the skills extension).  
**Tools**| `t`| View tools and execute them with form-like inputs.  
**Tasks**| `s`| List tasks, fetch their results, cancel them, and clear finished ones (servers that support Tasks).  
**Protocol**| `p`| JSON-RPC request/response/notification history.  
**Network**| `n`| HTTP traffic for SSE and [Streamable HTTP](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/) servers.  
**Console**| `o`| `stderr` from a connected stdio server process.  
  
The accelerators avoid collisions rather than always taking the first letter: **P** rotocol takes `p` so Pro**m** pts takes `m`, and **C** onsole takes `o` because `c` is the global Connect action. Ta**s** ks takes `s`, its only free letter, so Subscriptions takes `u` and Skills takes `k`.

Auth, Network, and Console appear only for the transports they apply to; Subscriptions, Skills, and Tasks appear only once a connected server supports them.

## Navigation

Key| Action  
---|---  
`Tab` / `Shift+Tab`| Move focus: server list → tab bar → list → details  
`Left` / `Right` arrows (tab bar focused), or a tab's letter| Switch tabs  
`Up` / `Down` arrows| Select a server, move through a list, or scroll details, depending on which pane has focus  
`Enter`| Select an item, execute a tool, or fetch a resource  
`c`| Connect to the selected server  
`d`| Disconnect  
`/`| Filter the current list (`Enter` keeps the filter, `Esc` clears it)  
`+`| Open the details pane full screen  
`y` / `w`| In a details dialog: copy the value, or save it to a file (`w` also saves a tool's result)  
`?`| Show or hide the keybinding help  
`Esc` or `Ctrl+C`| Exit (`Esc` closes an open dialog first)  
  
Press **`?`** whenever no dialog is open for the full keybinding reference, including the keys specific to the active tab.

## Authorizing an HTTP server

  1. Select an HTTP or SSE server and press **`c`** to connect.
  2. If the server requires authorization, the TUI starts OAuth automatically and opens the authorization URL in a browser.
  3. When the browser redirect lands on the TUI's loopback listener, the connection finishes on its own, with no second **`c`**.
  4. Use the **Auth** tab to inspect the resulting OAuth state, or to clear it.



The TUI's callback listener defaults to `http://127.0.0.1:6276/oauth/callback`. The port is fixed on purpose: a pre-registered (static) OAuth client, a [Client ID Metadata Document (CIMD)](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/client-registration/#client-id-metadata-documents), or an enterprise-managed IdP all need a redirect URI known in advance. Register that URI once and it works across sessions. On a remote host where your browser is on another machine, forward the callback port so the redirect reaches this listener; see [Callback URLs](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/#callback-urls).

The trade-off is that only one TUI OAuth flow can hold the port at a time; a second concurrent flow fails with `EADDRINUSE`. To override it, pass `--callback-url` or set `MCP_OAUTH_CALLBACK_URL`: use a different fixed port per instance, or `http://127.0.0.1:0/oauth/callback` for an OS-assigned ephemeral port when your authorization server registers redirect URIs dynamically.

Redirect URIs must match **exactly** what you registered. `localhost` and `127.0.0.1` are different URIs as far as an authorization server is concerned.

Per-server OAuth fields in the catalog (static client id/secret, scopes, the enterprise-managed flag) are applied automatically. Install-wide settings (CIMD, enterprise IdP) come from `~/.mcp-inspector/storage/client.json`, the same file the web client's **Client Settings** dialog writes. Point at a different one with `--client-config` or `MCP_CLIENT_CONFIG_PATH`.

See [Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/) for the full picture.

## Requirements

The TUI needs a real TTY with raw-mode support. It will not run usefully in a headless CI job; use the [CLI](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/) there.

[Security](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/ "Security")[Web client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/ "Web client")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
