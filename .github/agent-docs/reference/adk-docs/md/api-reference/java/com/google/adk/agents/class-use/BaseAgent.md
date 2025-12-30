JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseAgent.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [BaseAgent](../BaseAgent.html)



# Uses of Class  
com.google.adk.agents.BaseAgent

Packages that use [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.runner

 

com.google.adk.tools

 

com.google.adk.web

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Subclasses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[LlmAgent](../LlmAgent.html "class in com.google.adk.agents")`

The LLM-based agent.

`class `

`[LoopAgent](../LoopAgent.html "class in com.google.adk.agents")`

An agent that runs its sub-agents sequentially in a loop.

`class `

`[ParallelAgent](../ParallelAgent.html "class in com.google.adk.agents")`

A shell agent that runs its sub-agents in parallel in isolated manner.

`class `

`[SequentialAgent](../SequentialAgent.html "class in com.google.adk.agents")`

An agent that runs its sub-agents sequentially.

Methods in [com.google.adk.agents](../package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

InvocationContext.`[agent](../InvocationContext.html#agent\(\))()`

 

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[findAgent](../BaseAgent.html#findAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Finds an agent (this or descendant) by name.

`@Nullable [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[findSubAgent](../BaseAgent.html#findSubAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Recursively search sub agent by name.

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[parentAgent](../BaseAgent.html#parentAgent\(\))()`

Retrieves the parent agent in the agent tree.

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[rootAgent](../BaseAgent.html#rootAgent\(\))()`

Returns the root agent for this agent by traversing up the parent chain.

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

BaseAgent.`[subAgents](../BaseAgent.html#subAgents\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`void`

InvocationContext.`[agent](../InvocationContext.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`protected void`

BaseAgent.`[parentAgent](../BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") parentAgent)`

Sets the parent agent.

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[subAgents](../LlmAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[LoopAgent.Builder](../LoopAgent.Builder.html "class in com.google.adk.agents")`

LoopAgent.Builder.`[subAgents](../LoopAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[ParallelAgent.Builder](../ParallelAgent.Builder.html "class in com.google.adk.agents")`

ParallelAgent.Builder.`[subAgents](../ParallelAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[SequentialAgent.Builder](../SequentialAgent.Builder.html "class in com.google.adk.agents")`

SequentialAgent.Builder.`[subAgents](../SequentialAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

Method parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[subAgents](../LlmAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

`[LoopAgent.Builder](../LoopAgent.Builder.html "class in com.google.adk.agents")`

LoopAgent.Builder.`[subAgents](../LoopAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

`[ParallelAgent.Builder](../ParallelAgent.Builder.html "class in com.google.adk.agents")`

ParallelAgent.Builder.`[subAgents](../ParallelAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

`[SequentialAgent.Builder](../SequentialAgent.Builder.html "class in com.google.adk.agents")`

SequentialAgent.Builder.`[subAgents](../SequentialAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

Constructor parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[BaseAgent](../BaseAgent.html#%3Cinit%3E\(java.lang.String,java.lang.String,java.util.List,java.util.List,java.util.List\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

Creates a new BaseAgent.

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

Runner.`[agent](../../runner/Runner.html#agent\(\))()`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Creates a new `Runner`.

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [AgentTool](../../tools/AgentTool.html "class in com.google.adk.tools")`

AgentTool.`[create](../../tools/AgentTool.html#create\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

`static [AgentTool](../../tools/AgentTool.html "class in com.google.adk.tools")`

AgentTool.`[create](../../tools/AgentTool.html#create\(com.google.adk.agents.BaseAgent,boolean\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)`

 

Constructors in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

`protected `

`[AgentTool](../../tools/AgentTool.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,boolean\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return types with arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

AgentCompilerLoader.`[loadAgents](../../web/AgentCompilerLoader.html#loadAgents\(\))()`

Discovers, compiles, and loads agents from the configured source directory.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

AdkWebServer.`[loadedAgentRegistry](../../web/AdkWebServer.html#loadedAgentRegistry\(com.google.adk.web.AgentCompilerLoader,com.google.adk.web.config.AgentLoadingProperties\))([AgentCompilerLoader](../../web/AgentCompilerLoader.html "class in com.google.adk.web") loader, [AgentLoadingProperties](../../web/config/AgentLoadingProperties.html "class in com.google.adk.web.config") props)`

 

Methods in [com.google.adk.web](../../web/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

AgentGraphGenerator.`[getAgentGraphDotSource](../../web/AgentGraphGenerator.html#getAgentGraphDotSource\(com.google.adk.agents.BaseAgent,java.util.List\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") rootAgent, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> highlightPairs)`

Generates the DOT source string for the agent graph.

Constructor parameters in [com.google.adk.web](../../web/package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[AgentController](../../web/AdkWebServer.AgentController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.util.Map,com.google.adk.web.AdkWebServer.ApiServerSpanExporter,com.google.adk.web.AdkWebServer.RunnerService\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [AdkWebServer.ApiServerSpanExporter](../../web/AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter, [AdkWebServer.RunnerService](../../web/AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)`

Constructs the AgentController.

` `

`[RunnerService](../../web/AdkWebServer.RunnerService.html#%3Cinit%3E\(java.util.Map,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 




* * *

Copyright (C) 2025\. All rights reserved.
