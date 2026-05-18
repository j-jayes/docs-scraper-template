JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Event.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](../package-summary.html)
  2. [Event](../Event.html)



# Uses of Class  
com.google.adk.events.Event

Packages that use [Event](../Event.html "class in com.google.adk.events")

Package

Description

com.google.adk.a2a.agent

 

com.google.adk.a2a.converters

 

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.summarizer

 

com.google.adk.telemetry

 

com.google.adk.web.controller

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Methods in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runAsyncImpl](../../a2a/agent/RemoteA2AAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runLiveImpl](../../a2a/agent/RemoteA2AAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html)

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) that return [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Event](../Event.html "class in com.google.adk.events")`

ResponseConverter.`[artifactToEvent](../../a2a/converters/ResponseConverter.html#artifactToEvent\(io.a2a.spec.Artifact,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Artifact artifact, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an artifact to an ADK event.

`static @Nullable [Event](../Event.html "class in com.google.adk.events")`

EventConverter.`[findUserFunctionCall](../../a2a/converters/EventConverter.html#findUserFunctionCall\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Returns the last user function call event from the list of events.

`static [Event](../Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToEvent](../../a2a/converters/ResponseConverter.html#messageToEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message back to ADK events.

`static [Event](../Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToEvent](../../a2a/converters/ResponseConverter.html#messageToEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext,boolean\))(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, boolean isPending)`

Converts an A2A message back to ADK events.

`static [Event](../Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToFailedEvent](../../a2a/converters/ResponseConverter.html#messageToFailedEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message for a failed task to ADK event filling in the error message.

`static [Event](../Event.html "class in com.google.adk.events")`

ResponseConverter.`[taskToEvent](../../a2a/converters/ResponseConverter.html#taskToEvent\(io.a2a.spec.Task,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Task task, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A `Task` to an ADK [`Event`](../Event.html "class in com.google.adk.events").

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseConverter.`[clientEventToEvent](../../a2a/converters/ResponseConverter.html#clientEventToEvent\(io.a2a.client.ClientEvent,com.google.adk.agents.InvocationContext\))(io.a2a.client.ClientEvent event, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts a A2A `ClientEvent` to an ADK [`Event`](../Event.html "class in com.google.adk.events"), based on the event type.

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

EventConverter.`[contextId](../../a2a/converters/EventConverter.html#contextId\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

Returns the context ID from the event.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

EventConverter.`[taskId](../../a2a/converters/EventConverter.html#taskId\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

Returns the task ID from the event.

Method parameters in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static @Nullable [Event](../Event.html "class in com.google.adk.events")`

EventConverter.`[findUserFunctionCall](../../a2a/converters/EventConverter.html#findUserFunctionCall\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Returns the last user function call event from the list of events.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<io.a2a.spec.TaskArtifactUpdateEvent>`

Callbacks.AfterEventCallback.`[call](../../a2a/executor/Callbacks.AfterEventCallback.html#call\(io.a2a.server.agentexecution.RequestContext,io.a2a.spec.TaskArtifactUpdateEvent,com.google.adk.events.Event\))(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.spec.TaskArtifactUpdateEvent processedEvent, [Event](../Event.html "class in com.google.adk.events") event)`

Callback which will be called after an ADK event is successfully converted to an A2A event.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

PlanningContext.`[events](../../agents/PlanningContext.html#events\(\))()`

Returns all events in the current session.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

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

PlannerAgent.`[runAsyncImpl](../../agents/PlannerAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

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

PlannerAgent.`[runLiveImpl](../../agents/PlannerAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

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

Event.`[fromJson](../Event.html#fromJson\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)`

Parses an event from a JSON string.

Methods in [com.google.adk.events](../package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

EventStream.`[iterator](../EventStream.html#iterator\(\))()`

Returns an iterator that fetches events lazily.

Constructor parameters in [com.google.adk.events](../package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier

Constructor

Description

` `

`[EventStream](../EventStream.html#%3Cinit%3E\(java.util.function.Supplier\))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "interface in java.util.function")<[Event](../Event.html "class in com.google.adk.events")> eventSupplier)`

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

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Event](../Event.html "class in com.google.adk.events")`

OutputSchema.`[createFinalModelResponseEvent](../../flows/llmflows/OutputSchema.html#createFinalModelResponseEvent\(com.google.adk.agents.InvocationContext,java.lang.String\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonResponse)`

Create a final model response event from set_model_response JSON.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")>`

RequestProcessor.RequestProcessingResult.`[events](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#events\(\))()`

Events generated during processing.

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")>`

ResponseProcessor.ResponseProcessingResult.`[events](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#events\(\))()`

Events generated during processing.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[generateRequestConfirmationEvent](../../flows/llmflows/Functions.html#generateRequestConfirmationEvent\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[run](../../flows/llmflows/BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(Context, InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[runLive](../../flows/llmflows/BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[generateRequestConfirmationEvent](../../flows/llmflows/Functions.html#generateRequestConfirmationEvent\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall>`

Functions.`[getAskUserConfirmationFunctionCalls](../../flows/llmflows/Functions.html#getAskUserConfirmationFunctionCalls\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") event)`

Gets the ask user confirmation function calls from the event.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

OutputSchema.`[getStructuredModelResponse](../../flows/llmflows/OutputSchema.html#getStructuredModelResponse\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Check if function response contains set_model_response and extract JSON.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`static void`

Functions.`[populateClientFunctionCallId](../../flows/llmflows/Functions.html#populateClientFunctionCallId\(com.google.adk.events.Event\))([Event](../Event.html "class in com.google.adk.events") modelResponseEvent)`

Populates missing function call IDs in the provided event's content.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

Post-processes the LLM response after receiving it from the LLM.

Method parameters in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

RequestProcessor.RequestProcessingResult.`[create](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#create\(com.google.adk.models.LlmRequest,java.lang.Iterable\))([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events)`

Creates a new [`RequestProcessor.RequestProcessingResult`](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows").

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable\))([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.lang.String\))([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../Event.html "class in com.google.adk.events")> events, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") transferToAgent)`

 

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

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BigQueryAgentAnalyticsPlugin.`[onEventCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BigQueryAgentAnalyticsPlugin.`[onEventCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../Event.html "class in com.google.adk.events") event)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent with an invocation-based mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runAsyncImpl](../../runner/Runner.html#runAsyncImpl\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent asynchronously using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../Event.html "class in com.google.adk.events")>`

Runner.`[runLiveImpl](../../runner/Runner.html#runLiveImpl\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, @Nullable [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

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

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

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

ListEventsResponse.Builder.`[events](../../sessions/ListEventsResponse.Builder.html#events\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

`[Session.Builder](../../sessions/Session.Builder.html "class in com.google.adk.sessions")`

Session.Builder.`[events](../../sessions/Session.Builder.html#events\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.summarizer](../../summarizer/package-summary.html)

Methods in [com.google.adk.summarizer](../../summarizer/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BaseEventSummarizer.`[summarizeEvents](../../summarizer/BaseEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LlmEventSummarizer.`[summarizeEvents](../../summarizer/LlmEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

Method parameters in [com.google.adk.summarizer](../../summarizer/package-summary.html) with type arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

BaseEventSummarizer.`[summarizeEvents](../../summarizer/BaseEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.

`io.reactivex.rxjava3.core.Maybe<[Event](../Event.html "class in com.google.adk.events")>`

LlmEventSummarizer.`[summarizeEvents](../../summarizer/LlmEventSummarizer.html#summarizeEvents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")> events)`

 

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.telemetry](../../telemetry/package-summary.html)

Methods in [com.google.adk.telemetry](../../telemetry/package-summary.html) with parameters of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`static void`

Tracing.`[traceMergedToolCalls](../../telemetry/Tracing.html#traceMergedToolCalls\(io.opentelemetry.api.trace.Span,java.lang.String,com.google.adk.events.Event\))(io.opentelemetry.api.trace.Span span, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") responseEventId, [Event](../Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces merged tool call events.

`static void`

Tracing.`[traceToolExecution](../../telemetry/Tracing.html#traceToolExecution\(io.opentelemetry.api.trace.Span,java.lang.String,java.lang.String,java.lang.String,java.util.Map,com.google.adk.events.Event,java.lang.Exception\))(io.opentelemetry.api.trace.Span span, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolDescription, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolType, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, @Nullable [Event](../Event.html "class in com.google.adk.events") functionResponseEvent, @Nullable [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Traces a tool execution, including its arguments, response, and any potential error.

  * ## Uses of [Event](../Event.html "class in com.google.adk.events") in [com.google.adk.web.controller](../../web/controller/package-summary.html)

Methods in [com.google.adk.web.controller](../../web/controller/package-summary.html) that return types with arguments of type [Event](../Event.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../Event.html "class in com.google.adk.events")>`

ExecutionController.`[agentRun](../../web/controller/ExecutionController.html#agentRun\(com.google.adk.web.dto.AgentRunRequest\))([AgentRunRequest](../../web/dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes a non-streaming agent run for a given session and message.




* * *

Copyright (C) 1980\. All rights reserved.
