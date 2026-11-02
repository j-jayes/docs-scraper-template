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
    * [MCP FAQ: Versions, Authorization and Troubleshooting](https://modelcontextprotocol.info/docs/faqs/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/faqs/)
  * [简体中文](https://mcpcn.com/docs/faqs/)



  * Light 

  * Dark 

  * System 




On this page

  * Versions and specifications
  * Which revision should a new implementation target?
  * Can a historical revision or SEP define current behavior?
  * Is a Draft proposal already a protocol capability?
  * Requests and interaction
  * What is MRTR?
  * What is elicitation?
  * How do protocol Tasks differ from application tasks?
  * Authorization and security
  * Does every server require OAuth?
  * How does a client discover the authorization server?
  * Can registrations be reused across authorization servers?
  * Does using MCP establish security or compliance?
  * Failure handling
  * What should be checked first when connection or capability use fails?
  * How should repeated remote authorization failures be diagnosed?
  * What happens when a pagination cursor or cache becomes invalid?
  * Where can a suspected specification problem be reported?
  * Related specification



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

MCP FAQ: Versions, Authorization and Troubleshooting

# MCP FAQ: Versions, Authorization and Troubleshooting

This page answers implementation questions that can be checked against the [2026-07-28 documentation](https://modelcontextprotocol.io/docs/2026-07-28) and its specification. Check the peer's actual supported revisions and capabilities before adopting a feature.

## Versions and specifications

### Which revision should a new implementation target?

Use the site's current `2026-07-28` revision as the reference, then choose an SDK that supports it. Package versions and protocol revisions differ. Discover or negotiate the revision and capabilities actually supported by both peers; upgrading a package alone does not establish interoperability.

### Can a historical revision or SEP define current behavior?

[Historical specifications](https://modelcontextprotocol.info/specification/) support maintenance and explain evolution. SEPs record proposals and decisions; later specifications or extensions can change the result. Implement against the applicable published specification, extension and changelog.

### Is a Draft proposal already a protocol capability?

No. A Draft is under discussion. A proposal becomes an interoperability contract only through the applicable published specification or extension and its required capability negotiation.

## Requests and interaction

### What is MRTR?

[Multi-Round-Trip Requests](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/) let a server end a request with `InputRequiredResult`; after obtaining input, the client retries the original method with a new JSON-RPC ID. The client must return `requestState` unchanged and must not inspect, parse or modify it.

### What is elicitation?

Elicitation asks a user for information needed to complete an operation. Form mode collects structured input; URL mode handles sensitive interactions outside the client. Show the request's source and purpose, and open a URL only after explicit user acceptance. Return `decline` or `cancel` when the user declines or cancels; client policy may map a timeout to `cancel`. The server can then choose a fallback, retry later or stop.

### How do protocol Tasks differ from application tasks?

[The Tasks extension](https://modelcontextprotocol.info/extensions/tasks/overview/) defines durable handles, polling, input during execution and deferred result retrieval. A to-do item or business job is application data unless it implements and negotiates that extension. [SEP-1686](https://modelcontextprotocol.info/seps/1686-tasks/) records the earlier core-protocol design; `2026-07-28` moved Tasks into an official extension.

## Authorization and security

### Does every server require OAuth?

Local stdio servers normally rely on host and operating-system security boundaries. A protected remote HTTP server should publish protected-resource metadata and use the flow appropriate to its client under [the authorization specification](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/). MCP does not create an OS sandbox or grant automatic user approval.

### How does a client discover the authorization server?

Prefer `resource_metadata` in the `WWW-Authenticate` challenge from a 401 response; when absent, try the specification's ordered protected-resource well-known URIs. Validate the discovered `issuer`, request tokens for the target `resource`, and reject credentials whose issuer, resource or audience does not match the intended server.

### Can registrations be reused across authorization servers?

No. Client IDs, credentials and tokens belong to the authorization server that issued them. Store separate registration state and credentials for each server listed by PRM.

### Does using MCP establish security or compliance?

No. Implement authentication, authorization, input validation, user controls, audit and retention for the application. Use least privilege, validate credentials and external data, prohibit token passthrough, and keep secrets out of logs. See [local-server boundaries](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/).

## Failure handling

### What should be checked first when connection or capability use fails?

Confirm the actual revision, transport and capabilities, then the method's requirements. Keep redacted JSON-RPC error codes, HTTP status and correlation IDs. Separate revision mismatch, missing capability, invalid input and server failure; [the debugging guide](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/) includes controlled failure cases.

### How should repeated remote authorization failures be diagnosed?

Check PRM, authorization-server discovery, issuer, registration ownership, exact redirect URI, PKCE, scope, resource and token audience in order. Do not disable issuer or audience validation to make a connection pass. [The authorization tutorial](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/) distinguishes local resource checks from untested IdP flows.

### What happens when a pagination cursor or cache becomes invalid?

Cache cursor pages separately. If a cursor is rejected, discard all cached pages for that list and restart without a cursor. A relevant change notification invalidates the cache even before TTL expires.

### Where can a suspected specification problem be reported?

First isolate the specification, SDK or implementation with a minimal request and redacted logs. Report to the appropriate repository, or use [MCP GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions).

## Related specification

  * [Elicitation and declined requests](https://modelcontextprotocol.info/specification/2026-07-28/client/elicitation/)
  * [Pagination](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/pagination/) and [cache behavior](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/caching/)
  * [Measured client capabilities](https://modelcontextprotocol.info/docs/clients/) (a dated observation, not a result for every client)



[MCP Clients: What Each One Supports and How to Confirm What a Client Declares](https://modelcontextprotocol.info/docs/clients/ "MCP Clients: What Each One Supports and How to Confirm What a Client Declares")[MCP Server Best Practices: Transport, Security and Tool Design](https://modelcontextprotocol.info/docs/best-practices/ "MCP Server Best Practices: Transport, Security and Tool Design")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
