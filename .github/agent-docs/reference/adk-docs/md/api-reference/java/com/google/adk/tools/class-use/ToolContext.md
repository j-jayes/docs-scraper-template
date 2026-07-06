JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ToolContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](../package-summary.html)
  2. [ToolContext](../ToolContext.html)



# Uses of Class  
com.google.adk.tools.ToolContext

Packages that use [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Package

Description

com.example

 

com.example.a2a_basic

 

com.example.helloworld

 

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.computeruse

 

com.google.adk.tools.mcp

 

com.google.adk.tools.retrieval

 

com.google.adk.tools.skills

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.example](../../../../example/package-summary.html)

Methods in [com.example](../../../../example/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

CustomDieTool.`[rollDie](../../../../example/CustomDieTool.html#rollDie\(int,com.google.adk.tools.ToolContext\))(int sides, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.example.a2a_basic](../../../../example/a2a_basic/package-summary.html)

Methods in [com.example.a2a_basic](../../../../example/a2a_basic/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

A2AAgent.`[rollDie](../../../../example/a2a_basic/A2AAgent.html#rollDie\(int,com.google.adk.tools.ToolContext\))(int sides, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.example.helloworld](../../../../example/helloworld/package-summary.html)

Methods in [com.example.helloworld](../../../../example/helloworld/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

HelloWorldAgent.`[rollDie](../../../../example/helloworld/HelloWorldAgent.html#rollDie\(int,com.google.adk.tools.ToolContext\))(int sides, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.AfterToolCallback.`[call](../../agents/Callbacks.AfterToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") response)`

Async callback after tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.AfterToolCallbackSync.`[call](../../agents/Callbacks.AfterToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") response)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.BeforeToolCallback.`[call](../../agents/Callbacks.BeforeToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Async callback before tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.BeforeToolCallbackSync.`[call](../../agents/Callbacks.BeforeToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.OnToolErrorCallback.`[call](../../agents/Callbacks.OnToolErrorCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Async callback when tool call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Callbacks.OnToolErrorCallbackSync.`[call](../../agents/Callbacks.OnToolErrorCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Exception\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static void`

AgentTransfer.`[transferToAgent](../../flows/llmflows/AgentTransfer.html#transferToAgent\(java.lang.String,com.google.adk.tools.ToolContext\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

LoggingPlugin.`[afterToolCallback](../../plugins/LoggingPlugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Plugin.`[afterToolCallback](../../plugins/Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

Callback executed after a tool has been called.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

PluginManager.`[afterToolCallback](../../plugins/PluginManager.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

LoggingPlugin.`[beforeToolCallback](../../plugins/LoggingPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Plugin.`[beforeToolCallback](../../plugins/Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

PluginManager.`[beforeToolCallback](../../plugins/PluginManager.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

ReplayPlugin.`[beforeToolCallback](../../plugins/ReplayPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

LoggingPlugin.`[onToolErrorCallback](../../plugins/LoggingPlugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

Plugin.`[onToolErrorCallback](../../plugins/Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a tool call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

PluginManager.`[onToolErrorCallback](../../plugins/PluginManager.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[afterToolCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[beforeToolCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BigQueryAgentAnalyticsPlugin.`[onToolErrorCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Methods in [com.google.adk.tools](../package-summary.html) that return [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`[ToolContext](../ToolContext.html "class in com.google.adk.tools")`

ToolContext.Builder.`[build](../ToolContext.Builder.html#build\(\))()`

 

Methods in [com.google.adk.tools](../package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[appendArtifactsToLlmRequest](../LoadArtifactsTool.html#appendArtifactsToLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

FunctionTool.`[callLive](../FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`static void`

ExitLoopTool.`[exitLoop](../ExitLoopTool.html#exitLoop\(com.google.adk.tools.ToolContext\))([ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Exit the [`LoopAgent`](../../agents/LoopAgent.html "class in com.google.adk.agents") execution.

`static io.reactivex.rxjava3.core.Single<[LoadMemoryResponse](../LoadMemoryResponse.html "class in com.google.adk.tools")>`

LoadMemoryTool.`[loadMemory](../LoadMemoryTool.html#loadMemory\(java.lang.String,com.google.adk.tools.ToolContext\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") query, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Loads the memory for the current user.

`io.reactivex.rxjava3.core.Completable`

BaseTool.`[processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`default io.reactivex.rxjava3.core.Completable`

BaseToolset.`[processLlmRequest](../BaseToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`io.reactivex.rxjava3.core.Completable`

BuiltInCodeExecutionTool.`[processLlmRequest](../BuiltInCodeExecutionTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

ExampleTool.`[processLlmRequest](../ExampleTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleMapsTool.`[processLlmRequest](../GoogleMapsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleSearchTool.`[processLlmRequest](../GoogleSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[processLlmRequest](../LoadArtifactsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadMemoryTool.`[processLlmRequest](../LoadMemoryTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

UrlContextTool.`[processLlmRequest](../UrlContextTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

VertexAiSearchTool.`[processLlmRequest](../VertexAiSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

AgentTool.`[runAsync](../AgentTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments, returning the results converted to a specified class.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool with generic arguments and returns a map of results.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

FunctionTool.`[runAsync](../FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

LoadArtifactsTool.`[runAsync](../LoadArtifactsTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

SetModelResponseTool.`[runAsync](../SetModelResponseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Methods in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

IntegrationConnectorTool.`[runAsync](../applicationintegrationtoolset/IntegrationConnectorTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.computeruse](../computeruse/package-summary.html)

Methods in [com.google.adk.tools.computeruse](../computeruse/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

ComputerUseToolset.`[processLlmRequest](../computeruse/ComputerUseToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Adds computer use configuration to the LLM request.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

ComputerUseTool.`[runAsync](../computeruse/ComputerUseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

McpAsyncTool.`[runAsync](../mcp/McpAsyncTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

McpTool.`[runAsync](../mcp/McpTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Methods in [com.google.adk.tools.retrieval](../retrieval/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

VertexAiRagRetrieval.`[processLlmRequest](../retrieval/VertexAiRagRetrieval.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

VertexAiRagRetrieval.`[runAsync](../retrieval/VertexAiRagRetrieval.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.skills](../skills/package-summary.html)

Methods in [com.google.adk.tools.skills](../skills/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

SkillToolset.`[processLlmRequest](../skills/SkillToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 




* * *

Copyright (C) 1980\. All rights reserved.
