JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RemoteA2AAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     5. toolOrigin()

Hide sidebar  Show sidebar

# Class RemoteA2AAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`[AgentEnums.AgentOrigin](../../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils")`

`toolOrigin()`

Returns the origin of the tool when this agent is used as a tool.

### Methods inherited from class [BaseAgent](../../agents/BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](../../agents/BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](../../agents/BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [canonicalAfterAgentCallbacks](../../agents/BaseAgent.html#canonicalAfterAgentCallbacks\(\) "canonicalAfterAgentCallbacks\(\)"), [canonicalBeforeAgentCallbacks](../../agents/BaseAgent.html#canonicalBeforeAgentCallbacks\(\) "canonicalBeforeAgentCallbacks\(\)"), [close](../../agents/BaseAgent.html#close\(\) "close\(\)"), [description](../../agents/BaseAgent.html#description\(\) "description\(\)"), [findAgent](../../agents/BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](../../agents/BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](../../agents/BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [name](../../agents/BaseAgent.html#name\(\) "name\(\)"), [parentAgent](../../agents/BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](../../agents/BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](../../agents/BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](../../agents/BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](../../agents/BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [subAgents](../../agents/BaseAgent.html#subAgents\(\) "subAgents\(\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](../../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[afterAgentCallback](../../agents/BaseAgent.html#afterAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](../../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[beforeAgentCallback](../../agents/BaseAgent.html#beforeAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](../../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[canonicalAfterAgentCallbacks](../../agents/BaseAgent.html#canonicalAfterAgentCallbacks\(\))()`

The resolved afterAgentCallback field as a list.

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](../../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[canonicalBeforeAgentCallbacks](../../agents/BaseAgent.html#canonicalBeforeAgentCallbacks\(\))()`

The resolved beforeAgentCallback field as a list.

`io.reactivex.rxjava3.core.Completable`

`[close](../../agents/BaseAgent.html#close\(\))()`

Closes all sub-agents.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](../../agents/BaseAgent.html#description\(\))()`

Gets the one-line description of the agent's capability.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")>`

`[findAgent](../../agents/BaseAgent.html#findAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")>`

`[findSubAgent](../../agents/BaseAgent.html#findSubAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Recursively search sub agent by name.

`static [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`

`[fromConfig](../../agents/BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgentConfig](../../agents/BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](../../agents/BaseAgent.html#name\(\))()`

Gets the agent's unique name.

`[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`

`[parentAgent](../../agents/BaseAgent.html#parentAgent\(\))()`

Retrieves the parent agent in the agent tree.

`protected void`

`[parentAgent](../../agents/BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") parentAgent)`

Sets the parent agent.

`[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`

`[rootAgent](../../agents/BaseAgent.html#rootAgent\(\))()`

Returns the root agent for this agent by traversing up the parent chain.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`[runAsync](../../agents/BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent asynchronously.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`[runLive](../../agents/BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent synchronously.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")>`

`[subAgents](../../agents/BaseAgent.html#subAgents\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




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

    * ### toolOrigin

public [AgentEnums.AgentOrigin](../../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils") toolOrigin()

Description copied from class: `[BaseAgent](../../agents/BaseAgent.html#toolOrigin\(\))`

Returns the origin of the tool when this agent is used as a tool.

Overrides:
    `[toolOrigin](../../agents/BaseAgent.html#toolOrigin\(\))` in class `[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`
Returns:
    the tool origin, defaults to "BASE_AGENT".




* * *

Copyright (C) 1980\. All rights reserved.
