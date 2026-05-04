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
  5. Constructor Details
     1. BaseAgent(String, String, List, List, List)
  6. Method Details
     1. close()
     2. name()
     3. description()
     4. parentAgent()
     5. parentAgent(BaseAgent)
     6. rootAgent()
     7. findAgent(String)
     8. findSubAgent(String)
     9. subAgents()
     10. beforeAgentCallback()
     11. afterAgentCallback()
     12. toolOrigin()
     13. canonicalBeforeAgentCallbacks()
     14. canonicalAfterAgentCallbacks()
     15. runAsync(InvocationContext)
     16. runLive(InvocationContext)
     17. runAsyncImpl(InvocationContext)
     18. runLiveImpl(InvocationContext)
     19. fromConfig(BaseAgentConfig, String)

Hide sidebar  Show sidebar

# Class BaseAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.BaseAgent

Direct Known Subclasses:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents"), [LoopAgent](LoopAgent.html "class in com.google.adk.agents"), [ParallelAgent](ParallelAgent.html "class in com.google.adk.agents"), [PlannerAgent](PlannerAgent.html "class in com.google.adk.agents"), [RemoteA2AAgent](../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent"), [SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

* * *

public abstract class BaseAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

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

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`description()`

Gets the one-line description of the agent's capability.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`findSubAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Recursively search sub agent by name.

`static [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`fromConfig([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

Gets the agent's unique name.

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

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`subAgents()`

 

`[AgentEnums.AgentOrigin](../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils")`

`toolOrigin()`

Returns the origin of the tool when this agent is used as a tool.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### BaseAgent

public BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)

Creates a new BaseAgent.

Parameters:
    `name` \- Unique agent name. Cannot be "user" (reserved).
    `description` \- Agent purpose.
    `subAgents` \- Agents managed by this agent.
    `beforeAgentCallback` \- Callbacks before agent execution. Invoked in order until one doesn't return null.
    `afterAgentCallback` \- Callbacks after agent execution. Invoked in order until one doesn't return null.

  * ## Method Details

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Closes all sub-agents.

Returns:
    a `Completable` that completes when all sub-agents are closed.

    * ### name

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

Gets the agent's unique name.

Returns:
    the unique name of the agent.

    * ### description

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description()

Gets the one-line description of the agent's capability.

Returns:
    the description of the agent.

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
