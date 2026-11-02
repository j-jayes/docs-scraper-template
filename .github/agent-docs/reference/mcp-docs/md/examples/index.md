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

    * [Registries](https://modelcontextprotocol.info/registry/)
    * [The MCP Registry](https://modelcontextprotocol.info/registry/about/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/registry/about/)
  * [简体中文](https://mcpcn.com/registry/about/)



  * Light 

  * Dark 

  * System 




On this page

  * The MCP Registry Ecosystem
  * Relationship with Package Registries
  * Relationship with Server Developers
  * Relationship with Downstream Aggregators
  * Relationship with Other MCP Registries
  * Relationship with MCP Host Applications
  * Trust and Security
  * Verifying Server Authenticity
  * Security Scanning
  * Spam Prevention



Scroll to top

[Registries](https://modelcontextprotocol.info/registry/)

The MCP Registry

# The MCP Registry

Source: [MCP d5b4a98b](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/d5b4a98b4bb294f1e997be21102fe86b5c39c21a/docs/registry/about.mdx)

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).

The MCP Registry is the official centralized metadata repository for publicly accessible MCP servers, backed by major trusted contributors to the MCP ecosystem such as Anthropic, GitHub, PulseMCP, and Microsoft.

The MCP Registry provides:

  * A single place for server creators to publish metadata about their servers
  * Namespace management through DNS verification
  * A REST API for MCP clients and aggregators to discover available servers
  * Standardized installation and configuration information



Server metadata is stored in a standardized [`server.json` format](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/draft/server.schema.json), which contains:

  * The server's unique name (e.g., `io.github.user/server-name`)
  * Where to locate the server (e.g., npm package name, remote server URL)
  * Execution instructions (e.g., command-line args, env vars)
  * Other discovery data (e.g., description, server capabilities)



## The MCP Registry Ecosystem

The MCP Registry is part of an ecosystem that looks something like:

### Relationship with Package Registries

Package registries — such as npm, PyPI, and Docker Hub — host packages with code and binaries.

The MCP Registry hosts metadata that points to those packages.

For example, a `weather-mcp` package could be hosted on npm, and metadata in the MCP Registry could map the "weather v1.2.0" server to `npm:weather-mcp`.

The [Package Types guide](https://modelcontextprotocol.info/registry/package-types/) lists the supported package types and registries. More package registries may be supported in the future based on community demand. If you are interested in building support for a package registry, please [open an issue](https://github.com/modelcontextprotocol/registry).

### Relationship with Server Developers

The MCP Registry supports both open-source and closed-source servers. Server developers can publish their server's metadata to the registry as long as the server's installation method is publicly available (e.g., an npm package or a Docker image on a public registry) _or_ the server itself is publicly accessible (e.g., a remote server that is not restricted to private networks).

The MCP Registry **does not** support private servers. Private servers are those that are only accessible to a narrow set of users. For example, servers published on a private network (like `mcp.acme-corp.internal`) or on private package registries (e.g. `npx -y @acme/mcp --registry https://artifactory.acme-corp.internal/npm`). If you want to publish private servers, we recommend that you host your own private MCP registry and add them there.

### Relationship with Downstream Aggregators

The MCP Registry is intended to be consumed primarily by downstream aggregators, such as MCP server marketplaces.

The metadata hosted by the MCP Registry is deliberately unopinionated. Downstream aggregators can provide curation or additional metadata such as community ratings.

We expect that downstream aggregators will use the MCP Registry API to pull new metadata on a regular but infrequent basis (for example, once per hour). See the [MCP Registry Aggregators guide](https://modelcontextprotocol.info/registry/registry-aggregators/) for more information.

### Relationship with Other MCP Registries

In addition to a public REST API, the MCP Registry defines an [OpenAPI spec](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/openapi.yaml) that other MCP registries can implement in order to provide a standardized interface for MCP host applications.

We expect that many downstream aggregators will implement this interface. Private MCP registries can implement it as well to benefit from existing host application support.

Note that the official MCP Registry codebase is **not** designed for self-hosting, and the registry maintainers cannot provide support for this use case. If you choose to fork it, you would need to maintain and operate it independently.

### Relationship with MCP Host Applications

The MCP Registry is not intended to be directly consumed by host applications. Instead, host applications should consume other MCP registries, such as downstream marketplaces, via a REST API conforming to the official MCP Registry's OpenAPI spec.

## Trust and Security

### Verifying Server Authenticity

The MCP Registry uses namespace authentication to ensure that servers come from their claimed sources. Server names follow a reverse DNS format (like `io.github.username/server` or `com.example/server`) that ties them to verified GitHub accounts or domains.

This namespace system ensures that only the legitimate owner of a GitHub account or domain can publish servers under that namespace, providing trust and accountability in the ecosystem. For details on authentication methods, see the [Authentication guide](https://modelcontextprotocol.info/registry/authentication/).

### Security Scanning

The MCP Registry delegates security scanning to:

  * **Underlying package registries** — npm, PyPI, Docker Hub, and other package registries perform their own security scanning and vulnerability detection.
  * **Downstream aggregators** — MCP Registry aggregators and marketplaces can implement additional security checks, ratings, or curation.



The MCP Registry focuses on namespace authentication and metadata hosting, while relying on the broader ecosystem for security scanning of actual server code.

### Spam Prevention

The MCP Registry uses multiple mechanisms to prevent spam:

  * **Namespace authentication requirements** — Publishers must verify ownership of their namespace through GitHub, DNS, or HTTP challenges, preventing arbitrary spam submissions.
  * **Character limits and validation** — Free-form fields have strict character limits and regex validation to prevent abuse.
  * **Manual takedown** — The registry maintainers can manually remove spam or malicious servers. See the [Moderation Policy](https://modelcontextprotocol.info/registry/moderation-policy/) for details on what content is removed.



Future spam prevention measures under consideration include stricter rate limiting, AI-based spam detection, and community reporting capabilities.

[Quickstart: Publish an MCP Server to the MCP Registry](https://modelcontextprotocol.info/registry/quickstart/ "Quickstart: Publish an MCP Server to the MCP Registry")[The MCP Registry Moderation Policy](https://modelcontextprotocol.info/registry/moderation-policy/ "The MCP Registry Moderation Policy")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
