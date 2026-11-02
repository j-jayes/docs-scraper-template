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
    * [Versioning](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/learn/versioning/)



  * Light 

  * Dark 

  * System 




On this page

  * Revisions
  * Feature States
  * Negotiation



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

Versioning

# Versioning

Source: [MCP 29affa6b](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/29affa6b11e2dbd5a8b5678e9b90aa4a336769a4/docs/docs/2026-07-28/learn/versioning.mdx)

## Site explanation: distinguish three versions before upgrading

The reference below is pinned to the attributed upstream commit. A protocol revision date, an SDK package version and a server software version identify different things. Upgrading an SDK does not prove that the peer supports the same protocol revision; installing newer server software does not replace checking its supported revisions.

Think of compatibility as a set intersection. If a client supports A and B while a server supports B and C, B is their only shared revision. Sending C merely because it is newer does not establish compatibility. If there is no intersection, report incompatibility and upgrade one side or choose a mutually supported implementation; repeating the same request cannot resolve it.

Problem| Evidence to collect| Next step  
---|---|---  
A version is rejected| The request's declared revision and the peer's supported revisions| Find an intersection and construct the request according to that revision  
The version is accepted but a capability is unavailable| Advertised capabilities and the requested method| Check capability requirements rather than treating every failure as a version failure  
An older client cannot connect| Each side's initialization flow and protocol revision| Read the backward-compatibility guidance below instead of mixing two flows  
  
Test a shared revision, no shared revision, and a matching revision with a missing capability. Keep the error code and request revision with the result. A, B and C are explanatory symbols, not actual strings to send to a server. Use the pinned specification below for concrete fields and procedures.

The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.

The protocol version will _not_ be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability.

## Revisions

Revisions may be marked as:

  * **Draft** : in-progress specifications, not yet ready for consumption.
  * **Current** : the current protocol version, which is ready for use and may continue to receive backwards compatible changes.
  * **Final** : past, complete specifications that will not be changed.



The **current** protocol version is [**2026-07-28**](https://modelcontextprotocol.info/specification/2026-07-28/).

## Feature States

Individual features of the specification may additionally be marked as **Deprecated** under the [feature lifecycle and deprecation policy](https://modelcontextprotocol.info/community/feature-lifecycle/): the feature remains part of the specification, but is scheduled for removal. Deprecated features document a migration path (or state that none is required) and remain in the specification for at least twelve months, or at least ninety days under the policy's [expedited-removal exception](https://modelcontextprotocol.info/community/feature-lifecycle/#expedited-removal), before they become eligible for removal, after which they may be **Removed** in a future revision.

Features that are currently Deprecated are listed in the [deprecated features registry](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/).

## Negotiation

Every request declares the protocol version it is using via the `io.modelcontextprotocol/protocolVersion` key in its [`_meta`](https://modelcontextprotocol.info/specification/2026-07-28/basic/#_meta) field, and the server accepts or rejects each request independently. On Streamable HTTP, the same value is also carried in the [`MCP-Protocol-Version` header](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/#protocol-version-header). Clients and servers **MAY** support multiple protocol versions simultaneously.

If the server does not support the requested version, it responds with an [`UnsupportedProtocolVersionError`](https://modelcontextprotocol.info/specification/2026-07-28/basic/versioning/#protocol-version-negotiation) listing the versions it does support. The client can then retry the request with a mutually supported version, or surface an error to the user if none exists.

Clients that want to select a version up front can call [`server/discover`](https://modelcontextprotocol.info/specification/2026-07-28/server/discover/), a mandatory RPC that returns the server's supported protocol versions, capabilities, and identity in a single request. Calling it is optional: a client is free to send any request directly and handle a version error if one comes back.

For interoperability with servers and clients that implement the handshake-based protocol revisions (`2025-11-25` and earlier), see [Backward Compatibility](https://modelcontextprotocol.info/specification/2026-07-28/basic/versioning/#backward-compatibility-with-initialization-based-versions).

[Build an MCP Server](https://modelcontextprotocol.info/docs/development/build-server/ "Build an MCP Server")[Build an MCP Client](https://modelcontextprotocol.info/docs/development/build-client/ "Build an MCP Client")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
