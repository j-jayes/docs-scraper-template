JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Event.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.events](../package-summary.html)
  2. [Event](../Event.html)



# Uses of Class  
com.google.adk.events.Event

Packages that use [Event](../Event.html "class in com.google.adk.events")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.web

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk](../../package-summary.html)

Methods in [com.google.adk](../../package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static void`

Telemetry.`[traceToolResponse](../../Telemetry.html#traceToolResponse\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ReadonlyContext.`[events](../../agents/ReadonlyContext.html#events\(\))()`

Returns an unmodifiable view of the events of the session.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseAgent.`[runAsync](../../agents/BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent asynchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseAgent.`[runAsyncImpl](../../agents/BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

LlmAgent.`[runAsyncImpl](../../agents/LlmAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

LoopAgent.`[runAsyncImpl](../../agents/LoopAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

ParallelAgent.`[runAsyncImpl](../../agents/ParallelAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents in parallel and emits their events.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

SequentialAgent.`[runAsyncImpl](../../agents/SequentialAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseAgent.`[runLive](../../agents/BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent synchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseAgent.`[runLiveImpl](../../agents/BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

LlmAgent.`[runLiveImpl](../../agents/LlmAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

LoopAgent.`[runLiveImpl](../../agents/LoopAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

ParallelAgent.`[runLiveImpl](../../agents/ParallelAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Not supported for ParallelAgent.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

SequentialAgent.`[runLiveImpl](../../agents/SequentialAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially in live mode.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.events](../package-summary.html)

Classes in [com.google.adk.events](../package-summary.html) that implement interfaces with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Class

Description

`class `

`[EventStream](../EventStream.html "class in com.google.adk.events")`

Iterable stream of [`Event`](../Event.html "class in com.google.adk.events") objects.

Methods in [com.google.adk.events](../package-summary.html) that return [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[Event](../Event.html "class in com.google.adk.events")`

Event.Builder.`[build](../Event.Builder.html#build\(\))()`

 

`static [Event](../Event.html "class in com.google.adk.events")`

Event.`[fromJson](../Event.html#fromJson\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)`

Parses an event from a JSON string.

Methods in [com.google.adk.events](../package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

EventStream.`[iterator](../EventStream.html#iterator\(\))()`

Returns an iterator that fetches events lazily.

Constructor parameters in [com.google.adk.events](../package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier

Constructor

Description

` `

`[EventStream](../EventStream.html#%3Cinit%3E\(java.util.function.Supplier\))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<[Event](../Event.html "class in com.google.adk.events")> eventSupplier)`

Constructs a new event stream.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.flows](../../flows/package-summary.html)

Methods in [com.google.adk.flows](../../flows/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseFlow.`[run](../../flows/BaseFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Run this flow.

`default io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseFlow.`[runLive](../../flows/BaseFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")>`

RequestProcessor.RequestProcessingResult.`[events](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#events\(\))()`

 

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseProcessor.ResponseProcessingResult.`[events](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#events\(\))()`

 

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[run](../../flows/llmflows/BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(com.google.adk.agents.InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[runLive](../../flows/llmflows/BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static void`

Functions.`[populateClientFunctionCallId](../../flows/llmflows/Functions.html#populateClientFunctionCallId\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") modelResponseEvent)`

Populates missing function call IDs in the provided event's content.

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

Method parameters in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

RequestProcessor.RequestProcessingResult.`[create](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#create\(com.google.adk.models.LlmRequest,java.lang.Iterable\))([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.util.Optional\))([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)`

Asynchronously runs the agent for a given user and session, processing a new message and using a default [`RunConfig`](../../agents/RunConfig.html "class in com.google.adk.agents").

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runWithSessionId](../../runner/Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent asynchronously with a default user ID.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.sessions](../../sessions/package-summary.html)

Methods in [com.google.adk.sessions](../../sessions/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

BaseSessionService.`[appendEvent](../../sessions/BaseSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

Appends an event to an in-memory session object and updates the session's state based on the event's state delta, if applicable.

`io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

InMemorySessionService.`[appendEvent](../../sessions/InMemorySessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

VertexAiSessionService.`[appendEvent](../../sessions/VertexAiSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

 

`abstract com.google.common.collect.ImmutableList<[Event](../Event.html "class in com.google.adk.events")>`

ListEventsResponse.`[events](../../sessions/ListEventsResponse.html#events\(\))()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

Session.`[events](../../sessions/Session.html#events\(\))()`

 

Methods in [com.google.adk.sessions](../../sessions/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

BaseSessionService.`[appendEvent](../../sessions/BaseSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

Appends an event to an in-memory session object and updates the session's state based on the event's state delta, if applicable.

`io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

InMemorySessionService.`[appendEvent](../../sessions/InMemorySessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Single<[Event](../Event.html "class in com.google.adk.events")>`

VertexAiSessionService.`[appendEvent](../../sessions/VertexAiSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

 

Method parameters in [com.google.adk.sessions](../../sessions/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`abstract [ListEventsResponse.Builder](../../sessions/ListEventsResponse.Builder.html "class in com.google.adk.sessions")`

ListEventsResponse.Builder.`[events](../../sessions/ListEventsResponse.Builder.html#events\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

`[Session.Builder](../../sessions/Session.Builder.html "class in com.google.adk.sessions")`

Session.Builder.`[events](../../sessions/Session.Builder.html#events\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

AdkWebServer.AgentController.`[agentRun](../../web/AdkWebServer.AgentController.html#agentRun\(com.google.adk.web.AdkWebServer.AgentRunRequest\))([AdkWebServer.AgentRunRequest](../../web/AdkWebServer.AgentRunRequest.html "class in com.google.adk.web") request)`

Executes a non-streaming agent run for a given session and message.




* * *

Copyright (C) 2025\. All rights reserved.
