JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CallbackPlugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [CallbackPlugin](CallbackPlugin.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. getName()
     2. getBeforeAgentCallback()
     3. getAfterAgentCallback()
     4. getBeforeModelCallback()
     5. getAfterModelCallback()
     6. getBeforeToolCallback()
     7. getAfterToolCallback()
     8. builder()

Hide sidebar  Show sidebar

# Class CallbackPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.plugins.PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins")

com.google.adk.agents.CallbackPlugin

All Implemented Interfaces:
    `[Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")`

* * *

public class CallbackPlugin extends [PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins")

A plugin that wraps callbacks and exposes them as a plugin.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

Builder for [`CallbackPlugin`](CallbackPlugin.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`getAfterAgentCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

`getAfterModelCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>`

`getAfterToolCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`getBeforeAgentCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>`

`getBeforeModelCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

`getBeforeToolCallback()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getName()`

 

### Methods inherited from class [PluginManager](../plugins/PluginManager.html#method-summary "class in com.google.adk.plugins")

`[afterAgentCallback](../plugins/PluginManager.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "afterAgentCallback\(BaseAgent, CallbackContext\)"), [afterModelCallback](../plugins/PluginManager.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\) "afterModelCallback\(CallbackContext, LlmResponse\)"), [afterRunCallback](../plugins/PluginManager.html#afterRunCallback\(com.google.adk.agents.InvocationContext\) "afterRunCallback\(InvocationContext\)"), [afterToolCallback](../plugins/PluginManager.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\) "afterToolCallback\(BaseTool, Map, ToolContext, Map\)"), [beforeAgentCallback](../plugins/PluginManager.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "beforeAgentCallback\(BaseAgent, CallbackContext\)"), [beforeModelCallback](../plugins/PluginManager.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\) "beforeModelCallback\(CallbackContext, LlmRequest.Builder\)"), [beforeRunCallback](../plugins/PluginManager.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\) "beforeRunCallback\(InvocationContext\)"), [beforeToolCallback](../plugins/PluginManager.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\) "beforeToolCallback\(BaseTool, Map, ToolContext\)"), [getPlugin](../plugins/PluginManager.html#getPlugin\(java.lang.String\) "getPlugin\(String\)"), [onEventCallback](../plugins/PluginManager.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\) "onEventCallback\(InvocationContext, Event\)"), [onModelErrorCallback](../plugins/PluginManager.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\) "onModelErrorCallback\(CallbackContext, LlmRequest.Builder, Throwable\)"), [onToolErrorCallback](../plugins/PluginManager.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\) "onToolErrorCallback\(BaseTool, Map, ToolContext, Throwable\)"), [onUserMessageCallback](../plugins/PluginManager.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\) "onUserMessageCallback\(InvocationContext, Content\)"), [registerPlugin](../plugins/PluginManager.html#registerPlugin\(com.google.adk.plugins.Plugin\) "registerPlugin\(Plugin\)"), [runAfterAgentCallback](../plugins/PluginManager.html#runAfterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "runAfterAgentCallback\(BaseAgent, CallbackContext\)"), [runAfterModelCallback](../plugins/PluginManager.html#runAfterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\) "runAfterModelCallback\(CallbackContext, LlmResponse\)"), [runAfterRunCallback](../plugins/PluginManager.html#runAfterRunCallback\(com.google.adk.agents.InvocationContext\) "runAfterRunCallback\(InvocationContext\)"), [runAfterToolCallback](../plugins/PluginManager.html#runAfterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\) "runAfterToolCallback\(BaseTool, Map, ToolContext, Map\)"), [runBeforeAgentCallback](../plugins/PluginManager.html#runBeforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "runBeforeAgentCallback\(BaseAgent, CallbackContext\)"), [runBeforeModelCallback](../plugins/PluginManager.html#runBeforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\) "runBeforeModelCallback\(CallbackContext, LlmRequest.Builder\)"), [runBeforeRunCallback](../plugins/PluginManager.html#runBeforeRunCallback\(com.google.adk.agents.InvocationContext\) "runBeforeRunCallback\(InvocationContext\)"), [runBeforeToolCallback](../plugins/PluginManager.html#runBeforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\) "runBeforeToolCallback\(BaseTool, Map, ToolContext\)"), [runOnEventCallback](../plugins/PluginManager.html#runOnEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\) "runOnEventCallback\(InvocationContext, Event\)"), [runOnModelErrorCallback](../plugins/PluginManager.html#runOnModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\) "runOnModelErrorCallback\(CallbackContext, LlmRequest.Builder, Throwable\)"), [runOnToolErrorCallback](../plugins/PluginManager.html#runOnToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\) "runOnToolErrorCallback\(BaseTool, Map, ToolContext, Throwable\)"), [runOnUserMessageCallback](../plugins/PluginManager.html#runOnUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\) "runOnUserMessageCallback\(InvocationContext, Content\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### getName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getName()

Specified by:
    `[getName](../plugins/Plugin.html#getName\(\))` in interface `[Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")`
Overrides:
    `[getName](../plugins/PluginManager.html#getName\(\))` in class `[PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins")`

    * ### getBeforeAgentCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> getBeforeAgentCallback()

    * ### getAfterAgentCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> getAfterAgentCallback()

    * ### getBeforeModelCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")> getBeforeModelCallback()

    * ### getAfterModelCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")> getAfterModelCallback()

    * ### getBeforeToolCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")> getBeforeToolCallback()

    * ### getAfterToolCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")> getAfterToolCallback()

    * ### builder

public static [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") builder()




* * *

Copyright (C) 1980\. All rights reserved.
