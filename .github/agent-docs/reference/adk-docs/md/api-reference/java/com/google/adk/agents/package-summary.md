JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)



Contents

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Related Packages
  3. Classes and Interfaces



# Package com.google.adk.agents

* * *

package com.google.adk.agents

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesEnum ClassesRecord Classes

Class

Description

[BaseAgent](BaseAgent.html "class in com.google.adk.agents")

Base class for all agents.

[BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

Base configuration for all agents.

[CallbackContext](CallbackContext.html "class in com.google.adk.agents")

The context of various callbacks for an agent invocation.

[Callbacks](Callbacks.html "class in com.google.adk.agents")

Functional interfaces for agent lifecycle callbacks.

[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterAgentCallback.

[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterModelCallback.

[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")

 

[Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync afterToolCallback.

[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeAgentCallback.

[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeModelCallback.

[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")

 

[Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")

Helper interface to allow for sync beforeToolCallback.

[CallbackUtil](CallbackUtil.html "class in com.google.adk.agents")

Utility methods for normalizing agent callbacks.

[Instruction](Instruction.html "interface in com.google.adk.agents")

Represents an instruction that can be provided to an agent to guide its behavior.

[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")

Returns an instruction dynamically constructed from the given context.

[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")

Plain instruction directly provided to the agent.

[InvocationContext](InvocationContext.html "class in com.google.adk.agents")

The context for an agent invocation.

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

[ParallelAgent](ParallelAgent.html "class in com.google.adk.agents")

A shell agent that runs its sub-agents in parallel in isolated manner.

[ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents")

Builder for [`ParallelAgent`](ParallelAgent.html "class in com.google.adk.agents").

[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

Provides read-only access to the context of an agent run.

[RunConfig](RunConfig.html "class in com.google.adk.agents")

Configuration to modify an agent's LLM's underlying behavior.

[RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")

Streaming mode for the runner.

[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially.

[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").




* * *

Copyright (C) 2025\. All rights reserved.
