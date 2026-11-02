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
    * [mcpdo connection client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/mcpdo/)



  * Light 

  * Dark 

  * System 




On this page

  * Install
  * Quickstart
  * Choosing what to connect
  * Addressing a connection
  * Tasks
  * Output
  * Authorization
  * Elicitation
  * Protocol eras
  * The daemon
  * Isolating untrusted stdio servers
  * Environment variables
  * Using mcpdo from a coding agent



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

mcpdo connection client

# mcpdo connection client

Source: [MCP c1c81072](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/c1c81072057ed9a3eb40a1213eb7577651c1937b/docs/docs/2026-07-28/tools/inspector/mcpdo.mdx)

## When a command hangs or is rejected, check these first

Symptom| Cause| Fix  
---|---|---  
A command never returns| Another call is in flight on that connection| One connection runs one call at a time; queue behind it  
New calls are rejected| A previous call has a pending elicitation| Answer from any shell with elicitation/respond, or let it expire after 10 minutes  
Other commands wait during -load| The load test owns the connection| Wait for it to finish, or open another connection  
Odd behavior after upgrading the package| The old daemon still runs old code| mcpdo daemon stop, then reconnect  
A connection "mysteriously" rebuilds| Transport self-healing| Expected; only auth_required needs a fresh connect  
  
Human-in-the-loop split: connecting to a protected server without a TTY returns pendingAuth plus an authUrl — hand that URL to whoever will log in; the connection completes by itself, so don't reconnect repeatedly. In scripts and agents, always pass @name / -connection; omitting it fails outright without a TTY, a guard against background tasks hitting your most-recent server.

`mcpdo` is an **experimental** command-line client that ships in the `@modelcontextprotocol/inspector` package alongside `mcp-inspector`. Where the [CLI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/) connects, runs one `--method` and disconnects, `mcpdo` **connects once** and keeps the connection open, so you can run many commands against it from any shell, the way `ssh-agent` keeps keys loaded.

| `mcp-inspector --cli`| `mcpdo`  
---|---|---  
**Lifecycle**|  Connect, one `--method`, disconnect| Connect once, many commands  
**State**|  None between runs| Named connections held by a daemon  
**Best for**|  CI assertions, one JSON blob per run| Exploring a server, agent tool use, multi-step flows over one session (tasks, subscriptions, elicitation)  
  
Connections are held by a local background daemon, `mcpdod`, which `mcpdo` starts on demand and stops after its last connection closes. You never start it by hand. What it exposes, and how it is protected, is described under [The mcpdo connection daemon](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/#the-mcpdo-connection-daemon).

Watch the [mcpdo tutorial video](https://www.youtube.com/watch?v=_a6eG0y156k).

## Install

`mcpdo` is a second bin in the same package, so install the package globally, or run it through `npx -p`:
    
    
    npm install -g @modelcontextprotocol/inspector
    mcpdo --help
    
    # or without installing
    npx -p @modelcontextprotocol/inspector mcpdo --help

## Quickstart
    
    
    mcpdo servers/list                            # catalog entries you can connect
    mcpdo connect my-server                       # connect a catalog entry
    mcpdo @my-server tools/list
    mcpdo @my-server tools/call echo message:=hi
    mcpdo @my-server resources/read file:///tmp/notes.txt
    mcpdo connections/list                        # what's open
    mcpdo disconnect my-server

`mcpdo help`, or `mcpdo <command> --help`, prints the full, authoritative list of commands and flags.

## Choosing what to connect

`connect` takes a catalog entry name or an ad-hoc target:
    
    
    mcpdo connect my-server                        # from the default catalog
    mcpdo connect my-server --config ./mcp.json    # from a read-only config file
    mcpdo connect https://example.com/mcp          # ad-hoc HTTP/SSE server
    mcpdo connect node build/index.js              # ad-hoc stdio server

The catalog and `--config` behave exactly as for the other clients (see [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#choosing-servers)): the default catalog is `~/.mcp-inspector/mcp.json`, overridable with `--catalog` or `MCP_CATALOG_PATH`. `servers/list` and `servers/show <name>` read entries from disk. `connections/*` shows what the daemon currently holds. There are no commands to edit the catalog; edit the file directly.

A stdio server runs with the working directory and command resolution of the shell that ran `connect`, not of the daemon, so relative paths and bare command names mean what you would expect.

## Addressing a connection

A catalog connection is named after its entry. An ad-hoc one is named after its first token (`node`, `docker`, or the URL itself) unless you name it at connect time with `@name`:
    
    
    mcpdo connect @api https://example.com/mcp

Name the connection on each command with `@name`, or with `--connection <name>` (shorthand `--conn`). A connection named after a URL can only be addressed with `--conn <url>`, since `@name` takes only letters, digits, `_`, `.` and `-`:
    
    
    mcpdo @my-server tools/list
    mcpdo --conn my-server tools/list

Omitting the name falls back to the most recently used connection, but only on an interactive TTY. From a script or an agent, where stdin is not a TTY, an unqualified command is an error, so that a background job never acts on whichever server you last used. Set `MCP_ALLOW_DEFAULT_CONNECTION=1` to allow the fallback anyway.

`mcpdo connections/use <name>` sets the most recently used connection without sending anything to the server.

Connections **self-heal** : a dropped transport (an expired HTTP session, an exited stdio child) is re-dialed transparently on next use with the stored credentials. Only an `auth_required` error needs you to run `connect` again.

A connection runs **one call at a time**. Commands against it from other shells queue behind the call in flight, and while a call is parked on an elicitation, new calls on that connection are refused until it is answered. A long call does not block other connections.

`tools/call` also accepts the one-shot CLI's `--load` family (`--load`, `--load-concurrency`, `--load-connections`, `--load-duration`, `--load-requests`, `--load-rate`, `--load-max-error-rate`, `--load-max-p99`), with the same defaults and the same summary, run inside the daemon against the connection (see [CI gates](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/#ci-gates)). `--load-connections` opens its extra sessions with stored credentials only. Later commands on the connection wait until the run ends.

## Tasks

On a legacy connection, a plain `tools/call` refuses a tool that requires task support. Add `--task` to make a task-augmented call. `--task` applies to legacy servers only. On a modern connection the server decides per request whether to return a task, and the flag changes nothing on the wire. The call still **blocks** until the task finishes, then prints the final result:
    
    
    mcpdo @my-server tools/call --task start_job size:=large   # task-augmented call on a legacy connection

If the task reaches `input_required`, its question is handled like any other elicitation.

## Output

Flag| Output  
---|---  
`--format text` (default)| Human-readable, with ANSI styling on a TTY unless `--plain` or `NO_COLOR` is set.  
`--format json`| The pretty-printed payload, with no `{ result }` envelope. For scripts and agents.  
  
The global flags are `--format`, `--plain`, `--connection` / `--conn`, `--catalog` / `--config`, and `--stored-auth-only`. They may go before or after the subcommand, but before any `--`. The `@name` shorthand must come before the subcommand.

Terminal-bound text (results, elicitation prompts, daemon errors) has control characters stripped, so a server cannot rewrite your terminal. `--format json` stays verbatim.

## Authorization

`mcpdo` shares `oauth.json` and the secret store with the other Inspector clients, so a server you have already authorized elsewhere connects without a prompt. OAuth runs at **connect time**. Mid-session step-up is handled by the one-shot CLI, not by `mcpdo`.

Command| Effect  
---|---  
`mcpdo connect <name> --relogin` (`-r`)| Clear this server's stored tokens before connecting (HTTP/SSE only), so it signs in fresh if the server requires auth.  
`mcpdo disconnect <name> --clear-auth` (`-c`)| Close the connection **and** clear its stored tokens, so the next `connect` signs in fresh.  
`mcpdo auth/list`| Stored credentials, each annotated with the catalog or connection names it is "known as", and `● live` when an open connection holds it.  
`mcpdo auth/clear <url-or-name>`| Clear one stored credential, by store URL or friendly name. `--all --yes` clears every one.  
`mcpdo auth/ema-login` / `auth/ema-status` / `auth/ema-logout`| Enterprise-managed authorization: sign in to the IdP once, then connect to EMA servers silently. `mcpdo connect <name> --ema` treats a catalog entry as enterprise-managed for that connect, overriding its `oauth.enterpriseManaged`. It needs the entry's OAuth client ID and secret, so it cannot be used with an ad-hoc target.  
  
When a browser sign-in is needed and neither stdin nor stderr is a TTY (and `MCP_AUTO_OPEN_ENABLED` is not forced on), `connect` exits `0` immediately with `pendingAuth: true` and an `authUrl`. Relay that URL to whoever will sign in. The connection completes on its own once they do: the next real command against it finishes the connection, and `connections/list` reports `pendingAuthSignedIn` in the meantime. Don't reconnect to fix a pending sign-in.

On a host with no OS keychain, `mcpdo` stores tokens in the shared `secrets.json` file, never in memory, because its commands and the daemon are separate processes. That file is plaintext unless you supply a key; see [Where secrets are stored](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#where-secrets-are-stored).

## Elicitation

When a server asks a question mid-call (a legacy `elicitation/create`, a modern MRTR round, or a task that reaches `input_required`):

  * **On an interactive TTY** , `mcpdo` prompts inline. Form mode renders one prompt per field with a review step. URL mode prints the URL and waits for you to confirm you finished.
  * **From a script or agent** (`--format json`, or no TTY), the command returns `elicitationPending` with an `elicitationId`, and the call stays **parked** on the daemon. Answer it from any shell:


    
    
    mcpdo elicitation/respond <elicitationId> approved:=true   # form fields as key:=value or JSON
    mcpdo elicitation/respond <elicitationId> --done           # URL mode: I finished
    mcpdo elicitation/respond <elicitationId> --decline        # form mode only
    mcpdo elicitation/respond <elicitationId> --cancel         # either mode

A parked elicitation is cancelled after 10 minutes, and a connection holds one at a time; until it is answered, other calls on that connection are refused. URL mode is never auto-accepted. To keep a server from asking at all, connect with `--elicit off`. `--elicit url`, `form` or `both` (the default) choose which modes are advertised.

## Protocol eras

`mcpdo` negotiates the same [protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/) as the other clients. `connect --era legacy|auto|modern` overrides a catalog entry's `protocolEra`, and is the only way to set it for an ad-hoc target. `connections/list` tags each connection `[legacy]` or `[modern]`, and `connections/show <name>` gives the negotiated version, server info, capabilities, and the supported-versions list when the server was probed.

## The daemon

Command| Effect  
---|---  
`mcpdo daemon status`| Whether a daemon is running, and its connections and idle countdown.  
`mcpdo daemon stop`| Close every connection and stop the daemon.  
`eval "$(mcpdo private)"`| Give this shell its own daemon and connections.  
  
By default every shell you run `mcpdo` from shares one daemon, so a connection opened in one terminal is usable in another. `mcpdo private` exports `MCP_INSPECTOR_DAEMON_DIR` and `MCP_INSPECTOR_DAEMON_TOKEN` so the current shell gets a separate daemon. That keeps connections apart; it is not a security boundary against other processes running as you.

The daemon exits about a minute after its last connection closes. A daemon started before an upgrade keeps running the old code until then, so run `mcpdo daemon stop` after upgrading the package.

## Isolating untrusted stdio servers

The daemon's token controls who can **command** the daemon, not what a server can **do**. A stdio server runs with your full user privileges. To contain one you don't fully trust, make the stdio command a container:
    
    
    mcpdo connect @sandboxed -- docker run -i --rm --network none -v "$PWD:/work:ro" <server-image>

Without `@sandboxed`, the connection would be named `docker`.

Adjust the network and mount flags to what the server needs. HTTP and SSE servers run no local code, so they need no process isolation.

## Environment variables

`mcpdo` reads the same catalog, storage and secret-store variables as the other clients (see [Environment variables](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#environment-variables)), plus these:

Variable| Effect  
---|---  
`MCP_INSPECTOR_DAEMON_DIR`| Directory holding the daemon's socket, lock, token and log. Defaults to `MCP_STORAGE_DIR` when set, else `~/.mcp-inspector`. Set by `mcpdo private`.  
`MCP_INSPECTOR_DAEMON_TOKEN`| IPC token to present to, or start, the daemon. Unset, the `mcpdo` command that starts the daemon generates one, and the daemon publishes it to `mcpdod.token`. Set by `mcpdo private`.  
`MCP_ALLOW_DEFAULT_CONNECTION`| `1` lets a command without `@name` / `--connection` use the most recently used connection even when stdin is not a TTY.  
  
## Using mcpdo from a coding agent

The package ships an agent skill that teaches an agent to drive `mcpdo`: connections it holds then extend the agent's toolset, and it knows to relay sign-in URLs and answer parked elicitations. `mcpdo agent-help` prints the guide, `mcpdo agent-help --skill-path` prints the path of the installable skill file, and `mcpdo agent-help --instructions` prints a block to append to a project's `CLAUDE.md` or `AGENTS.md`. The skill can also be installed with `npx skills add modelcontextprotocol/inspector --skill mcpdo`.

[Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/ "Configuration and flags")[Protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/ "Protocol eras")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
