JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Callbacks.BeforeAgentCallback.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [Callbacks](../Callbacks.html)
  3. [BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html)



# Uses of Interface  
com.google.adk.agents.Callbacks.BeforeAgentCallback

Packages that use [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Package

Description

com.example

 

com.google.adk.a2a.agent

 

com.google.adk.agents

 

com.google.adk.utils

 

  * ## Uses of [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") in [com.example](../../../../example/package-summary.html)

Fields in [com.example](../../../../example/package-summary.html) declared as [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`static final [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_AGENT_CALLBACK](../../../../example/CoreCallbacks.html#BEFORE_AGENT_CALLBACK)`

 

`static final [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_AGENT_CALLBACK1](../../../../example/CoreCallbacks.html#BEFORE_AGENT_CALLBACK1)`

 

`static final [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_AGENT_CALLBACK2](../../../../example/CoreCallbacks.html#BEFORE_AGENT_CALLBACK2)`

 

`static final [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")`

CoreCallbacks.`[BEFORE_AGENT_CALLBACK3](../../../../example/CoreCallbacks.html#BEFORE_AGENT_CALLBACK3)`

 

  * ## Uses of [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Method parameters in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) with type arguments of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[RemoteA2AAgent.Builder](../../a2a/agent/RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

RemoteA2AAgent.Builder.`[beforeAgentCallback](../../a2a/agent/RemoteA2AAgent.Builder.html#beforeAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback)`

 

  * ## Uses of [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Fields in [com.google.adk.agents](../package-summary.html) with type parameters of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Field

Description

`protected com.google.common.collect.ImmutableList<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.Builder.`[beforeAgentCallback](../BaseAgent.Builder.html#beforeAgentCallback)`

 

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.`[beforeAgentCallback](../BaseAgent.html#beforeAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

BaseAgent.`[canonicalBeforeAgentCallbacks](../BaseAgent.html#canonicalBeforeAgentCallbacks\(\))()`

The resolved beforeAgentCallback field as a list.

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

CallbackUtil.`[getBeforeAgentCallbacks](../CallbackUtil.html#getBeforeAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallbacks)`

Normalizes before-agent callbacks.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[B](../BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder")`

BaseAgent.Builder.`[beforeAgentCallback](../BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

  * ## Uses of [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

ComponentRegistry.`[resolveBeforeAgentCallback](../../utils/ComponentRegistry.html#resolveBeforeAgentCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 




* * *

Copyright (C) 1980\. All rights reserved.
