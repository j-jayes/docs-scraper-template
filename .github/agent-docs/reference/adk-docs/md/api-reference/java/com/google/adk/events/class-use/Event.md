JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Event.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
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

 

com.google.adk.a2a

 

com.google.adk.a2a.converters

 

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.plugins

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.summarizer

 

com.google.adk.web.controller

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk](../../package-summary.html)

Methods in [com.google.adk](../../package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static void`

Telemetry.`[traceToolResponse](../../Telemetry.html#traceToolResponse\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.a2a](../../a2a/package-summary.html)

Methods in [com.google.adk.a2a](../../a2a/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Event](../Event.html "class in com.google.adk.events")>>`

A2ASendMessageExecutor.AgentExecutionStrategy.`[execute](../../a2a/A2ASendMessageExecutor.AgentExecutionStrategy.html#execute\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runAsyncImpl](../../a2a/RemoteA2AAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runLiveImpl](../../a2a/RemoteA2AAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html)

Fields in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with type parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Field

Description

`final com.google.common.collect.ImmutableList<[Event](../Event.html "class in com.google.adk.events")>`

ConversationPreprocessor.PreparedInput.`[historyEvents](../../a2a/converters/ConversationPreprocessor.PreparedInput.html#historyEvents)`

Historical events that should remain in the session transcript.

`final [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ConversationPreprocessor.PreparedInput.`[userEvent](../../a2a/converters/ConversationPreprocessor.PreparedInput.html#userEvent)`

The concrete event that supplied [`ConversationPreprocessor.PreparedInput.userContent`](../../a2a/converters/ConversationPreprocessor.PreparedInput.html#userContent), for callers needing metadata.

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

RequestConverter.`[convertA2aMessageToAdkEvent](../../a2a/converters/RequestConverter.html#convertA2aMessageToAdkEvent\(io.a2a.spec.Message,java.lang.String\))(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Convert an A2A Message to an ADK Event.

`static com.google.common.collect.ImmutableList<[Event](../Event.html "class in com.google.adk.events")>`

RequestConverter.`[convertAggregatedA2aMessageToAdkEvents](../../a2a/converters/RequestConverter.html#convertAggregatedA2aMessageToAdkEvents\(io.a2a.spec.Message,java.lang.String\))(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Convert an aggregated A2A Message to multiple ADK Events.

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseConverter.`[messageToEvents](../../a2a/converters/ResponseConverter.html#messageToEvents\(io.a2a.spec.Message,java.lang.String,java.lang.String\))(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Converts an A2A message back to ADK events.

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseConverter.`[sendMessageResponseToEvents](../../a2a/converters/ResponseConverter.html#sendMessageResponseToEvents\(io.a2a.spec.SendMessageResponse,java.lang.String,java.lang.String\))(io.a2a.spec.SendMessageResponse response, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Converts a `SendMessageResponse` containing a `Message` result into ADK events.

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message>`

EventConverter.`[convertEventToA2AMessage](../../a2a/converters/EventConverter.html#convertEventToA2AMessage\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

 

`static io.a2a.spec.Message`

ResponseConverter.`[eventToMessage](../../a2a/converters/ResponseConverter.html#eventToMessage\(com.google.adk.events.Event,java.lang.String\))([Event](../Event.html "class in com.google.adk.events") event, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") contextId)`

Converts a single ADK event into an A2A message.

Method parameters in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static io.a2a.spec.Message`

ResponseConverter.`[eventsToMessage](../../a2a/converters/ResponseConverter.html#eventsToMessage\(java.util.List,java.lang.String,java.lang.String\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") contextId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") taskId)`

Converts a list of ADK events into a single aggregated A2A message.

`static [ConversationPreprocessor.PreparedInput](../../a2a/converters/ConversationPreprocessor.PreparedInput.html "class in com.google.adk.a2a.converters")`

ConversationPreprocessor.`[extractHistoryAndUserContent](../../a2a/converters/ConversationPreprocessor.html#extractHistoryAndUserContent\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> inputEvents)`

Splits the provided event list into history and the latest user-authored text message.

Constructor parameters in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier

Constructor

Description

` `

`[PreparedInput](../../a2a/converters/ConversationPreprocessor.PreparedInput.html#%3Cinit%3E\(com.google.common.collect.ImmutableList,java.util.Optional,java.util.Optional\))(com.google.common.collect.ImmutableList<[Event](../Event.html "class in com.google.adk.events")> historyEvents, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> userEvent)`

Creates a new instance.

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

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`boolean`

InvocationContext.`[shouldPauseInvocation](../../agents/InvocationContext.html#shouldPauseInvocation\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

Returns whether to pause the invocation right after this [event].

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

Events generated during processing.

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseProcessor.ResponseProcessingResult.`[events](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#events\(\))()`

Events generated during processing.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[generateRequestConfirmationEvent](../../flows/llmflows/Functions.html#generateRequestConfirmationEvent\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[run](../../flows/llmflows/BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[runLive](../../flows/llmflows/BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[generateRequestConfirmationEvent](../../flows/llmflows/Functions.html#generateRequestConfirmationEvent\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall>`

Functions.`[getAskUserConfirmationFunctionCalls](../../flows/llmflows/Functions.html#getAskUserConfirmationFunctionCalls\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

Gets the ask user confirmation function calls from the event.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`static void`

Functions.`[populateClientFunctionCallId](../../flows/llmflows/Functions.html#populateClientFunctionCallId\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") modelResponseEvent)`

Populates missing function call IDs in the provided event's content.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

Method parameters in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

RequestProcessor.RequestProcessingResult.`[create](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#create\(com.google.adk.models.LlmRequest,java.lang.Iterable\))([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events)`

Creates a new [`RequestProcessor.RequestProcessingResult`](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows").

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.util.Optional\))([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

Creates a new [`ResponseProcessor.ResponseProcessingResult`](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows").

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LoggingPlugin.`[onEventCallback](../../plugins/LoggingPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

`default io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Plugin.`[onEventCallback](../../plugins/Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

PluginManager.`[onEventCallback](../../plugins/PluginManager.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

PluginManager.`[runOnEventCallback](../../plugins/PluginManager.html#runOnEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LoggingPlugin.`[onEventCallback](../../plugins/LoggingPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

`default io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Plugin.`[onEventCallback](../../plugins/Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

PluginManager.`[onEventCallback](../../plugins/PluginManager.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

PluginManager.`[runOnEventCallback](../../plugins/PluginManager.html#runOnEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

Runs the agent with an invocation-based mode.

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

FirestoreSessionService.`[appendEvent](../../sessions/FirestoreSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

Appends an event to a session, updating the session state and persisting to Firestore.

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

FirestoreSessionService.`[appendEvent](../../sessions/FirestoreSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Event](../Event.html "class in com.google.adk.events") event)`

Appends an event to a session, updating the session state and persisting to Firestore.

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

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.summarizer](../../summarizer/package-summary.html)

Methods in [com.google.adk.summarizer](../../summarizer/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BaseEventSummarizer.`[summarizeEvents](../../summarizer/BaseEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LlmEventSummarizer.`[summarizeEvents](../../summarizer/LlmEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

Method parameters in [com.google.adk.summarizer](../../summarizer/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BaseEventSummarizer.`[summarizeEvents](../../summarizer/BaseEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LlmEventSummarizer.`[summarizeEvents](../../summarizer/LlmEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.web.controller](../../web/controller/package-summary.html)

Methods in [com.google.adk.web.controller](../../web/controller/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ExecutionController.`[agentRun](../../web/controller/ExecutionController.html#agentRun\(com.google.adk.web.dto.AgentRunRequest\))([AgentRunRequest](../../web/dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes a non-streaming agent run for a given session and message.




* * *

Copyright (C) 1980\. All rights reserved.
