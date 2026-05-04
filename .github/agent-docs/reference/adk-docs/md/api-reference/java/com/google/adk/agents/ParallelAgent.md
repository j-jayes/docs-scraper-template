JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ParallelAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [ParallelAgent](ParallelAgent.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. fromConfig(ParallelAgentConfig, String)
     3. runAsyncImpl(InvocationContext)
     4. runLiveImpl(InvocationContext)

Hide sidebar  Show sidebar

# Class ParallelAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.ParallelAgent

* * *

public class ParallelAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

A shell agent that runs its sub-agents in parallel in isolated manner. 

This approach is beneficial for scenarios requiring multiple perspectives or attempts on a single task, such as running different algorithms simultaneously or generating multiple responses for review by a subsequent evaluation agent.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`ParallelAgent`](ParallelAgent.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`static [ParallelAgent](ParallelAgent.html "class in com.google.adk.agents")`

`fromConfig([ParallelAgentConfig](ParallelAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a ParallelAgent from configuration.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents in parallel and emits their events.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Not supported for ParallelAgent.

### Methods inherited from class [BaseAgent](BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [canonicalAfterAgentCallbacks](BaseAgent.html#canonicalAfterAgentCallbacks\(\) "canonicalAfterAgentCallbacks\(\)"), [canonicalBeforeAgentCallbacks](BaseAgent.html#canonicalBeforeAgentCallbacks\(\) "canonicalBeforeAgentCallbacks\(\)"), [close](BaseAgent.html#close\(\) "close\(\)"), [description](BaseAgent.html#description\(\) "description\(\)"), [findAgent](BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [name](BaseAgent.html#name\(\) "name\(\)"), [parentAgent](BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [subAgents](BaseAgent.html#subAgents\(\) "subAgents\(\)"), [toolOrigin](BaseAgent.html#toolOrigin\(\) "toolOrigin\(\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\))()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[canonicalAfterAgentCallbacks](BaseAgent.html#canonicalAfterAgentCallbacks\(\))()`

The resolved afterAgentCallback field as a list.

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[canonicalBeforeAgentCallbacks](BaseAgent.html#canonicalBeforeAgentCallbacks\(\))()`

The resolved beforeAgentCallback field as a list.

`io.reactivex.rxjava3.core.Completable`

`[close](BaseAgent.html#close\(\))()`

Closes all sub-agents.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](BaseAgent.html#description\(\))()`

Gets the one-line description of the agent's capability.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[findAgent](BaseAgent.html#findAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Recursively search sub agent by name.

`static [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`[fromConfig](BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BaseAgent.html#name\(\))()`

Gets the agent's unique name.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`[parentAgent](BaseAgent.html#parentAgent\(\))()`

Retrieves the parent agent in the agent tree.

`protected void`

`[parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\))([BaseAgent](BaseAgent.html "class in com.google.adk.agents") parentAgent)`

Sets the parent agent.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`[rootAgent](BaseAgent.html#rootAgent\(\))()`

Returns the root agent for this agent by traversing up the parent chain.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\))([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent asynchronously.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent synchronously.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[subAgents](BaseAgent.html#subAgents\(\))()`

 

`[AgentEnums.AgentOrigin](../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils")`

`[toolOrigin](BaseAgent.html#toolOrigin\(\))()`

Returns the origin of the tool when this agent is used as a tool.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### builder

public static [ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents") builder()

    * ### fromConfig

public static [ParallelAgent](ParallelAgent.html "class in com.google.adk.agents") fromConfig([ParallelAgentConfig](ParallelAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Creates a ParallelAgent from configuration.

Parameters:
    `config` \- the agent configuration
    `configAbsPath` \- The absolute path to the agent config file.
Returns:
    the configured ParallelAgent
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the configuration is invalid

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Runs sub-agents in parallel and emits their events. 

Sets the branch and merges event streams from all sub-agents.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable emitting events from all sub-agents.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Not supported for ParallelAgent.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable that always throws UnsupportedOperationException.




* * *

Copyright (C) 1980\. All rights reserved.
