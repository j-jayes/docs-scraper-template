JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseTool.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools](../package-summary.html)
  2. [BaseTool](../BaseTool.html)



# Uses of Class  
com.google.adk.tools.BaseTool

Packages that use [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.models.springai

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.computeruse

 

com.google.adk.tools.mcp

 

com.google.adk.tools.retrieval

 

com.google.adk.utils

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../../agents/LlmAgent.html#canonicalTools\(\))()`

Constructs the list of tools for this agent based on the [`LlmAgent.tools()`](../../agents/LlmAgent.html#tools\(\)) field.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../../agents/LlmAgent.html#canonicalTools\(com.google.adk.agents.ReadonlyContext\))(@Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the list of tools for this agent based on the [`LlmAgent.tools()`](../../agents/LlmAgent.html#tools\(\)) field.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>>`

LlmAgent.`[tools](../../agents/LlmAgent.html#tools\(\))()`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallback.`[call](../../agents/Callbacks.AfterToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

Async callback after tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallbackSync.`[call](../../agents/Callbacks.AfterToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallback.`[call](../../agents/Callbacks.BeforeToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Async callback before tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallbackSync.`[call](../../agents/Callbacks.BeforeToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.OnToolErrorCallback.`[call](../../agents/Callbacks.OnToolErrorCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

Async callback when tool call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.OnToolErrorCallbackSync.`[call](../../agents/Callbacks.OnToolErrorCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Method parameters in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with type arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

Functions.`[getLongRunningFunctionCalls](../../flows/llmflows/Functions.html#getLongRunningFunctionCalls\(java.util.List,java.util.Map\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.FunctionCall> functionCalls, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCallsLive](../../flows/llmflows/Functions.html#handleFunctionCallsLive\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.models](../../models/package-summary.html)

Methods in [com.google.adk.models](../../models/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmRequest.`[tools](../../models/LlmRequest.html#tools\(\))()`

Returns a map of tools available to the LLM.

Method parameters in [com.google.adk.models](../../models/package-summary.html) with type arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`final [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendTools](../../models/LlmRequest.Builder.html#appendTools\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

`abstract [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[tools](../../models/LlmRequest.Builder.html#tools\(java.util.Map\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.models.springai](../../models/springai/package-summary.html)

Method parameters in [com.google.adk.models.springai](../../models/springai/package-summary.html) with type arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<org.springframework.ai.tool.ToolCallback>`

ToolConverter.`[convertToSpringAiTools](../../models/springai/ToolConverter.html#convertToSpringAiTools\(java.util.Map\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

Converts ADK tools to Spring AI ToolCallback format for tool calling.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConverter.ToolMetadata](../../models/springai/ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")>`

ToolConverter.`[createToolRegistry](../../models/springai/ToolConverter.html#createToolRegistry\(java.util.Map\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

Creates a tool registry from ADK tools for internal tracking.

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

LoggingPlugin.`[afterToolCallback](../../plugins/LoggingPlugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Plugin.`[afterToolCallback](../../plugins/Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

Callback executed after a tool has been called.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

PluginManager.`[afterToolCallback](../../plugins/PluginManager.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

LoggingPlugin.`[beforeToolCallback](../../plugins/LoggingPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Plugin.`[beforeToolCallback](../../plugins/Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

PluginManager.`[beforeToolCallback](../../plugins/PluginManager.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

ReplayPlugin.`[beforeToolCallback](../../plugins/ReplayPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

LoggingPlugin.`[onToolErrorCallback](../../plugins/LoggingPlugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Plugin.`[onToolErrorCallback](../../plugins/Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a tool call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

PluginManager.`[onToolErrorCallback](../../plugins/PluginManager.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[afterToolCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[beforeToolCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[onToolErrorCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[AgentTool](../AgentTool.html "class in com.google.adk.tools")`

AgentTool implements a tool that allows an agent to call another agent.

`final class `

`[BuiltInCodeExecutionTool](../BuiltInCodeExecutionTool.html "class in com.google.adk.tools")`

A built-in code execution tool that is automatically invoked by Gemini 2 models.

`final class `

`[ExampleTool](../ExampleTool.html "class in com.google.adk.tools")`

A tool that injects (few-shot) examples into the outgoing LLM request as system instructions.

`class `

`[FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

FunctionTool implements a customized function calling tool.

`class `

`[GoogleMapsTool](../GoogleMapsTool.html "class in com.google.adk.tools")`

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Maps.

`class `

`[GoogleSearchAgentTool](../GoogleSearchAgentTool.html "class in com.google.adk.tools")`

A tool that wraps a sub-agent that only uses google_search tool.

`final class `

`[GoogleSearchTool](../GoogleSearchTool.html "class in com.google.adk.tools")`

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve search results from Google Search.

`final class `

`[LoadArtifactsTool](../LoadArtifactsTool.html "class in com.google.adk.tools")`

A tool that loads artifacts and adds them to the session.

`class `

`[LoadMemoryTool](../LoadMemoryTool.html "class in com.google.adk.tools")`

A tool that loads memory for the current user.

`class `

`[LongRunningFunctionTool](../LongRunningFunctionTool.html "class in com.google.adk.tools")`

A function tool that returns the result asynchronously.

`class `

`[SetModelResponseTool](../SetModelResponseTool.html "class in com.google.adk.tools")`

Internal tool used for output schema workaround.

`final class `

`[UrlContextTool](../UrlContextTool.html "class in com.google.adk.tools")`

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve information from the given URLs.

`class `

`[VertexAiSearchAgentTool](../VertexAiSearchAgentTool.html "class in com.google.adk.tools")`

A tool that wraps a sub-agent that only uses vertex_ai_search tool.

`class `

`[VertexAiSearchTool](../VertexAiSearchTool.html "class in com.google.adk.tools")`

A built-in tool using Vertex AI Search.

Methods in [com.google.adk.tools](../package-summary.html) that return [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static [BaseTool](../BaseTool.html "class in com.google.adk.tools")`

AgentTool.`[fromConfig](../AgentTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolArgsConfig,java.lang.String\))([BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

 

`static [BaseTool](../BaseTool.html "class in com.google.adk.tools")`

BaseTool.`[fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a tool instance from a config.

Methods in [com.google.adk.tools](../package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

BaseToolset.`[getTools](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

Methods in [com.google.adk.tools](../package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`default boolean`

BaseToolset.`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") toolFilter, @Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Checks if a tool should be selected based on a filter.

`boolean`

NamedToolPredicate.`[test](../NamedToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

 

`default boolean`

ToolPredicate.`[test](../ToolPredicate.html#test\(com.google.adk.tools.BaseTool,com.google.adk.agents.ReadonlyContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, @Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Decides if the given tool is selected.

`boolean`

ToolPredicate.`[test](../ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Deprecated.

Use [`ToolPredicate.test(BaseTool, ReadonlyContext)`](../ToolPredicate.html#test\(com.google.adk.tools.BaseTool,com.google.adk.agents.ReadonlyContext\)) instead.

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Modifier and Type

Class

Description

`class `

`[IntegrationConnectorTool](../applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Application Integration Tool

Methods in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

ApplicationIntegrationToolset.`[getTools](../applicationintegrationtoolset/ApplicationIntegrationToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))(@Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.computeruse](../computeruse/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.computeruse](../computeruse/package-summary.html)

Modifier and Type

Class

Description

`class `

`[ComputerUseTool](../computeruse/ComputerUseTool.html "class in com.google.adk.tools.computeruse")`

A tool that wraps computer control functions for use with LLMs.

Methods in [com.google.adk.tools.computeruse](../computeruse/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

ComputerUseToolset.`[getTools](../computeruse/ComputerUseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Modifier and Type

Class

Description

`class `

`[AbstractMcpTool](../mcp/AbstractMcpTool.html "class in com.google.adk.tools.mcp")<T>`

Base class for MCP tools.

`final class `

`[McpAsyncTool](../mcp/McpAsyncTool.html "class in com.google.adk.tools.mcp")`

Initializes a MCP tool.

`final class `

`[McpTool](../mcp/McpTool.html "class in com.google.adk.tools.mcp")`

Initializes a MCP tool.

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

McpAsyncToolset.`[getTools](../mcp/McpAsyncToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

McpToolset.`[getTools](../mcp/McpToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.modelcontextprotocol.spec.McpSchema.Tool`

ConversionUtils.`[adkToMcpToolType](../mcp/ConversionUtils.html#adkToMcpToolType\(com.google.adk.tools.BaseTool\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Modifier and Type

Class

Description

`class `

`[BaseRetrievalTool](../retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")`

Base class for retrieval tools.

`class `

`[VertexAiRagRetrieval](../retrieval/VertexAiRagRetrieval.html "class in com.google.adk.tools.retrieval")`

A retrieval tool that fetches context from Vertex AI RAG.

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseTool](../BaseTool.html "class in com.google.adk.tools")>>`

AdkComponentProvider.`[getToolClasses](../../utils/AdkComponentProvider.html#getToolClasses\(\))()`

Returns a list of tool classes to register.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseTool](../BaseTool.html "class in com.google.adk.tools")>>`

CoreAdkComponentProvider.`[getToolClasses](../../utils/CoreAdkComponentProvider.html#getToolClasses\(\))()`

Returns tool classes for [`AgentTool`](../AgentTool.html "class in com.google.adk.tools"), [`LongRunningFunctionTool`](../LongRunningFunctionTool.html "class in com.google.adk.tools") and [`ExampleTool`](../ExampleTool.html "class in com.google.adk.tools").

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

AdditionalAdkComponentProvider.`[getToolInstances](../../utils/AdditionalAdkComponentProvider.html#getToolInstances\(\))()`

Returns tool instances for [`GoogleSearchTool`](../GoogleSearchTool.html "class in com.google.adk.tools") and [`GoogleMapsTool`](../GoogleMapsTool.html "class in com.google.adk.tools").

`default [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

AdkComponentProvider.`[getToolInstances](../../utils/AdkComponentProvider.html#getToolInstances\(\))()`

Returns a map of tool instances to register, with tool name as key.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

CoreAdkComponentProvider.`[getToolInstances](../../utils/CoreAdkComponentProvider.html#getToolInstances\(\))()`

Returns tool instances for [`LoadArtifactsTool`](../LoadArtifactsTool.html "class in com.google.adk.tools"), [`ExitLoopTool`](../ExitLoopTool.html "class in com.google.adk.tools") and [`UrlContextTool`](../UrlContextTool.html "class in com.google.adk.tools").

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseTool](../BaseTool.html "class in com.google.adk.tools")>>`

ComponentRegistry.`[resolveToolClass](../../utils/ComponentRegistry.html#resolveToolClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolClassName)`

Resolves the tool class based on the tool class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

ComponentRegistry.`[resolveToolInstance](../../utils/ComponentRegistry.html#resolveToolInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 




* * *

Copyright (C) 1980\. All rights reserved.
