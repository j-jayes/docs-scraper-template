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

    * [Specification](https://modelcontextprotocol.info/specification/2026-07-28/)
    * [Roots](https://modelcontextprotocol.info/specification/2026-07-28/client/roots/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/specification/2026-07-28/client/roots/)
  * [简体中文](https://mcpcn.com/specification/2026-07-28/client/roots/)



  * Light 

  * Dark 

  * System 




On this page

  * User Interaction Model
  * Capabilities
  * Protocol Messages
  * Listing Roots
  * Message Flow
  * Data Types
  * Root
  * Project Directory
  * Multiple Repositories
  * Error Handling
  * Security Considerations
  * Implementation Guidelines



Scroll to top

[Specification](https://modelcontextprotocol.info/specification/)

[Specification](https://modelcontextprotocol.info/specification/2026-07-28/)

Roots

# Roots

Source: [MCP 29affa6b](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/29affa6b11e2dbd5a8b5678e9b90aa4a336769a4/docs/specification/2026-07-28/client/roots.mdx)

**Deprecated** : The Roots feature is deprecated as of protocol version `2026-07-28` ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)). Under the [feature lifecycle policy](https://modelcontextprotocol.info/community/feature-lifecycle/), it remains in the specification for at least twelve months after this revision's release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to passing directories or files via tool parameters, resource URIs, or server configuration. See the [deprecated features registry](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/).

The Model Context Protocol (MCP) provides a standardized way for clients to expose filesystem "roots" to servers. Roots inform servers about the directories and files the client considers relevant, so that servers can focus their operations accordingly. They are informational guidance rather than an access-control mechanism. The protocol does not enforce that servers stay within roots. Servers can request the list of roots from supporting clients.

## User Interaction Model

Roots in MCP are typically exposed through workspace or project configuration interfaces.

For example, implementations could offer a workspace/project picker that allows users to select directories and files the server should have access to. This can be combined with automatic workspace detection from version control systems or project files.

However, implementations are free to expose roots through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## Capabilities

Clients that support roots **MUST** declare the `roots` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request:
    
    
    {
      "_meta": {
        "io.modelcontextprotocol/clientCapabilities": {
          "roots": {}
        }
      }
    }

## Protocol Messages

### Listing Roots

To retrieve roots during the processing of a client request, servers send an `InputRequiredResult` containing a `roots/list` request:

**Input request (delivered inside[`InputRequiredResult.inputRequests`](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/#inputrequests)):**
    
    
    {
      "method": "roots/list"
    }

**Client result (returned inside`inputResponses` on the retried request):**
    
    
    {
      "roots": [
        {
          "uri": "file:///home/user/projects/myproject",
          "name": "My Project"
        }
      ]
    }

## Message Flow
    
    
      sequenceDiagram
        participant Server
        participant Client
    
        Note over Server,Client: Initial Request
        Client->>Server: tools/call(id: 1)
        Server-->>Client: InputRequiredResult(roots/list)
        Client->>Server: tools/call(id: 2, inputResponses{key: roots} + requestState)
    

## Data Types

### Root

A root definition includes:

  * `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current specification.
  * `name`: Optional human-readable name for display purposes.



Example roots for different use cases:

#### Project Directory
    
    
    {
      "uri": "file:///home/user/projects/myproject",
      "name": "My Project"
    }

#### Multiple Repositories
    
    
    [
      {
        "uri": "file:///home/user/repos/frontend",
        "name": "Frontend Repository"
      },
      {
        "uri": "file:///home/user/repos/backend",
        "name": "Backend Repository"
      }
    ]

## Error Handling

If an error occurs, the client does not need to replay the initial call with an error message as the server is not waiting for a response with the `InputRequiredResult` pattern.

## Security Considerations

  1. Clients **MUST** :

     * Only expose roots with appropriate permissions
     * Validate all root URIs to prevent path traversal
     * Implement proper access controls
     * Monitor root accessibility
  2. Servers **SHOULD** :

     * Handle cases where roots become unavailable
     * Respect root boundaries during operations
     * Validate all paths against provided roots



## Implementation Guidelines

  1. Clients **SHOULD** :

     * Prompt users for consent before exposing roots to servers
     * Provide clear user interfaces for root management
     * Validate root accessibility before exposing
     * Monitor for root changes
  2. Servers **SHOULD** :

     * Check for roots capability before usage
     * Respect root boundaries in operations
     * Cache root information appropriately



[Key Changes](https://modelcontextprotocol.info/specification/2026-07-28/changelog/ "Key Changes")[Sampling](https://modelcontextprotocol.info/specification/2026-07-28/client/sampling/ "Sampling")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
