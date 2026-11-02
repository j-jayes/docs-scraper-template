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
    * [Understanding MCP clients](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/learn/client-concepts/)



  * Light 

  * Dark 

  * System 




On this page

  * Core Client Features
  * Elicitation
  * Overview
  * Example: Holiday Booking Approval
  * User Interaction Model
  * Roots
  * Overview
  * Example: Travel Planning Workspace
  * Design Philosophy
  * User Interaction Model
  * Sampling
  * Overview
  * Example: Flight Analysis Tool
  * User Interaction Model



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

Understanding MCP clients

# Understanding MCP clients

Source: [MCP 89153404](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/891534049ae842de72190fe4af7ce9a0f7c045e6/docs/docs/2026-07-28/learn/client-concepts.mdx)

## Where these client concepts are implemented

  * [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/) wires exactly one client to one server, as this page describes, and exercises discovery, a successful call, typed and missing-argument errors, timeout recovery and server exit with a pinned five-file lab — no model required.
  * [Client best practices](https://modelcontextprotocol.info/docs/2026-07-28/develop/clients/client-best-practices/) is the host-scale continuation of this page: when tool definitions enter context (progressive discovery), and how a host composes calls (code mode).
  * What clients' own pages claim today — which of elicitation, roots and sampling each vendor states — is listed per client in the [client capability matrix](https://modelcontextprotocol.info/docs/clients/), dated and sourced to vendor wording; the page's embedded probe server is the way to observe what the client in front of you actually declares on the wire.
  * Roots and sampling are deprecated in `2026-07-28`; their method lifecycle and successors are tracked in the [SEP impact guide](https://modelcontextprotocol.info/docs/reference/sep-impact-guide/) and [deprecated features](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/).



MCP clients are instantiated by host applications to communicate with particular MCP servers. The host application, like Claude.ai or an IDE, manages the overall user experience and coordinates multiple clients. Each client handles one direct communication with one server.

Understanding the distinction is important: the _host_ is the application users interact with, while _clients_ are the protocol-level components that enable server connections.

## Core Client Features

In addition to making use of context provided by servers, clients may provide several features to servers. These client features allow server authors to build richer interactions.

Feature| Explanation| Example  
---|---|---  
**Elicitation**|  Elicitation enables servers to request specific information from users during interactions, providing a structured way for servers to gather information on demand.| A server booking travel may ask for the user's preferences on airplane seats, room type or their contact number to finalize a booking.  
**Roots**|  Roots allow clients to specify which directories servers should focus on, communicating intended scope through a coordination mechanism. Roots are [deprecated](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/) as of protocol version `2026-07-28`.| A server for booking travel may be given access to a specific directory, from which it can read a user's calendar.  
**Sampling**|  Sampling allows servers to request LLM completions through the client, enabling an agentic workflow. This approach puts the client in complete control of user permissions and security measures. Sampling is deprecated as of protocol version `2026-07-28`.| A server for booking travel may send a list of flights to an LLM and request that the LLM pick the best flight for the user.  
  
### Elicitation

Elicitation enables servers to request specific information from users during interactions, creating more dynamic and responsive workflows.

#### Overview

Elicitation provides a structured way for servers to gather necessary information on demand. Instead of requiring all information up front or failing when data is missing, servers can pause their operations to request specific inputs from users. This creates more flexible interactions where servers adapt to user needs rather than following rigid patterns.

Elicitation supports two modes:

  * **Form mode** : The server asks the client to collect structured data from the user. The request includes a schema that the client uses to build an input form and validate the response.
  * **URL mode** : The server provides a URL for the user to open. The interaction happens out of band and its data never passes through the client, which makes this mode suitable for sensitive flows such as credential entry or third-party OAuth authorization.



Elicitation follows the [Multi Round-Trip Requests](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/) (MRTR) pattern. When a server needs user input while processing a request such as `tools/call`, it responds with an `InputRequiredResult` whose `inputRequests` field carries one or more `elicitation/create` requests. The client gathers the input and retries the original request, attaching the collected `inputResponses` and echoing back any `requestState` the server included.

**Elicitation flow:**
    
    
      sequenceDiagram
        participant User
        participant Client
        participant Server
    
        Client->>Server: tools/call (id: 1)
        Note over Server: Server needs more information
        Server-->>Client: InputRequiredResult with elicitation/create request
    
        Note over Client,User: Human interaction
        Client->>User: Present elicitation UI
        User-->>Client: Provide requested information
    
        Note over Client,Server: Retry request with user input
        Client->>Server: tools/call (id: 2, inputResponses)
    
        Note over Server: Continue processing with new information
        Server-->>Client: Final result
    

The flow enables dynamic information gathering. Servers can request specific data when needed, users provide information through appropriate UI, and servers complete the retried request with the newly acquired context.

**Elicitation request example (delivered inside`InputRequiredResult.inputRequests`):**
    
    
    {
      method: "elicitation/create",
      params: {
        mode: "form",
        message: "Please confirm your Barcelona vacation booking details:",
        requestedSchema: {
          type: "object",
          properties: {
            confirmBooking: {
              type: "boolean",
              description: "Confirm the booking (Flights + Hotel = $3,000)"
            },
            seatPreference: {
              type: "string",
              enum: ["window", "aisle", "no preference"],
              description: "Preferred seat type for flights"
            },
            roomType: {
              type: "string",
              enum: ["sea view", "city view", "garden view"],
              description: "Preferred room type at hotel"
            },
            travelInsurance: {
              type: "boolean",
              default: false,
              description: "Add travel insurance ($150)"
            }
          },
          required: ["confirmBooking"]
        }
      }
    }

#### Example: Holiday Booking Approval

A travel booking server demonstrates elicitation's power through the final booking confirmation process. When a user has selected their ideal vacation package to Barcelona, the server needs to gather final approval and any missing details before proceeding.

The server elicits booking confirmation with a structured request that includes the trip summary (Barcelona flights June 15-22, beachfront hotel, total $3,000) and fields for any additional preferences—such as seat selection, room type, or travel insurance options.

As the booking progresses, the server elicits contact information needed to complete the reservation. It might ask for traveler details for flight bookings, special requests for the hotel, or emergency contact information.

#### User Interaction Model

Elicitation interactions are designed to be clear, contextual, and respectful of user autonomy:

**Request presentation** : Clients display elicitation requests with clear context about which server is asking, why the information is needed, and how it will be used. The request message explains the purpose while the schema provides structure and validation.

**Response options** : Users can provide the requested information through appropriate UI controls (text fields, dropdowns, checkboxes), decline to provide information with optional explanation, or cancel the entire operation. Clients validate responses against the provided schema before returning them to servers.

**URL handling** : For URL mode, clients show the full URL and gather explicit consent before opening it, and never fetch the URL automatically. The client only learns whether the user consented. The interaction itself stays between the user and the target site.

**Privacy considerations** : Servers must not use form mode to request sensitive information such as passwords, API keys, access tokens, or payment credentials. Those interactions belong in URL mode, which keeps the data out of band so it never passes through the client or the LLM context. Clients warn about suspicious requests and let users review form data before sending.

### Roots

Roots are [deprecated](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/) as of protocol version `2026-07-28` and scheduled for removal. New implementations should pass directories or files via tool parameters, resource URIs, or server configuration instead.

Roots define filesystem boundaries for server operations, allowing clients to specify which directories servers should focus on.

#### Overview

Roots are a mechanism for clients to communicate filesystem access boundaries to servers. They consist of file URIs that indicate directories where servers can operate, helping servers understand the scope of available files and folders. While roots communicate intended boundaries, they do not enforce security restrictions. Actual security must be enforced at the operating system level, via file permissions and/or sandboxing.

**Root structure:**
    
    
    {
      "uri": "file:///Users/agent/travel-planning",
      "name": "Travel Planning Workspace"
    }

Roots are exclusively filesystem paths and always use the `file://` URI scheme. They help servers understand project boundaries, workspace organization, and accessible directories. The roots list can change as users work with different projects or folders. Servers pick up the updated boundaries the next time they request the roots list.

#### Example: Travel Planning Workspace

A travel agent working with multiple client trips benefits from roots to organize filesystem access. Consider a workspace with different directories for various aspects of travel planning.

The client provides filesystem roots to the travel planning server:

  * `file:///Users/agent/travel-planning` \- Main workspace containing all travel files
  * `file:///Users/agent/travel-templates` \- Reusable itinerary templates and resources
  * `file:///Users/agent/client-documents` \- Client passports and travel documents



When the agent creates a Barcelona itinerary, well-behaved servers respect these boundaries—accessing templates, saving the new itinerary, and referencing client documents within the specified roots. Servers typically access files within roots by using relative paths from the root directories or by utilizing file search tools that respect the root boundaries.

If the agent opens an archive folder like `file:///Users/agent/archive/2023-trips`, the client adds it to the roots list, and the server sees the new boundary on its next `roots/list` request.

For a complete implementation of a server that respects roots, see the [filesystem server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) in the official servers repository.

#### Design Philosophy

Roots serve as a coordination mechanism between clients and servers, not a security boundary. The specification requires that servers "SHOULD respect root boundaries," and not that they "MUST enforce" them, because servers run code the client cannot control.

Roots work best when servers are trusted or vetted, users understand their advisory nature, and the goal is preventing accidents rather than stopping malicious behavior. They excel at context scoping (telling servers where to focus), accident prevention (helping well-behaved servers stay in bounds), and workflow organization (such as managing project boundaries automatically).

#### User Interaction Model

Roots are typically managed automatically by host applications based on user actions, though some applications may expose manual root management:

**Automatic root detection** : When users open folders, clients automatically expose them as roots. Opening a travel workspace allows the client to expose that directory as a root, helping servers understand which itineraries and documents are in scope for the current work.

**Manual root configuration** : Advanced users can specify roots through configuration. For example, adding `/travel-templates` for reusable resources while excluding directories with financial records.

### Sampling

Sampling is [deprecated](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/) as of protocol version `2026-07-28` and scheduled for removal. New implementations should integrate directly with LLM provider APIs instead.

Sampling allows servers to request language model completions through the client, enabling agentic behaviors while maintaining security and user control.

#### Overview

Sampling enables servers to perform AI-dependent tasks without directly integrating with or paying for AI models. Instead, servers can request that the client—which already has AI model access—handle these tasks on their behalf. This approach puts the client in complete control of user permissions and security measures. Because sampling requests occur within the context of other operations—like a tool analyzing data—and are processed as separate model calls, they maintain clear boundaries between different contexts, allowing for more efficient use of the context window.

Sampling follows the same [Multi Round-Trip Requests](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/) flow described under elicitation, with the `InputRequiredResult` carrying a `sampling/createMessage` request.

Servers can also request tool use during sampling by including a `tools` array and an optional `toolChoice` field in the request. The tool definitions are scoped to that sampling request and do not need to correspond to tools the server exposes. Clients declare support through the `sampling.tools` capability, and servers must not send tool-enabled sampling requests to clients that have not declared it. See [sampling](https://modelcontextprotocol.info/specification/2026-07-28/client/sampling/#tools-in-sampling) in the specification for details.

**Sampling flow:**
    
    
      sequenceDiagram
        participant LLM
        participant User
        participant Client
        participant Server
    
        Client->>Server: tools/call (id: 1)
        Note over Server: Server needs an LLM completion
        Server-->>Client: InputRequiredResult with sampling/createMessage request
    
        Note over Client,User: Human-in-the-loop review
        Client->>User: Present request for approval
        User-->>Client: Review and approve/modify
    
        Note over Client,LLM: Model interaction
        Client->>LLM: Forward approved request
        LLM-->>Client: Return generation
    
        Note over Client,User: Response review
        Client->>User: Present response for approval
        User-->>Client: Review and approve/modify
    
        Note over Client,Server: Retry request with approved response
        Client->>Server: tools/call (id: 2, inputResponses)
        Server-->>Client: Final result
    

The flow ensures security through multiple human-in-the-loop checkpoints. Users review and can modify both the initial request and the generated response before the client retries the original request with it.

**Request parameters example:**
    
    
    {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: "Analyze these flight options and recommend the best choice:\n" +
                  "[47 flights with prices, times, airlines, and layovers]\n" +
                  "User preferences: morning departure, max 1 layover"
          }
        }
      ],
      modelPreferences: {
        hints: [{
          name: "claude-sonnet" // Prefer Sonnet-class models
        }],
        costPriority: 0.3,      // Less concerned about API cost
        speedPriority: 0.2,     // Can wait for thorough analysis
        intelligencePriority: 0.9  // Need complex trade-off evaluation
      },
      systemPrompt: "You are a travel expert helping users find the best flights based on their preferences",
      maxTokens: 1500
    }

#### Example: Flight Analysis Tool

Consider a travel booking server with a tool called `findBestFlight` that uses sampling to analyze available flights and recommend the optimal choice. When a user asks "Book me the best flight to Barcelona next month," the tool needs AI assistance to evaluate complex trade-offs.

The tool queries airline APIs and gathers 47 flight options. It then requests AI assistance to analyze these options: "Analyze these flight options and recommend the best choice: [47 flights with prices, times, airlines, and layovers] User preferences: morning departure, max 1 layover."

The client initiates the sampling request, allowing the AI to evaluate trade-offs—like cheaper red-eye flights versus convenient morning departures. The tool uses this analysis to present the top three recommendations.

#### User Interaction Model

While not a requirement, sampling is designed to allow human-in-the-loop control. Users can maintain oversight through several mechanisms:

**Approval controls** : Sampling requests may require explicit user consent. Clients can show what the server wants to analyze and why. Users can approve, deny, or modify requests.

**Transparency features** : Clients can display the exact prompt, model selection, and token limits, allowing users to review AI responses before they return to the server.

**Configuration options** : Users can set model preferences, configure auto-approval for trusted operations, or require approval for everything. Clients may provide options to redact sensitive information.

**Security considerations** : Both clients and servers must handle sensitive data appropriately during sampling. Clients should implement rate limiting and validate all message content. The human-in-the-loop design ensures that server-requested AI interactions cannot compromise security or access sensitive data without explicit user consent.

[Understanding Authorization in MCP](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/ "Understanding Authorization in MCP")[Understanding MCP servers](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/ "Understanding MCP servers")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
