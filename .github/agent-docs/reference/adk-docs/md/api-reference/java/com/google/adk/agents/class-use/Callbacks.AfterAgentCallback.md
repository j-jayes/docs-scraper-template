JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.AfterAgentCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
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

com.example

 

com.google.adk.a2a.agent

 

com.google.adk.agents

 

com.google.adk.utils

 

  * ## Uses of [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") in [com.example](../../../../example/package-summary.html)

Fields in [com.example](../../../../example/package-summary.html) declared as [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`static final [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[AFTER_AGENT_CALLBACK](../../../../example/CoreCallbacks.html#AFTER_AGENT_CALLBACK)`

 

`static final [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[AFTER_AGENT_CALLBACK1](../../../../example/CoreCallbacks.html#AFTER_AGENT_CALLBACK1)`

 

`static final [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[AFTER_AGENT_CALLBACK2](../../../../example/CoreCallbacks.html#AFTER_AGENT_CALLBACK2)`

 

`static final [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[AFTER_AGENT_CALLBACK3](../../../../example/CoreCallbacks.html#AFTER_AGENT_CALLBACK3)`

 

  * ## Uses of [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Method parameters in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) with type arguments of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[RemoteA2AAgent.Builder](../../a2a/agent/RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

RemoteA2AAgent.Builder.`[afterAgentCallback](../../a2a/agent/RemoteA2AAgent.Builder.html#afterAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

 

  * ## Uses of [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Fields in [com.google.adk.agents](../package-summary.html) with type parameters of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`protected com.google.common.collect.ImmutableList<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.Builder.`[afterAgentCallback](../BaseAgent.Builder.html#afterAgentCallback)`

 

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.`[afterAgentCallback](../BaseAgent.html#afterAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.`[canonicalAfterAgentCallbacks](../BaseAgent.html#canonicalAfterAgentCallbacks\(\))()`

The resolved afterAgentCallback field as a list.

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

CallbackUtil.`[getAfterAgentCallbacks](../CallbackUtil.html#getAfterAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

Normalizes after-agent callbacks.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[B](../BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder")`

BaseAgent.Builder.`[afterAgentCallback](../BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

  * ## Uses of [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

ComponentRegistry.`[resolveAfterAgentCallback](../../utils/ComponentRegistry.html#resolveAfterAgentCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 




* * *

Copyright (C) 1980\. All rights reserved.
