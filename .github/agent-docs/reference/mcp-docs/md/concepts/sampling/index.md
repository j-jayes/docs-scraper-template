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
    * [Sampling](https://modelcontextprotocol.info/specification/2026-07-28/client/sampling/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/specification/2026-07-28/client/sampling/)
  * [简体中文](https://mcpcn.com/specification/2026-07-28/client/sampling/)



  * Light 

  * Dark 

  * System 




On this page

  * User Interaction Model
  * Tools in Sampling
  * Capabilities
  * Protocol Messages
  * Creating Messages
  * Sampling with Tools
  * Multi-turn Tool Loop
  * Message Content Constraints
  * Tool Result Messages
  * Tool Use and Result Balance
  * Cross-API Compatibility
  * Message Roles
  * Tool Choice Modes
  * Parallel Tool Use
  * Message Flow
  * Data Types
  * Messages
  * Text Content
  * Image Content
  * Audio Content
  * Model Preferences
  * Capability Priorities
  * Model Hints
  * System Prompt
  * Context Inclusion
  * Sampling Parameters
  * Result Fields
  * Error Handling
  * Security Considerations



Scroll to top

[Specification](https://modelcontextprotocol.info/specification/)

[Specification](https://modelcontextprotocol.info/specification/2026-07-28/)

Sampling

# Sampling

Source: [MCP 29affa6b](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/29affa6b11e2dbd5a8b5678e9b90aa4a336769a4/docs/specification/2026-07-28/client/sampling.mdx)

**Deprecated** : The Sampling feature is deprecated as of protocol version `2026-07-28` ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)). Under the [feature lifecycle policy](https://modelcontextprotocol.info/community/feature-lifecycle/), it remains in the specification for at least twelve months after this revision's release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to integrating directly with LLM provider APIs. See the [deprecated features registry](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/).

The Model Context Protocol (MCP) provides a standardized way for servers to request LLM sampling ("completions" or "generations") from language models via clients. This flow allows clients to maintain control over model access, selection, and permissions while enabling servers to leverage AI capabilities—with no server API keys necessary. Servers can request text, audio, or image-based interactions and optionally include context from MCP servers in their prompts.

## User Interaction Model

Sampling in MCP allows servers to implement agentic behaviors, by enabling LLM calls to occur _nested_ inside other MCP server features.

Implementations are free to expose sampling through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

For trust & safety and security, there **SHOULD** always be a human in the loop with the ability to deny sampling requests.

Applications **SHOULD** :

  * Provide UI that makes it easy and intuitive to review sampling requests
  * Allow users to view and edit prompts before sending
  * Present generated responses for review before delivery



## Tools in Sampling

Servers can request that the client's LLM use tools during sampling by providing a `tools` array and optional `toolChoice` configuration in their sampling requests. The tool definitions in the `tools` array are scoped to the sampling request — they don't need to correspond to registered tools. This enables servers to implement agentic behaviors where the LLM can call specially designated tools, receive results, and continue the conversation - all within a single sampling request flow.

Clients **MUST** declare support for tool use via the `sampling.tools` capability to receive tool-enabled sampling requests. Servers **MUST NOT** send tool-enabled sampling requests to Clients that have not declared support for tool use via the `sampling.tools` capability.

## Capabilities

Clients that support sampling **MUST** declare the `sampling` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request:

**Basic sampling:**
    
    
    {
      "_meta": {
        "io.modelcontextprotocol/clientCapabilities": {
          "sampling": {}
        }
      }
    }

**With tool use support:**
    
    
    {
      "_meta": {
        "io.modelcontextprotocol/clientCapabilities": {
          "sampling": {
            "tools": {}
          }
        }
      }
    }

**With context inclusion support (deprecated):**
    
    
    {
      "_meta": {
        "io.modelcontextprotocol/clientCapabilities": {
          "sampling": {
            "context": {}
          }
        }
      }
    }

The `includeContext` parameter values `"thisServer"` and `"allServers"` are deprecated under the [feature lifecycle policy](https://modelcontextprotocol.info/community/feature-lifecycle/#deprecating-a-feature) ([SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)); they will be removed no later than the Sampling feature itself. Servers **SHOULD** avoid using these values (e.g. can just omit `includeContext` since it defaults to `"none"`), and **SHOULD NOT** use them unless the client declares `sampling.context` capability. See the [deprecated features registry](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/).

## Protocol Messages

### Creating Messages

To request a language model generation during the processing of a client request, servers send an `InputRequiredResult` containing a `sampling/createMessage` request:

**Input request (delivered inside[`InputRequiredResult.inputRequests`](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/#inputrequests)):**
    
    
    {
      "method": "sampling/createMessage",
      "params": {
        "messages": [
          {
            "role": "user",
            "content": {
              "type": "text",
              "text": "What is the capital of France?"
            }
          }
        ],
        "modelPreferences": {
          "hints": [
            {
              "name": "claude-3-sonnet"
            }
          ],
          "costPriority": 0.3,
          "intelligencePriority": 0.8,
          "speedPriority": 0.5
        },
        "temperature": 0.1,
        "systemPrompt": "You are a helpful assistant.",
        "includeContext": "thisServer",
        "maxTokens": 100
      }
    }

**Client result (returned inside`inputResponses` on the retried request):**
    
    
    {
      "role": "assistant",
      "content": {
        "type": "text",
        "text": "The capital of France is Paris."
      },
      "model": "claude-3-sonnet-20240307",
      "stopReason": "endTurn"
    }

### Sampling with Tools

The following diagram illustrates the complete flow of sampling with tools, including the multi-turn tool loop:
    
    
      sequenceDiagram
        participant Server
        participant Client
        participant User
        participant LLM
    
        Client->>Server: tools/call(id:1)
        note right of Server: Server needs more info
        Server->>Client: InputRequiredResult(<br/>sampling/createMessage<br/>(messages + tools))
    
        Note over Client,User: Human-in-the-loop review
        Client->>User: Present request for approval
        User-->>Client: Approve/modify
    
        Client->>LLM: Forward request with tools
        LLM-->>Client: Response with tool_use<br/>(stopReason: "toolUse")
    
        Client->>User: Present tool calls for review
        User-->>Client: Approve tool calls
        Client-->>Server: tools/call(id:2, Return tool_use response)
    
        Note over Server: Execute tool(s)
        Server->>Server: Run get_weather("Paris")<br/>Run get_weather("London")
    
        Note over Server,Client: Continue with tool results
        Server->>Client: InputRequiredResult(<br/>sampling/createMessage<br/>(history + tool_results + tools))
    
        Client->>User: Present continuation
        User-->>Client: Approve
    
        Client->>LLM: Forward with tool results
        LLM-->>Client: Final text response<br/>(stopReason: "endTurn")
    
        Client->>User: Present response
        User-->>Client: Approve
        Client-->>Server: tools/call(id:3, Return final response)
    
        Note over Server: Server processes result<br/>(may continue conversation...)
    

To request LLM generation with tool use capabilities, servers include `tools` and optionally `toolChoice` in the request:

**Input request (Server -> Client, delivered inside`InputRequiredResult.inputRequests`):**
    
    
    {
      "method": "sampling/createMessage",
      "params": {
        "messages": [
          {
            "role": "user",
            "content": {
              "type": "text",
              "text": "What's the weather like in Paris and London?"
            }
          }
        ],
        "tools": [
          {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "inputSchema": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string",
                  "description": "City name"
                }
              },
              "required": ["city"]
            }
          }
        ],
        "toolChoice": {
          "mode": "auto"
        },
        "maxTokens": 1000
      }
    }

**Client result (Client -> Server, returned inside`inputResponses` on the retried request):**
    
    
    {
      "role": "assistant",
      "content": [
        {
          "type": "tool_use",
          "id": "call_abc123",
          "name": "get_weather",
          "input": {
            "city": "Paris"
          }
        },
        {
          "type": "tool_use",
          "id": "call_def456",
          "name": "get_weather",
          "input": {
            "city": "London"
          }
        }
      ],
      "model": "claude-3-sonnet-20240307",
      "stopReason": "toolUse"
    }

### Multi-turn Tool Loop

After receiving tool use requests from the LLM, the server typically:

  1. Executes the requested tool uses.
  2. Sends a new sampling request with the tool results appended
  3. Receives the LLM's response (which might contain new tool uses)
  4. Repeats as many times as needed (server might cap the maximum number of iterations, and e.g. pass `toolChoice: {mode: "none"}` on the last iteration to force a final result)



**Follow-up input request (Server -> Client, delivered inside`InputRequiredResult.inputRequests`) with tool results:**
    
    
    {
      "method": "sampling/createMessage",
      "params": {
        "messages": [
          {
            "role": "user",
            "content": {
              "type": "text",
              "text": "What's the weather like in Paris and London?"
            }
          },
          {
            "role": "assistant",
            "content": [
              {
                "type": "tool_use",
                "id": "call_abc123",
                "name": "get_weather",
                "input": { "city": "Paris" }
              },
              {
                "type": "tool_use",
                "id": "call_def456",
                "name": "get_weather",
                "input": { "city": "London" }
              }
            ]
          },
          {
            "role": "user",
            "content": [
              {
                "type": "tool_result",
                "toolUseId": "call_abc123",
                "content": [
                  {
                    "type": "text",
                    "text": "Weather in Paris: 18°C, partly cloudy"
                  }
                ]
              },
              {
                "type": "tool_result",
                "toolUseId": "call_def456",
                "content": [
                  {
                    "type": "text",
                    "text": "Weather in London: 15°C, rainy"
                  }
                ]
              }
            ]
          }
        ],
        "tools": [
          {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "inputSchema": {
              "type": "object",
              "properties": {
                "city": { "type": "string" }
              },
              "required": ["city"]
            }
          }
        ],
        "maxTokens": 1000
      }
    }

**Final client result (Client -> Server, returned inside`inputResponses` on the retried request):**
    
    
    {
      "role": "assistant",
      "content": {
        "type": "text",
        "text": "Based on the current weather data:\n\n- **Paris**: 18°C and partly cloudy - quite pleasant!\n- **London**: 15°C and rainy - you'll want an umbrella.\n\nParis has slightly warmer and drier conditions today."
      },
      "model": "claude-3-sonnet-20240307",
      "stopReason": "endTurn"
    }

## Message Content Constraints

### Tool Result Messages

When a user message contains tool results (type: "tool_result"), it **MUST** contain ONLY tool results. Mixing tool results with other content types (text, image, audio) in the same message is not allowed.

This constraint ensures compatibility with provider APIs that use dedicated roles for tool results (e.g., OpenAI's "tool" role, Gemini's "function" role).

**Valid - single tool result:**
    
    
    {
      "role": "user",
      "content": {
        "type": "tool_result",
        "toolUseId": "call_123",
        "content": [{ "type": "text", "text": "Result data" }]
      }
    }

**Valid - multiple tool results:**
    
    
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "toolUseId": "call_123",
          "content": [{ "type": "text", "text": "Result 1" }]
        },
        {
          "type": "tool_result",
          "toolUseId": "call_456",
          "content": [{ "type": "text", "text": "Result 2" }]
        }
      ]
    }

**Invalid - mixed content:**
    
    
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Here are the results:"
        },
        {
          "type": "tool_result",
          "toolUseId": "call_123",
          "content": [{ "type": "text", "text": "Result data" }]
        }
      ]
    }

### Tool Use and Result Balance

When using tool use in sampling, every assistant message containing `ToolUseContent` blocks **MUST** be followed by a user message that consists entirely of `ToolResultContent` blocks, with each tool use (e.g. with `id: $id`) matched by a corresponding tool result (with `toolUseId: $id`), before any other message.

This requirement ensures:

  * Tool uses are always resolved before the conversation continues
  * Provider APIs can concurrently process multiple tool uses and fetch their results in parallel
  * The conversation maintains a consistent request-response pattern



**Example valid sequence:**

  1. User message: "What's the weather like in Paris and London?"
  2. Assistant message: `ToolUseContent` (`id: "call_abc123", name: "get_weather", input: {city: "Paris"}`) + `ToolUseContent` (`id: "call_def456", name: "get_weather", input: {city: "London"}`)
  3. User message: `ToolResultContent` (`toolUseId: "call_abc123", content: "18°C, partly cloudy"`) + `ToolResultContent` (`toolUseId: "call_def456", content: "15°C, rainy"`)
  4. Assistant message: Text response comparing the weather in both cities



**Invalid sequence - missing tool result:**

  1. User message: "What's the weather like in Paris and London?"
  2. Assistant message: `ToolUseContent` (`id: "call_abc123", name: "get_weather", input: {city: "Paris"}`) + `ToolUseContent` (`id: "call_def456", name: "get_weather", input: {city: "London"}`)
  3. User message: `ToolResultContent` (`toolUseId: "call_abc123", content: "18°C, partly cloudy"`) ← Missing result for call_def456
  4. Assistant message: Text response (invalid - not all tool uses were resolved)



## Cross-API Compatibility

The sampling specification is designed to work across multiple LLM provider APIs (Claude, OpenAI, Gemini, etc.). Key design decisions for compatibility:

### Message Roles

MCP uses two roles: "user" and "assistant".

Tool use requests are sent in CreateMessageResult with the "assistant" role. Tool results are sent back in messages with the "user" role. Messages with tool results cannot contain other kinds of content.

### Tool Choice Modes

`CreateMessageRequest.params.toolChoice` controls the tool use ability of the model:

  * `{mode: "auto"}`: Model decides whether to use tools (default)
  * `{mode: "required"}`: Model MUST use at least one tool before completing
  * `{mode: "none"}`: Model MUST NOT use any tools



### Parallel Tool Use

MCP allows models to make multiple tool use requests in parallel (returning an array of `ToolUseContent`). All major provider APIs support this:

  * **Claude** : Supports parallel tool use natively
  * **OpenAI** : Supports parallel tool calls (can be disabled with `parallel_tool_calls: false`)
  * **Gemini** : Supports parallel function calls natively



Implementations wrapping providers that support disabling parallel tool use MAY expose this as an extension, but it is not part of the core MCP specification.

## Message Flow
    
    
      sequenceDiagram
        participant Server
        participant Client
        participant User
        participant LLM
    
        Client->>Server: tools/call(id:1)
        note right of Server: Server needs more info
        Server->>Client: InputRequiredResult(<br/>sampling/createMessage<br/>(messages + tools))
    
        Note over Client,User: Human-in-the-loop review
        Client->>User: Present request for approval
        User-->>Client: Review and approve/modify
    
        Note over Client,LLM: Model interaction
        Client->>LLM: Forward approved request
        LLM-->>Client: Return generation
    
        Note over Client,User: Response review
        Client->>User: Present response for approval
        User-->>Client: Review and approve/modify
    
        Note over Server,Client: Replay Request with approved response
        Client-->>Server: tools/call(id:3, Return approved response)
    

## Data Types

### Messages

Sampling messages **MUST** contain a `role` field of `"user"` or `"assistant"`; and a `content` field representing the message data.

The list of messages in a sampling request **SHOULD NOT** be retained between separate requests.

The `content` field can contain:

#### Text Content
    
    
    {
      "type": "text",
      "text": "The message content"
    }

#### Image Content
    
    
    {
      "type": "image",
      "data": "base64-encoded-image-data",
      "mimeType": "image/jpeg"
    }

#### Audio Content
    
    
    {
      "type": "audio",
      "data": "base64-encoded-audio-data",
      "mimeType": "audio/wav"
    }

### Model Preferences

Model selection in MCP requires careful abstraction since servers and clients may use different AI providers with distinct model offerings. A server cannot simply request a specific model by name since the client may not have access to that exact model or may prefer to use a different provider's equivalent model.

To solve this, MCP implements a preference system that combines abstract capability priorities with optional model hints:

#### Capability Priorities

Servers express their needs through three normalized priority values (0-1):

  * `costPriority`: How important is minimizing costs? Higher values prefer cheaper models.
  * `speedPriority`: How important is low latency? Higher values prefer faster models.
  * `intelligencePriority`: How important are advanced capabilities? Higher values prefer more capable models.



#### Model Hints

While priorities help select models based on characteristics, `hints` allow servers to suggest specific models or model families:

  * Hints are treated as substrings that can match model names flexibly
  * Multiple hints are evaluated in order of preference
  * Clients **MAY** map hints to equivalent models from different providers
  * Hints are advisory—clients make final model selection



For example:
    
    
    {
      "hints": [
        { "name": "claude-3-sonnet" }, // Prefer Sonnet-class models
        { "name": "claude" } // Fall back to any Claude model
      ],
      "costPriority": 0.3, // Cost is less important
      "speedPriority": 0.8, // Speed is very important
      "intelligencePriority": 0.5 // Moderate capability needs
    }

The client processes these preferences to select an appropriate model from its available options. For instance, if the client doesn't have access to Claude models but has Gemini, it might map the sonnet hint to `gemini-1.5-pro` based on similar capabilities.

### System Prompt

The optional `systemPrompt` field allows servers to request a specific system prompt. The client **MAY** modify or ignore this field without communicating this to the server.

### Context Inclusion

The `includeContext` parameter specifies what context information the client is expected to include in its response:

  * `"none"`: No additional context.
  * `"thisServer"`: Include context from the requesting server.
  * `"allServers"`: Include context from all connected MCP servers.



The `"thisServer"` and `"allServers"` values are deprecated; see Capabilities.

The client **MAY** modify or ignore this field without communicating this to the server. For example, a client could determine that respecting this field in a particular request would require sharing sensitive information with a server, and constrain its response accordingly.

### Sampling Parameters

LLM sampling can be fine-tuned with the following parameters:

  * `temperature`: Controls randomness in model responses. Higher values produce higher randomness, and lower values produce more stable output. Valid range depends upon the model provider.
  * `maxTokens`: Maximum tokens to generate; required.
  * `stopSequences`: Array of sequences that stop generation.
  * `metadata`: Additional provider-specific parameters.



The client **MUST** respect the `maxTokens` parameter.

The client **MAY** modify or ignore `temperature`, `stopSequences` and `metadata`. For example, a client could use a model that does not support one or more of these parameters, and would therefore be unable to leverage them.

### Result Fields

Sampling results will contain the following fields:

  * `role`: The message role; see Messages.

  * `content`: The message content. This can be either:

    * A single content block when the response contains only one content block, such as a single text response.
    * An array of content blocks when the response contains one or more content blocks, such as multiple tool uses or mixed content.

See Messages for content block types.

  * `model`: The name of the model that generated the message.

  * `stopReason`: The reason why sampling stopped, if known. The specification defines the following (non-exhaustive) stop reasons, although implementations **MAY** provide their own arbitrary values:

    * `"endTurn"`: The participant is yielding the conversation to the other party.
    * `"stopSequence"`: Message generation encountered one of the requested `stopSequences`.
    * `"maxTokens"`: The token limit was reached.
    * `"toolUse"`: The model wants to use one or more tools.



## Error Handling

If an error occurs or the user declines the sampling request, the client does not need to replay the initial call with an error message, as the server is not waiting for a response with the `InputRequiredResult` pattern.

## Security Considerations

  1. Clients **SHOULD** implement user approval controls
  2. Both parties **SHOULD** validate message content
  3. Clients **SHOULD** respect model preference hints
  4. Clients **SHOULD** implement rate limiting
  5. Both parties **MUST** handle sensitive data appropriately



When tools are used in sampling, additional security considerations apply:

  6. Servers **MUST** ensure that when replying to a `stopReason: "toolUse"`, each `ToolUseContent` item is responded to with a `ToolResultContent` item with a matching `toolUseId`, and that the user message contains only tool results (no other content types)
  7. Both parties **SHOULD** implement iteration limits for tool loops



[Roots](https://modelcontextprotocol.info/specification/2026-07-28/client/roots/ "Roots")[Schema Reference](https://modelcontextprotocol.info/specification/2026-07-28/schema/ "Schema Reference")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
