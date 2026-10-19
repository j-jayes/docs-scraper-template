JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SequentialAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [SequentialAgent](SequentialAgent.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. runAsyncImpl(InvocationContext)
     3. runLiveImpl(InvocationContext)
     4. fromConfig(SequentialAgentConfig, String)

Hide sidebar  Show sidebar

# Class SequentialAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.workflow.BaseNode](../workflow/BaseNode.html "class in com.google.adk.workflow")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.SequentialAgent

All Implemented Interfaces:
    `[Node](../workflow/Node.html "interface in com.google.adk.workflow")`

* * *

public class SequentialAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially. 

**Composition with[`LlmAgent`](LlmAgent.html "class in com.google.adk.agents")s:** a `SequentialAgent` does not transfer control back to a parent [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents"). Use it as the root or transferred-to agent and place any follow-up [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents") as the next sibling. Upstream publishes via `outputKey` and downstream reads via `{key}` placeholders in its instruction: 
    
    
    var draft =
        LlmAgent.builder()
            .name("draft")
            .model("gemini-flash-latest")
            .instruction("Draft a summary.")
            .outputKey("draft")
            .build();
    var reviewer =
        LlmAgent.builder()
            .name("reviewer")
            .model("gemini-flash-latest")
            .instruction("Polish the draft: {draft}")
            .build();
    var pipeline =
        SequentialAgent.builder().name("pipeline").subAgents(draft, reviewer).build();
    

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`static [SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

`fromConfig([SequentialAgentConfig](SequentialAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a SequentialAgent from configuration.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially in live mode.

### Methods inherited from class [BaseAgent](BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [canonicalAfterAgentCallbacks](BaseAgent.html#canonicalAfterAgentCallbacks\(\) "canonicalAfterAgentCallbacks\(\)"), [canonicalBeforeAgentCallbacks](BaseAgent.html#canonicalBeforeAgentCallbacks\(\) "canonicalBeforeAgentCallbacks\(\)"), [close](BaseAgent.html#close\(\) "close\(\)"), [findAgent](BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [parentAgent](BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [runNode](BaseAgent.html#runNode\(com.google.adk.agents.Context,java.lang.Object\) "runNode\(Context, Object\)"), [subAgents](BaseAgent.html#subAgents\(\) "subAgents\(\)"), [toolOrigin](BaseAgent.html#toolOrigin\(\) "toolOrigin\(\)")`

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

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[findAgent](BaseAgent.html#findAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Recursively search sub agent by name.

`static [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`[fromConfig](BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

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

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runNode](BaseAgent.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs this agent as a workflow node through its [`BaseAgent.runAsync(InvocationContext)`](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\)) lifecycle, including its callbacks.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[subAgents](BaseAgent.html#subAgents\(\))()`

 

`[AgentEnums.AgentOrigin](../utils/AgentEnums.AgentOrigin.html "enum class in com.google.adk.utils")`

`[toolOrigin](BaseAgent.html#toolOrigin\(\))()`

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




  * ## Method Details

    * ### builder

public static [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") builder()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Runs sub-agents sequentially. 

Three modes: with resumability on, a resume fast-forwards to the checkpointed sub-agent and pauses on a long-running call; with the deprecated shim on, the same happens but the resume point is reconstructed from history and nothing is checkpointed; with neither, sub-agents just run in order.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable emitting events from sub-agents.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Runs sub-agents sequentially in live mode.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable emitting events from sub-agents in live mode.

    * ### fromConfig

public static [SequentialAgent](SequentialAgent.html "class in com.google.adk.agents") fromConfig([SequentialAgentConfig](SequentialAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Creates a SequentialAgent from configuration.

Parameters:
    `config` \- the agent configuration
    `configAbsPath` \- The absolute path to the agent config file.
Returns:
    the configured SequentialAgent
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the configuration is invalid




* * *

Copyright (C) 1980\. All rights reserved.
