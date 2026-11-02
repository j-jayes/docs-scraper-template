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
    * [Authorization](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/authorization/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/authorization/)



  * Light 

  * Dark 

  * System 




On this page

  * The flow, end to end
  * Connect, and get refused
  * Discover the authorization server
  * Register or identify the client
  * Authorize in the browser
  * Receive the callback
  * Exchange and retry
  * Callback URLs
  * Where credentials live
  * Mid-session re-authorization
  * Non-interactive and CI runs
  * Handing off from the web client to the CLI
  * Inspecting auth state



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

Authorization

# Authorization

Source: [MCP d998c804](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/d998c8049b8850d49d1fe3389ebf0e4a63262ab5/docs/docs/2026-07-28/tools/inspector/authorization.mdx)

## Pick registration by what your IdP supports; debug failures layer by layer

Your IdP / scenario| Registration  
---|---  
Supports dynamic client registration| Zero config, just connect  
Requires pre-registered redirect URIs| Static client -client-id / -client-secret; register the 6276 callback first  
Can only provide a client ID metadata document| CIMD -client-metadata-url  
Enterprise-managed IdP| Enterprise-managed authorization (EMA)  
  
Failure triage:

Symptom| Layer| Fix  
---|---|---  
Browser login completes but the connection never resumes| Callback listener| Port taken or not forwarded; switch ports or forward 6276  
redirect_uri_mismatch-style error| Registration| URI must match character for character (localhost ≠ 127.0.0.1)  
Mid-session 401| Token| Re-authorization; Inspector parses the challenge and retries  
403 insufficient_scope| Scopes| Step-up, or surface the error per the server setting  
A second flow dies with EADDRINUSE| Concurrency| One fixed port per instance, or 127.0.0.1:0  
  
In CI use -stored-auth-only to fail fast; to let a human log in while a script makes the calls, print the deep link and forward command with -print-handoff, then block on -wait-for-auth.

Remote MCP servers usually require authorization. The Inspector implements the full [authorization](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/) flow in all three clients, sharing the resulting tokens on disk so a login done once is usable everywhere.

## The flow, end to end

### Connect, and get refused

The Inspector connects to the server URL. The server answers `401`. When the response carries a `WWW-Authenticate` header, it points at the protected-resource metadata URL (`resource_metadata`) and, optionally, the scopes the request requires.

### Discover the authorization server

The Inspector fetches the server's [protected-resource and authorization-server metadata](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/authorization-server-discovery/) to learn the endpoints and the supported grants.

### Register or identify the client

The Inspector identifies itself to the authorization server through whichever mechanism is configured: [dynamic client registration](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/client-registration/#dynamic-client-registration), a pre-registered static client (`--client-id` / `--client-secret`), a [Client ID Metadata Document](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/client-registration/#client-id-metadata-documents) (`--client-metadata-url`), or an [enterprise-managed IdP](https://modelcontextprotocol.info/extensions/auth/enterprise-managed-authorization/).

### Authorize in the browser

The Inspector opens the authorization URL. You sign in and consent.

### Receive the callback

The authorization server redirects to the Inspector's callback URL, carrying the authorization code.

### Exchange and retry

The code is exchanged for tokens, the tokens are persisted, and the original connect is retried. For a mid-session challenge, the CLI retries the refused request automatically, and the web client asks you to retry the action.

## Callback URLs

The web app listens for the OAuth callback on its own URL, while the CLI and TUI deliberately share a second one:

Surface| Default callback| Why  
---|---|---  
**Web**| `<origin you opened the Inspector at>/oauth/callback`, by default `http://127.0.0.1:6274/oauth/callback`| The main app server already has an HTTP listener. Copy the exact value from the **Redirect URI** field in Server Settings.  
**CLI**| `http://127.0.0.1:6276/oauth/callback`| A dedicated loopback listener, so it doesn't collide with a running web Inspector.  
**TUI**| `http://127.0.0.1:6276/oauth/callback`| The same listener as the CLI.  
  
**Register`http://127.0.0.1:6276/oauth/callback`** on any IdP that requires pre-registered redirect URIs before using the CLI or TUI. A predictable default is the point: you register once and reuse it.

For the CLI and TUI, override it with `--callback-url` or `MCP_OAUTH_CALLBACK_URL`. The web callback always follows the page's origin, so `localhost` and `127.0.0.1` produce different redirect URIs there too.

The callback URL **must bind a loopback host** : `localhost`, `127.0.0.0/8`, or `[::1]`. The listener receives the authorization code over plaintext `http`, so a non-loopback host is rejected with an error and there is no flag to override that. If your browser runs on a different machine, forward the callback port to it, or complete the login in a web Inspector instead: `--print-handoff` (below) prints a `portForwardCmd` for the web Inspector's ports.

Redirect URIs must match your registration **exactly**. `http://localhost:6276/...` and `http://127.0.0.1:6276/...` are different URIs to an authorization server, even though they reach the same listener.

Only one process can hold the default port at a time; a second concurrent flow fails with `EADDRINUSE`. Use a different fixed port per instance, or `http://127.0.0.1:0/oauth/callback` for an OS-assigned ephemeral port when your authorization server supports dynamic redirect-URI registration.

## Where credentials live

File| Contents  
---|---  
`~/.mcp-inspector/storage/oauth.json`| Non-secret OAuth state (discovery metadata, PKCE verifiers, granted scope, public client ids), keyed by canonicalized server URL. Written owner-only.  
`~/.mcp-inspector/storage/client.json`| Install-level client settings (client metadata URL, enterprise IdP). The same file the web client's **Client Settings** dialog writes.  
The server's `oauth` block in the [catalog file](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#catalog-file-format)| Per-server client id/secret, scopes, the enterprise-managed flag, and the step-up policy.  
  
The path to `oauth.json` is resolved in order: `MCP_INSPECTOR_OAUTH_STATE_PATH`, then ``MCP_STORAGE_DIR`/oauth.json` (see [Environment variables](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#environment-variables)), then the default above. All three clients resolve it the same way. Command-line `--client-id` / `--client-secret` / `--client-metadata-url` override `client.json`.

The secrets themselves (access and refresh tokens, client secrets, registration access tokens, and IdP session tokens) are not in `oauth.json`. They go to the [secret store](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#where-secrets-are-stored), which is the OS keychain when one is reachable. `MCP_INSPECTOR_PERSIST_TOKENS` limits which acquired tokens are kept: `all` (default), `access` (no refresh tokens), or `none` (re-authorize every run). See [Secret store variables](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#secret-store-variables).

## Mid-session re-authorization

A server can refuse a _single_ request mid-session with a `401` or a `403 insufficient_scope`, and the Inspector handles both without dropping the connection:

  * **Re-authorization** : the token expired or was revoked. The Inspector parses the `WWW-Authenticate` challenge and re-runs the flow, then retries the failed request.
  * **Step-up** : the request needs scopes the current token doesn't carry. The Inspector re-authorizes for the union of the held and required scopes, so the new token covers everything the old one did plus the newly required scopes.



In the **web** client, re-authorization shows a **Re-authentication required** banner, and step-up opens an **Additional permissions required** dialog listing the scopes, which you confirm with **Authorize**. Each server's **Insufficient-scope response** setting can turn step-up off so the `403` surfaces as an error instead. In the **CLI** , step-up prompts on stderr:
    
    
    Proceed with step-up authorization? [y/N]

Answer **y** to continue. Piped input works (`echo y | ...`), as long as it's newline-terminated or stdin closes. **N** , or EOF with no answer, declines. A non-TTY stdin that sends nothing within 5 seconds fails with `auth_required`, which is distinct from an explicit decline. Enterprise-managed step-up re-mints silently, with no prompt.

## Non-interactive and CI runs

Interactive OAuth requires a TTY on **stdin or stderr** , or [`MCP_AUTO_OPEN_ENABLED=true`](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#environment-variables). Redirecting stderr into a pipe, as in `2>&1 | tee`, still works because stdin stays a TTY. When neither is true, which is the normal CI shape, the CLI fails fast with `auth_required` rather than waiting up to fifteen minutes for a callback nobody will complete.

For CI, be explicit:
    
    
    mcp-inspector --cli "$URL" --transport http --stored-auth-only --method tools/list

`--stored-auth-only` never starts interactive OAuth or step-up, never opens a browser, uses the shared store if a token is there, and fails immediately otherwise.

## Handing off from the web client to the CLI

The common case: a human completed OAuth in the web Inspector on this machine, and now a script wants to use that token.

Flag| Behavior  
---|---  
`--use-stored-auth`| Read the stored auth for `--server-url` and inject `Authorization: Bearer`. When a refresh token is stored, run the refresh grant first and inject the **fresh** token, persisting the rotation. Exits `3` (`no_stored_token`, listing the stored server URLs) when nothing matches.  
`--wait-for-auth <sec>`| Poll the state file until a token for `--server-url` appears, then inject it. Times out at `<sec>` with exit `3` (`auth_wait_timeout`). Use after handing a login off to a human.  
`--list-stored-auth`| Print `{ oauthStatePath, storedServerUrls }` and exit without connecting.  
`--print-handoff`| Print a JSON block (`deepLink`, `portForwardCmd`, `oauthStatePath`, `apiToken`) for `--server-url` and exit; this is everything a remote script needs to drive the browser side.  
`--relogin`| Delete the stored OAuth for this server URL before connecting, and revoke the grant at the authorization server (skip with `--no-revoke`). HTTP/SSE only.  
  
A typical remote-VM sequence. It assumes a web Inspector is running on the VM with a known `MCP_INSPECTOR_API_TOKEN`, and the same value is exported in the shell below; without it, the handoff's `deepLink` carries no `autoConnect` token and the web client rejects it.
    
    
    # On the VM: print what the human needs in order to complete OAuth in their browser
    mcp-inspector --cli --server-url https://api.example/mcp --print-handoff
    
    # Then block until the token lands, and run the call with it
    mcp-inspector --cli --transport http --server-url https://api.example/mcp \
      --wait-for-auth 120 --method tools/list

The `deepLink` in the handoff block navigates a browser straight to a _connected_ Inspector; see [Deep links](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/#deep-links).

Because the stored entry records no expiry, a stored refresh token is exercised on **every** `--use-stored-auth` run. With rotating (single-use) refresh tokens that opens two narrow failure windows: two concurrent invocations against the same state file can race for the token, and a crash between a successful refresh and the write-back leaves the rotated token unsaved. Both are unlikely; re-authorize in the web client to recover.

## Inspecting auth state

  * **Web** : the Connection Info panel shows the authorization status, the client registration type, the client ID, granted scopes, and the access token, and offers **Clear OAuth state and disconnect** for the active server. Clearing also revokes the grant unless the server's **Revoke tokens on clear** setting is off.
  * **TUI** : the **Auth** tab (`a`) shows the same fields and clears state the same way.
  * **CLI** : `--list-stored-auth` shows what's on disk, and `--relogin` revokes and discards it and starts over.



[CLI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/ "CLI client")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
