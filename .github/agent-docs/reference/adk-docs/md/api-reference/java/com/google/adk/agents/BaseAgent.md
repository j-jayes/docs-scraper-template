JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [BaseAgent](BaseAgent.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BaseNode
     2. Methods inherited from class Object
     3. Methods inherited from interface Node
  5. Constructor Details
     1. BaseAgent(String, String, List, List, List)
  6. Method Details
     1. close()
     2. parentAgent()
     3. parentAgent(BaseAgent)
     4. rootAgent()
     5. findAgent(String)
     6. findSubAgent(String)
     7. subAgents()
     8. beforeAgentCallback()
     9. afterAgentCallback()
     10. toolOrigin()
     11. canonicalBeforeAgentCallbacks()
     12. canonicalAfterAgentCallbacks()
     13. runAsync(InvocationContext)
     14. runLive(InvocationContext)
     15. runNode(Context, Object)
     16. runAsyncImpl(InvocationContext)
     17. runLiveImpl(InvocationContext)
     18. fromConfig(BaseAgentConfig, String)

Hide sidebar  Show sidebar

# Class BaseAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.workflow.BaseNode](../workflow/BaseNode.html "class in com.google.adk.workflow")

com.google.adk.agents.BaseAgent

All Implemented Interfaces:
    `[Node](../workflow/Node.html "interface in com.google.adk.workflow")`

Direct Known Subclasses:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents"), [LoopAgent](LoopAgent.html "class in com.google.adk.agents"), [ParallelAgent](ParallelAgent.html "class in com.google.adk.agents"), [PlannerAgent](PlannerAgent.html "class in com.google.adk.agents"), [RemoteA2AAgent](../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent"), [SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

* * *

public abstract class BaseAgent extends [BaseNode](../workflow/BaseNode.html "class in com.google.adk.workflow")

Base class for all agents.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[B](BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder") extends [BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[B](BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder")>>`

Base Builder for all agents.

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

Creates a new BaseAgent.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`afterAgentCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`beforeAgentCallback()`

 

`com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`canonicalAfterAgentCallbacks()`

The resolved afterAgentCallback field as a list.

`com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`canonicalBeforeAgentCallbacks()`

The resolved beforeAgentCallback field as a list.

`io.reactivex.rxjava3.core.Completable`

`close()`

Closes all sub-agents.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`findSubAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Recursively search sub agent by name.

`static [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`fromConfig([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`parentAgent()`

Retrieves the parent agent in the agent tree.

`protected void`

`parentAgent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") parentAgent)`

Sets the parent agent.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`rootAgent()`

Returns the root agent for this agent by traversing up the parent chain.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent asynchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)`

Runs the agent synchronously.

`protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runNode([Context](Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs this agent as a workflow node through its `runAsync(InvocationContext)` lifecycle, including its callbacks.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`subAgents()`

 

`[AgentEnums.AgentOrigin](../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils")`

`toolOrigin()`

Returns the origin of the tool when this agent is used as a tool.

### Methods inherited from class [BaseNode](../workflow/BaseNode.html#method-summary "class in com.google.adk.workflow")

`[config](../workflow/BaseNode.html#config\(\) "config\(\)"), [description](../workflow/BaseNode.html#description\(\) "description\(\)"), [inputSchema](../workflow/BaseNode.html#inputSchema\(\) "inputSchema\(\)"), [name](../workflow/BaseNode.html#name\(\) "name\(\)"), [outputSchema](../workflow/BaseNode.html#outputSchema\(\) "outputSchema\(\)"), [rerunOnResume](../workflow/BaseNode.html#rerunOnResume\(\) "rerunOnResume\(\)"), [stateSchema](../workflow/BaseNode.html#stateSchema\(\) "stateSchema\(\)"), [waitForOutput](../workflow/BaseNode.html#waitForOutput\(\) "waitForOutput\(\)")`

Modifier and Type

Method

Description

`[NodeConfig](../workflow/NodeConfig.html "class in com.google.adk.workflow")`

`[config](../workflow/BaseNode.html#config\(\))()`

Returns the node's retry policy and execution timeout.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](../workflow/BaseNode.html#description\(\))()`

Returns what the node does, for humans and for a model that may call it.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[inputSchema](../workflow/BaseNode.html#inputSchema\(\))()`

Returns the schema the node's input must match.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](../workflow/BaseNode.html#name\(\))()`

Returns the name that identifies the node within its graph.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[outputSchema](../workflow/BaseNode.html#outputSchema\(\))()`

Returns the schema that the node's output value must match.

`boolean`

`[rerunOnResume](../workflow/BaseNode.html#rerunOnResume\(\))()`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[stateSchema](../workflow/BaseNode.html#stateSchema\(\))()`

Returns the schema declaring the state keys the node uses.

`boolean`

`[waitForOutput](../workflow/BaseNode.html#waitForOutput\(\))()`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Node](../workflow/Node.html#method-summary "interface in com.google.adk.workflow")

`[requiresAllPredecessors](../workflow/Node.html#requiresAllPredecessors\(\) "requiresAllPredecessors\(\)")`

Modifier and Type

Method

Description

`default boolean`

`[requiresAllPredecessors](../workflow/Node.html#requiresAllPredecessors\(\))()`

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.




  * ## Constructor Details

    * ### BaseAgent

public BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)

Creates a new BaseAgent.

Parameters:
    `name` \- Unique agent name. Cannot be "user" (reserved).
    `description` \- Agent purpose; null is treated as an empty string.
    `subAgents` \- Agents managed by this agent.
    `beforeAgentCallback` \- Callbacks before agent execution. Invoked in order until one doesn't return null.
    `afterAgentCallback` \- Callbacks after agent execution. Invoked in order until one doesn't return null.

  * ## Method Details

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Closes all sub-agents.

Returns:
    a `Completable` that completes when all sub-agents are closed.

    * ### parentAgent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") parentAgent()

Retrieves the parent agent in the agent tree.

Returns:
    the parent agent, or `null` if this agent does not have a parent.

    * ### parentAgent

protected void parentAgent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") parentAgent)

Sets the parent agent.

Parameters:
    `parentAgent` \- The parent agent to set.

    * ### rootAgent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") rootAgent()

Returns the root agent for this agent by traversing up the parent chain.

Returns:
    the root agent.

    * ### findAgent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Finds an agent (this or descendant) by name.

Returns:
    an [`Optional`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util") containing the agent or descendant with the given name, or [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\)) if not found.

    * ### findSubAgent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> findSubAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Recursively search sub agent by name.

Returns:
    an [`Optional`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util") containing the sub agent with the given name, or [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\)) if not found.

    * ### subAgents

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents()

    * ### beforeAgentCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback()

    * ### afterAgentCallback

public com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback()

    * ### toolOrigin

public [AgentEnums.AgentOrigin](../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils") toolOrigin()

Returns the origin of the tool when this agent is used as a tool.

Returns:
    the tool origin, defaults to "BASE_AGENT".

    * ### canonicalBeforeAgentCallbacks

public com.google.common.collect.ImmutableList<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> canonicalBeforeAgentCallbacks()

The resolved beforeAgentCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalAfterAgentCallbacks

public com.google.common.collect.ImmutableList<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> canonicalAfterAgentCallbacks()

The resolved afterAgentCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)

Runs the agent asynchronously.

Parameters:
    `parentContext` \- Parent context to inherit.
Returns:
    stream of agent-generated events.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([InvocationContext](InvocationContext.html "class in com.google.adk.agents") parentContext)

Runs the agent synchronously.

Parameters:
    `parentContext` \- Parent context to inherit.
Returns:
    stream of agent-generated events.

    * ### runNode

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runNode([Context](Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)

Runs this agent as a workflow node through its `runAsync(InvocationContext)` lifecycle, including its callbacks. The node input is not used.

    * ### runAsyncImpl

protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Agent-specific asynchronous logic.

Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected abstract io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Agent-specific synchronous logic.

Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### fromConfig

public static [BaseAgent](BaseAgent.html "class in com.google.adk.agents") fromConfig([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)

Creates a new agent instance from a configuration object.

Parameters:
    `config` \- Agent configuration.
    `configAbsPath` \- Absolute path to the configuration file.
Returns:
    new agent instance.




* * *

Copyright (C) 1980\. All rights reserved.
