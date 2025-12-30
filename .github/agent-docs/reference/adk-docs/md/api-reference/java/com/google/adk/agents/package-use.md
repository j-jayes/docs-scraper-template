JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Package](package-summary.html)
  * Use
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)



# Uses of Package  
com.google.adk.agents

Packages that use [com.google.adk.agents](package-summary.html)

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.flows

 

com.google.adk.flows.llmflows

 

com.google.adk.runner

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.mcp

 

com.google.adk.utils

 

com.google.adk.web

 

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk](../package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.agents](package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.agents)

Base class for all agents.

[BaseAgentConfig](class-use/BaseAgentConfig.html#com.google.adk.agents)

Base configuration for all agents.

[CallbackContext](class-use/CallbackContext.html#com.google.adk.agents)

The context of various callbacks for an agent invocation.

[Callbacks.AfterAgentCallback](class-use/Callbacks.AfterAgentCallback.html#com.google.adk.agents)

 

[Callbacks.AfterAgentCallbackSync](class-use/Callbacks.AfterAgentCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterAgentCallback.

[Callbacks.AfterModelCallback](class-use/Callbacks.AfterModelCallback.html#com.google.adk.agents)

 

[Callbacks.AfterModelCallbackSync](class-use/Callbacks.AfterModelCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterModelCallback.

[Callbacks.AfterToolCallback](class-use/Callbacks.AfterToolCallback.html#com.google.adk.agents)

 

[Callbacks.AfterToolCallbackSync](class-use/Callbacks.AfterToolCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync afterToolCallback.

[Callbacks.BeforeAgentCallback](class-use/Callbacks.BeforeAgentCallback.html#com.google.adk.agents)

 

[Callbacks.BeforeAgentCallbackSync](class-use/Callbacks.BeforeAgentCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeAgentCallback.

[Callbacks.BeforeModelCallback](class-use/Callbacks.BeforeModelCallback.html#com.google.adk.agents)

 

[Callbacks.BeforeModelCallbackSync](class-use/Callbacks.BeforeModelCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeModelCallback.

[Callbacks.BeforeToolCallback](class-use/Callbacks.BeforeToolCallback.html#com.google.adk.agents)

 

[Callbacks.BeforeToolCallbackSync](class-use/Callbacks.BeforeToolCallbackSync.html#com.google.adk.agents)

Helper interface to allow for sync beforeToolCallback.

[Instruction](class-use/Instruction.html#com.google.adk.agents)

Represents an instruction that can be provided to an agent to guide its behavior.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.agents)

The context for an agent invocation.

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

[LoopAgent](class-use/LoopAgent.html#com.google.adk.agents)

An agent that runs its sub-agents sequentially in a loop.

[LoopAgent.Builder](class-use/LoopAgent.Builder.html#com.google.adk.agents)

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

[ParallelAgent](class-use/ParallelAgent.html#com.google.adk.agents)

A shell agent that runs its sub-agents in parallel in isolated manner.

[ParallelAgent.Builder](class-use/ParallelAgent.Builder.html#com.google.adk.agents)

Builder for [`ParallelAgent`](ParallelAgent.html "class in com.google.adk.agents").

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.agents)

Provides read-only access to the context of an agent run.

[RunConfig](class-use/RunConfig.html#com.google.adk.agents)

Configuration to modify an agent's LLM's underlying behavior.

[RunConfig.Builder](class-use/RunConfig.Builder.html#com.google.adk.agents)

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

[RunConfig.StreamingMode](class-use/RunConfig.StreamingMode.html#com.google.adk.agents)

Streaming mode for the runner.

[SequentialAgent](class-use/SequentialAgent.html#com.google.adk.agents)

An agent that runs its sub-agents sequentially.

[SequentialAgent.Builder](class-use/SequentialAgent.Builder.html#com.google.adk.agents)

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

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

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.runner](../runner/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.runner)

Base class for all agents.

[LiveRequestQueue](class-use/LiveRequestQueue.html#com.google.adk.runner)

A queue of live requests to be sent to the model.

[RunConfig](class-use/RunConfig.html#com.google.adk.runner)

Configuration to modify an agent's LLM's underlying behavior.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools](../tools/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.tools)

Base class for all agents.

[CallbackContext](class-use/CallbackContext.html#com.google.adk.tools)

The context of various callbacks for an agent invocation.

[InvocationContext](class-use/InvocationContext.html#com.google.adk.tools)

The context for an agent invocation.

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools.applicationintegrationtoolset](../tools/applicationintegrationtoolset/package-summary.html)

Class

Description

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools.applicationintegrationtoolset)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.tools.mcp](../tools/mcp/package-summary.html)

Class

Description

[ReadonlyContext](class-use/ReadonlyContext.html#com.google.adk.tools.mcp)

Provides read-only access to the context of an agent run.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.utils](../utils/package-summary.html)

Class

Description

[InvocationContext](class-use/InvocationContext.html#com.google.adk.utils)

The context for an agent invocation.

  * Classes in [com.google.adk.agents](package-summary.html) used by [com.google.adk.web](../web/package-summary.html)

Class

Description

[BaseAgent](class-use/BaseAgent.html#com.google.adk.web)

Base class for all agents.




* * *

Copyright (C) 2025\. All rights reserved.
