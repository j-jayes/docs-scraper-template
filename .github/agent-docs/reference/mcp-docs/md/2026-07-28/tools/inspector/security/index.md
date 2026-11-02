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
    * [Security](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/security/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/tools/inspector/security/)



  * Light 

  * Dark 

  * System 




On this page

  * The web backend and its API token
  * Where the backend listens
  * Docker
  * Publish the port on loopback only
  * The data volume puts secrets on disk
  * Secret storage
  * The automatic plaintext fallback
  * What the file store protects against
  * stdio servers run as you
  * The mcpdo connection daemon
  * How clients reach it, and who else can
  * How it authenticates commands
  * What it holds in memory
  * Lifetime
  * What it writes to disk



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Inspector](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)

Security

# Security

Source: [MCP c1c81072](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/c1c81072057ed9a3eb40a1213eb7577651c1937b/docs/docs/2026-07-28/tools/inspector/security.mdx)

## Pre-deployment self-check: three red lines and "who can read my secrets"

Red lines (breaking any one hands over a backend that can start processes on your machine):

  1. Never combine DANGEROUSLY_OMIT_AUTH with a non-loopback bind; to share access, put a real control boundary in front (authenticated reverse proxy, SSH tunnel, or private network).
  2. Prefix every container-published port with 127.0.0.1:; a bare -p places the backend and its token-disclosing page on your whole LAN.
  3. Keep the key file away from the secrets file itself, its backups, volumes and repos; pass it via MCP_INSPECTOR_SECRET_KEY_FILE, not an environment variable (readable via docker inspect).



Who can read your secrets (quick reference):

Store form| Same-user programs| root / docker group| File copies (backups/snapshots/commits)  
---|---|---|---  
Plaintext secrets.json| yes| yes| yes  
Encrypted secrets.json| yes (can read the key)| yes| only if the key leaks too  
OS keychain| via Inspector| yes| no (not in a file)  
  
Two commonly underestimated boundaries: a stdio server is a process running with your full user rights — wrap untrusted ones in a container (e.g. -network none); and the mcpdo daemon has no TCP port, but its token file is readable by your user — private mode isolates connections, it is not a security boundary.

The Inspector is a developer tool that holds real credentials and starts real processes. This page gathers everything it protects, what it trusts, and where the boundaries sit, so you can decide which setup fits your machine. The configuration and recipe pages link here rather than repeating the reasoning.

The short version:

  * **The web backend can spawn processes.** Its API token is what stands between that capability and anything else that can reach the port.
  * **Secrets go to the OS keychain when there is one.** Without one, they go to a file that is **plaintext unless you supply a key** , and that fallback happens automatically.
  * **stdio servers run as you.** Anything the Inspector can read, a server it starts can usually read too.
  * **The mcpdo daemon is a long-lived process holding live connections** , guarded by a token and same-user file permissions.



## The web backend and its API token

The web client is a browser app backed by a Node server that owns the MCP connections. That server can start stdio processes on request, so every `/api/*` route requires a per-launch bearer token (`x-mcp-remote-auth: Bearer <token>`). How the browser obtains it is described under [The session token](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/#the-session-token).

What the token does and does not protect:

  * **The token is the real guard for non-browser clients.** The origin allow-list (`ALLOWED_ORIGINS`) stops other web pages from driving the backend, but a request that arrives with **no** `Origin` header (curl, a script, any non-browser client) skips that check entirely. A `Host` header allow-list runs ahead of every route, including `GET /`, and answers `403` to a request whose `Host` is not a loopback name, an IP literal, the bind host, an `ALLOWED_ORIGINS` hostname, or an entry of `MCP_INSPECTOR_ALLOWED_HOSTS`, so a DNS-rebinding page cannot load the page and read the token (see [Host binding and origins](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/web/#host-binding-and-origins)).
  * **`GET /` discloses the token.** The backend injects it into the served HTML so that a reload or a bookmark keeps working. Anyone who can load the page can therefore read the token, which is why the bind address matters more than the token's value. Pinning your own `MCP_INSPECTOR_API_TOKEN` does not change this, since a custom token is disclosed exactly like a generated one.
  * **`DANGEROUSLY_OMIT_AUTH=true` removes the guard completely.** Anything that can reach the port can then spawn processes as you and use any OAuth token the Inspector holds. Only `true` or `1` turns auth off; any other value, including `false`, keeps it on.
  * **Only`/api/*` is gated.** The page itself, its static assets and `GET /healthz` are served without the token. `/healthz` returns only `{"status":"ok"}`, for container and orchestrator probes.



### Where the backend listens

The backend binds `127.0.0.1` by default. Binding every interface (`0.0.0.0`, `::` and equivalent spellings) is refused unless you set `DANGEROUSLY_BIND_ALL_INTERFACES=true`. Binding one specific address is allowed without that opt-in, because it is one deliberate exposure rather than all of them at once. See [Hosting on a network](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/#hosting-on-a-network).

Never combine `DANGEROUSLY_OMIT_AUTH` with a non-loopback bind. If you need the Inspector reachable by others, put a real access-control boundary in front of it: an authenticating reverse proxy, an SSH tunnel, or a private network.

## Docker

The [Docker image](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/#docker) changes two things about the picture above.

### Publish the port on loopback only

Inside the container the Inspector must bind `0.0.0.0` to be reachable through `-p`, so the image sets `DANGEROUSLY_BIND_ALL_INTERFACES=true`. That opt-in governs the **container 's** interfaces, not the host's. Which host interfaces see the Inspector is decided by how you publish the port:

Publish flag| Reachable from  
---|---  
`-p 127.0.0.1:6274:6274`| This machine only.  
`-p 6274:6274` (bare)| **Every host interface** , so your whole network.  
  
A bare `-p` puts a process-spawning backend, and the page that discloses its token, on your local network. Keep the `127.0.0.1:` prefix on every published port (`6274`, and `6275` / `6278` if you publish the MCP Apps listeners).

### The data volume puts secrets on disk

A container has no OS keychain. Without a volume on `/home/node/.mcp-inspector`, secrets stay **in memory** for the session and are lost when the container exits. Mounting that volume to keep your server list also switches secrets to a `secrets.json` file on the volume, and that file is **plaintext unless you supply a key**. It is then readable by root and every member of the host's `docker` group (which is equivalent to root), and by anyone who obtains a backup, snapshot or copy of the volume.

Supply the key as a file with `MCP_INSPECTOR_SECRET_KEY_FILE` (a Docker or Compose secret) rather than as an environment variable: a key passed with `-e MCP_INSPECTOR_SECRET_KEY=…` is visible to anyone who can run `docker inspect` or `docker exec`. The recipe shows both forms.

## Secret storage

The Inspector keeps credentials out of `mcp.json`, `client.json` and `oauth.json` so that sharing, committing or syncing those files does not leak them. These are stored as secrets:

  * acquired OAuth tokens (access, refresh and ID tokens), subject to [`MCP_INSPECTOR_PERSIST_TOKENS`](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#secret-store-variables), and IdP session tokens from enterprise-managed authorization;
  * each server's OAuth client secret, and the enterprise IdP client secret;
  * dynamically registered client secrets and their registration access tokens;
  * each stdio server's `env:` values.



**`headers` are not secrets.** They are saved in `mcp.json` exactly as written, so a header that carries a credential (an API key, a static `Authorization` value) stays in the file.

How the store is selected, and how to change it, is under [Where secrets are stored](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/configuration/#where-secrets-are-stored). This section covers the risks.

### The automatic plaintext fallback

On a host where the OS keychain cannot be reached (Linux without libsecret or a running Secret Service, a headless server or SSH session with no D-Bus session, Android/Termux), the Inspector **automatically** stores secrets in `~/.mcp-inspector/secrets.json`. You do not have to ask for it, and unless you supply a key that file is **unencrypted**.

The only signs are a warning on stderr when the store is selected and a footer in the web client's settings dialogs.

Treat that as a risk, not just a configuration fact. The file is written with mode `0600`, which keeps out other non-root users and nothing else. To close it, do one of the following:

  * get a keychain back (install libsecret and run a Secret Service such as `gnome-keyring`, or run inside a desktop session);
  * encrypt the file with a generated key in `MCP_INSPECTOR_SECRET_KEY_FILE`;
  * or set `MCP_INSPECTOR_SECRET_STORE=memory` and re-enter secrets each session.



### What the file store protects against

The file store exists for machines without a keychain, and it is weaker than one. Treat keeping secrets in it, **even encrypted** , as a moderate risk.

**Without a key (plaintext, mode`0600`):**

Threat| Protected?  
---|---  
Other non-root users on the machine, while the mode holds| Yes  
Root, and on a container host every member of the `docker` group| No  
Anyone with a copy of the file: a backup, a snapshot, a synced home directory, a commit| No  
Any program running as your user, including the stdio servers the Inspector starts| No  
  
**With a key (AES-256-GCM, key stretched with scrypt against a per-write random salt):**

Threat| Protected?  
---|---  
The file leaking on its own (a backup, snapshot, copy or commit), provided the key is high-entropy and did not leak with it| Yes  
Anyone who can read the key where it lives| No  
Root on the host, or the `docker` group: they can read the file, the key, or the process memory holding decrypted values| No  
Code running as the same user| No  
A weak passphrase: anyone holding the file can guess offline, quickly, because the scrypt cost is kept low for per-save derivation| No  
  
Where the key lives decides the second row. With `MCP_INSPECTOR_SECRET_KEY`, the key is in the Inspector's environment, readable through `/proc/<pid>/environ` by the same user or root, through `docker inspect` / `docker exec` for a container, and wherever you stored it for launching (a shell profile, an `.env` file, a Compose file). `MCP_INSPECTOR_SECRET_KEY_FILE` narrows that to whoever can read the key file, but the Inspector has to read it, so the same user can too. If the key sits beside the secrets file, in the same backup, volume or repository, encryption buys nothing.

In short, encryption turns "the file leaked" into "the file **and** the key leaked". It does not help against anyone who already has root, or the Inspector's own user, on the machine or in the container. When that is not acceptable, use a keychain or the memory store.

Two failure modes are deliberately loud rather than silent:

  * If the key file is missing, unreadable or empty, if `MCP_INSPECTOR_SECRET_KEY_FILE` is set to an empty value, or if both key variables are set, the store **refuses to read or write** rather than falling back to plaintext.
  * If the passphrase changes or is lost, the existing file can no longer be decrypted. The Inspector reads it as empty and **refuses to overwrite it** , so restore the passphrase, or delete the file and re-enter the values.



## stdio servers run as you

A stdio MCP server is a process the Inspector starts with your user's privileges, exactly as any MCP host would.

  * **Environment:** the Inspector does not pass its own environment through. A stdio server gets a short allowlist (`HOME`, `LOGNAME`, `PATH`, `SHELL`, `TERM`, `USER` on macOS and Linux) plus its configured `env:`. So a key in `MCP_INSPECTOR_SECRET_KEY` is not handed to it directly.
  * **But it is the same user.** A server can open `secrets.json` itself, read `oauth.json` and your catalog, and usually read the Inspector's environment through `/proc/<pid>/environ`. The environment allowlist is hygiene, not isolation.



Only connect stdio servers you would trust with these secrets. To isolate one you don't, wrap its command in a container, for example `docker run -i --rm --network none <image>` as the stdio command. HTTP and SSE servers run no local code, so they need no process isolation.

## The mcpdo connection daemon

[mcpdo](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/mcpdo/) keeps connections open between commands by handing them to a background daemon, `mcpdod`. It is started **automatically** the first time a command needs it (`mcpdo connect`, or any command against a connection). There is no separate "start the daemon" step to opt into. This section describes what that process exposes.

### How clients reach it, and who else can

Platform| Endpoint  
---|---  
macOS / Linux| A Unix socket, `mcpdod.sock`, inside the daemon directory (default `~/.mcp-inspector`).  
Windows| A named pipe, `\\.\pipe\mcp-conn-<hash>`, derived from the daemon directory. No directory permissions surround it, so the token is the guard.  
  
There is **no TCP port** , so nothing off the machine can reach the daemon. On Unix, the daemon directory is created, or tightened if it already exists, to mode `0700`, owned by you, and must be a real directory rather than a symlink. The socket and lock file inside it are `0600`. Other non-root users therefore cannot reach the socket. Root, and any process running as you, can.

The directory is chosen in this order: `MCP_INSPECTOR_DAEMON_DIR`, then `MCP_STORAGE_DIR`, then `~/.mcp-inspector`. A socket path longer than the platform's limit (about 104 bytes on macOS, 108 on Linux) is refused up front with an error naming the variable to shorten.

### How it authenticates commands

Every request must carry a bearer token. There is no unauthenticated request path.

  * **Shared mode (the default):** the `mcpdo` command that starts the daemon generates a random 256-bit token and passes it to the daemon in its environment. The daemon publishes it to `mcpdod.token` (mode `0600`) in the daemon directory, so that any `mcpdo` command run by the same user can read it. Filesystem permissions on that file are the trust boundary, which is the same same-user boundary the socket has.
  * **Private mode:** `eval "$(mcpdo private)"` creates a fresh `0700` directory under `$TMPDIR/mcp-conn-<uid>/` and exports `MCP_INSPECTOR_DAEMON_DIR` and `MCP_INSPECTOR_DAEMON_TOKEN` into that shell, so the shell gets its own daemon and its own connections. The parent `mcp-conn-<uid>` directory is checked for ownership and symlinks before use, because `$TMPDIR` can be shared.



Tokens are compared in constant time. A request line larger than 1 MiB is rejected. A command presenting the wrong token to a live daemon fails loudly. It never replaces that daemon.

Private mode separates connections and daemon state between shells. It is **not** a security boundary against other processes running as your user: anything with your UID that learns the daemon directory can read its token. For a hard boundary, use a separate user account or a container.

### What it holds in memory

For as long as it runs, the daemon holds, for each open connection:

  * the live MCP connection, and for stdio servers the child process, started with the daemon as its parent;
  * the connection's resolved configuration, including stdio `env:` values pulled from the secret store;
  * the OAuth tokens in use for HTTP connections, which it also re-reads from the store to re-dial a dropped transport;
  * any elicitation a non-interactive command left parked, until it is answered or expires after 10 minutes.



The daemon is started with the environment of the `mcpdo` command that spawned it. It inherits that shell's variables (including `MCP_INSPECTOR_SECRET_KEY`, if set there, and its own IPC token in `MCP_INSPECTOR_DAEMON_TOKEN`) and keeps them for its whole lifetime, even after you change them in your shell. stdio servers it starts still receive only the allowlist above plus their `env:`, snapshotted from the shell that ran `mcpdo connect`.

On a keychain-less host, mcpdo never uses the memory store as its automatic fallback. Its front-end commands and the daemon are separate processes, so a per-process store could not carry a token from one to the other. mcpdo uses the **shared`secrets.json` file** instead, with the same plaintext-unless-keyed caveat as above. `MCP_INSPECTOR_SECRET_STORE=memory` set explicitly still wins. mcpdo prints the store warning once per `connect` rather than on every command.

### Lifetime

  * **Start:** on the first command that needs it. If two start at once, an `O_EXCL` lock (`mcpdod.lock`) lets exactly one win. The lock left by a dead daemon is reclaimed, and a live daemon is never taken over.
  * **Stop:** `mcpdo daemon stop`, or `SIGINT` / `SIGTERM`. It also exits by itself about **60 seconds after its last connection closes**. There is no maximum lifetime: while any connection is open, the daemon stays up.
  * **On a clean stop:** new work is refused, in-flight requests get a short grace period, every connection is closed, and the socket, token file and lock are removed.
  * **On a crash:** every connection it held is gone, and stdio servers lose their stdin, which normally ends them. Stored OAuth tokens and secrets are unaffected. The next `mcpdo` command starts a fresh daemon, which clears the stale socket, reclaims the lock and writes a new token. Connections must be re-established with `mcpdo connect`.



Find a stray daemon with `pgrep mcpdod`. It sets its process title to `mcpdod`.

### What it writes to disk

All in the daemon directory, which is `0700`:

File| Mode| Contents  
---|---|---  
`mcpdod.sock`| `0600`| The IPC socket (Unix only).  
`mcpdod.lock`| `0600`| The single-instance lock, holding the daemon's pid.  
`mcpdod.token`| `0600`| The IPC bearer token. Written at start, removed at clean shutdown.  
`mcpdod.log`| `0600`| The daemon's stderr, recreated on each start. Startup failures and the secret-store warning land here.  
  
The daemon writes OAuth state and secrets through the same `oauth.json` and secret store as the other clients, so everything under Secret storage applies to it unchanged.

[Recipes](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/ "Recipes")[TUI client](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/tui/ "TUI client")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
