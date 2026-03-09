JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RemoteA2AAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.a2a](package-summary.html)
  2. [RemoteA2AAgent](RemoteA2AAgent.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Constructor Details
     1. RemoteA2AAgent()
  7. Method Details
     1. builder()
     2. rpcUrl()
     3. runAsyncImpl(InvocationContext)
     4. runLiveImpl(InvocationContext)

Hide sidebar  Show sidebar

# Class RemoteA2AAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")

com.google.adk.a2a.RemoteA2AAgent

* * *

public class RemoteA2AAgent extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")

Agent that communicates with a remote A2A agent via A2A client. 

This agent supports multiple ways to specify the remote agent: 

  1. Direct AgentCard object 
  2. URL to agent card JSON 
  3. File path to agent card JSON 


The agent handles: 

  * Agent card resolution and validation 
  * A2A message conversion and error handling 
  * Session state management across requests 


**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[RemoteA2AAgent.A2AClientError](RemoteA2AAgent.A2AClientError.html "class in com.google.adk.a2a")`

Exception thrown when the A2A client encounters an error.

`static class `

`[RemoteA2AAgent.AgentCardResolutionError](RemoteA2AAgent.AgentCardResolutionError.html "class in com.google.adk.a2a")`

Exception thrown when the agent card cannot be resolved.

`static class `

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

Builder for [`RemoteA2AAgent`](RemoteA2AAgent.html "class in com.google.adk.a2a").

`static class `

`[RemoteA2AAgent.TypeError](RemoteA2AAgent.TypeError.html "class in com.google.adk.a2a")`

Exception thrown when a type error occurs.

  * ## Field Summary

### Fields inherited from class [BaseAgent](../agents/BaseAgent.html#field-summary "class in com.google.adk.agents")

`[callbackPlugin](../agents/BaseAgent.html#callbackPlugin)`

  * ## Constructor Summary

Constructors

Constructor

Description

`RemoteA2AAgent()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a")`

`builder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`rpcUrl()`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

### Methods inherited from class [BaseAgent](../agents/BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](../agents/BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](../agents/BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [description](../agents/BaseAgent.html#description\(\) "description\(\)"), [findAgent](../agents/BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](../agents/BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](../agents/BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [getPlugin](../agents/BaseAgent.html#getPlugin\(\) "getPlugin\(\)"), [name](../agents/BaseAgent.html#name\(\) "name\(\)"), [parentAgent](../agents/BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](../agents/BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](../agents/BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](../agents/BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](../agents/BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [subAgents](../agents/BaseAgent.html#subAgents\(\) "subAgents\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### RemoteA2AAgent

public RemoteA2AAgent()

  * ## Method Details

    * ### builder

public static [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a") builder()

    * ### rpcUrl

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> rpcUrl()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](../agents/BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific asynchronous logic.

Specified by:
    `[runAsyncImpl](../agents/BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](../agents/BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific synchronous logic.

Specified by:
    `[runLiveImpl](../agents/BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.




* * *

Copyright (C) 1980\. All rights reserved.
