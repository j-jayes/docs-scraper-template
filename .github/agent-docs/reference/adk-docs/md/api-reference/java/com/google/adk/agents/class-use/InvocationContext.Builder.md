JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../InvocationContext.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [InvocationContext](../InvocationContext.html)
  3. [Builder](../InvocationContext.Builder.html)



# Uses of Class  
com.google.adk.agents.InvocationContext.Builder

Packages that use [InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return [InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[agent](../InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent)`

Sets the agent being invoked.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[artifactService](../InvocationContext.Builder.html#artifactService\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

Sets the artifact service for persisting artifacts.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[branch](../InvocationContext.Builder.html#branch\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Sets the branch ID for the invocation.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[branch](../InvocationContext.Builder.html#branch\(java.util.Optional\))([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.Builder.branch(String)`](../InvocationContext.Builder.html#branch\(java.lang.String\)) instead.

`static [InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.`[builder](../InvocationContext.html#builder\(\))()`

Returns a new [`InvocationContext.Builder`](../InvocationContext.Builder.html "class in com.google.adk.agents") for creating [`InvocationContext`](../InvocationContext.html "class in com.google.adk.agents") instances.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[endInvocation](../InvocationContext.Builder.html#endInvocation\(boolean\))(boolean endInvocation)`

Sets whether this invocation should be ended.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[invocationId](../InvocationContext.Builder.html#invocationId\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Sets the unique ID for the invocation.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[liveRequestQueue](../InvocationContext.Builder.html#liveRequestQueue\(com.google.adk.agents.LiveRequestQueue\))([LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue)`

Sets the queue for managing live requests.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[liveRequestQueue](../InvocationContext.Builder.html#liveRequestQueue\(java.util.Optional\))([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.Builder.liveRequestQueue(LiveRequestQueue)`](../InvocationContext.Builder.html#liveRequestQueue\(com.google.adk.agents.LiveRequestQueue\)) instead.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[memoryService](../InvocationContext.Builder.html#memoryService\(com.google.adk.memory.BaseMemoryService\))([BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Sets the memory service for accessing agent memory.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[pluginManager](../InvocationContext.Builder.html#pluginManager\(com.google.adk.plugins.Plugin\))([Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager)`

Sets the plugin manager for accessing tools and plugins.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[resumabilityConfig](../InvocationContext.Builder.html#resumabilityConfig\(com.google.adk.flows.llmflows.ResumabilityConfig\))([ResumabilityConfig](../../flows/llmflows/ResumabilityConfig.html "class in com.google.adk.flows.llmflows") resumabilityConfig)`

Sets the resumability configuration for the current agent run.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[runConfig](../InvocationContext.Builder.html#runConfig\(com.google.adk.agents.RunConfig\))([RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Sets the configuration for the current agent run.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[session](../InvocationContext.Builder.html#session\(com.google.adk.sessions.Session\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session)`

Sets the session associated with this invocation.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[sessionService](../InvocationContext.Builder.html#sessionService\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Sets the session service for managing session state.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.`[toBuilder](../InvocationContext.html#toBuilder\(\))()`

Returns a [`InvocationContext.Builder`](../InvocationContext.Builder.html "class in com.google.adk.agents") initialized with the values of this instance.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[userContent](../InvocationContext.Builder.html#userContent\(com.google.genai.types.Content\))(com.google.genai.types.Content userContent)`

Sets the user content that triggered this invocation.

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[userContent](../InvocationContext.Builder.html#userContent\(java.util.Optional\))([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent)`

Sets the user content that triggered this invocation.

Constructors in [com.google.adk.agents](../package-summary.html) with parameters of type [InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")

Modifier

Constructor

Description

`protected `

`[InvocationContext](../InvocationContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext.Builder\))([InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents") builder)`

 




* * *

Copyright (C) 1980\. All rights reserved.
