JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseAgent.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [BaseAgent](BaseAgent.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseAgent(String, String, List, List, List)
  5. Method Details
     1. name()
     2. description()
     3. parentAgent()
     4. parentAgent(BaseAgent)
     5. rootAgent()
     6. findAgent(String)
     7. findSubAgent(String)
     8. subAgents()
     9. beforeAgentCallback()
     10. afterAgentCallback()
     11. runAsync(InvocationContext)
     12. runLive(InvocationContext)
     13. runAsyncImpl(InvocationContext)
     14. runLiveImpl(InvocationContext)



# Class BaseAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.BaseAgent

Direct Known Subclasses:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`, `[LoopAgent](LoopAgent.html "class in com.google.adk.agents")`, `[ParallelAgent](ParallelAgent.html "class in com.google.adk.agents")`, `[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

* * *

public abstract class BaseAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Base class for all agents.

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

Creates a new BaseAgent.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>>`

`afterAgentCallback()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>>`

`beforeAgentCallback()`

 

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`description()`

Gets the one-line description of the agent's capability.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Finds an agent (this or descendant) by name.

`@Nullable [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`findSubAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Recursively search sub agent by name.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

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

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`subAgents()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseAgent

public BaseAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)

Creates a new BaseAgent.

Parameters:
    `name` \- Unique agent name. Cannot be "user" (reserved).
    `description` \- Agent purpose.
    `subAgents` \- Agents managed by this agent.
    `beforeAgentCallback` \- Callbacks before agent execution. Invoked in order until one doesn't return null.
    `afterAgentCallback` \- Callbacks after agent execution. Invoked in order until one doesn't return null.

  * ## Method Details

    * ### name

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name()

Gets the agent's unique name.

Returns:
    the unique name of the agent.

    * ### description

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description()

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

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Finds an agent (this or descendant) by name.

Returns:
    the agent or descendant with the given name, or `null` if not found.

    * ### findSubAgent

public @Nullable [BaseAgent](BaseAgent.html "class in com.google.adk.agents") findSubAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Recursively search sub agent by name.

    * ### subAgents

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents()

    * ### beforeAgentCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>> beforeAgentCallback()

    * ### afterAgentCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>> afterAgentCallback()

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




* * *

Copyright (C) 2025\. All rights reserved.
