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
    * [CLI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/cli/)



  * Light 

  * Dark 

  * System 




On this page

  * Choosing a server
  * Methods
  * Passing arguments
  * Output
  * Probing MCP Apps
  * Exit codes and error envelopes
  * Authorization in scripts
  * Recipes
  * Verify a server in CI
  * CI gates
  * Branch on the failure class
  * Smoke-test every tool that has a UI
  * Inspect a catalog without connecting
  * Editing the catalog
  * Proxies



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

CLI client

# CLI client

Source: [MCP c1c81072](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/c1c81072057ed9a3eb40a1213eb7577651c1937b/docs/docs/2026-07-28/tools/inspector/cli.mdx)

## A runnable CLI lab and its limits

For executable examples with failure interpretation, start with [the Inspector 2.12.0 lab](https://modelcontextprotocol.info/tools/inspector/). It includes a Python SDK `2.3.0` reference server, the complete smoke script, 26 previously recorded scenarios and explicit untested features. A CLI invocation runs one method on a fresh connection; several successful invocations do not establish a long-running session or UI workflow.

Task| Entry| Check before use  
---|---|---  
Scripts, CI and troubleshooting| This reference and the linked lab| Pin `@modelcontextprotocol/[[email protected]](/cdn-cgi/l/email-protection)`; separate server and Inspector arguments  
Inspect requests interactively| [Web client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/)| Its backend can spawn local processes; read API-token and bind-address boundaries before exposing a port  
Import configuration| [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/)| Use read-only `--config` for someone else's file; writable `--catalog` is different; inspect stdio commands before executing them  
Sign in or recover expired credentials| [Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/)| Check the client's callback URL, storage and non-interactive policy; keep credentials out of logs  
  
In the CLI, stdio server arguments precede `--`, and Inspector options follow it. Web / TUI use a different split, so do not copy a complete command between modes. Declare the protocol era in automation: the default `legacy` success establishes only the legacy path, `auto` can probe and fall back, and `modern` does not fall back. Strict schema failures, connection failures and a tool's `isError` are separate outcomes.

On 2026-10-30 only the subset needed here was rerun: clean stdio, pre-start banner, process exit, legacy HTTP versus modern, and 401 / 403 / 404 / HTML. Other scenarios retain the lab's previous recordings; all 26 were not rerun. Web / TUI, `mcpdo`, real OAuth, skills verification and App UI remain untested. The pinned reference below documents options; their presence does not establish a site test result.

Each CLI run connects to a server, invokes the single request you name with `--method`, prints the result, and exits. That makes it a good fit for CI pipelines, shell one-liners, and coding agents that need to verify a server change immediately.
    
    
    npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list

Running several commands against the same server, or a flow that spans one session (tasks, subscriptions, elicitation)? The [mcpdo connection client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/) connects once and keeps the connection open between commands.

The examples below use the installed `mcp-inspector` binary. Without a global install, prefix each command with `npx @modelcontextprotocol/inspector` instead, as above.

## Choosing a server

The CLI accepts a positional command (stdio), a `--server-url` (HTTP/SSE), or a named server out of a catalog or config file:
    
    
    # stdio: everything positional is the command to spawn
    mcp-inspector --cli node build/index.js --method tools/list
    
    # HTTP
    mcp-inspector --cli https://api.example.com/mcp --transport http --method tools/list
    
    # From a file
    mcp-inspector --cli --config ./mcp.json --server myserver --method tools/list

When the server comes from a file, its per-server settings (headers, timeouts, OAuth, [protocol era](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/), and roots) apply to the connection, resolved exactly as the TUI and web client resolve them. A `--header` flag overrides the file's headers for that run while leaving its timeouts and OAuth in place.

Later examples abbreviate whichever of these forms you use, along with its `--transport` or `--config`/`--server` flags, as `<server>`.

**The config file is the only durable way to give a run its[roots](https://modelcontextprotocol.info/specification/2026-07-28/client/roots/):** there is no roots flag, and the CLI has no `roots/set` method. Roots configured for a server are advertised at connect, so a server that calls `roots/list` (as `@modelcontextprotocol/server-filesystem` does, to learn its allowed directories) gets them.

See [Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/) for `--catalog` vs. `--config`, the `--` separator, and the shared server-selection flags.

## Methods

`--method`| Required companions| Notes  
---|---|---  
`initialize`| None| Connect-only probe: `{serverInfo, protocolVersion, capabilities, instructions}`.  
`tools/list`| None| `--strict` turns its schema portability check into a gate (see CI gates).  
`tools/call`| `--tool-name`, plus optional `--tool-arg` / `--tool-args-json`|   
`resources/list`| None|   
`resources/read`| `--uri`|   
`resources/templates/list`| None|   
`resources/directory/read`| `--uri`, plus optional `--cursor`| One page at a time; pass back the previous page's `nextCursor`.  
`prompts/list`| None|   
`prompts/get`| `--prompt-name`, plus optional `--prompt-args`|   
`logging/setLevel`| `--log-level`| Legacy era only; modern servers opt in per request instead.  
`skills/list`| None| `--verify` checks the skills returned (see CI gates).  
`skills/get`| `--uri`| Same `--verify` option.  
`servers/list`| None| Read the catalog **without connecting** to anything.  
`servers/show`| `--server`| Same, for one entry.  
`servers/add`| `--server`, plus a positional target or `--server-url`| Write the catalog without connecting (see Editing the catalog).  
`servers/edit`| `--server`, plus what to change| Same.  
`servers/remove`| `--server`| Same.  
  
Stream- or session-only methods (`logging/tail`, for example) are rejected, since a process that exits can't hold a stream open.

### Passing arguments

`--tool-arg` takes `key=value` and **coerces** each value by JSON-parsing it when it parses, so `count=1` and `zip=10001` both send numbers. A value that is not valid JSON (`zip=012`, a bare word) is sent as a string, and a string is then converted to the type the tool's input schema declares for that property, so `zip=012` against a numeric `zip` still sends `12`:
    
    
    mcp-inspector --cli <server> --method tools/call --tool-name mytool \
      --tool-arg key=value --tool-arg count=1 --tool-arg 'options={"format":"json"}'

`--tool-args-json` takes the whole argument object at once and skips the `key=value` parsing, so `{"zip":"10001"}` sends the string `"10001"` rather than a number. The schema conversion still applies to string values, so this only keeps a string a string when the schema types that property as a string (or doesn't declare it). The two flags are mutually exclusive:
    
    
    mcp-inspector --cli <server> --method tools/call --tool-name mytool \
      --tool-args-json '{"zip":"10001"}'

## Output

`--format text` (the default) pretty-prints for humans. `--format json` emits a single JSON object on stdout with no banners, so the whole output pipes cleanly:
    
    
    mcp-inspector --cli <server> --method tools/list --format json | jq '.result.tools[].name'

## Probing MCP Apps

`--app-info` reports whether a tool ships an [MCP App](https://modelcontextprotocol.info/extensions/apps/overview/) UI (its `ui://` resource, CSP, and permissions) **without calling the tool** , so a pipeline can decide whether it needs a browser before invoking anything:
    
    
    # One tool -> one JSON line
    mcp-inspector --cli <server> --method tools/call --tool-name my_tool --app-info
    # {"hasApp":true,"toolName":"my_tool","resourceUri":"ui://...","csp":{...},"permissions":{...}}
    
    # Every tool -> NDJSON, one line each, over a single connection
    mcp-inspector --cli <server> --method tools/list --app-info | jq -c 'select(.hasApp)'

Exit codes distinguish the outcomes: a tool with an app exits `0`, one with no app exits `2`, and a missing tool exits `5`, so a typo isn't mistaken for "no app". A probe failure (unreadable UI resource, malformed `resourceUri`) is reported in a `resourceError` field rather than aborting, so one bad tool never kills a whole listing.

The CLI can't render an App, so by default it doesn't advertise the MCP Apps extension at `initialize`. A server that exposes its App tools only to clients claiming App support will then look app-less (exit `2`). Add `--advertise-apps` to claim the extension for that run.

`tools/list --app-info` always emits NDJSON (one line per tool) regardless of `--format`; `--format json` reshapes only the single-tool output of `tools/call --app-info`.

## Exit codes and error envelopes

Every non-zero exit maps to a stable failure class, so a caller can branch on _why_ without scraping prose:

Code| Meaning  
---|---  
`0`| Success.  
`1`| Usage or unexpected error (the catch-all), including an unreadable secret store or OAuth state file.  
`2`| No MCP App found on the tool (`--app-info` probe).  
`3`| Server requires authentication (HTTP 401/403, or an SDK authorization error).  
`4`| Server unreachable (DNS, connection refused, timeout, `fetch failed`).  
`5`| Tool error: `tools/call` returned `isError: true`, or the tool wasn't found.  
`6`| `--strict` found an error-severity tool-schema portability problem.  
`7`| `--verify` found a skill that violates SEP-2640 (conformance, digest, or size mismatch).  
`8`| `--verify` couldn't check every skill within its read bounds.  
`9`| `--verify --require-digests` found a skill that advertises no digests.  
`10`| A `--load` run breached a `--load-max-error-rate` or `--load-max-p99` threshold. The summary is printed first, and the envelope `code` names the threshold: `load_error_rate_exceeded` or `load_p99_exceeded`.  
`11`| The server answered HTTP 429 (envelope `code` `rate_limited`). The envelope also carries `method`, plus `retryAfter` (the `Retry-After` header as sent) and `retryAfterMs` when the server sent one that parses.  
  
On any non-zero exit the CLI also writes a **single JSON line to stderr** :
    
    
    {
      "error": {
        "code": "auth_required",
        "message": "Unauthorized",
        "status": 401,
        "url": "https://api.example/mcp"
      }
    }

The envelope carries `code` and `message` always, plus `cause` (the underlying error, such as a DNS failure), `status` (the HTTP status) and `url` when known. Query-string secrets in a URL are redacted. `code` is a stable name for the failure: `auth_required`, `unreachable`, `tool_not_found`, `tool_is_error`, `no_app`, `schema_unportable`, `store_unavailable`, `oauth_state_unrecognized`, `rate_limited`, or the catch-all `error`, among others.

Because it's one line, a caller can parse it with `2>&1 | tail -1 | jq .error`.

A `tools/call` that returns `isError: true` still prints its payload, but exits `5`, so an `&&` chain doesn't proceed on a failed call.

## Authorization in scripts

By default the CLI runs the same loopback OAuth flow as the TUI: it opens a browser and waits on a localhost callback that a CI job can't complete. Two flags make non-interactive runs predictable:

  * `--stored-auth-only`: never start interactive OAuth or step-up, and never auto-open a browser. Use tokens from the shared store if present, otherwise fail immediately with `auth_required`. This is the flag CI wants.
  * `--use-stored-auth`: reuse a token that the web Inspector already obtained on this machine, refreshing it first when a refresh token is stored. It looks the token up by URL, so it requires `--server-url`.



Without either, and with no TTY on stdin or stderr, the CLI fails fast with `auth_required` rather than hanging for fifteen minutes on a callback nobody will complete.

See [Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/) for the full flow, the web-to-CLI handoff, and `--print-handoff`.

## Recipes

### Verify a server in CI
    
    
    set -euo pipefail
    
    # Fail the build if the server can't be reached or doesn't expose the tool
    mcp-inspector --cli --config ./ci-servers.json --server my-server \
      --stored-auth-only --method tools/list --format json \
      | jq -e '.result.tools | map(.name) | index("get_weather")' > /dev/null

### CI gates

These flags turn a check into a non-zero exit, each with its own code so a job can tell the failures apart:

  * `--strict` (with `tools/list`): reports tool-schema portability problems in full on stderr (path, issue, suggested fix) and exits `6` if any is error-severity. Without it, `tools/list` prints only a one-line count. Under `--format json` the findings are folded into the output as `schemaFindings`.
  * `--verify` (with `skills/list` or `skills/get`): runs the SEP-2640 conformance and digest checks, writes one JSON report per skill on stdout, and exits `7` on a violation or `8` when the read bounds stopped it before every skill was checked. `--skill-catalog-max-skills` and `--skill-catalog-max-bytes` set those bounds.
  * `--require-digests` (with `--verify`): exits `9` for a skill that advertises no digests, instead of reporting it as unverifiable and exiting `0`.
  * `--load-max-error-rate <fraction>` and `--load-max-p99 <ms>` (with `--load`): turn a load run into a gate. The run prints its summary, then exits `10` when the share of failed calls is above the fraction (`0` to `1`, so `0` fails on any failed call), when the p99 latency is above the given milliseconds, or when no call completed. `--load` (with `tools/call --tool-name`) calls the tool repeatedly and concurrently and prints a latency and error-rate summary instead of a result, bounded by `--load-duration <sec>` (default `10` when `--load-requests` is not set) and `--load-requests <n>`, with in-flight calls still finishing. `--load-concurrency <n>` (default `10`) caps the calls in flight, `--load-connections <n>` (default `1`, at most `--load-concurrency`, HTTP and SSE servers only) spreads them over independent sessions opened before timing starts, and `--load-rate <n>` (default unlimited) caps the calls started per second.


    
    
    mcp-inspector --cli <server> --method tools/list --strict > /dev/null
    mcp-inspector --cli <server> --method skills/list --verify --require-digests
    mcp-inspector --cli <server> --method tools/call --tool-name get_weather --load --load-requests 200 --load-max-p99 500

### Branch on the failure class
    
    
    if out=$(mcp-inspector --cli "$URL" --transport http --method tools/list 2>err.json); then
      echo "$out"
    else
      case $? in
        3) echo "needs auth: run the web inspector once to sign in" ;;
        4) echo "server unreachable" ;;
        *) jq .error < err.json ;;
      esac
    fi

### Smoke-test every tool that has a UI
    
    
    mcp-inspector --cli "$URL" --transport http --method tools/list --app-info \
      | jq -r 'select(.hasApp) | .toolName'

### Inspect a catalog without connecting
    
    
    mcp-inspector --cli --catalog ~/.mcp-inspector/mcp.json --method servers/list
    mcp-inspector --cli --catalog ~/.mcp-inspector/mcp.json --method servers/show --server my-server

`servers/show` redacts secret-bearing fields (`env` values, sensitive headers, OAuth client secrets), but it does **not** scrub credentials embedded in a server `url` (userinfo or query tokens) or in stdio `args`. Treat raw URL and `detail` fields as sensitive before pasting them into an issue.

### Editing the catalog

`servers/add`, `servers/edit`, and `servers/remove` write the catalog without connecting to anything. They go through the same code as the web client's server list, so `env` values and client secrets land in the [secret store](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#where-secrets-are-stored) exactly as they would from the UI, and a running web client picks up the change.
    
    
    # Add: the positional target or --server-url describes the entry, not a server to connect to
    mcp-inspector --cli node build/index.js -e API_KEY=secret --method servers/add --server my-server
    
    # Edit: change the target, -e, --cwd, --header, or --protocol-era, or rename it
    mcp-inspector --cli --method servers/edit --server my-server --rename my-renamed-server
    
    # Remove the entry and its stored secrets
    mcp-inspector --cli --method servers/remove --server my-renamed-server

Only the writable catalog (`--catalog`, `MCP_CATALOG_PATH`, or the default) can be written; `--config` is refused. With an in-memory secret store, a write that supplies `-e` values (and a `--rename`) is refused, since the secrets would be lost when the run exits.

## Proxies

Connections to remote HTTP/SSE servers honor the conventional proxy variables: `HTTPS_PROXY` / `HTTP_PROXY` (and their lowercase forms) select the proxy and `NO_PROXY` exempts hosts. No Inspector-specific flag is needed, and the proxy agent is loaded lazily, so runs without a proxy pay nothing. The same applies to the web client's backend.

[Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/ "Authorization")[Configuration and flags](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/ "Configuration and flags")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
