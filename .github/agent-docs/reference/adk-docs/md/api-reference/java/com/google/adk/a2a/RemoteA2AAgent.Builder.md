JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RemoteA2AAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.a2a](package-summary.html)
  2. [RemoteA2AAgent](RemoteA2AAgent.html)
  3. [Builder](RemoteA2AAgent.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. name(String)
     2. agentCardOrSource(Object)
     3. description(String)
     4. a2aClient(A2AClient)
     5. subAgents(List)
     6. beforeAgentCallback(List)
     7. afterAgentCallback(List)
     8. build()

Hide sidebar  Show sidebar

# Class RemoteA2AAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.RemoteA2AAgent.Builder

Enclosing class:
    `[RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a")`

* * *

public static class RemoteA2AAgent.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`RemoteA2AAgent`](RemoteA2AAgent.html "class in com.google.adk.a2a").

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

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`a2aClient(@Nullable [A2AClient](A2AClient.html "class in com.google.adk.a2a") a2aClient)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`agentCardOrSource([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") agentCardOrSource)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback)`

 

`[RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a")`

`build()`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### agentCardOrSource

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") agentCardOrSource([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") agentCardOrSource)

    * ### description

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### a2aClient

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") a2aClient(@Nullable [A2AClient](A2AClient.html "class in com.google.adk.a2a") a2aClient)

    * ### subAgents

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)

    * ### build

public [RemoteA2AAgent](RemoteA2AAgent.html "class in com.google.adk.a2a") build()




* * *

Copyright (C) 1980\. All rights reserved.
