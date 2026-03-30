JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseAgent.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [BaseAgent](../BaseAgent.html)



# Uses of Class  
com.google.adk.agents.BaseAgent

Packages that use [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Package

Description

com.example.a2a_basic

 

com.google.adk.a2a.agent

 

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.maven

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.runner

 

com.google.adk.tools

 

com.google.adk.tutorials

 

com.google.adk.utils

 

com.google.adk.web

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.example.a2a_basic](../../../../example/a2a_basic/package-summary.html)

Constructors in [com.example.a2a_basic](../../../../example/a2a_basic/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[A2AAgentRun](../../../../example/a2a_basic/A2AAgentRun.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Subclasses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Modifier and Type

Class

Description

`class `

`[RemoteA2AAgent](../../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent")`

Agent that communicates with a remote A2A agent via an A2A client.

Method parameters in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[RemoteA2AAgent.Builder](../../a2a/agent/RemoteA2AAgent.Builder.html "class in com.google.adk.a2a.agent")`

RemoteA2AAgent.Builder.`[subAgents](../../a2a/agent/RemoteA2AAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[AgentExecutor.Builder](../../a2a/executor/AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutor.Builder.`[agent](../../a2a/executor/AgentExecutor.Builder.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

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

Fields in [com.google.adk.agents](../package-summary.html) with type parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Field

Description

`protected com.google.common.collect.ImmutableList<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

BaseAgent.Builder.`[subAgents](../BaseAgent.Builder.html#subAgents)`

 

Methods in [com.google.adk.agents](../package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

InvocationContext.`[agent](../InvocationContext.html#agent\(\))()`

Returns the agent being invoked.

`abstract [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.Builder.`[build](../BaseAgent.Builder.html#build\(\))()`

 

`static [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[fromConfig](../BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`static [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

ConfigAgentUtils.`[fromConfig](../ConfigAgentUtils.html#fromConfig\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configPath)`

Load agent from a YAML config file path.

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

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

BaseAgent.`[findAgent](../BaseAgent.html#findAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Finds an agent (this or descendant) by name.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

BaseAgent.`[findSubAgent](../BaseAgent.html#findSubAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Recursively search sub agent by name.

`static com.google.common.collect.ImmutableList<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

ConfigAgentUtils.`[resolveSubAgents](../ConfigAgentUtils.html#resolveSubAgents\(java.util.List,java.lang.String\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.AgentRefConfig](../BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgentConfigs, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Resolves subagent configurations into actual BaseAgent instances.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

BaseAgent.`[subAgents](../BaseAgent.html#subAgents\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[agent](../InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

Sets the agent being invoked.

`protected void`

BaseAgent.`[parentAgent](../BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") parentAgent)`

Sets the parent agent.

`[B](../BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder")`

BaseAgent.Builder.`[subAgents](../BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

Method parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[B](../BaseAgent.Builder.html#type-param-B "type parameter in BaseAgent.Builder")`

BaseAgent.Builder.`[subAgents](../BaseAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

Constructor parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[BaseAgent](../BaseAgent.html#%3Cinit%3E\(java.lang.String,java.lang.String,java.util.List,java.util.List,java.util.List\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")> subAgents, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeAgentCallback](../Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterAgentCallback](../Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback)`

Creates a new BaseAgent.

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.apps](../../apps/package-summary.html)

Methods in [com.google.adk.apps](../../apps/package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

App.`[rootAgent](../../apps/App.html#rootAgent\(\))()`

 

Methods in [com.google.adk.apps](../../apps/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[rootAgent](../../apps/App.Builder.html#rootAgent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") rootAgent)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.maven](../../maven/package-summary.html)

Methods in [com.google.adk.maven](../../maven/package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

AgentLoader.`[loadAgent](../../maven/AgentLoader.html#loadAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Loads the BaseAgent instance for the specified agent name.

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

ConfigAgentLoader.`[loadAgent](../../maven/ConfigAgentLoader.html#loadAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[afterAgentCallback](../../plugins/LoggingPlugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[afterAgentCallback](../../plugins/Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[afterAgentCallback](../../plugins/PluginManager.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[beforeAgentCallback](../../plugins/LoggingPlugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[beforeAgentCallback](../../plugins/Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[beforeAgentCallback](../../plugins/PluginManager.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[afterAgentCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[beforeAgentCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

Runner.`[agent](../../runner/Runner.html#agent\(\))()`

 

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[agent](../../runner/Runner.Builder.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[FirestoreDatabaseRunner](../../runner/FirestoreDatabaseRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,com.google.cloud.firestore.Firestore\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") baseAgent, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner

` `

`[FirestoreDatabaseRunner](../../runner/FirestoreDatabaseRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.cloud.firestore.Firestore\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner with appName

` `

`[FirestoreDatabaseRunner](../../runner/FirestoreDatabaseRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,java.util.List,com.google.cloud.firestore.Firestore\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner with parent runners

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

 

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,java.util.List\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

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

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.tutorials](../../tutorials/package-summary.html)

Fields in [com.google.adk.tutorials](../../tutorials/package-summary.html) declared as [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Field

Description

`static final [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

CityTimeWeather.`[ROOT_AGENT](../../tutorials/CityTimeWeather.html#ROOT_AGENT)`

 

`static final [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

LiveAudioSingleAgent.`[WEATHER_AGENT](../../tutorials/LiveAudioSingleAgent.html#WEATHER_AGENT)`

 

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>>`

AdkComponentProvider.`[getAgentClasses](../../utils/AdkComponentProvider.html#getAgentClasses\(\))()`

Returns a list of agent classes to register.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>>`

CoreAdkComponentProvider.`[getAgentClasses](../../utils/CoreAdkComponentProvider.html#getAgentClasses\(\))()`

Returns agent classes for [`LlmAgent`](../LlmAgent.html "class in com.google.adk.agents"), [`LoopAgent`](../LoopAgent.html "class in com.google.adk.agents"), [`ParallelAgent`](../ParallelAgent.html "class in com.google.adk.agents") and [`SequentialAgent`](../SequentialAgent.html "class in com.google.adk.agents").

`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

ComponentRegistry.`[resolveAgentClass](../../utils/ComponentRegistry.html#resolveAgentClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentClassName)`

Resolves the agent class based on the agent class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

ComponentRegistry.`[resolveAgentInstance](../../utils/ComponentRegistry.html#resolveAgentInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Resolves an agent instance from the registry.

  * ## Uses of [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

AgentLoader.`[loadAgent](../../web/AgentLoader.html#loadAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Loads the BaseAgent instance for the specified agent name.

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

AgentStaticLoader.`[loadAgent](../../web/AgentStaticLoader.html#loadAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

CompiledAgentLoader.`[loadAgent](../../web/CompiledAgentLoader.html#loadAgent\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

Methods in [com.google.adk.web](../../web/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

AgentGraphGenerator.`[getAgentGraphDotSource](../../web/AgentGraphGenerator.html#getAgentGraphDotSource\(com.google.adk.agents.BaseAgent,java.util.List\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") rootAgent, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> highlightPairs)`

Generates the DOT source string for the agent graph.

`static void`

AdkWebServer.`[start](../../web/AdkWebServer.html#start\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... agents)`

 

Constructors in [com.google.adk.web](../../web/package-summary.html) with parameters of type [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[AgentStaticLoader](../../web/AgentStaticLoader.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent...\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents")... agents)`

 




* * *

Copyright (C) 1980\. All rights reserved.
