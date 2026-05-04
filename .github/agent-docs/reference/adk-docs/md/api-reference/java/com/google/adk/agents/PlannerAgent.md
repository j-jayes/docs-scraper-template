JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PlannerAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [PlannerAgent](PlannerAgent.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. planner()
     2. maxIterations()
     3. runAsyncImpl(InvocationContext)
     4. runLiveImpl(InvocationContext)
     5. builder()

Hide sidebar  Show sidebar

# Class PlannerAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.PlannerAgent

* * *

public class PlannerAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

An agent that delegates execution planning to a [`Planner`](Planner.html "interface in com.google.adk.agents") strategy. 

The `PlannerAgent` owns a set of sub-agents and a planner. At runtime, the planner inspects session state and decides which sub-agent(s) to run next. This enables dynamic, goal-oriented agent orchestration — the execution topology is determined at runtime rather than being fixed at build time. 

The planning loop: 

  1. Planner is initialized with context and available agents 
  2. Planner returns what to do next via [`PlannerAction`](PlannerAction.html "interface in com.google.adk.agents")
  3. Selected sub-agent(s) execute, producing events 
  4. Session state (world state) is updated from events 
  5. Planner sees updated state and decides the next action 
  6. Repeat until [`PlannerAction.Done`](PlannerAction.Done.html "class in com.google.adk.agents") or maxIterations 


Example usage with a custom planner: 
    
    
    PlannerAgent agent = PlannerAgent.builder()
        .name("myAgent")
        .subAgents(agentA, agentB, agentC)
        .planner(new GoalOrientedPlanner("finalOutput", metadata))
        .maxIterations(20)
        .build();
    

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[PlannerAgent.Builder](PlannerAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`PlannerAgent`](PlannerAgent.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [PlannerAgent.Builder](PlannerAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

Returns a new [`PlannerAgent.Builder`](PlannerAgent.Builder.html "class in com.google.adk.agents") for creating [`PlannerAgent`](PlannerAgent.html "class in com.google.adk.agents") instances.

`int`

`maxIterations()`

Returns the maximum number of planning iterations.

`[Planner](Planner.html "interface in com.google.adk.agents")`

`planner()`

Returns the planner strategy used by this agent.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

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

    * ### planner

public [Planner](Planner.html "interface in com.google.adk.agents") planner()

Returns the planner strategy used by this agent.

    * ### maxIterations

public int maxIterations()

Returns the maximum number of planning iterations.

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific asynchronous logic.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific synchronous logic.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### builder

public static [PlannerAgent.Builder](PlannerAgent.Builder.html "class in com.google.adk.agents") builder()

Returns a new [`PlannerAgent.Builder`](PlannerAgent.Builder.html "class in com.google.adk.agents") for creating [`PlannerAgent`](PlannerAgent.html "class in com.google.adk.agents") instances.




* * *

Copyright (C) 1980\. All rights reserved.
