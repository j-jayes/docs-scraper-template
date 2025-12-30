JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../InvocationContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [InvocationContext](../InvocationContext.html)



# Uses of Class  
com.google.adk.agents.InvocationContext

Packages that use [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.tools

 

com.google.adk.utils

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk](../../package-summary.html)

Methods in [com.google.adk](../../package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static void`

Telemetry.`[traceCallLlm](../../Telemetry.html#traceCallLlm\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

`static void`

Telemetry.`[traceSendData](../../Telemetry.html#traceSendData\(com.google.adk.agents.InvocationContext,java.lang.String,java.util.List\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)`

Traces the sending of data (history or new content) to the agent/model.

`static void`

Telemetry.`[traceToolResponse](../../Telemetry.html#traceToolResponse\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](../../events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Fields in [com.google.adk.agents](../package-summary.html) declared as [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Field

Description

`protected final [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

ReadonlyContext.`[invocationContext](../ReadonlyContext.html#invocationContext)`

 

Methods in [com.google.adk.agents](../package-summary.html) that return [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[copyOf](../InvocationContext.html#copyOf\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") other)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallback.`[call](../Callbacks.AfterToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

Async callback after tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallbackSync.`[call](../Callbacks.AfterToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallback.`[call](../Callbacks.BeforeToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Async callback before tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallbackSync.`[call](../Callbacks.BeforeToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[copyOf](../InvocationContext.html#copyOf\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") other)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseAgent.`[runAsync](../BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent asynchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseAgent.`[runAsyncImpl](../BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

LlmAgent.`[runAsyncImpl](../LlmAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

LoopAgent.`[runAsyncImpl](../LoopAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

ParallelAgent.`[runAsyncImpl](../ParallelAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents in parallel and emits their events.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

SequentialAgent.`[runAsyncImpl](../SequentialAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseAgent.`[runLive](../BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent synchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseAgent.`[runLiveImpl](../BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

LlmAgent.`[runLiveImpl](../LlmAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

LoopAgent.`[runLiveImpl](../LoopAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

ParallelAgent.`[runLiveImpl](../ParallelAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Not supported for ParallelAgent.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

SequentialAgent.`[runLiveImpl](../SequentialAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially in live mode.

Constructors in [com.google.adk.agents](../package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[CallbackContext](../CallbackContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext,com.google.adk.events.EventActions\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../../events/EventActions.html "class in com.google.adk.events") eventActions)`

Initializes callback context.

` `

`[ReadonlyContext](../ReadonlyContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.flows](../../flows/package-summary.html)

Methods in [com.google.adk.flows](../../flows/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseFlow.`[run](../../flows/BaseFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Run this flow.

`default io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseFlow.`[runLive](../../flows/BaseFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`protected io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[preprocess](../../flows/llmflows/BaseLlmFlow.html#preprocess\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)`

Pre-processes the LLM request before sending it to the LLM.

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

AgentTransfer.`[processRequest](../../flows/llmflows/AgentTransfer.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Basic.`[processRequest](../../flows/llmflows/Basic.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Contents.`[processRequest](../../flows/llmflows/Contents.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Examples.`[processRequest](../../flows/llmflows/Examples.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Identity.`[processRequest](../../flows/llmflows/Identity.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Instructions.`[processRequest](../../flows/llmflows/Instructions.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

RequestProcessor.`[processRequest](../../flows/llmflows/RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

`io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

ResponseProcessor.`[processResponse](../../flows/llmflows/ResponseProcessor.html#processResponse\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmResponse\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") response)`

Process the LLM response as part of the post-processing stage.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[run](../../flows/llmflows/BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(com.google.adk.agents.InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[runLive](../../flows/llmflows/BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [ToolContext.Builder](../../tools/ToolContext.Builder.html "class in com.google.adk.tools")`

ToolContext.`[builder](../../tools/ToolContext.html#builder\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

InstructionUtils.`[injectSessionState](../../utils/InstructionUtils.html#injectSessionState\(com.google.adk.agents.InvocationContext,java.lang.String\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") template)`

Populates placeholders in an instruction template string with values from the session state or loaded artifacts.




* * *

Copyright (C) 2025\. All rights reserved.
