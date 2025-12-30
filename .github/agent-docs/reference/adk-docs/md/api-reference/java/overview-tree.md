JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * Tree
  * [Index](index-all.html)
  * [Search](search.html)






# Hierarchy For All Packages

Package Hierarchies:

  * [com.google.adk](com/google/adk/package-tree.html), 
  * [com.google.adk.agents](com/google/adk/agents/package-tree.html), 
  * [com.google.adk.artifacts](com/google/adk/artifacts/package-tree.html), 
  * [com.google.adk.events](com/google/adk/events/package-tree.html), 
  * [com.google.adk.examples](com/google/adk/examples/package-tree.html), 
  * [com.google.adk.exceptions](com/google/adk/exceptions/package-tree.html), 
  * [com.google.adk.flows](com/google/adk/flows/package-tree.html), 
  * [com.google.adk.flows.llmflows](com/google/adk/flows/llmflows/package-tree.html), 
  * [com.google.adk.flows.llmflows.audio](com/google/adk/flows/llmflows/audio/package-tree.html), 
  * [com.google.adk.memory](com/google/adk/memory/package-tree.html), 
  * [com.google.adk.models](com/google/adk/models/package-tree.html), 
  * [com.google.adk.models.langchain4j](com/google/adk/models/langchain4j/package-tree.html), 
  * [com.google.adk.network](com/google/adk/network/package-tree.html), 
  * [com.google.adk.runner](com/google/adk/runner/package-tree.html), 
  * [com.google.adk.sessions](com/google/adk/sessions/package-tree.html), 
  * [com.google.adk.tools](com/google/adk/tools/package-tree.html), 
  * [com.google.adk.tools.applicationintegrationtoolset](com/google/adk/tools/applicationintegrationtoolset/package-tree.html), 
  * [com.google.adk.tools.mcp](com/google/adk/tools/mcp/package-tree.html), 
  * [com.google.adk.tools.retrieval](com/google/adk/tools/retrieval/package-tree.html), 
  * [com.google.adk.utils](com/google/adk/utils/package-tree.html), 
  * [com.google.adk.web](com/google/adk/web/package-tree.html), 
  * [com.google.adk.web.config](com/google/adk/web/config/package-tree.html)



## Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * org.springframework.web.socket.handler.AbstractWebSocketHandler (implements org.springframework.web.socket.WebSocketHandler) 
      * org.springframework.web.socket.handler.TextWebSocketHandler 
        * com.google.adk.web.[AdkWebServer.LiveWebSocketHandler](com/google/adk/web/AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web")
    * com.google.adk.web.config.[AdkWebCorsConfig](com/google/adk/web/config/AdkWebCorsConfig.html "class in com.google.adk.web.config")
    * com.google.adk.web.[AdkWebServer](com/google/adk/web/AdkWebServer.html "class in com.google.adk.web") (implements org.springframework.web.servlet.config.annotation.WebMvcConfigurer)
    * com.google.adk.web.[AdkWebServer.AddSessionToEvalSetRequest](com/google/adk/web/AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.AgentController](com/google/adk/web/AdkWebServer.AgentController.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.AgentRunRequest](com/google/adk/web/AdkWebServer.AgentRunRequest.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.ApiServerSpanExporter](com/google/adk/web/AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") (implements io.opentelemetry.sdk.trace.export.SpanExporter)
    * com.google.adk.web.[AdkWebServer.GraphResponse](com/google/adk/web/AdkWebServer.GraphResponse.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.OpenTelemetryConfig](com/google/adk/web/AdkWebServer.OpenTelemetryConfig.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.RunEvalRequest](com/google/adk/web/AdkWebServer.RunEvalRequest.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.RunnerService](com/google/adk/web/AdkWebServer.RunnerService.html "class in com.google.adk.web")
    * com.google.adk.web.[AdkWebServer.WebSocketConfig](com/google/adk/web/AdkWebServer.WebSocketConfig.html "class in com.google.adk.web") (implements org.springframework.web.socket.config.annotation.WebSocketConfigurer)
    * com.google.adk.web.[AgentCompilerLoader](com/google/adk/web/AgentCompilerLoader.html "class in com.google.adk.web")
    * com.google.adk.web.[AgentGraphGenerator](com/google/adk/web/AgentGraphGenerator.html "class in com.google.adk.web")
    * com.google.adk.web.config.[AgentLoadingProperties](com/google/adk/web/config/AgentLoadingProperties.html "class in com.google.adk.web.config")
    * com.google.adk.flows.llmflows.[AgentTransfer](com/google/adk/flows/llmflows/AgentTransfer.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.tools.[Annotations](com/google/adk/tools/Annotations.html "class in com.google.adk.tools")
    * com.google.adk.network.[ApiResponse](com/google/adk/network/ApiResponse.html "class in com.google.adk.network") (implements java.lang.[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")) 
      * com.google.adk.network.[HttpApiResponse](com/google/adk/network/HttpApiResponse.html "class in com.google.adk.network")
    * com.google.adk.sessions.[ApiResponse](com/google/adk/sessions/ApiResponse.html "class in com.google.adk.sessions") (implements java.lang.[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")) 
      * com.google.adk.sessions.[HttpApiResponse](com/google/adk/sessions/HttpApiResponse.html "class in com.google.adk.sessions")
    * com.google.adk.tools.applicationintegrationtoolset.[ApplicationIntegrationToolset](com/google/adk/tools/applicationintegrationtoolset/ApplicationIntegrationToolset.html "class in com.google.adk.tools.applicationintegrationtoolset") (implements com.google.adk.tools.[BaseToolset](com/google/adk/tools/BaseToolset.html "interface in com.google.adk.tools"))
    * com.google.adk.agents.[BaseAgent](com/google/adk/agents/BaseAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LlmAgent](com/google/adk/agents/LlmAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LoopAgent](com/google/adk/agents/LoopAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[ParallelAgent](com/google/adk/agents/ParallelAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[SequentialAgent](com/google/adk/agents/SequentialAgent.html "class in com.google.adk.agents")
    * com.google.adk.agents.[BaseAgentConfig](com/google/adk/agents/BaseAgentConfig.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LlmAgentConfig](com/google/adk/agents/LlmAgentConfig.html "class in com.google.adk.agents")
    * com.google.adk.models.[BaseLlm](com/google/adk/models/BaseLlm.html "class in com.google.adk.models")
      * com.google.adk.models.[Claude](com/google/adk/models/Claude.html "class in com.google.adk.models")
      * com.google.adk.models.[Gemini](com/google/adk/models/Gemini.html "class in com.google.adk.models")
      * com.google.adk.models.langchain4j.[LangChain4j](com/google/adk/models/langchain4j/LangChain4j.html "class in com.google.adk.models.langchain4j")
    * com.google.adk.flows.llmflows.[BaseLlmFlow](com/google/adk/flows/llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.[BaseFlow](com/google/adk/flows/BaseFlow.html "interface in com.google.adk.flows")) 
      * com.google.adk.flows.llmflows.[SingleFlow](com/google/adk/flows/llmflows/SingleFlow.html "class in com.google.adk.flows.llmflows")
        * com.google.adk.flows.llmflows.[AutoFlow](com/google/adk/flows/llmflows/AutoFlow.html "class in com.google.adk.flows.llmflows")
    * com.google.adk.tools.[BaseTool](com/google/adk/tools/BaseTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.[AgentTool](com/google/adk/tools/AgentTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.retrieval.[BaseRetrievalTool](com/google/adk/tools/retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")
        * com.google.adk.tools.retrieval.[VertexAiRagRetrieval](com/google/adk/tools/retrieval/VertexAiRagRetrieval.html "class in com.google.adk.tools.retrieval")
      * com.google.adk.tools.[BuiltInCodeExecutionTool](com/google/adk/tools/BuiltInCodeExecutionTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.[FunctionTool](com/google/adk/tools/FunctionTool.html "class in com.google.adk.tools")
        * com.google.adk.tools.[LongRunningFunctionTool](com/google/adk/tools/LongRunningFunctionTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.[GoogleSearchTool](com/google/adk/tools/GoogleSearchTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.applicationintegrationtoolset.[IntegrationConnectorTool](com/google/adk/tools/applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset")
      * com.google.adk.tools.[LoadArtifactsTool](com/google/adk/tools/LoadArtifactsTool.html "class in com.google.adk.tools")
      * com.google.adk.tools.mcp.[McpAsyncTool](com/google/adk/tools/mcp/McpAsyncTool.html "class in com.google.adk.tools.mcp")
      * com.google.adk.tools.mcp.[McpTool](com/google/adk/tools/mcp/McpTool.html "class in com.google.adk.tools.mcp")
    * com.google.adk.flows.llmflows.[Basic](com/google/adk/flows/llmflows/Basic.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.agents.[Callbacks](com/google/adk/agents/Callbacks.html "class in com.google.adk.agents")
    * com.google.adk.agents.[CallbackUtil](com/google/adk/agents/CallbackUtil.html "class in com.google.adk.agents")
    * com.google.adk.utils.[CollectionUtils](com/google/adk/utils/CollectionUtils.html "class in com.google.adk.utils")
    * com.google.adk.tools.applicationintegrationtoolset.[ConnectionsClient](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.html "class in com.google.adk.tools.applicationintegrationtoolset")
    * com.google.adk.tools.applicationintegrationtoolset.[ConnectionsClient.ActionSchema](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset")
    * com.google.adk.tools.applicationintegrationtoolset.[ConnectionsClient.ConnectionDetails](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset")
    * com.google.adk.tools.applicationintegrationtoolset.[ConnectionsClient.EntitySchemaAndOperations](com/google/adk/tools/applicationintegrationtoolset/ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset")
    * com.google.adk.flows.llmflows.[Contents](com/google/adk/flows/llmflows/Contents.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.tools.mcp.[ConversionUtils](com/google/adk/tools/mcp/ConversionUtils.html "class in com.google.adk.tools.mcp")
    * com.google.adk.tools.mcp.[DefaultMcpTransportBuilder](com/google/adk/tools/mcp/DefaultMcpTransportBuilder.html "class in com.google.adk.tools.mcp") (implements com.google.adk.tools.mcp.[McpTransportBuilder](com/google/adk/tools/mcp/McpTransportBuilder.html "interface in com.google.adk.tools.mcp"))
    * com.google.adk.events.[Event.Builder](com/google/adk/events/Event.Builder.html "class in com.google.adk.events")
    * com.google.adk.events.[EventActions](com/google/adk/events/EventActions.html "class in com.google.adk.events")
    * com.google.adk.events.[EventActions.Builder](com/google/adk/events/EventActions.Builder.html "class in com.google.adk.events")
    * com.google.adk.events.[EventStream](com/google/adk/events/EventStream.html "class in com.google.adk.events") (implements java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<T>)
    * com.google.adk.examples.[Example](com/google/adk/examples/Example.html "class in com.google.adk.examples")
    * com.google.adk.examples.[Example.Builder](com/google/adk/examples/Example.Builder.html "class in com.google.adk.examples")
    * com.google.adk.flows.llmflows.[Examples](com/google/adk/flows/llmflows/Examples.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.examples.[ExampleUtils](com/google/adk/examples/ExampleUtils.html "class in com.google.adk.examples")
    * com.google.adk.tools.[ExitLoopTool](com/google/adk/tools/ExitLoopTool.html "class in com.google.adk.tools")
    * com.google.adk.tools.[FunctionCallingUtils](com/google/adk/tools/FunctionCallingUtils.html "class in com.google.adk.tools")
    * com.google.adk.flows.llmflows.[Functions](com/google/adk/flows/llmflows/Functions.html "class in com.google.adk.flows.llmflows")
    * com.google.adk.artifacts.[GcsArtifactService](com/google/adk/artifacts/GcsArtifactService.html "class in com.google.adk.artifacts") (implements com.google.adk.artifacts.[BaseArtifactService](com/google/adk/artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts"))
    * com.google.adk.models.[Gemini.Builder](com/google/adk/models/Gemini.Builder.html "class in com.google.adk.models")
    * com.google.adk.models.[GeminiLlmConnection](com/google/adk/models/GeminiLlmConnection.html "class in com.google.adk.models") (implements com.google.adk.models.[BaseLlmConnection](com/google/adk/models/BaseLlmConnection.html "interface in com.google.adk.models"))
    * com.google.adk.sessions.[GetSessionConfig](com/google/adk/sessions/GetSessionConfig.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[GetSessionConfig.Builder](com/google/adk/sessions/GetSessionConfig.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[HttpApiClient](com/google/adk/sessions/HttpApiClient.html "class in com.google.adk.sessions")
    * com.google.adk.flows.llmflows.[Identity](com/google/adk/flows/llmflows/Identity.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.artifacts.[InMemoryArtifactService](com/google/adk/artifacts/InMemoryArtifactService.html "class in com.google.adk.artifacts") (implements com.google.adk.artifacts.[BaseArtifactService](com/google/adk/artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts"))
    * com.google.adk.memory.[InMemoryMemoryService](com/google/adk/memory/InMemoryMemoryService.html "class in com.google.adk.memory") (implements com.google.adk.memory.[BaseMemoryService](com/google/adk/memory/BaseMemoryService.html "interface in com.google.adk.memory"))
    * com.google.adk.sessions.[InMemorySessionService](com/google/adk/sessions/InMemorySessionService.html "class in com.google.adk.sessions") (implements com.google.adk.sessions.[BaseSessionService](com/google/adk/sessions/BaseSessionService.html "interface in com.google.adk.sessions"))
    * com.google.adk.flows.llmflows.[Instructions](com/google/adk/flows/llmflows/Instructions.html "class in com.google.adk.flows.llmflows") (implements com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows"))
    * com.google.adk.utils.[InstructionUtils](com/google/adk/utils/InstructionUtils.html "class in com.google.adk.utils")
    * com.google.adk.tools.applicationintegrationtoolset.[IntegrationClient](com/google/adk/tools/applicationintegrationtoolset/IntegrationClient.html "class in com.google.adk.tools.applicationintegrationtoolset")
    * com.google.adk.agents.[InvocationContext](com/google/adk/agents/InvocationContext.html "class in com.google.adk.agents")
    * com.google.adk.[JsonBaseModel](com/google/adk/JsonBaseModel.html "class in com.google.adk")
      * com.google.adk.web.[AdkWebServer.RunEvalResult](com/google/adk/web/AdkWebServer.RunEvalResult.html "class in com.google.adk.web")
      * com.google.adk.events.[Event](com/google/adk/events/Event.html "class in com.google.adk.events")
      * com.google.adk.agents.[LiveRequest](com/google/adk/agents/LiveRequest.html "class in com.google.adk.agents")
      * com.google.adk.models.[LlmRequest](com/google/adk/models/LlmRequest.html "class in com.google.adk.models")
      * com.google.adk.models.[LlmResponse](com/google/adk/models/LlmResponse.html "class in com.google.adk.models")
      * com.google.adk.sessions.[Session](com/google/adk/sessions/Session.html "class in com.google.adk.sessions")
    * com.google.adk.artifacts.[ListArtifactsResponse](com/google/adk/artifacts/ListArtifactsResponse.html "class in com.google.adk.artifacts")
    * com.google.adk.artifacts.[ListArtifactsResponse.Builder](com/google/adk/artifacts/ListArtifactsResponse.Builder.html "class in com.google.adk.artifacts")
    * com.google.adk.artifacts.[ListArtifactVersionsResponse](com/google/adk/artifacts/ListArtifactVersionsResponse.html "class in com.google.adk.artifacts")
    * com.google.adk.artifacts.[ListArtifactVersionsResponse.Builder](com/google/adk/artifacts/ListArtifactVersionsResponse.Builder.html "class in com.google.adk.artifacts")
    * com.google.adk.sessions.[ListEventsResponse](com/google/adk/sessions/ListEventsResponse.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListEventsResponse.Builder](com/google/adk/sessions/ListEventsResponse.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListSessionsResponse](com/google/adk/sessions/ListSessionsResponse.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListSessionsResponse.Builder](com/google/adk/sessions/ListSessionsResponse.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.agents.[LiveRequest.Builder](com/google/adk/agents/LiveRequest.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LiveRequestQueue](com/google/adk/agents/LiveRequestQueue.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LlmAgent.Builder](com/google/adk/agents/LlmAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.models.[LlmRegistry](com/google/adk/models/LlmRegistry.html "class in com.google.adk.models")
    * com.google.adk.models.[LlmRequest.Builder](com/google/adk/models/LlmRequest.Builder.html "class in com.google.adk.models")
    * com.google.adk.models.[LlmResponse.Builder](com/google/adk/models/LlmResponse.Builder.html "class in com.google.adk.models")
    * com.google.adk.agents.[LoopAgent.Builder](com/google/adk/agents/LoopAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.tools.mcp.[McpSessionManager](com/google/adk/tools/mcp/McpSessionManager.html "class in com.google.adk.tools.mcp")
    * com.google.adk.tools.mcp.[McpToolset](com/google/adk/tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp") (implements com.google.adk.tools.[BaseToolset](com/google/adk/tools/BaseToolset.html "interface in com.google.adk.tools"))
    * com.google.adk.memory.[MemoryEntry](com/google/adk/memory/MemoryEntry.html "class in com.google.adk.memory")
    * com.google.adk.memory.[MemoryEntry.Builder](com/google/adk/memory/MemoryEntry.Builder.html "class in com.google.adk.memory")
    * com.google.adk.models.[Model](com/google/adk/models/Model.html "class in com.google.adk.models")
    * com.google.adk.models.[Model.Builder](com/google/adk/models/Model.Builder.html "class in com.google.adk.models")
    * com.google.adk.utils.[Pairs](com/google/adk/utils/Pairs.html "class in com.google.adk.utils")
    * com.google.adk.agents.[ParallelAgent.Builder](com/google/adk/agents/ParallelAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[ReadonlyContext](com/google/adk/agents/ReadonlyContext.html "class in com.google.adk.agents")
      * com.google.adk.agents.[CallbackContext](com/google/adk/agents/CallbackContext.html "class in com.google.adk.agents")
        * com.google.adk.tools.[ToolContext](com/google/adk/tools/ToolContext.html "class in com.google.adk.tools")
    * com.google.adk.flows.llmflows.[RequestProcessor.RequestProcessingResult](com/google/adk/flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")
    * com.google.adk.flows.llmflows.[ResponseProcessor.ResponseProcessingResult](com/google/adk/flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")
    * com.google.adk.agents.[RunConfig](com/google/adk/agents/RunConfig.html "class in com.google.adk.agents")
    * com.google.adk.agents.[RunConfig.Builder](com/google/adk/agents/RunConfig.Builder.html "class in com.google.adk.agents")
    * com.google.adk.runner.[Runner](com/google/adk/runner/Runner.html "class in com.google.adk.runner")
      * com.google.adk.runner.[InMemoryRunner](com/google/adk/runner/InMemoryRunner.html "class in com.google.adk.runner")
    * com.google.adk.[SchemaUtils](com/google/adk/SchemaUtils.html "class in com.google.adk")
    * com.google.adk.memory.[SearchMemoryResponse](com/google/adk/memory/SearchMemoryResponse.html "class in com.google.adk.memory")
    * com.google.adk.memory.[SearchMemoryResponse.Builder](com/google/adk/memory/SearchMemoryResponse.Builder.html "class in com.google.adk.memory")
    * com.google.adk.agents.[SequentialAgent.Builder](com/google/adk/agents/SequentialAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.sessions.[Session.Builder](com/google/adk/sessions/Session.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[SessionUtils](com/google/adk/sessions/SessionUtils.html "class in com.google.adk.sessions")
    * com.google.adk.tools.mcp.[SseServerParameters](com/google/adk/tools/mcp/SseServerParameters.html "class in com.google.adk.tools.mcp")
    * com.google.adk.tools.mcp.[SseServerParameters.Builder](com/google/adk/tools/mcp/SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")
    * com.google.adk.sessions.[State](com/google/adk/sessions/State.html "class in com.google.adk.sessions") (implements java.util.concurrent.[ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<K,V>)
    * com.google.adk.[Telemetry](com/google/adk/Telemetry.html "class in com.google.adk")
    * java.lang.[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") (implements java.io.[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")) 
      * java.lang.[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")
        * com.google.adk.exceptions.[LlmCallsLimitExceededException](com/google/adk/exceptions/LlmCallsLimitExceededException.html "class in com.google.adk.exceptions")
        * java.lang.[RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang")
          * com.google.adk.tools.mcp.[McpToolset.McpToolsetException](com/google/adk/tools/mcp/McpToolset.McpToolsetException.html "class in com.google.adk.tools.mcp")
            * com.google.adk.tools.mcp.[McpToolset.McpInitializationException](com/google/adk/tools/mcp/McpToolset.McpInitializationException.html "class in com.google.adk.tools.mcp")
            * com.google.adk.tools.mcp.[McpToolset.McpToolLoadingException](com/google/adk/tools/mcp/McpToolset.McpToolLoadingException.html "class in com.google.adk.tools.mcp")
          * com.google.adk.sessions.[SessionException](com/google/adk/sessions/SessionException.html "class in com.google.adk.sessions")
            * com.google.adk.sessions.[SessionNotFoundException](com/google/adk/sessions/SessionNotFoundException.html "class in com.google.adk.sessions")
    * com.google.adk.tools.[ToolContext.Builder](com/google/adk/tools/ToolContext.Builder.html "class in com.google.adk.tools")
    * com.google.adk.[Version](com/google/adk/Version.html "class in com.google.adk")
    * com.google.adk.sessions.[VertexAiSessionService](com/google/adk/sessions/VertexAiSessionService.html "class in com.google.adk.sessions") (implements com.google.adk.sessions.[BaseSessionService](com/google/adk/sessions/BaseSessionService.html "interface in com.google.adk.sessions"))
    * com.google.adk.models.[VertexCredentials](com/google/adk/models/VertexCredentials.html "class in com.google.adk.models")
    * com.google.adk.models.[VertexCredentials.Builder](com/google/adk/models/VertexCredentials.Builder.html "class in com.google.adk.models")
    * com.google.adk.flows.llmflows.audio.[VertexSpeechClient](com/google/adk/flows/llmflows/audio/VertexSpeechClient.html "class in com.google.adk.flows.llmflows.audio") (implements com.google.adk.flows.llmflows.audio.[SpeechClientInterface](com/google/adk/flows/llmflows/audio/SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio"))



## Interface Hierarchy

  * java.lang.[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")
    * com.google.adk.tools.[BaseToolset](com/google/adk/tools/BaseToolset.html "interface in com.google.adk.tools")
    * com.google.adk.flows.llmflows.audio.[SpeechClientInterface](com/google/adk/flows/llmflows/audio/SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")
  * com.google.adk.artifacts.[BaseArtifactService](com/google/adk/artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")
  * com.google.adk.examples.[BaseExampleProvider](com/google/adk/examples/BaseExampleProvider.html "interface in com.google.adk.examples")
  * com.google.adk.flows.[BaseFlow](com/google/adk/flows/BaseFlow.html "interface in com.google.adk.flows")
  * com.google.adk.models.[BaseLlmConnection](com/google/adk/models/BaseLlmConnection.html "interface in com.google.adk.models")
  * com.google.adk.memory.[BaseMemoryService](com/google/adk/memory/BaseMemoryService.html "interface in com.google.adk.memory")
  * com.google.adk.sessions.[BaseSessionService](com/google/adk/sessions/BaseSessionService.html "interface in com.google.adk.sessions")
  * com.google.adk.agents.Callbacks.AfterAgentCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterAgentCallback](com/google/adk/agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterAgentCallbackSync](com/google/adk/agents/Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.AfterModelCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterModelCallback](com/google/adk/agents/Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterModelCallbackSync](com/google/adk/agents/Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.AfterToolCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterToolCallback](com/google/adk/agents/Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterToolCallbackSync](com/google/adk/agents/Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeAgentCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeAgentCallback](com/google/adk/agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeAgentCallbackSync](com/google/adk/agents/Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeModelCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeModelCallback](com/google/adk/agents/Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeModelCallbackSync](com/google/adk/agents/Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeToolCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeToolCallback](com/google/adk/agents/Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeToolCallbackSync](com/google/adk/agents/Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.[Instruction](com/google/adk/agents/Instruction.html "interface in com.google.adk.agents")
  * com.google.adk.models.[LlmRegistry.LlmFactory](com/google/adk/models/LlmRegistry.LlmFactory.html "interface in com.google.adk.models")
  * com.google.adk.tools.mcp.[McpTransportBuilder](com/google/adk/tools/mcp/McpTransportBuilder.html "interface in com.google.adk.tools.mcp")
  * com.google.adk.flows.llmflows.[RequestProcessor](com/google/adk/flows/llmflows/RequestProcessor.html "interface in com.google.adk.flows.llmflows")
  * com.google.adk.flows.llmflows.[ResponseProcessor](com/google/adk/flows/llmflows/ResponseProcessor.html "interface in com.google.adk.flows.llmflows")
  * com.google.adk.tools.[ToolPredicate](com/google/adk/tools/ToolPredicate.html "interface in com.google.adk.tools")



## Annotation Interface Hierarchy

  * com.google.adk.tools.[Annotations.Schema](com/google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools") (implements java.lang.annotation.[Annotation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/annotation/Annotation.html "class or interface in java.lang.annotation"))



## Enum Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<E> (implements java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang")<T>, java.lang.constant.[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "class or interface in java.lang.constant"), java.io.[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")) 
      * com.google.adk.agents.[LlmAgent.IncludeContents](com/google/adk/agents/LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")
      * com.google.adk.agents.[RunConfig.StreamingMode](com/google/adk/agents/RunConfig.StreamingMode.html "enum class in com.google.adk.agents")



## Record Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * java.lang.[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")
      * com.google.adk.web.config.[AdkWebCorsProperties](com/google/adk/web/config/AdkWebCorsProperties.html "class in com.google.adk.web.config")
      * com.google.adk.agents.[Instruction.Provider](com/google/adk/agents/Instruction.Provider.html "class in com.google.adk.agents") (implements com.google.adk.agents.[Instruction](com/google/adk/agents/Instruction.html "interface in com.google.adk.agents"))
      * com.google.adk.agents.[Instruction.Static](com/google/adk/agents/Instruction.Static.html "class in com.google.adk.agents") (implements com.google.adk.agents.[Instruction](com/google/adk/agents/Instruction.html "interface in com.google.adk.agents"))



* * *

Copyright (C) 2025\. All rights reserved.
