JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Package](package-summary.html)
  * Use
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)



# Uses of Package  
com.google.adk.agents

Packages that use [com.google.adk.agents](package-summary.html)

Package

Description

com.example

 

com.example.a2a_basic

 

com.example.helloworld

 

com.example.mcpfilesystem

 

com.google.adk.a2a.agent

 

com.google.adk.a2a.converters

 

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.codeexecutors

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.maven

 

com.google.adk.plugins

 

com.google.adk.runner

 

com.google.adk.samples.a2aagent.agent

 

com.google.adk.telemetry

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.computeruse

 

com.google.adk.tools.mcp

 

com.google.adk.tutorials

 

com.google.adk.utils

 

com.google.adk.web

 

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.example](../../../example/package-summary.html)

Class

Description

[Callbacks.AfterAgentCallback](class-use/Callbacks.AfterAgentCallback.html#com.example)

Async callback interface for actions to be performed after an agent has finished running.

[Callbacks.AfterModelCallback](class-use/Callbacks.AfterModelCallback.html#com.example)

 

[Callbacks.AfterToolCallback](class-use/Callbacks.AfterToolCallback.html#com.example)

Async callback interface for actions to be performed after a tool has been invoked.

[Callbacks.BeforeAgentCallback](class-use/Callbacks.BeforeAgentCallback.html#com.example)

Async callback interface for actions to be performed before an agent starts running.

[Callbacks.BeforeModelCallback](class-use/Callbacks.BeforeModelCallback.html#com.example)

 

[Callbacks.BeforeToolCallback](class-use/Callbacks.BeforeToolCallback.html#com.example)

Async callback interface for actions to be performed before a tool is invoked.

[LlmAgent](class-use/LlmAgent.html#com.example)

The LLM-based agent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.example.a2a_basic](../../../example/a2a_basic/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.example.a2a_basic)

Base class for all agents.

[LlmAgent](class-use/LlmAgent.html#com.example.a2a_basic)

The LLM-based agent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.example.helloworld](../../../example/helloworld/package-summary.html)

Class

Description

[LlmAgent](class-use/LlmAgent.html#com.example.helloworld)

The LLM-based agent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.example.mcpfilesystem](../../../example/mcpfilesystem/package-summary.html)

Class

Description

[LlmAgent](class-use/LlmAgent.html#com.example.mcpfilesystem)

The LLM-based agent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.a2a.agent](../a2a/agent/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.a2a.agent)

Base class for all agents.

[Callbacks.AfterAgentCallback](class-use/Callbacks.AfterAgentCallback.html#com.google.adk.a2a.agent)

Async callback interface for actions to be performed after an agent has finished running.

[Callbacks.BeforeAgentCallback](class-use/Callbacks.BeforeAgentCallback.html#com.google.adk.a2a.agent)

Async callback interface for actions to be performed before an agent starts running.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.a2a.agent)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.a2a.converters](../a2a/converters/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.a2a.converters)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.a2a.executor](../a2a/executor/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.a2a.executor)

Base class for all agents.

[RunConfig](class-use/RunConfig.html#com.google.adk.a2a.executor)

Configuration to modify an agent's LLM's underlying behavior.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.agents](package-summary.html)

Class

Description

[ActiveStreamingTool](class-use/ActiveStreamingTool.html#com.google.adk.agents)

Manages streaming tool related resources during invocation.

[BaseAgent](class-use/BaseAgent.html#com.google.adk.agents)

Base class for all agents.

[BaseAgent.Builder](class-use/BaseAgent.Builder.html#com.google.adk.agents)

Base Builder for all agents.

[BaseAgentConfig](class-use/BaseAgentConfig.html#com.google.adk.agents)

Base configuration for all agents with subagent support.

[BaseAgentConfig.AgentRefConfig](class-use/BaseAgentConfig.AgentRefConfig.html#com.google.adk.agents)

Configuration for referencing other agents (subagents).

[BaseAgentConfig.CallbackRef](class-use/BaseAgentConfig.CallbackRef.html#com.google.adk.agents)

Reference to a callback stored in the ComponentRegistry.

[CallbackContext](class-use/CallbackContext.html#com.google.adk.agents)

The context of various callbacks for an agent invocation.

[Callbacks.AfterAgentCallback](class-use/Callbacks.AfterAgentCallback.html#com.google.adk.agents)

Async callback interface for actions to be performed after an agent has finished running.

[Callbacks.AfterAgentCallbackSync](class-use/Callbacks.AfterAgentCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterAgentCallback.

[Callbacks.AfterModelCallback](class-use/Callbacks.AfterModelCallback.html#com.google.adk.agents)

 

[Callbacks.AfterModelCallbackSync](class-use/Callbacks.AfterModelCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterModelCallback.

[Callbacks.AfterToolCallback](class-use/Callbacks.AfterToolCallback.html#com.google.adk.agents)

Async callback interface for actions to be performed after a tool has been invoked.

[Callbacks.AfterToolCallbackSync](class-use/Callbacks.AfterToolCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterToolCallback.

[Callbacks.BeforeAgentCallback](class-use/Callbacks.BeforeAgentCallback.html#com.google.adk.agents)

Async callback interface for actions to be performed before an agent starts running.

[Callbacks.BeforeAgentCallbackSync](class-use/Callbacks.BeforeAgentCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeAgentCallback.

[Callbacks.BeforeModelCallback](class-use/Callbacks.BeforeModelCallback.html#com.google.adk.agents)

 

[Callbacks.BeforeModelCallbackSync](class-use/Callbacks.BeforeModelCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeModelCallback.

[Callbacks.BeforeToolCallback](class-use/Callbacks.BeforeToolCallback.html#com.google.adk.agents)

Async callback interface for actions to be performed before a tool is invoked.

[Callbacks.BeforeToolCallbackSync](class-use/Callbacks.BeforeToolCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeToolCallback.

[Callbacks.OnModelErrorCallback](class-use/Callbacks.OnModelErrorCallback.html#com.google.adk.agents)

Async callback interface for handling errors that occur during an LLM model call.

[Callbacks.OnModelErrorCallbackSync](class-use/Callbacks.OnModelErrorCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync onModelErrorCallback.

[Callbacks.OnToolErrorCallback](class-use/Callbacks.OnToolErrorCallback.html#com.google.adk.agents)

Async callback interface for handling errors that occur during a tool invocation.

[Callbacks.OnToolErrorCallbackSync](class-use/Callbacks.OnToolErrorCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync onToolErrorCallback.

[ConfigAgentUtils.ConfigurationException](class-use/ConfigAgentUtils.ConfigurationException.html#com.google.adk.agents)

Exception thrown when configuration is invalid.

[ContextCacheConfig](class-use/ContextCacheConfig.html#com.google.adk.agents)

Configuration for context caching across all agents in an app.

[Instruction](class-use/Instruction.html#com.google.adk.agents)

Represents an instruction that can be provided to an agent to guide its behavior.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.agents)

The context for an agent invocation.

[InvocationContext.Builder](class-use/InvocationContext.Builder.html#com.google.adk.agents)

Builder for [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

[LiveRequest](class-use/LiveRequest.html#com.google.adk.agents)

Represents a request to be sent to a live connection to the LLM model.

[LiveRequest.Builder](class-use/LiveRequest.Builder.html#com.google.adk.agents)

Builder for constructing [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") instances.

[LiveRequestQueue](class-use/LiveRequestQueue.html#com.google.adk.agents)

A queue of live requests to be sent to the model.

[LlmAgent](class-use/LlmAgent.html#com.google.adk.agents)

The LLM-based agent.

[LlmAgent.Builder](class-use/LlmAgent.Builder.html#com.google.adk.agents)

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

[LlmAgent.IncludeContents](class-use/LlmAgent.IncludeContents.html#com.google.adk.agents)

Enum to define if contents of previous events should be included in requests to the underlying LLM.

[LlmAgentConfig](class-use/LlmAgentConfig.html#com.google.adk.agents)

Configuration for LlmAgent.

[LoopAgent](class-use/LoopAgent.html#com.google.adk.agents)

An agent that runs its sub-agents sequentially in a loop.

[LoopAgent.Builder](class-use/LoopAgent.Builder.html#com.google.adk.agents)

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

[LoopAgentConfig](class-use/LoopAgentConfig.html#com.google.adk.agents)

Configuration for LoopAgent.

[ParallelAgent](class-use/ParallelAgent.html#com.google.adk.agents)

A shell agent that runs its sub-agents in parallel in isolated manner.

[ParallelAgent.Builder](class-use/ParallelAgent.Builder.html#com.google.adk.agents)

Builder for [`ParallelAgent`](ParallelAgent.html "class in com.google.adk.agents").

[ParallelAgentConfig](class-use/ParallelAgentConfig.html#com.google.adk.agents)

Configuration for ParallelAgent.

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.agents)

Provides read-only access to the context of an agent run.

[RunConfig](class-use/RunConfig.html#com.google.adk.agents)

Configuration to modify an agent's LLM's underlying behavior.

[RunConfig.Builder](class-use/RunConfig.Builder.html#com.google.adk.agents)

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

[RunConfig.StreamingMode](class-use/RunConfig.StreamingMode.html#com.google.adk.agents)

Streaming mode for the runner.

[RunConfig.ToolExecutionMode](class-use/RunConfig.ToolExecutionMode.html#com.google.adk.agents)

Tool execution mode for the runner, when they are multiple tools requested (by the models or callbacks).

[SequentialAgent](class-use/SequentialAgent.html#com.google.adk.agents)

An agent that runs its sub-agents sequentially.

[SequentialAgent.Builder](class-use/SequentialAgent.Builder.html#com.google.adk.agents)

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

[SequentialAgentConfig](class-use/SequentialAgentConfig.html#com.google.adk.agents)

Configuration for SequentialAgent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.apps](../apps/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.apps)

Base class for all agents.

[ContextCacheConfig](class-use/ContextCacheConfig.html#com.google.adk.apps)

Configuration for context caching across all agents in an app.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.codeexecutors](../codeexecutors/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.codeexecutors)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.flows](../flows/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.flows)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.flows.llmflows](../flows/llmflows/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.flows.llmflows)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.maven](../maven/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.maven)

Base class for all agents.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.plugins](../plugins/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.plugins)

Base class for all agents.

[CallbackContext](class-use/CallbackContext.html#com.google.adk.plugins)

The context of various callbacks for an agent invocation.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.plugins)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.runner](../runner/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.runner)

Base class for all agents.

[ContextCacheConfig](class-use/ContextCacheConfig.html#com.google.adk.runner)

Configuration for context caching across all agents in an app.

[LiveRequestQueue](class-use/LiveRequestQueue.html#com.google.adk.runner)

A queue of live requests to be sent to the model.

[RunConfig](class-use/RunConfig.html#com.google.adk.runner)

Configuration to modify an agent's LLM's underlying behavior.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.samples.a2aagent.agent](../samples/a2aagent/agent/package-summary.html)

Class

Description

[LlmAgent](class-use/LlmAgent.html#com.google.adk.samples.a2aagent.agent)

The LLM-based agent.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.telemetry](../telemetry/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.telemetry)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools](../tools/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.tools)

Base class for all agents.

[CallbackContext](class-use/CallbackContext.html#com.google.adk.tools)

The context of various callbacks for an agent invocation.

[ConfigAgentUtils.ConfigurationException](class-use/ConfigAgentUtils.ConfigurationException.html#com.google.adk.tools)

Exception thrown when configuration is invalid.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.tools)

The context for an agent invocation.

[LlmAgent](class-use/LlmAgent.html#com.google.adk.tools)

The LLM-based agent.

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools.applicationintegrationtoolset](../tools/applicationintegrationtoolset/package-summary.html)

Class

Description

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools.applicationintegrationtoolset)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools.computeruse](../tools/computeruse/package-summary.html)

Class

Description

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools.computeruse)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools.mcp](../tools/mcp/package-summary.html)

Class

Description

[ConfigAgentUtils.ConfigurationException](class-use/ConfigAgentUtils.ConfigurationException.html#com.google.adk.tools.mcp)

Exception thrown when configuration is invalid.

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools.mcp)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tutorials](../tutorials/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.tutorials)

Base class for all agents.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.utils](../utils/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.utils)

Base class for all agents.

[Callbacks.AfterAgentCallback](class-use/Callbacks.AfterAgentCallback.html#com.google.adk.utils)

Async callback interface for actions to be performed after an agent has finished running.

[Callbacks.AfterModelCallback](class-use/Callbacks.AfterModelCallback.html#com.google.adk.utils)

 

[Callbacks.AfterToolCallback](class-use/Callbacks.AfterToolCallback.html#com.google.adk.utils)

Async callback interface for actions to be performed after a tool has been invoked.

[Callbacks.BeforeAgentCallback](class-use/Callbacks.BeforeAgentCallback.html#com.google.adk.utils)

Async callback interface for actions to be performed before an agent starts running.

[Callbacks.BeforeModelCallback](class-use/Callbacks.BeforeModelCallback.html#com.google.adk.utils)

 

[Callbacks.BeforeToolCallback](class-use/Callbacks.BeforeToolCallback.html#com.google.adk.utils)

Async callback interface for actions to be performed before a tool is invoked.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.utils)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.web](../web/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.web)

Base class for all agents.




* * *

Copyright (C) 1980\. All rights reserved.
