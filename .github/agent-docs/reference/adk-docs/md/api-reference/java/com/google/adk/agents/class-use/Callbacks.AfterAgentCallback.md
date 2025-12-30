JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.AfterAgentCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [Callbacks](../Callbacks.html)
  3. [AfterAgentCallback](../Callbacks.AfterAgentCallback.html)



# Uses of Interface  
com.google.adk.agents.Callbacks.AfterAgentCallback

Packages that use [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>>`

BaseAgent.`[afterAgentCallback](../BaseAgent.html#afterAgentCallback\(\))()`

 

`static @Nullable com.google.common.collect.ImmutableList<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

CallbackUtil.`[getAfterAgentCallbacks](../CallbackUtil.html#getAfterAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

Normalizes after-agent callbacks.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[afterAgentCallback](../LlmAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[LoopAgent.Builder](../LoopAgent.Builder.html "class in com.google.adk.agents")`

LoopAgent.Builder.`[afterAgentCallback](../LoopAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[ParallelAgent.Builder](../ParallelAgent.Builder.html "class in com.google.adk.agents")`

ParallelAgent.Builder.`[afterAgentCallback](../ParallelAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[SequentialAgent.Builder](../SequentialAgent.Builder.html "class in com.google.adk.agents")`

SequentialAgent.Builder.`[afterAgentCallback](../SequentialAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 




* * *

Copyright (C) 2025\. All rights reserved.
