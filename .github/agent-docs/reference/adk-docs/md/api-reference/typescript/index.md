[ADK for TypeScript: API Reference](index.html)

SystemLightDark

Search…




Preparing search index...

# ADK for TypeScript: API Reference

## Enumerations

[LogLevel](enums/LogLevel.html)
    
[PolicyOutcome](enums/PolicyOutcome.html)
    
[StreamingMode](enums/StreamingMode.html)
    

## Classes

[AgentTool](classes/AgentTool.html)
    
[BaseAgent](classes/BaseAgent.html)
    
[BaseLlm](classes/BaseLlm.html)
    
[BasePlugin](classes/BasePlugin.html)
    
[BaseSessionService](classes/BaseSessionService.html)
    
[BaseTool](classes/BaseTool.html)
    
[BaseToolset](classes/BaseToolset.html)
    
[CallbackContext](classes/CallbackContext.html)
    
[FunctionTool](classes/FunctionTool.html)
    
[GcsArtifactService](classes/GcsArtifactService.html)
    
[Gemini](classes/Gemini.html)
    
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
    
[Runner](classes/Runner.html)
    
[SecurityPlugin](classes/SecurityPlugin.html)
    
[SequentialAgent](classes/SequentialAgent.html)
    
[ToolConfirmation](classes/ToolConfirmation.html)
    
[ToolContext](classes/ToolContext.html)
    

## Interfaces

[AppendEventRequest](interfaces/AppendEventRequest.html)
    
[BaseArtifactService](interfaces/BaseArtifactService.html)
    
[BaseCredentialService](interfaces/BaseCredentialService.html)
    
[BaseLlmConnection](interfaces/BaseLlmConnection.html)
    
[BaseMemoryService](interfaces/BaseMemoryService.html)
    
[BasePolicyEngine](interfaces/BasePolicyEngine.html)
    
[BaseToolParams](interfaces/BaseToolParams.html)
    
[CreateSessionRequest](interfaces/CreateSessionRequest.html)
    
[DeleteArtifactRequest](interfaces/DeleteArtifactRequest.html)
    
[DeleteSessionRequest](interfaces/DeleteSessionRequest.html)
    
[Event](interfaces/Event.html)
    
[EventActions](interfaces/EventActions.html)
    
[GeminiParams](interfaces/GeminiParams.html)
    
[GetSessionConfig](interfaces/GetSessionConfig.html)
    
[GetSessionRequest](interfaces/GetSessionRequest.html)
    
[ListArtifactKeysRequest](interfaces/ListArtifactKeysRequest.html)
    
[ListSessionsRequest](interfaces/ListSessionsRequest.html)
    
[ListSessionsResponse](interfaces/ListSessionsResponse.html)
    
[ListVersionsRequest](interfaces/ListVersionsRequest.html)
    
[LiveRequest](interfaces/LiveRequest.html)
    
[LlmRequest](interfaces/LlmRequest.html)
    
[LlmResponse](interfaces/LlmResponse.html)
    
[LoadArtifactRequest](interfaces/LoadArtifactRequest.html)
    
[OtelExportersConfig](interfaces/OtelExportersConfig.html)
    
[OTelHooks](interfaces/OTelHooks.html)
    
[PolicyCheckResult](interfaces/PolicyCheckResult.html)
    
[RunAsyncToolRequest](interfaces/RunAsyncToolRequest.html)
    
[RunConfig](interfaces/RunConfig.html)
    
[SaveArtifactRequest](interfaces/SaveArtifactRequest.html)
    
[SearchMemoryRequest](interfaces/SearchMemoryRequest.html)
    
[SearchMemoryResponse](interfaces/SearchMemoryResponse.html)
    
[Session](interfaces/Session.html)
    
[StdioConnectionParams](interfaces/StdioConnectionParams.html)
    
[StreamableHTTPConnectionParams](interfaces/StreamableHTTPConnectionParams.html)
    
[ToolCallPolicyContext](interfaces/ToolCallPolicyContext.html)
    
[ToolProcessLlmRequest](interfaces/ToolProcessLlmRequest.html)
    

## Type Aliases

[AfterModelCallback](types/AfterModelCallback.html)
    
[AfterToolCallback](types/AfterToolCallback.html)
    
[BeforeModelCallback](types/BeforeModelCallback.html)
    
[BeforeToolCallback](types/BeforeToolCallback.html)
    
[MCPConnectionParams](types/MCPConnectionParams.html)
    
[SingleAfterModelCallback](types/SingleAfterModelCallback.html)
    
[SingleAfterToolCallback](types/SingleAfterToolCallback.html)
    
[SingleBeforeModelCallback](types/SingleBeforeModelCallback.html)
    
[SingleBeforeToolCallback](types/SingleBeforeToolCallback.html)
    

## Variables

[functionsExportedForTestingOnly](variables/functionsExportedForTestingOnly.html)
    
[GOOGLE_SEARCH](variables/GOOGLE_SEARCH.html)
    
[REQUEST_CONFIRMATION_FUNCTION_CALL_NAME](variables/REQUEST_CONFIRMATION_FUNCTION_CALL_NAME.html)
    

## Functions

[createEvent](functions/createEvent.html)
    
[createEventActions](functions/createEventActions.html)
    
[createSession](functions/createSession.html)
    
[getAskUserConfirmationFunctionCalls](functions/getAskUserConfirmationFunctionCalls.html)
    
[getFunctionCalls](functions/getFunctionCalls.html)
    
[getFunctionResponses](functions/getFunctionResponses.html)
    
[getGcpExporters](functions/getGcpExporters.html)
    
[getGcpResource](functions/getGcpResource.html)
    
[hasTrailingCodeExecutionResult](functions/hasTrailingCodeExecutionResult.html)
    
[isFinalResponse](functions/isFinalResponse.html)
    
[maybeSetOtelProviders](functions/maybeSetOtelProviders.html)
    
[setLogLevel](functions/setLogLevel.html)
    
[stringifyContent](functions/stringifyContent.html)
    
[zodObjectToSchema](functions/zodObjectToSchema.html)
    

Enumerations

LogLevelPolicyOutcomeStreamingMode

Classes

AgentToolBaseAgentBaseLlmBasePluginBaseSessionServiceBaseToolBaseToolsetCallbackContextFunctionToolGcsArtifactServiceGeminiInMemoryArtifactServiceInMemoryMemoryServiceInMemoryPolicyEngineInMemoryRunnerInMemorySessionServiceInvocationContextLiveRequestQueueLlmAgentLLMRegistryLoggingPluginLongRunningFunctionToolLoopAgentMCPSessionManagerMCPToolMCPToolsetParallelAgentPluginManagerRunnerSecurityPluginSequentialAgentToolConfirmationToolContext

Interfaces

AppendEventRequestBaseArtifactServiceBaseCredentialServiceBaseLlmConnectionBaseMemoryServiceBasePolicyEngineBaseToolParamsCreateSessionRequestDeleteArtifactRequestDeleteSessionRequestEventEventActionsGeminiParamsGetSessionConfigGetSessionRequestListArtifactKeysRequestListSessionsRequestListSessionsResponseListVersionsRequestLiveRequestLlmRequestLlmResponseLoadArtifactRequestOtelExportersConfigOTelHooksPolicyCheckResultRunAsyncToolRequestRunConfigSaveArtifactRequestSearchMemoryRequestSearchMemoryResponseSessionStdioConnectionParamsStreamableHTTPConnectionParamsToolCallPolicyContextToolProcessLlmRequest

Type Aliases

AfterModelCallbackAfterToolCallbackBeforeModelCallbackBeforeToolCallbackMCPConnectionParamsSingleAfterModelCallbackSingleAfterToolCallbackSingleBeforeModelCallbackSingleBeforeToolCallback

Variables

functionsExportedForTestingOnlyGOOGLE_SEARCHREQUEST_CONFIRMATION_FUNCTION_CALL_NAME

Functions

createEventcreateEventActionscreateSessiongetAskUserConfirmationFunctionCallsgetFunctionCallsgetFunctionResponsesgetGcpExportersgetGcpResourcehasTrailingCodeExecutionResultisFinalResponsemaybeSetOtelProviderssetLogLevelstringifyContentzodObjectToSchema

[ADK for TypeScript: API Reference](index.html)

  * Loading...


