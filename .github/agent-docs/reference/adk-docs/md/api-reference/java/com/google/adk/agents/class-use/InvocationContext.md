JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../InvocationContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [InvocationContext](../InvocationContext.html)



# Uses of Class  
com.google.adk.agents.InvocationContext

Packages that use [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk.a2a.agent

 

com.google.adk.a2a.converters

 

com.google.adk.agents

 

com.google.adk.codeexecutors

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.telemetry

 

com.google.adk.tools

 

com.google.adk.utils

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Methods in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runAsyncImpl](../../a2a/agent/RemoteA2AAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

RemoteA2AAgent.`[runLiveImpl](../../a2a/agent/RemoteA2AAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html)

Methods in [com.google.adk.a2a.converters](../../a2a/converters/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Event](../../events/Event.html "class in com.google.adk.events")`

ResponseConverter.`[artifactToEvent](../../a2a/converters/ResponseConverter.html#artifactToEvent\(io.a2a.spec.Artifact,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Artifact artifact, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an artifact to an ADK event.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

ResponseConverter.`[clientEventToEvent](../../a2a/converters/ResponseConverter.html#clientEventToEvent\(io.a2a.client.ClientEvent,com.google.adk.agents.InvocationContext\))(io.a2a.client.ClientEvent event, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts a A2A `ClientEvent` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events"), based on the event type.

`static com.google.common.collect.ImmutableList<io.a2a.spec.Part<?>>`

EventConverter.`[messagePartsFromContext](../../a2a/converters/EventConverter.html#messagePartsFromContext\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context)`

Returns the parts from the context events that should be sent to the agent.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToEvent](../../a2a/converters/ResponseConverter.html#messageToEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Message message, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message back to ADK events.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToEvent](../../a2a/converters/ResponseConverter.html#messageToEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext,boolean\))(io.a2a.spec.Message message, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, boolean isPending)`

Converts an A2A message back to ADK events.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

ResponseConverter.`[messageToFailedEvent](../../a2a/converters/ResponseConverter.html#messageToFailedEvent\(io.a2a.spec.Message,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Message message, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message for a failed task to ADK event filling in the error message.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

ResponseConverter.`[taskToEvent](../../a2a/converters/ResponseConverter.html#taskToEvent\(io.a2a.spec.Task,com.google.adk.agents.InvocationContext\))(io.a2a.spec.Task task, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A `Task` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events").

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

`[InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[build](../InvocationContext.Builder.html#build\(\))()`

Builds the [`InvocationContext`](../InvocationContext.html "class in com.google.adk.agents") instance.

`[InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

ReadonlyContext.`[invocationContext](../ReadonlyContext.html#invocationContext\(\))()`

Returns the invocation context.

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

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.OnToolErrorCallback.`[call](../Callbacks.OnToolErrorCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

Async callback when tool call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.OnToolErrorCallbackSync.`[call](../Callbacks.OnToolErrorCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

 

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

`[CallbackContext](../CallbackContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext,com.google.adk.events.EventActions,java.lang.String\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../../events/EventActions.html "class in com.google.adk.events") eventActions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)`

Initializes callback context.

` `

`[ReadonlyContext](../ReadonlyContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.codeexecutors](../../codeexecutors/package-summary.html)

Methods in [com.google.adk.codeexecutors](../../codeexecutors/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`abstract [CodeExecutionUtils.CodeExecutionResult](../../codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

BaseCodeExecutor.`[executeCode](../../codeexecutors/BaseCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](../../codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

Executes code and return the code execution result.

`[CodeExecutionUtils.CodeExecutionResult](../../codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

BuiltInCodeExecutor.`[executeCode](../../codeexecutors/BuiltInCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](../../codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

 

`[CodeExecutionUtils.CodeExecutionResult](../../codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[executeCode](../../codeexecutors/ContainerCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](../../codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

 

`[CodeExecutionUtils.CodeExecutionResult](../../codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

VertexAiCodeExecutor.`[executeCode](../../codeexecutors/VertexAiCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](../../codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

 

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

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[generateRequestConfirmationEvent](../../flows/llmflows/Functions.html#generateRequestConfirmationEvent\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Event](../../events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

AgentTransfer.`[processRequest](../../flows/llmflows/AgentTransfer.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Basic.`[processRequest](../../flows/llmflows/Basic.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Compaction.`[processRequest](../../flows/llmflows/Compaction.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Contents.`[processRequest](../../flows/llmflows/Contents.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Identity.`[processRequest](../../flows/llmflows/Identity.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Instructions.`[processRequest](../../flows/llmflows/Instructions.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

RequestConfirmationLlmRequestProcessor.`[processRequest](../../flows/llmflows/RequestConfirmationLlmRequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

RequestProcessor.`[processRequest](../../flows/llmflows/RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

`io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

ResponseProcessor.`[processResponse](../../flows/llmflows/ResponseProcessor.html#processResponse\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmResponse\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") response)`

Process the LLM response as part of the post-processing stage.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[run](../../flows/llmflows/BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(Context, InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[runLive](../../flows/llmflows/BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

LoggingPlugin.`[afterRunCallback](../../plugins/LoggingPlugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`default io.reactivex.rxjava3.core.Completable`

Plugin.`[afterRunCallback](../../plugins/Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`io.reactivex.rxjava3.core.Completable`

PluginManager.`[afterRunCallback](../../plugins/PluginManager.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Completable`

ReplayPlugin.`[afterRunCallback](../../plugins/ReplayPlugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[beforeRunCallback](../../plugins/LoggingPlugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[beforeRunCallback](../../plugins/Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[beforeRunCallback](../../plugins/PluginManager.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

ReplayPlugin.`[beforeRunCallback](../../plugins/ReplayPlugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

LoggingPlugin.`[onEventCallback](../../plugins/LoggingPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)`

 

`default io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Plugin.`[onEventCallback](../../plugins/Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

PluginManager.`[onEventCallback](../../plugins/PluginManager.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[onUserMessageCallback](../../plugins/LoggingPlugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable com.google.genai.types.Content userMessage)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[onUserMessageCallback](../../plugins/Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[onUserMessageCallback](../../plugins/PluginManager.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[runBeforeRunCallback](../../plugins/PluginManager.html#runBeforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[runOnUserMessageCallback](../../plugins/PluginManager.html#runOnUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

BigQueryAgentAnalyticsPlugin.`[afterRunCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[beforeRunCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

BigQueryAgentAnalyticsPlugin.`[onEventCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[onUserMessageCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.telemetry](../../telemetry/package-summary.html)

Methods in [com.google.adk.telemetry](../../telemetry/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static <T> [Tracing.TracerProvider](../../telemetry/Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

Tracing.`[traceAgent](../../telemetry/Tracing.html#traceAgent\(java.lang.String,java.lang.String,java.lang.String,com.google.adk.agents.InvocationContext\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Returns a transformer that traces an agent invocation.

`static void`

Tracing.`[traceAgentInvocation](../../telemetry/Tracing.html#traceAgentInvocation\(io.opentelemetry.api.trace.Span,java.lang.String,java.lang.String,com.google.adk.agents.InvocationContext\))(io.opentelemetry.api.trace.Span span, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Sets span attributes immediately available on agent invocation according to OTEL semconv version 1.37.

`static void`

Tracing.`[traceCallLlm](../../telemetry/Tracing.html#traceCallLlm\(io.opentelemetry.api.trace.Span,com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))(io.opentelemetry.api.trace.Span span, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

`static void`

Tracing.`[traceSendData](../../telemetry/Tracing.html#traceSendData\(com.google.adk.agents.InvocationContext,java.lang.String,java.util.List\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)`

Traces the sending of data (history or new content) to the agent/model.

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [ToolContext.Builder](../../tools/ToolContext.Builder.html "class in com.google.adk.tools")`

ToolContext.`[builder](../../tools/ToolContext.html#builder\(com.google.adk.agents.InvocationContext\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

FunctionTool.`[callLive](../../tools/FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Uses of [InvocationContext](../InvocationContext.html "class in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) with parameters of type [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

InstructionUtils.`[injectSessionState](../../utils/InstructionUtils.html#injectSessionState\(com.google.adk.agents.InvocationContext,java.lang.String\))([InvocationContext](../InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") template)`

Populates placeholders in an instruction template string with values from the session state or loaded artifacts.




* * *

Copyright (C) 1980\. All rights reserved.
