[ADK for TypeScript: API Reference](index.html)

SystemLightDark

Search…




Preparing search index...

# ADK for TypeScript: API Reference - v1.5.0

## Hierarchy Summary

  * [BaseAgent](classes/BaseAgent.html)
    * [RemoteA2AAgent](classes/RemoteA2AAgent.html)
    * [Agent](classes/Agent.html)
    * [LoopAgent](classes/LoopAgent.html)
    * [ParallelAgent](classes/ParallelAgent.html)
    * [RoutedAgent](classes/RoutedAgent.html)
    * [SequentialAgent](classes/SequentialAgent.html)


  * [BaseAgentConfig](interfaces/BaseAgentConfig.html)
    * [RemoteA2AAgentConfig](interfaces/RemoteA2AAgentConfig.html)
    * [LlmAgentConfig](interfaces/LlmAgentConfig.html)
    * [LoopAgentConfig](interfaces/LoopAgentConfig.html)
    * [RoutedAgentConfig](interfaces/RoutedAgentConfig.html)


  * [BaseArtifactService](interfaces/BaseArtifactService.html)
    * [FileArtifactService](classes/FileArtifactService.html)
    * [GcsArtifactService](classes/GcsArtifactService.html)
    * [InMemoryArtifactService](classes/InMemoryArtifactService.html)


  * [BaseCodeExecutor](classes/BaseCodeExecutor.html)
    * [AgentEngineSandboxCodeExecutor](classes/AgentEngineSandboxCodeExecutor.html)
    * [UnsafeLocalCodeExecutor](classes/UnsafeLocalCodeExecutor.html)
    * [BuiltInCodeExecutor](classes/BuiltInCodeExecutor.html)


  * [BaseContextCompactor](interfaces/BaseContextCompactor.html)
    * [AgentControlledContextCompactor](classes/AgentControlledContextCompactor.html)
    * [AnchoredContextCompactor](classes/AnchoredContextCompactor.html)
    * [TokenBasedContextCompactor](classes/TokenBasedContextCompactor.html)
    * [TrajectoryThoughtPruningCompactor](classes/TrajectoryThoughtPruningCompactor.html)
    * [TruncatingContextCompactor](classes/TruncatingContextCompactor.html)


  * [BaseCredentialExchanger](interfaces/BaseCredentialExchanger.html)
    * [OAuth2CredentialExchanger](classes/OAuth2CredentialExchanger.html)


  * [BaseCredentialService](interfaces/BaseCredentialService.html)
    * [InMemoryCredentialService](classes/InMemoryCredentialService.html)
    * [SessionStateCredentialService](classes/SessionStateCredentialService.html)


  * [BaseLlm](classes/BaseLlm.html)
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


  * [BasePlugin](classes/BasePlugin.html)
    * [GlobalInstructionPlugin](classes/GlobalInstructionPlugin.html)
    * [LoggingPlugin](classes/LoggingPlugin.html)
    * [SecurityPlugin](classes/SecurityPlugin.html)


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
    * [RunSkillInlineScriptTool](classes/RunSkillInlineScriptTool.html)
    * [RunSkillScriptTool](classes/RunSkillScriptTool.html)
    * [AgentTool](classes/AgentTool.html)
    * [ConsolidateContextTool](classes/ConsolidateContextTool.html)
    * [EnterpriseWebSearchTool](classes/EnterpriseWebSearchTool.html)
    * [ExampleTool](classes/ExampleTool.html)
    * [ExitLoopTool](classes/ExitLoopTool.html)
    * [FunctionTool](classes/FunctionTool.html)
      * [LongRunningFunctionTool](classes/LongRunningFunctionTool.html)
    * [GoogleMapsGroundingTool](classes/GoogleMapsGroundingTool.html)
    * [GoogleSearchTool](classes/GoogleSearchTool.html)
    * [LoadArtifactsTool](classes/LoadArtifactsTool.html)
    * [LoadMemoryTool](classes/LoadMemoryTool.html)
    * [PreloadMemoryTool](classes/PreloadMemoryTool.html)
    * [UrlContextTool](classes/UrlContextTool.html)
    * [VertexAiSearchTool](classes/VertexAiSearchTool.html)
    * [VertexRagRetrievalTool](classes/VertexRagRetrievalTool.html)
    * [ListSkillsTool](classes/ListSkillsTool.html)
    * [LoadSkillResourceTool](classes/LoadSkillResourceTool.html)
    * [LoadSkillTool](classes/LoadSkillTool.html)
    * [SearchSkillsTool](classes/SearchSkillsTool.html)
    * [RestApiTool](classes/RestApiTool.html)


  * [BaseToolset](classes/BaseToolset.html)
    * [AgentRegistrySingleMCPToolset](classes/AgentRegistrySingleMCPToolset.html)
    * [MCPToolset](classes/MCPToolset.html)
    * [SkillToolset](classes/SkillToolset.html)
    * [OpenAPIToolset](classes/OpenAPIToolset.html)


  * [CompositeSessionKey](interfaces/CompositeSessionKey.html)
    * [DeleteArtifactRequest](interfaces/DeleteArtifactRequest.html)
    * [ListVersionsRequest](interfaces/ListVersionsRequest.html)
    * [LoadArtifactRequest](interfaces/LoadArtifactRequest.html)
    * [SaveArtifactRequest](interfaces/SaveArtifactRequest.html)
    * [GetSessionRequest](interfaces/GetSessionRequest.html)


  * [GeminiParams](interfaces/GeminiParams.html)
    * [ApigeeLlmParams](interfaces/ApigeeLlmParams.html)


  * [LlmResponse](interfaces/LlmResponse.html)
    * [Event](interfaces/Event.html)
      * [CompactedEvent](interfaces/CompactedEvent.html)


  * [ReadonlyContext](classes/ReadonlyContext.html)
    * [Context](classes/Context.html)


  * [Runner](classes/Runner.html)
    * [InMemoryRunner](classes/InMemoryRunner.html)


  * [SkillRegistry](interfaces/SkillRegistry.html)
    * [GCPSkillRegistry](classes/GCPSkillRegistry.html)



[ADK for TypeScript: API Reference - v1.5.0](index.html)

  * Loading...


