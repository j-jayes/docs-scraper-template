JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.BeforeAgentCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [Callbacks](../Callbacks.html)
  3. [BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html)



# Uses of Interface  
com.google.adk.agents.Callbacks.BeforeAgentCallback

Packages that use [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>>`

BaseAgent.`[beforeAgentCallback](../BaseAgent.html#beforeAgentCallback\(\))()`

 

`static @Nullable com.google.common.collect.ImmutableList<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

CallbackUtil.`[getBeforeAgentCallbacks](../CallbackUtil.html#getBeforeAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

Normalizes before-agent callbacks.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[beforeAgentCallback](../LlmAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[LoopAgent.Builder](../LoopAgent.Builder.html "class in com.google.adk.agents")`

LoopAgent.Builder.`[beforeAgentCallback](../LoopAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[ParallelAgent.Builder](../ParallelAgent.Builder.html "class in com.google.adk.agents")`

ParallelAgent.Builder.`[beforeAgentCallback](../ParallelAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[SequentialAgent.Builder](../SequentialAgent.Builder.html "class in com.google.adk.agents")`

SequentialAgent.Builder.`[beforeAgentCallback](../SequentialAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 




* * *

Copyright (C) 2025\. All rights reserved.
