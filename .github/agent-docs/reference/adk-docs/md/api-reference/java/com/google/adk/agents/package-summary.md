JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.agents

* * *

package com.google.adk.agents

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesEnum ClassesRecord ClassesException Classes

Class

Description

[ActiveStreamingTool](ActiveStreamingTool.html "class in com.google.adk.agents")

Manages streaming tool related resources during invocation.

[BaseAgent](BaseAgent.html "class in com.google.adk.agents")

Base class for all agents.

[BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<B extends [BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<B>>

Base Builder for all agents.

[BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

Base configuration for all agents with subagent support.

[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")

Configuration for referencing other agents (subagents).

[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")

Reference to a callback stored in the ComponentRegistry.

[CallbackContext](CallbackContext.html "class in com.google.adk.agents")

The context of various callbacks for an agent invocation.

[Callbacks](Callbacks.html "class in com.google.adk.agents")

Functional interfaces for agent lifecycle callbacks.

[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

Async callback interface for actions to be performed after an agent has finished running.

[Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterAgentCallback.

[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterModelCallback.

[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")

Async callback interface for actions to be performed after a tool has been invoked.

[Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterToolCallback.

[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

Async callback interface for actions to be performed before an agent starts running.

[Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeAgentCallback.

[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeModelCallback.

[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

Async callback interface for actions to be performed before a tool is invoked.

[Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeToolCallback.

[Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")

Async callback interface for handling errors that occur during an LLM model call.

[Callbacks.OnModelErrorCallbackSync](Callbacks.OnModelErrorCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync onModelErrorCallback.

[Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")

Async callback interface for handling errors that occur during a tool invocation.

[Callbacks.OnToolErrorCallbackSync](Callbacks.OnToolErrorCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync onToolErrorCallback.

[CallbackUtil](CallbackUtil.html "class in com.google.adk.agents")

Utility methods for normalizing agent callbacks.

[ConfigAgentUtils](ConfigAgentUtils.html "class in com.google.adk.agents")

Utility class for loading agent configurations from YAML files.

[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Exception thrown when configuration is invalid.

[ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents")

Configuration for context caching across all agents in an app.

[Instruction](Instruction.html "interface in com.google.adk.agents")

Represents an instruction that can be provided to an agent to guide its behavior.

[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")

Returns an instruction dynamically constructed from the given context.

[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")

Plain instruction directly provided to the agent.

[InvocationContext](InvocationContext.html "class in com.google.adk.agents")

The context for an agent invocation.

[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")

Builder for [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

[LiveRequest](LiveRequest.html "class in com.google.adk.agents")

Represents a request to be sent to a live connection to the LLM model.

[LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")

Builder for constructing [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") instances.

[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")

A queue of live requests to be sent to the model.

[LlmAgent](LlmAgent.html "class in com.google.adk.agents")

The LLM-based agent.

[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")

Enum to define if contents of previous events should be included in requests to the underlying LLM.

[LlmAgentConfig](LlmAgentConfig.html "class in com.google.adk.agents")

Configuration for LlmAgent.

[LoopAgent](LoopAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially in a loop.

[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

[LoopAgentConfig](LoopAgentConfig.html "class in com.google.adk.agents")

Configuration for LoopAgent.

[ParallelAgent](ParallelAgent.html "class in com.google.adk.agents")

A shell agent that runs its sub-agents in parallel in isolated manner.

[ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents")

Builder for [`ParallelAgent`](ParallelAgent.html "class in com.google.adk.agents").

[ParallelAgentConfig](ParallelAgentConfig.html "class in com.google.adk.agents")

Configuration for ParallelAgent.

[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

Provides read-only access to the context of an agent run.

[RunConfig](RunConfig.html "class in com.google.adk.agents")

Configuration to modify an agent's LLM's underlying behavior.

[RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")

Streaming mode for the runner.

[RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents")

Tool execution mode for the runner, when they are multiple tools requested (by the models or callbacks).

[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially.

[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

[SequentialAgentConfig](SequentialAgentConfig.html "class in com.google.adk.agents")

Configuration for SequentialAgent.




* * *

Copyright (C) 1980\. All rights reserved.
