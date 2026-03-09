JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.AfterModelCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [Callbacks](../Callbacks.html)
  3. [AfterModelCallback](../Callbacks.AfterModelCallback.html)



# Uses of Interface  
com.google.adk.agents.Callbacks.AfterModelCallback

Packages that use [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

Package

Description

com.example

 

com.google.adk.agents

 

com.google.adk.utils

 

  * ## Uses of [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") in [com.example](../../../../example/package-summary.html)

Fields in [com.example](../../../../example/package-summary.html) declared as [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`static final [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[AFTER_MODEL_CALLBACK](../../../../example/CoreCallbacks.html#AFTER_MODEL_CALLBACK)`

 

  * ## Uses of [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>>`

LlmAgent.`[afterModelCallback](../LlmAgent.html#afterModelCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

CallbackPlugin.`[getAfterModelCallback](../CallbackPlugin.html#getAfterModelCallback\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[CallbackPlugin.Builder](../CallbackPlugin.Builder.html "class in com.google.adk.agents")`

CallbackPlugin.Builder.`[addAfterModelCallback](../CallbackPlugin.Builder.html#addAfterModelCallback\(com.google.adk.agents.Callbacks.AfterModelCallback\))([Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") callback)`

 

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[afterModelCallback](../LlmAgent.Builder.html#afterModelCallback\(com.google.adk.agents.Callbacks.AfterModelCallback\))([Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") afterModelCallback)`

 

  * ## Uses of [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Callbacks.AfterModelCallback](../Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

ComponentRegistry.`[resolveAfterModelCallback](../../utils/ComponentRegistry.html#resolveAfterModelCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 




* * *

Copyright (C) 1980\. All rights reserved.
