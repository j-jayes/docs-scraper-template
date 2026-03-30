JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RemoteA2AAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.agent](package-summary.html)
  2. [RemoteA2AAgent](RemoteA2AAgent.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. isStreaming()
     3. runAsyncImpl(InvocationContext)
     4. runLiveImpl(InvocationContext)

Hide sidebar  Show sidebar

# Class RemoteA2AAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")

com.google.adk.a2a.agent.RemoteA2AAgent

* * *

public class RemoteA2AAgent extends [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")

Agent that communicates with a remote A2A agent via an A2A client. 

The remote agent can be specified directly by providing an `AgentCard` to the builder, or it can be resolved automatically using the provided A2A client. 

Key responsibilities of this agent include: 

  * Agent card resolution and validation 
  * Converting ADK session history events into A2A requests (`Message`) 
  * Handling streaming and non-streaming responses from the A2A client 
  * Buffering and aggregating streamed response chunks into ADK [`Event`](../../events/Event.html "class in com.google.adk.events")s 
  * Converting A2A client responses back into ADK format 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[RemoteA2AAgent.AgentCardResolutionError](RemoteA2AAgent.AgentCardResolutionError.html "class in com.google.adk.a2a.agent")`

Exception thrown when the agent card cannot be resolved.

`static class `

`[RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

Builder for [`RemoteA2AAgent`](RemoteA2AAgent.html "class in com.google.adk.a2a.agent").

`static class `

`[RemoteA2AAgent.TypeError](RemoteA2AAgent.TypeError.html "class in com.google.adk.a2a.agent")`

Exception thrown when a type error occurs.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

`builder()`

 

`boolean`

`isStreaming()`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

### Methods inherited from class [BaseAgent](../../agents/BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](../../agents/BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](../../agents/BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [canonicalAfterAgentCallbacks](../../agents/BaseAgent.html#canonicalAfterAgentCallbacks\(\) "canonicalAfterAgentCallbacks\(\)"), [canonicalBeforeAgentCallbacks](../../agents/BaseAgent.html#canonicalBeforeAgentCallbacks\(\) "canonicalBeforeAgentCallbacks\(\)"), [close](../../agents/BaseAgent.html#close\(\) "close\(\)"), [description](../../agents/BaseAgent.html#description\(\) "description\(\)"), [findAgent](../../agents/BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](../../agents/BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](../../agents/BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [name](../../agents/BaseAgent.html#name\(\) "name\(\)"), [parentAgent](../../agents/BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](../../agents/BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](../../agents/BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](../../agents/BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](../../agents/BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [subAgents](../../agents/BaseAgent.html#subAgents\(\) "subAgents\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### builder

public static [RemoteA2AAgent.Builder](RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent") builder()

    * ### isStreaming

public boolean isStreaming()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](../../agents/BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific asynchronous logic.

Specified by:
    `[runAsyncImpl](../../agents/BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](../../agents/BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific synchronous logic.

Specified by:
    `[runLiveImpl](../../agents/BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.




* * *

Copyright (C) 1980\. All rights reserved.
