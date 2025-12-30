JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * [Tree](overview-tree.html)
  * [Index](index-all.html)
  * [Search](search.html)






# All Classes and Interfaces

All Classes and InterfacesInterfacesClassesEnum ClassesRecord ClassesException ClassesAnnotation Interfaces

Class

Description

[AdkWebCorsConfig](com/google/adk/web/config/AdkWebCorsConfig.html "class in com.google.adk.web.config")

Configuration class for setting up Cross-Origin Resource Sharing (CORS) in the ADK Web application.

[AdkWebCorsProperties](com/google/adk/web/config/AdkWebCorsProperties.html "class in com.google.adk.web.config")

Properties for configuring CORS in ADK Web.

[AdkWebServer](com/google/adk/web/AdkWebServer.html "class in com.google.adk.web")

Single-file Spring Boot application for the Agent Server.

[AdkWebServer.AddSessionToEvalSetRequest](com/google/adk/web/AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web")

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/add-session requests.

[AdkWebServer.AgentController](com/google/adk/web/AdkWebServer.AgentController.html "class in com.google.adk.web")

Spring Boot REST Controller handling agent-related API endpoints.

[AdkWebServer.AgentRunRequest](com/google/adk/web/AdkWebServer.AgentRunRequest.html "class in com.google.adk.web")

Data Transfer Object (DTO) for POST /run and POST /run-sse requests.

[AdkWebServer.ApiServerSpanExporter](com/google/adk/web/AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web")

A custom SpanExporter that stores relevant span data.

[AdkWebServer.GraphResponse](com/google/adk/web/AdkWebServer.GraphResponse.html "class in com.google.adk.web")

DTO for the response of GET /apps/{appName}/users/{userId}/sessions/{sessionId}/events/{eventId}/graph.

[AdkWebServer.LiveWebSocketHandler](com/google/adk/web/AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web")

WebSocket Handler for the /run_live endpoint.

[AdkWebServer.OpenTelemetryConfig](com/google/adk/web/AdkWebServer.OpenTelemetryConfig.html "class in com.google.adk.web")

Configuration class for OpenTelemetry, setting up the tracer provider and span exporter.

[AdkWebServer.RunEvalRequest](com/google/adk/web/AdkWebServer.RunEvalRequest.html "class in com.google.adk.web")

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/run-eval requests.

[AdkWebServer.RunEvalResult](com/google/adk/web/AdkWebServer.RunEvalResult.html "class in com.google.adk.web")

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval.

[AdkWebServer.RunnerService](com/google/adk/web/AdkWebServer.RunnerService.html "class in com.google.adk.web")

Service for creating and caching Runner instances.

[AdkWebServer.WebSocketConfig](com/google/adk/web/AdkWebServer.WebSocketConfig.html "class in com.google.adk.web")

Configuration class for WebSocket handling.

[AgentCompilerLoader](com/google/adk/web/AgentCompilerLoader.html "class in com.google.adk.web")

Dynamically compiles and loads ADK [`BaseAgent`](com/google/adk/agents/BaseAgent.html "class in com.google.adk.agents") implementations from source files.

[AgentGraphGenerator](com/google/adk/web/AgentGraphGenerator.html "class in com.google.adk.web")

Utility class to generate Graphviz DOT representations of Agent structures.

[AgentLoadingProperties](com/google/adk/web/config/AgentLoadingProperties.html "class in com.google.adk.web.config")

Properties for loading agents.

[AgentTool](com/google/adk/tools/AgentTool.html "class in com.google.adk.tools")

AgentTool implements a tool that allows an agent to call another agent.

[AgentTransfer](com/google/adk/flows/llmflows/AgentTransfer.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles agent transfer for LLM flow.

[Annotations](com/google/adk/tools/Annotations.html "class in com.google.adk.tools")

Annotations for tools.

[Annotations.Schema](com/google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools")

The annotation for binding the 'Schema' input.

[ApiResponse](com/google/adk/network/ApiResponse.html "class in com.google.adk.network")

The API response contains a response to a call to the GenAI APIs.

[ApiResponse](com/google/adk/sessions/ApiResponse.html "class in com.google.adk.sessions")

The API response contains a response to a call to the GenAI APIs.

[ApplicationIntegrationToolset](com/google/adk/tools/applicationintegrationtoolset/ApplicationIntegrationToolset.html "class in com.google.adk.tools.applicationintegrationtoolset")

Application Integration Toolset

[AutoFlow](com/google/adk/flows/llmflows/AutoFlow.html "class in com.google.adk.flows.llmflows")

LLM flow with automatic agent transfer support.

[BaseAgent](com/google/adk/agents/BaseAgent.html "class in com.google.adk.agents")

Base class for all agents.

[BaseAgentConfig](com/google/adk/agents/BaseAgentConfig.html "class in com.google.adk.agents")

Base configuration for all agents.

[BaseArtifactService](com/google/adk/artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")

Base interface for artifact services.

[BaseExampleProvider](com/google/adk/examples/BaseExampleProvider.html "interface in com.google.adk.examples")

An interface that provides examples for a given query.

[BaseFlow](com/google/adk/flows/BaseFlow.html "interface in com.google.adk.flows")

Interface for the execution flows to run a group of agents.

[BaseLlm](com/google/adk/models/BaseLlm.html "class in com.google.adk.models")

Abstract base class for Large Language Models (LLMs).

[BaseLlmConnection](com/google/adk/models/BaseLlmConnection.html "interface in com.google.adk.models")

The base class for a live model connection.

[BaseLlmFlow](com/google/adk/flows/llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

A basic flow that calls the LLM in a loop until a final response is generated.

[BaseMemoryService](com/google/adk/memory/BaseMemoryService.html "interface in com.google.adk.memory")

Base contract for memory services.

[BaseRetrievalTool](com/google/adk/tools/retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")

Base class for retrieval tools.

[BaseSessionService](com/google/adk/sessions/BaseSessionService.html "interface in com.google.adk.sessions")

Defines the contract for managing [`Session`](com/google/adk/sessions/Session.html "class in com.google.adk.sessions")s and their associated [`Event`](com/google/adk/events/Event.html "class in com.google.adk.events")s.

[BaseTool](com/google/adk/tools/BaseTool.html "class in com.google.adk.tools")

The base class for all ADK tools.

[BaseToolset](com/google/adk/tools/BaseToolset.html "interface in com.google.adk.tools")

Base interface for toolsets.

[Basic](com/google/adk/flows/llmflows/Basic.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles basic information to build the LLM request.

[BuiltInCodeExecutionTool](com/google/adk/tools/BuiltInCodeExecutionTool.html "class in com.google.adk.tools")

A built-in code execution tool that is automatically invoked by Gemini 2 models.

[CallbackContext](com/google/adk/agents/CallbackContext.html "class in com.google.adk.agents")

The context of various callbacks for an agent invocation.

[Callbacks](com/google/adk/agents/Callbacks.html "class in com.google.adk.agents")

Functional interfaces for agent lifecycle callbacks.

[Callbacks.AfterAgentCallback](com/google/adk/agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterAgentCallbackSync](com/google/adk/agents/Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterAgentCallback.

[Callbacks.AfterModelCallback](com/google/adk/agents/Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterModelCallbackSync](com/google/adk/agents/Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterModelCallback.

[Callbacks.AfterToolCallback](com/google/adk/agents/Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterToolCallbackSync](com/google/adk/agents/Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterToolCallback.

[Callbacks.BeforeAgentCallback](com/google/adk/agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeAgentCallbackSync](com/google/adk/agents/Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeAgentCallback.

[Callbacks.BeforeModelCallback](com/google/adk/agents/Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeModelCallbackSync](com/google/adk/agents/Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeModelCallback.

[Callbacks.BeforeToolCallback](com/google/adk/agents/Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeToolCallbackSync](com/google/adk/agents/Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeToolCallback.

[CallbackUtil](com/google/adk/agents/CallbackUtil.html "class in com.google.adk.agents")

Utility methods for normalizing agent callbacks.

[Claude](com/google/adk/models/Claude.html "class in com.google.adk.models")

Represents the Claude Generative AI model by Anthropic.

[CollectionUtils](com/google/adk/utils/CollectionUtils.html "class in com.google.adk.utils")

Frequently used code snippets for collections.

[ConnectionsClient](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.html "class in com.google.adk.tools.applicationintegrationtoolset")

Utility class for interacting with the Google Cloud Connectors API.

[ConnectionsClient.ActionSchema](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset")

Represents the schema for an action.

[ConnectionsClient.ConnectionDetails](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset")

Represents details of a connection.

[ConnectionsClient.EntitySchemaAndOperations](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset")

Represents the schema and available operations for an entity.

[Contents](com/google/adk/flows/llmflows/Contents.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that populates content in request for LLM flows.

[ConversionUtils](com/google/adk/tools/mcp/ConversionUtils.html "class in com.google.adk.tools.mcp")

Utility class for converting between different representations of MCP tools.

[DefaultMcpTransportBuilder](com/google/adk/tools/mcp/DefaultMcpTransportBuilder.html "class in com.google.adk.tools.mcp")

The default builder for creating MCP client transports.

[Event](com/google/adk/events/Event.html "class in com.google.adk.events")

Represents an event in a session.

[Event.Builder](com/google/adk/events/Event.Builder.html "class in com.google.adk.events")

Builder for [`Event`](com/google/adk/events/Event.html "class in com.google.adk.events").

[EventActions](com/google/adk/events/EventActions.html "class in com.google.adk.events")

Represents the actions attached to an event.

[EventActions.Builder](com/google/adk/events/EventActions.Builder.html "class in com.google.adk.events")

Builder for [`EventActions`](com/google/adk/events/EventActions.html "class in com.google.adk.events").

[EventStream](com/google/adk/events/EventStream.html "class in com.google.adk.events")

Iterable stream of [`Event`](com/google/adk/events/Event.html "class in com.google.adk.events") objects.

[Example](com/google/adk/examples/Example.html "class in com.google.adk.examples")

Represents an few-shot example.

[Example.Builder](com/google/adk/examples/Example.Builder.html "class in com.google.adk.examples")

Builder for constructing [`Example`](com/google/adk/examples/Example.html "class in com.google.adk.examples") instances.

[Examples](com/google/adk/flows/llmflows/Examples.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that populates examples in LLM request.

[ExampleUtils](com/google/adk/examples/ExampleUtils.html "class in com.google.adk.examples")

Utility class for examples.

[ExitLoopTool](com/google/adk/tools/ExitLoopTool.html "class in com.google.adk.tools")

Exits the loop.

[FunctionCallingUtils](com/google/adk/tools/FunctionCallingUtils.html "class in com.google.adk.tools")

Utility class for function calling.

[Functions](com/google/adk/flows/llmflows/Functions.html "class in com.google.adk.flows.llmflows")

Utility class for handling function calls.

[FunctionTool](com/google/adk/tools/FunctionTool.html "class in com.google.adk.tools")

FunctionTool implements a customized function calling tool.

[GcsArtifactService](com/google/adk/artifacts/GcsArtifactService.html "class in com.google.adk.artifacts")

An artifact service implementation using Google Cloud Storage (GCS).

[Gemini](com/google/adk/models/Gemini.html "class in com.google.adk.models")

Represents the Gemini Generative AI model.

[Gemini.Builder](com/google/adk/models/Gemini.Builder.html "class in com.google.adk.models")

Builder for [`Gemini`](com/google/adk/models/Gemini.html "class in com.google.adk.models").

[GeminiLlmConnection](com/google/adk/models/GeminiLlmConnection.html "class in com.google.adk.models")

Manages a persistent, bidirectional connection to the Gemini model via WebSockets for real-time interaction.

[GetSessionConfig](com/google/adk/sessions/GetSessionConfig.html "class in com.google.adk.sessions")

Configuration for getting a session.

[GetSessionConfig.Builder](com/google/adk/sessions/GetSessionConfig.Builder.html "class in com.google.adk.sessions")

Builder for [`GetSessionConfig`](com/google/adk/sessions/GetSessionConfig.html "class in com.google.adk.sessions").

[GoogleSearchTool](com/google/adk/tools/GoogleSearchTool.html "class in com.google.adk.tools")

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Search.

[HttpApiClient](com/google/adk/sessions/HttpApiClient.html "class in com.google.adk.sessions")

Base client for the HTTP APIs.

[HttpApiResponse](com/google/adk/network/HttpApiResponse.html "class in com.google.adk.network")

Wraps a real HTTP response to expose the methods needed by the GenAI SDK.

[HttpApiResponse](com/google/adk/sessions/HttpApiResponse.html "class in com.google.adk.sessions")

Wraps a real HTTP response to expose the methods needed by the GenAI SDK.

[Identity](com/google/adk/flows/llmflows/Identity.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that gives the agent identity from the framework

[InMemoryArtifactService](com/google/adk/artifacts/InMemoryArtifactService.html "class in com.google.adk.artifacts")

An in-memory implementation of the [`BaseArtifactService`](com/google/adk/artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts").

[InMemoryMemoryService](com/google/adk/memory/InMemoryMemoryService.html "class in com.google.adk.memory")

An in-memory memory service for prototyping purposes only.

[InMemoryRunner](com/google/adk/runner/InMemoryRunner.html "class in com.google.adk.runner")

The class for the in-memory GenAi runner, using in-memory artifact and session services.

[InMemorySessionService](com/google/adk/sessions/InMemorySessionService.html "class in com.google.adk.sessions")

An in-memory implementation of [`BaseSessionService`](com/google/adk/sessions/BaseSessionService.html "interface in com.google.adk.sessions") assuming [`Session`](com/google/adk/sessions/Session.html "class in com.google.adk.sessions") objects are mutable regarding their state map, events list, and last update time.

[Instruction](com/google/adk/agents/Instruction.html "interface in com.google.adk.agents")

Represents an instruction that can be provided to an agent to guide its behavior.

[Instruction.Provider](com/google/adk/agents/Instruction.Provider.html "class in com.google.adk.agents")

Returns an instruction dynamically constructed from the given context.

[Instruction.Static](com/google/adk/agents/Instruction.Static.html "class in com.google.adk.agents")

Plain instruction directly provided to the agent.

[Instructions](com/google/adk/flows/llmflows/Instructions.html "class in com.google.adk.flows.llmflows")

[`RequestProcessor`](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles instructions and global instructions for LLM flows.

[InstructionUtils](com/google/adk/utils/InstructionUtils.html "class in com.google.adk.utils")

Utility methods for handling instruction templates.

[IntegrationClient](com/google/adk/tools/applicationintegrationtoolset/IntegrationClient.html "class in com.google.adk.tools.applicationintegrationtoolset")

Utility class for interacting with Google Cloud Application Integration.

[IntegrationConnectorTool](com/google/adk/tools/applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset")

Application Integration Tool

[InvocationContext](com/google/adk/agents/InvocationContext.html "class in com.google.adk.agents")

The context for an agent invocation.

[JsonBaseModel](com/google/adk/JsonBaseModel.html "class in com.google.adk")

The base class for the types that needs JSON serialization/deserialization capability.

[LangChain4j](com/google/adk/models/langchain4j/LangChain4j.html "class in com.google.adk.models.langchain4j")

 

[ListArtifactsResponse](com/google/adk/artifacts/ListArtifactsResponse.html "class in com.google.adk.artifacts")

Response for listing artifacts.

[ListArtifactsResponse.Builder](com/google/adk/artifacts/ListArtifactsResponse.Builder.html "class in com.google.adk.artifacts")

Builder for [`ListArtifactsResponse`](com/google/adk/artifacts/ListArtifactsResponse.html "class in com.google.adk.artifacts").

[ListArtifactVersionsResponse](com/google/adk/artifacts/ListArtifactVersionsResponse.html "class in com.google.adk.artifacts")

Response for listing artifact versions.

[ListArtifactVersionsResponse.Builder](com/google/adk/artifacts/ListArtifactVersionsResponse.Builder.html "class in com.google.adk.artifacts")

Builder for [`ListArtifactVersionsResponse`](com/google/adk/artifacts/ListArtifactVersionsResponse.html "class in com.google.adk.artifacts").

[ListEventsResponse](com/google/adk/sessions/ListEventsResponse.html "class in com.google.adk.sessions")

Response for listing events.

[ListEventsResponse.Builder](com/google/adk/sessions/ListEventsResponse.Builder.html "class in com.google.adk.sessions")

Builder for [`ListEventsResponse`](com/google/adk/sessions/ListEventsResponse.html "class in com.google.adk.sessions").

[ListSessionsResponse](com/google/adk/sessions/ListSessionsResponse.html "class in com.google.adk.sessions")

Response for listing sessions.

[ListSessionsResponse.Builder](com/google/adk/sessions/ListSessionsResponse.Builder.html "class in com.google.adk.sessions")

Builder for [`ListSessionsResponse`](com/google/adk/sessions/ListSessionsResponse.html "class in com.google.adk.sessions").

[LiveRequest](com/google/adk/agents/LiveRequest.html "class in com.google.adk.agents")

Represents a request to be sent to a live connection to the LLM model.

[LiveRequest.Builder](com/google/adk/agents/LiveRequest.Builder.html "class in com.google.adk.agents")

Builder for constructing [`LiveRequest`](com/google/adk/agents/LiveRequest.html "class in com.google.adk.agents") instances.

[LiveRequestQueue](com/google/adk/agents/LiveRequestQueue.html "class in com.google.adk.agents")

A queue of live requests to be sent to the model.

[LlmAgent](com/google/adk/agents/LlmAgent.html "class in com.google.adk.agents")

The LLM-based agent.

[LlmAgent.Builder](com/google/adk/agents/LlmAgent.Builder.html "class in com.google.adk.agents")

Builder for [`LlmAgent`](com/google/adk/agents/LlmAgent.html "class in com.google.adk.agents").

[LlmAgent.IncludeContents](com/google/adk/agents/LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")

Enum to define if contents of previous events should be included in requests to the underlying LLM.

[LlmAgentConfig](com/google/adk/agents/LlmAgentConfig.html "class in com.google.adk.agents")

Configuration for LlmAgent.

[LlmCallsLimitExceededException](com/google/adk/exceptions/LlmCallsLimitExceededException.html "class in com.google.adk.exceptions")

An error indicating that the limit for calls to the LLM has been exceeded.

[LlmRegistry](com/google/adk/models/LlmRegistry.html "class in com.google.adk.models")

Central registry for managing Large Language Model (LLM) instances.

[LlmRegistry.LlmFactory](com/google/adk/models/LlmRegistry.LlmFactory.html "interface in com.google.adk.models")

The factory interface for creating LLM instances.

[LlmRequest](com/google/adk/models/LlmRequest.html "class in com.google.adk.models")

Represents a request to be sent to the LLM.

[LlmRequest.Builder](com/google/adk/models/LlmRequest.Builder.html "class in com.google.adk.models")

Builder for constructing [`LlmRequest`](com/google/adk/models/LlmRequest.html "class in com.google.adk.models") instances.

[LlmResponse](com/google/adk/models/LlmResponse.html "class in com.google.adk.models")

Represents a response received from the LLM.

[LlmResponse.Builder](com/google/adk/models/LlmResponse.Builder.html "class in com.google.adk.models")

Builder for constructing [`LlmResponse`](com/google/adk/models/LlmResponse.html "class in com.google.adk.models") instances.

[LoadArtifactsTool](com/google/adk/tools/LoadArtifactsTool.html "class in com.google.adk.tools")

A tool that loads artifacts and adds them to the session.

[LongRunningFunctionTool](com/google/adk/tools/LongRunningFunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

[LoopAgent](com/google/adk/agents/LoopAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially in a loop.

[LoopAgent.Builder](com/google/adk/agents/LoopAgent.Builder.html "class in com.google.adk.agents")

Builder for [`LoopAgent`](com/google/adk/agents/LoopAgent.html "class in com.google.adk.agents").

[McpAsyncTool](com/google/adk/tools/mcp/McpAsyncTool.html "class in com.google.adk.tools.mcp")

Initializes a MCP tool.

[McpSessionManager](com/google/adk/tools/mcp/McpSessionManager.html "class in com.google.adk.tools.mcp")

Manages MCP client sessions.

[McpTool](com/google/adk/tools/mcp/McpTool.html "class in com.google.adk.tools.mcp")

Initializes a MCP tool.

[McpToolset](com/google/adk/tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp")

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools.

[McpToolset.McpInitializationException](com/google/adk/tools/mcp/McpToolset.McpInitializationException.html "class in com.google.adk.tools.mcp")

Exception thrown when there's an error during MCP session initialization.

[McpToolset.McpToolLoadingException](com/google/adk/tools/mcp/McpToolset.McpToolLoadingException.html "class in com.google.adk.tools.mcp")

Exception thrown when there's an error during loading tools from the MCP server.

[McpToolset.McpToolsetException](com/google/adk/tools/mcp/McpToolset.McpToolsetException.html "class in com.google.adk.tools.mcp")

Base exception for all errors originating from `McpToolset`.

[McpTransportBuilder](com/google/adk/tools/mcp/McpTransportBuilder.html "interface in com.google.adk.tools.mcp")

Interface for building McpClientTransport instances.

[MemoryEntry](com/google/adk/memory/MemoryEntry.html "class in com.google.adk.memory")

Represents one memory entry.

[MemoryEntry.Builder](com/google/adk/memory/MemoryEntry.Builder.html "class in com.google.adk.memory")

Builder for [`MemoryEntry`](com/google/adk/memory/MemoryEntry.html "class in com.google.adk.memory").

[Model](com/google/adk/models/Model.html "class in com.google.adk.models")

Represents a model by name or instance.

[Model.Builder](com/google/adk/models/Model.Builder.html "class in com.google.adk.models")

Builder for [`Model`](com/google/adk/models/Model.html "class in com.google.adk.models").

[Pairs](com/google/adk/utils/Pairs.html "class in com.google.adk.utils")

Utility class for creating ConcurrentHashMaps.

[ParallelAgent](com/google/adk/agents/ParallelAgent.html "class in com.google.adk.agents")

A shell agent that runs its sub-agents in parallel in isolated manner.

[ParallelAgent.Builder](com/google/adk/agents/ParallelAgent.Builder.html "class in com.google.adk.agents")

Builder for [`ParallelAgent`](com/google/adk/agents/ParallelAgent.html "class in com.google.adk.agents").

[ReadonlyContext](com/google/adk/agents/ReadonlyContext.html "class in com.google.adk.agents")

Provides read-only access to the context of an agent run.

[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows")

 

[RequestProcessor.RequestProcessingResult](com/google/adk/flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")

 

[ResponseProcessor](com/google/adk/flows/llmflows/ResponseProcessor.html "interface in com.google.adk.flows.llmflows")

 

[ResponseProcessor.ResponseProcessingResult](com/google/adk/flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")

 

[RunConfig](com/google/adk/agents/RunConfig.html "class in com.google.adk.agents")

Configuration to modify an agent's LLM's underlying behavior.

[RunConfig.Builder](com/google/adk/agents/RunConfig.Builder.html "class in com.google.adk.agents")

Builder for [`RunConfig`](com/google/adk/agents/RunConfig.html "class in com.google.adk.agents").

[RunConfig.StreamingMode](com/google/adk/agents/RunConfig.StreamingMode.html "enum class in com.google.adk.agents")

Streaming mode for the runner.

[Runner](com/google/adk/runner/Runner.html "class in com.google.adk.runner")

The main class for the GenAI Agents runner.

[SchemaUtils](com/google/adk/SchemaUtils.html "class in com.google.adk")

Utility class for validating schemas.

[SearchMemoryResponse](com/google/adk/memory/SearchMemoryResponse.html "class in com.google.adk.memory")

Represents the response from a memory search.

[SearchMemoryResponse.Builder](com/google/adk/memory/SearchMemoryResponse.Builder.html "class in com.google.adk.memory")

Builder for [`SearchMemoryResponse`](com/google/adk/memory/SearchMemoryResponse.html "class in com.google.adk.memory").

[SequentialAgent](com/google/adk/agents/SequentialAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially.

[SequentialAgent.Builder](com/google/adk/agents/SequentialAgent.Builder.html "class in com.google.adk.agents")

Builder for [`SequentialAgent`](com/google/adk/agents/SequentialAgent.html "class in com.google.adk.agents").

[Session](com/google/adk/sessions/Session.html "class in com.google.adk.sessions")

A [`Session`](com/google/adk/sessions/Session.html "class in com.google.adk.sessions") object that encapsulates the [`State`](com/google/adk/sessions/State.html "class in com.google.adk.sessions") and [`Event`](com/google/adk/events/Event.html "class in com.google.adk.events")s of a session.

[Session.Builder](com/google/adk/sessions/Session.Builder.html "class in com.google.adk.sessions")

Builder for [`Session`](com/google/adk/sessions/Session.html "class in com.google.adk.sessions").

[SessionException](com/google/adk/sessions/SessionException.html "class in com.google.adk.sessions")

Represents a general error that occurred during session management operations.

[SessionNotFoundException](com/google/adk/sessions/SessionNotFoundException.html "class in com.google.adk.sessions")

Indicates that a requested session could not be found.

[SessionUtils](com/google/adk/sessions/SessionUtils.html "class in com.google.adk.sessions")

Utility functions for session service.

[SingleFlow](com/google/adk/flows/llmflows/SingleFlow.html "class in com.google.adk.flows.llmflows")

Basic LLM flow with fixed request processors and no response post-processing.

[SpeechClientInterface](com/google/adk/flows/llmflows/audio/SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")

Interface for a speech-to-text client.

[SseServerParameters](com/google/adk/tools/mcp/SseServerParameters.html "class in com.google.adk.tools.mcp")

Parameters for establishing a MCP Server-Sent Events (SSE) connection.

[SseServerParameters.Builder](com/google/adk/tools/mcp/SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Builder for [`SseServerParameters`](com/google/adk/tools/mcp/SseServerParameters.html "class in com.google.adk.tools.mcp").

[State](com/google/adk/sessions/State.html "class in com.google.adk.sessions")

A [`State`](com/google/adk/sessions/State.html "class in com.google.adk.sessions") object that also keeps track of the changes to the state.

[Telemetry](com/google/adk/Telemetry.html "class in com.google.adk")

Utility class for capturing and reporting telemetry data within the ADK.

[ToolContext](com/google/adk/tools/ToolContext.html "class in com.google.adk.tools")

ToolContext object provides a structured context for executing tools or functions.

[ToolContext.Builder](com/google/adk/tools/ToolContext.Builder.html "class in com.google.adk.tools")

Builder for [`ToolContext`](com/google/adk/tools/ToolContext.html "class in com.google.adk.tools").

[ToolPredicate](com/google/adk/tools/ToolPredicate.html "interface in com.google.adk.tools")

Functional interface to decide whether a tool should be exposed to the LLM based on the current context.

[Version](com/google/adk/Version.html "class in com.google.adk")

Tracks the current ADK version.

[VertexAiRagRetrieval](com/google/adk/tools/retrieval/VertexAiRagRetrieval.html "class in com.google.adk.tools.retrieval")

A retrieval tool that fetches context from Vertex AI RAG.

[VertexAiSessionService](com/google/adk/sessions/VertexAiSessionService.html "class in com.google.adk.sessions")

TODO: Use the genai HttpApiClient and ApiResponse methods once they are public.

[VertexCredentials](com/google/adk/models/VertexCredentials.html "class in com.google.adk.models")

Credentials for accessing Gemini models through Vertex.

[VertexCredentials.Builder](com/google/adk/models/VertexCredentials.Builder.html "class in com.google.adk.models")

Builder for [`VertexCredentials`](com/google/adk/models/VertexCredentials.html "class in com.google.adk.models").

[VertexSpeechClient](com/google/adk/flows/llmflows/audio/VertexSpeechClient.html "class in com.google.adk.flows.llmflows.audio")

Implementation of SpeechClientInterface using Vertex AI SpeechClient.

* * *

Copyright (C) 2025\. All rights reserved.
