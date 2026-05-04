JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RemoteA2AAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.agent](package-summary.html)
  2. [RemoteA2AAgent](RemoteA2AAgent.html)
  3. [Builder](RemoteA2AAgent.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. streaming(boolean)
     2. name(String)
     3. agentCard(AgentCard)
     4. description(String)
     5. subAgents(List)
     6. beforeAgentCallback(List)
     7. afterAgentCallback(List)
     8. a2aClient(Client)
     9. build()

Hide sidebar  Show sidebar

# Class RemoteA2AAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.a2a.agent.RemoteA2AAgent.Builder

Enclosing class:
    `[RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a.agent")`

* * *

public static class RemoteA2AAgent.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`RemoteA2AAgent`](RemoteA2AAgent.html "class in com.google.adk.a2a.agent").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`a2aClient(io.a2a.client.Client a2aClient)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.AfterAgentCallback](../../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`agentCard(io.a2a.spec.AgentCard agentCard)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.BeforeAgentCallback](../../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback)`

 

`[RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a.agent")`

`build()`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`streaming(boolean streaming)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### streaming

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") streaming(boolean streaming)

    * ### name

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### agentCard

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") agentCard(io.a2a.spec.AgentCard agentCard)

    * ### description

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

    * ### subAgents

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.BeforeAgentCallback](../../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Callbacks.AfterAgentCallback](../../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)

    * ### a2aClient

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") a2aClient(io.a2a.client.Client a2aClient)

    * ### build

public [RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a.agent") build()




* * *

Copyright (C) 1980\. All rights reserved.
