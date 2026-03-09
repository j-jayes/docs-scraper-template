JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.BeforeToolCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [Callbacks](../Callbacks.html)
  3. [BeforeToolCallback](../Callbacks.BeforeToolCallback.html)



# Uses of Interface  
com.google.adk.agents.Callbacks.BeforeToolCallback

Packages that use [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Package

Description

com.example

 

com.google.adk.agents

 

com.google.adk.utils

 

  * ## Uses of [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") in [com.example](../../../../example/package-summary.html)

Fields in [com.example](../../../../example/package-summary.html) declared as [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`static final [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_TOOL_CALLBACK1](../../../../example/CoreCallbacks.html#BEFORE_TOOL_CALLBACK1)`

 

`static final [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_TOOL_CALLBACK2](../../../../example/CoreCallbacks.html#BEFORE_TOOL_CALLBACK2)`

 

`static final [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_TOOL_CALLBACK3](../../../../example/CoreCallbacks.html#BEFORE_TOOL_CALLBACK3)`

 

  * ## Uses of [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>>`

LlmAgent.`[beforeToolCallback](../LlmAgent.html#beforeToolCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

CallbackPlugin.`[getBeforeToolCallback](../CallbackPlugin.html#getBeforeToolCallback\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[CallbackPlugin.Builder](../CallbackPlugin.Builder.html "class in com.google.adk.agents")`

CallbackPlugin.Builder.`[addBeforeToolCallback](../CallbackPlugin.Builder.html#addBeforeToolCallback\(com.google.adk.agents.Callbacks.BeforeToolCallback\))([Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") callback)`

 

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[beforeToolCallback](../LlmAgent.Builder.html#beforeToolCallback\(com.google.adk.agents.Callbacks.BeforeToolCallback\))([Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)`

 

  * ## Uses of [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Callbacks.BeforeToolCallback](../Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

ComponentRegistry.`[resolveBeforeToolCallback](../../utils/ComponentRegistry.html#resolveBeforeToolCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 




* * *

Copyright (C) 1980\. All rights reserved.
