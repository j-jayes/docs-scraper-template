[ADK for TypeScript: API Reference](index.html)

SystemLightDark

Search…




Preparing search index...

# ADK for TypeScript: API Reference

## Enumerations

[AuthCredentialTypes](enums/AuthCredentialTypes.html)
    
[EventType](enums/EventType.html)
    
[GoogleLLMVariant](enums/GoogleLLMVariant.html)
    
[LogLevel](enums/LogLevel.html)
    
[PolicyOutcome](enums/PolicyOutcome.html)
    
[StreamingMode](enums/StreamingMode.html)
    

## Classes

[ActiveStreamingTool](classes/ActiveStreamingTool.html)
    
[AgentTool](classes/AgentTool.html)
    
[ApigeeLlm](classes/ApigeeLlm.html)
    
[BaseAgent](classes/BaseAgent.html)
    
[BaseCodeExecutor](classes/BaseCodeExecutor.html)
    
[BaseExampleProvider](classes/BaseExampleProvider.html)
    
[BaseLlm](classes/BaseLlm.html)
    
[BaseLlmRequestProcessor](classes/BaseLlmRequestProcessor.html)
    
[BaseLlmResponseProcessor](classes/BaseLlmResponseProcessor.html)
    
[BasePlugin](classes/BasePlugin.html)
    
[BaseSessionService](classes/BaseSessionService.html)
    
[BaseTool](classes/BaseTool.html)
    
[BaseToolset](classes/BaseToolset.html)
    
[BuiltInCodeExecutor](classes/BuiltInCodeExecutor.html)
    
[Context](classes/Context.html)
    
[DatabaseSessionService](classes/DatabaseSessionService.html)
    
[ExitLoopTool](classes/ExitLoopTool.html)
    
[FileArtifactService](classes/FileArtifactService.html)
    
[FunctionTool](classes/FunctionTool.html)
    
[GcsArtifactService](classes/GcsArtifactService.html)
    
[Gemini](classes/Gemini.html)
    
[GoogleSearchTool](classes/GoogleSearchTool.html)
    
[InMemoryArtifactService](classes/InMemoryArtifactService.html)
    
[InMemoryMemoryService](classes/InMemoryMemoryService.html)
    
[InMemoryPolicyEngine](classes/InMemoryPolicyEngine.html)
    
[InMemoryRunner](classes/InMemoryRunner.html)
    
[InMemorySessionService](classes/InMemorySessionService.html)
    
[InvocationContext](classes/InvocationContext.html)
    
[LiveRequestQueue](classes/LiveRequestQueue.html)
    
[LlmAgent](classes/LlmAgent.html)
    
[LLMRegistry](classes/LLMRegistry.html)
    
[LoggingPlugin](classes/LoggingPlugin.html)
    
[LongRunningFunctionTool](classes/LongRunningFunctionTool.html)
    
[LoopAgent](classes/LoopAgent.html)
    
[MCPSessionManager](classes/MCPSessionManager.html)
    
[MCPTool](classes/MCPTool.html)
    
[MCPToolset](classes/MCPToolset.html)
    
[ParallelAgent](classes/ParallelAgent.html)
    
[PluginManager](classes/PluginManager.html)
    
[ReadonlyContext](classes/ReadonlyContext.html)
    
[Runner](classes/Runner.html)
    
[SecurityPlugin](classes/SecurityPlugin.html)
    
[SequentialAgent](classes/SequentialAgent.html)
    
[State](classes/State.html)
    
[ToolConfirmation](classes/ToolConfirmation.html)
    

## Interfaces

[ActiveStreamingToolParams](interfaces/ActiveStreamingToolParams.html)
    
[ActivityEvent](interfaces/ActivityEvent.html)
    
[AgentToolConfig](interfaces/AgentToolConfig.html)
    
[ApigeeLlmParams](interfaces/ApigeeLlmParams.html)
    
[AppendEventRequest](interfaces/AppendEventRequest.html)
    
[ArtifactVersion](interfaces/ArtifactVersion.html)
    
[AuthConfig](interfaces/AuthConfig.html)
    
[AuthCredential](interfaces/AuthCredential.html)
    
[BaseAgentConfig](interfaces/BaseAgentConfig.html)
    
[BaseArtifactService](interfaces/BaseArtifactService.html)
    
[BaseCredentialService](interfaces/BaseCredentialService.html)
    
[BaseLlmConnection](interfaces/BaseLlmConnection.html)
    
[BaseMemoryService](interfaces/BaseMemoryService.html)
    
[BasePolicyEngine](interfaces/BasePolicyEngine.html)
    
[BaseToolParams](interfaces/BaseToolParams.html)
    
[CallCodeEvent](interfaces/CallCodeEvent.html)
    
[CodeExecutionInput](interfaces/CodeExecutionInput.html)
    
[CodeExecutionResult](interfaces/CodeExecutionResult.html)
    
[CodeResultEvent](interfaces/CodeResultEvent.html)
    
[ContentEvent](interfaces/ContentEvent.html)
    
[CreateSessionRequest](interfaces/CreateSessionRequest.html)
    
[DeleteArtifactRequest](interfaces/DeleteArtifactRequest.html)
    
[DeleteSessionRequest](interfaces/DeleteSessionRequest.html)
    
[ErrorEvent](interfaces/ErrorEvent.html)
    
[Event](interfaces/Event.html)
    
[EventActions](interfaces/EventActions.html)
    
[Example](interfaces/Example.html)
    
[ExecuteCodeParams](interfaces/ExecuteCodeParams.html)
    
[File](interfaces/File.html)
    
[FinishedEvent](interfaces/FinishedEvent.html)
    
[GeminiParams](interfaces/GeminiParams.html)
    
[GetSessionConfig](interfaces/GetSessionConfig.html)
    
[GetSessionRequest](interfaces/GetSessionRequest.html)
    
[HttpAuth](interfaces/HttpAuth.html)
    
[HttpCredentials](interfaces/HttpCredentials.html)
    
[InvocationContextParams](interfaces/InvocationContextParams.html)
    
[ListArtifactKeysRequest](interfaces/ListArtifactKeysRequest.html)
    
[ListSessionsRequest](interfaces/ListSessionsRequest.html)
    
[ListSessionsResponse](interfaces/ListSessionsResponse.html)
    
[ListVersionsRequest](interfaces/ListVersionsRequest.html)
    
[LiveRequest](interfaces/LiveRequest.html)
    
[LlmAgentConfig](interfaces/LlmAgentConfig.html)
    
[LlmRequest](interfaces/LlmRequest.html)
    
[LlmResponse](interfaces/LlmResponse.html)
    
[LoadArtifactRequest](interfaces/LoadArtifactRequest.html)
    
[Logger](interfaces/Logger.html)
    
[LoopAgentConfig](interfaces/LoopAgentConfig.html)
    
[MemoryEntry](interfaces/MemoryEntry.html)
    
[OAuth2Auth](interfaces/OAuth2Auth.html)
    
[OpenIdConnectWithConfig](interfaces/OpenIdConnectWithConfig.html)
    
[OtelExportersConfig](interfaces/OtelExportersConfig.html)
    
[OTelHooks](interfaces/OTelHooks.html)
    
[PolicyCheckResult](interfaces/PolicyCheckResult.html)
    
[RunAsyncToolRequest](interfaces/RunAsyncToolRequest.html)
    
[RunConfig](interfaces/RunConfig.html)
    
[RunnerConfig](interfaces/RunnerConfig.html)
    
[SaveArtifactRequest](interfaces/SaveArtifactRequest.html)
    
[SearchMemoryRequest](interfaces/SearchMemoryRequest.html)
    
[SearchMemoryResponse](interfaces/SearchMemoryResponse.html)
    
[ServiceAccount](interfaces/ServiceAccount.html)
    
[ServiceAccountCredential](interfaces/ServiceAccountCredential.html)
    
[Session](interfaces/Session.html)
    
[StdioConnectionParams](interfaces/StdioConnectionParams.html)
    
[StreamableHTTPConnectionParams](interfaces/StreamableHTTPConnectionParams.html)
    
[ThoughtEvent](interfaces/ThoughtEvent.html)
    
[ToolCallEvent](interfaces/ToolCallEvent.html)
    
[ToolCallPolicyContext](interfaces/ToolCallPolicyContext.html)
    
[ToolConfirmationEvent](interfaces/ToolConfirmationEvent.html)
    
[ToolProcessLlmRequest](interfaces/ToolProcessLlmRequest.html)
    
[ToolResultEvent](interfaces/ToolResultEvent.html)
    
[TranscriptionEntry](interfaces/TranscriptionEntry.html)
    

## Type Aliases

[AfterAgentCallback](types/AfterAgentCallback.html)
    
[AfterModelCallback](types/AfterModelCallback.html)
    
[AfterToolCallback](types/AfterToolCallback.html)
    
[AuthScheme](types/AuthScheme.html)
    
[BaseLlmType](types/BaseLlmType.html)
    
[BeforeAgentCallback](types/BeforeAgentCallback.html)
    
[BeforeModelCallback](types/BeforeModelCallback.html)
    
[BeforeToolCallback](types/BeforeToolCallback.html)
    
[InstructionProvider](types/InstructionProvider.html)
    
[LlmAgentSchema](types/LlmAgentSchema.html)
    
[MCPConnectionParams](types/MCPConnectionParams.html)
    
[SingleAfterModelCallback](types/SingleAfterModelCallback.html)
    
[SingleAfterToolCallback](types/SingleAfterToolCallback.html)
    
[SingleAgentCallback](types/SingleAgentCallback.html)
    
[SingleBeforeModelCallback](types/SingleBeforeModelCallback.html)
    
[SingleBeforeToolCallback](types/SingleBeforeToolCallback.html)
    
[StructuredEvent](types/StructuredEvent.html)
    
[ToolExecuteArgument](types/ToolExecuteArgument.html)
    
[ToolExecuteFunction](types/ToolExecuteFunction.html)
    
[ToolInputParameters](types/ToolInputParameters.html)
    
[ToolOptions](types/ToolOptions.html)
    
[ToolPredicate](types/ToolPredicate.html)
    
[ToolUnion](types/ToolUnion.html)
    

## Variables

[EXIT_LOOP](variables/EXIT_LOOP.html)
    
[functionsExportedForTestingOnly](variables/functionsExportedForTestingOnly.html)
    
[GOOGLE_SEARCH](variables/GOOGLE_SEARCH.html)
    
[REQUEST_CONFIRMATION_FUNCTION_CALL_NAME](variables/REQUEST_CONFIRMATION_FUNCTION_CALL_NAME.html)
    
[version](variables/version.html)
    

## Functions

[createEvent](functions/createEvent.html)
    
[createEventActions](functions/createEventActions.html)
    
[createSession](functions/createSession.html)
    
[geminiInitParams](functions/geminiInitParams.html)
    
[getArtifactServiceFromUri](functions/getArtifactServiceFromUri.html)
    
[getAskUserConfirmationFunctionCalls](functions/getAskUserConfirmationFunctionCalls.html)
    
[getFunctionCalls](functions/getFunctionCalls.html)
    
[getFunctionResponses](functions/getFunctionResponses.html)
    
[getGcpExporters](functions/getGcpExporters.html)
    
[getGcpResource](functions/getGcpResource.html)
    
[getLogger](functions/getLogger.html)
    
[getSessionServiceFromUri](functions/getSessionServiceFromUri.html)
    
[hasTrailingCodeExecutionResult](functions/hasTrailingCodeExecutionResult.html)
    
[isAgentTool](functions/isAgentTool.html)
    
[isBaseAgent](functions/isBaseAgent.html)
    
[isBaseExampleProvider](functions/isBaseExampleProvider.html)
    
[isBaseLlm](functions/isBaseLlm.html)
    
[isBaseTool](functions/isBaseTool.html)
    
[isBaseToolset](functions/isBaseToolset.html)
    
[isFinalResponse](functions/isFinalResponse.html)
    
[isFunctionTool](functions/isFunctionTool.html)
    
[isGemini2OrAbove](functions/isGemini2OrAbove.html)
    
[isLlmAgent](functions/isLlmAgent.html)
    
[isLoopAgent](functions/isLoopAgent.html)
    
[isParallelAgent](functions/isParallelAgent.html)
    
[isSequentialAgent](functions/isSequentialAgent.html)
    
[maybeSetOtelProviders](functions/maybeSetOtelProviders.html)
    
[mergeStates](functions/mergeStates.html)
    
[setLogger](functions/setLogger.html)
    
[setLogLevel](functions/setLogLevel.html)
    
[stringifyContent](functions/stringifyContent.html)
    
[toStructuredEvents](functions/toStructuredEvents.html)
    
[trimTempDeltaState](functions/trimTempDeltaState.html)
    
[zodObjectToSchema](functions/zodObjectToSchema.html)
    

Enumerations

AuthCredentialTypesEventTypeGoogleLLMVariantLogLevelPolicyOutcomeStreamingMode

Classes

ActiveStreamingToolAgentToolApigeeLlmBaseAgentBaseCodeExecutorBaseExampleProviderBaseLlmBaseLlmRequestProcessorBaseLlmResponseProcessorBasePluginBaseSessionServiceBaseToolBaseToolsetBuiltInCodeExecutorContextDatabaseSessionServiceExitLoopToolFileArtifactServiceFunctionToolGcsArtifactServiceGeminiGoogleSearchToolInMemoryArtifactServiceInMemoryMemoryServiceInMemoryPolicyEngineInMemoryRunnerInMemorySessionServiceInvocationContextLiveRequestQueueLlmAgentLLMRegistryLoggingPluginLongRunningFunctionToolLoopAgentMCPSessionManagerMCPToolMCPToolsetParallelAgentPluginManagerReadonlyContextRunnerSecurityPluginSequentialAgentStateToolConfirmation

Interfaces

ActiveStreamingToolParamsActivityEventAgentToolConfigApigeeLlmParamsAppendEventRequestArtifactVersionAuthConfigAuthCredentialBaseAgentConfigBaseArtifactServiceBaseCredentialServiceBaseLlmConnectionBaseMemoryServiceBasePolicyEngineBaseToolParamsCallCodeEventCodeExecutionInputCodeExecutionResultCodeResultEventContentEventCreateSessionRequestDeleteArtifactRequestDeleteSessionRequestErrorEventEventEventActionsExampleExecuteCodeParamsFileFinishedEventGeminiParamsGetSessionConfigGetSessionRequestHttpAuthHttpCredentialsInvocationContextParamsListArtifactKeysRequestListSessionsRequestListSessionsResponseListVersionsRequestLiveRequestLlmAgentConfigLlmRequestLlmResponseLoadArtifactRequestLoggerLoopAgentConfigMemoryEntryOAuth2AuthOpenIdConnectWithConfigOtelExportersConfigOTelHooksPolicyCheckResultRunAsyncToolRequestRunConfigRunnerConfigSaveArtifactRequestSearchMemoryRequestSearchMemoryResponseServiceAccountServiceAccountCredentialSessionStdioConnectionParamsStreamableHTTPConnectionParamsThoughtEventToolCallEventToolCallPolicyContextToolConfirmationEventToolProcessLlmRequestToolResultEventTranscriptionEntry

Type Aliases

AfterAgentCallbackAfterModelCallbackAfterToolCallbackAuthSchemeBaseLlmTypeBeforeAgentCallbackBeforeModelCallbackBeforeToolCallbackInstructionProviderLlmAgentSchemaMCPConnectionParamsSingleAfterModelCallbackSingleAfterToolCallbackSingleAgentCallbackSingleBeforeModelCallbackSingleBeforeToolCallbackStructuredEventToolExecuteArgumentToolExecuteFunctionToolInputParametersToolOptionsToolPredicateToolUnion

Variables

EXIT_LOOPfunctionsExportedForTestingOnlyGOOGLE_SEARCHREQUEST_CONFIRMATION_FUNCTION_CALL_NAMEversion

Functions

createEventcreateEventActionscreateSessiongeminiInitParamsgetArtifactServiceFromUrigetAskUserConfirmationFunctionCallsgetFunctionCallsgetFunctionResponsesgetGcpExportersgetGcpResourcegetLoggergetSessionServiceFromUrihasTrailingCodeExecutionResultisAgentToolisBaseAgentisBaseExampleProviderisBaseLlmisBaseToolisBaseToolsetisFinalResponseisFunctionToolisGemini2OrAboveisLlmAgentisLoopAgentisParallelAgentisSequentialAgentmaybeSetOtelProvidersmergeStatessetLoggersetLogLevelstringifyContenttoStructuredEventstrimTempDeltaStatezodObjectToSchema

[ADK for TypeScript: API Reference](index.html)

  * Loading...


