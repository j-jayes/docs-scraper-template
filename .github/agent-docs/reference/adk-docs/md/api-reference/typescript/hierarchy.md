[ADK for TypeScript: API Reference](index.html)

SystemLightDark

Search…




Preparing search index...

# ADK for TypeScript: API Reference - v2.2.1

## Hierarchy Summary

  * [BaseArtifactService](interfaces/BaseArtifactService.html)
    * [FileArtifactService](classes/FileArtifactService.html)
    * [GcsArtifactService](classes/GcsArtifactService.html)
    * [InMemoryArtifactService](classes/InMemoryArtifactService.html)


  * [BaseCodeExecutor](classes/BaseCodeExecutor.html)
    * [AgentEngineSandboxCodeExecutor](classes/AgentEngineSandboxCodeExecutor.html)
    * [ContainerCodeExecutor](classes/ContainerCodeExecutor.html)
    * [UnsafeLocalCodeExecutor](classes/UnsafeLocalCodeExecutor.html)
    * [BuiltInCodeExecutor](classes/BuiltInCodeExecutor.html)


  * [BaseContextCompactor](interfaces/BaseContextCompactor.html)
    * [AgentControlledContextCompactor](classes/AgentControlledContextCompactor.html)
    * [AnchoredContextCompactor](classes/AnchoredContextCompactor.html)
    * [TokenBasedContextCompactor](classes/TokenBasedContextCompactor.html)
    * [TrajectoryThoughtPruningCompactor](classes/TrajectoryThoughtPruningCompactor.html)
    * [TruncatingContextCompactor](classes/TruncatingContextCompactor.html)


  * [BaseCredentialExchanger](interfaces/BaseCredentialExchanger.html)
    * [AutoAuthCredentialExchanger](classes/AutoAuthCredentialExchanger.html)
    * [OAuth2BearerExchanger](classes/OAuth2BearerExchanger.html)
    * [OAuth2CredentialExchanger](classes/OAuth2CredentialExchanger.html)
    * [ServiceAccountCredentialExchanger](classes/ServiceAccountCredentialExchanger.html)


  * [BaseCredentialService](interfaces/BaseCredentialService.html)
    * [InMemoryCredentialService](classes/InMemoryCredentialService.html)
    * [SessionStateCredentialService](classes/SessionStateCredentialService.html)


  * [BaseEnvironment](classes/BaseEnvironment.html)
    * [LocalEnvironment](classes/LocalEnvironment.html)


  * [BaseExampleProvider](classes/BaseExampleProvider.html)
    * [VertexAiExampleStore](classes/VertexAiExampleStore.html)


  * [BaseLlm](classes/BaseLlm.html)
    * [ChromeBuiltInLlm](classes/ChromeBuiltInLlm.html)
    * [Gemini](classes/Gemini.html)
      * [ApigeeLlm](classes/ApigeeLlm.html)
    * [RoutedLlm](classes/RoutedLlm.html)


  * [BaseLlmRequestProcessor](classes/BaseLlmRequestProcessor.html)
    * [ContentRequestProcessor](classes/ContentRequestProcessor.html)
    * [ContextCompactorRequestProcessor](classes/ContextCompactorRequestProcessor.html)
    * [InteractionsRequestProcessor](classes/InteractionsRequestProcessor.html)
    * [AgentTransferLlmRequestProcessor](classes/AgentTransferLlmRequestProcessor.html)
    * [AuthPreprocessor](classes/AuthPreprocessor.html)


  * [BaseMemoryService](interfaces/BaseMemoryService.html)
    * [InMemoryMemoryService](classes/InMemoryMemoryService.html)
    * [VertexAiMemoryBankService](classes/VertexAiMemoryBankService.html)
    * [VertexAiRagMemoryService](classes/VertexAiRagMemoryService.html)


  * [BaseNode](classes/BaseNode.html)
    * [BaseAgent](classes/BaseAgent.html)
      * [RemoteA2AAgent](classes/RemoteA2AAgent.html)
      * [Agent](classes/Agent.html)
      * [LoopAgent](classes/LoopAgent.html)
      * [ParallelAgent](classes/ParallelAgent.html)
      * [RoutedAgent](classes/RoutedAgent.html)
      * [SequentialAgent](classes/SequentialAgent.html)
    * [FunctionNode](classes/FunctionNode.html)
    * [JoinNode](classes/JoinNode.html)
    * [ParallelWorker](classes/ParallelWorker.html)
    * [ToolNode](classes/ToolNode.html)
    * [Workflow](classes/Workflow.html)
    * [WorkflowNode](classes/WorkflowNode.html)


  * [BaseNodeConfig](interfaces/BaseNodeConfig.html)
    * [BaseAgentConfig](interfaces/BaseAgentConfig.html)
      * [RemoteA2AAgentConfig](interfaces/RemoteA2AAgentConfig.html)
      * [LlmAgentConfig](interfaces/LlmAgentConfig.html)
      * [LoopAgentConfig](interfaces/LoopAgentConfig.html)
      * [RoutedAgentConfig](interfaces/RoutedAgentConfig.html)


  * [BasePlanner](classes/BasePlanner.html)
    * [BuiltInPlanner](classes/BuiltInPlanner.html)
    * [PlanReActPlanner](classes/PlanReActPlanner.html)


  * [BasePlugin](classes/BasePlugin.html)
    * [GlobalInstructionPlugin](classes/GlobalInstructionPlugin.html)
    * [LoggingPlugin](classes/LoggingPlugin.html)
    * [ReflectAndRetryModelPlugin](classes/ReflectAndRetryModelPlugin.html)
    * [ReflectAndRetryToolPlugin](classes/ReflectAndRetryToolPlugin.html)
    * [SecurityPlugin](classes/SecurityPlugin.html)
    * [ToolCallIntegrityPlugin](classes/ToolCallIntegrityPlugin.html)


  * [BasePolicyEngine](interfaces/BasePolicyEngine.html)
    * [InMemoryPolicyEngine](classes/InMemoryPolicyEngine.html)


  * [BaseSessionService](classes/BaseSessionService.html)
    * [DatabaseSessionService](classes/DatabaseSessionService.html)
    * [VertexAiSessionService](classes/VertexAiSessionService.html)
    * [InMemorySessionService](classes/InMemorySessionService.html)


  * [BaseSummarizer](interfaces/BaseSummarizer.html)
    * [LlmSummarizer](classes/LlmSummarizer.html)


  * [BaseTool](classes/BaseTool.html)
    * [LoadMcpResourceTool](classes/LoadMcpResourceTool.html)
    * [MCPTool](classes/MCPTool.html)
    * [RestApiTool](classes/RestApiTool.html)
    * [LoadSkillResourceTool](classes/LoadSkillResourceTool.html)
    * [RunSkillInlineScriptTool](classes/RunSkillInlineScriptTool.html)
    * [RunSkillScriptTool](classes/RunSkillScriptTool.html)
    * [AgentTool](classes/AgentTool.html)
    * [BuiltInTool](classes/BuiltInTool.html)
      * [EnterpriseWebSearchTool](classes/EnterpriseWebSearchTool.html)
      * [GoogleMapsGroundingTool](classes/GoogleMapsGroundingTool.html)
      * [GoogleSearchTool](classes/GoogleSearchTool.html)
      * [UrlContextTool](classes/UrlContextTool.html)
      * [VertexAiSearchTool](classes/VertexAiSearchTool.html)
      * [VertexRagRetrievalTool](classes/VertexRagRetrievalTool.html)
    * [ConsolidateContextTool](classes/ConsolidateContextTool.html)
    * [ExampleTool](classes/ExampleTool.html)
    * [ExitLoopTool](classes/ExitLoopTool.html)
    * [FinishTaskTool](classes/FinishTaskTool.html)
    * [FunctionTool](classes/FunctionTool.html)
      * [LongRunningFunctionTool](classes/LongRunningFunctionTool.html)
    * [LoadArtifactsTool](classes/LoadArtifactsTool.html)
    * [LoadMemoryTool](classes/LoadMemoryTool.html)
    * [PreloadMemoryTool](classes/PreloadMemoryTool.html)
    * [BaseRetrievalTool](classes/BaseRetrievalTool.html)
      * [LlamaIndexRetrieval](classes/LlamaIndexRetrieval.html)
        * [FilesRetrieval](classes/FilesRetrieval.html)
    * [WebMCPTool](classes/WebMCPTool.html)
    * [ListSkillsTool](classes/ListSkillsTool.html)
    * [LoadSkillTool](classes/LoadSkillTool.html)
    * [SearchSkillsTool](classes/SearchSkillsTool.html)
    * [NodeTool](classes/NodeTool.html)


  * [BaseToolset](classes/BaseToolset.html)
    * [AgentRegistrySingleMCPToolset](classes/AgentRegistrySingleMCPToolset.html)
    * [MCPToolset](classes/MCPToolset.html)
    * [OpenAPIToolset](classes/OpenAPIToolset.html)
    * [SkillToolset](classes/SkillToolset.html)
    * [WebMCPToolset](classes/WebMCPToolset.html)


  * [ChromeCreateCoreOptions](interfaces/ChromeCreateCoreOptions.html)
    * [ChromeCreateOptions](interfaces/ChromeCreateOptions.html)


  * [CompositeSessionKey](interfaces/CompositeSessionKey.html)
    * [DeleteArtifactRequest](interfaces/DeleteArtifactRequest.html)
    * [ListVersionsRequest](interfaces/ListVersionsRequest.html)
    * [LoadArtifactRequest](interfaces/LoadArtifactRequest.html)
    * [SaveArtifactRequest](interfaces/SaveArtifactRequest.html)
    * [GetSessionRequest](interfaces/GetSessionRequest.html)


  * [CreateEventParams](interfaces/CreateEventParams.html)
    * [CreateNodeErrorEventParams](interfaces/CreateNodeErrorEventParams.html)


  * [CreateSessionRequest](interfaces/CreateSessionRequest.html)
    * [VertexAiCreateSessionRequest](interfaces/VertexAiCreateSessionRequest.html)


  * [FilesRetrievalParams](interfaces/FilesRetrievalParams.html)
    * [FilesRetrievalConstructorParams](interfaces/FilesRetrievalConstructorParams.html)


  * [GeminiParams](interfaces/GeminiParams.html)
    * [ApigeeLlmParams](interfaces/ApigeeLlmParams.html)


  * [LlmResponse](interfaces/LlmResponse.html)
    * [Event](interfaces/Event.html)
      * [CompactedEvent](interfaces/CompactedEvent.html)
      * [NodeErrorEvent](interfaces/NodeErrorEvent.html)


  * [ReadonlyContext](classes/ReadonlyContext.html)
    * [Context](classes/Context.html)


  * [Runner](classes/Runner.html)
    * [InMemoryRunner](classes/InMemoryRunner.html)


  * [SessionArtifactService](interfaces/SessionArtifactService.html)
    * [ForwardingArtifactService](classes/ForwardingArtifactService.html)
    * [ScopedArtifactService](classes/ScopedArtifactService.html)


  * [SkillRegistry](interfaces/SkillRegistry.html)
    * [GCPSkillRegistry](classes/GCPSkillRegistry.html)



[ADK for TypeScript: API Reference - v2.2.1](index.html)

  * Loading...


