JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ContextCacheConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [ContextCacheConfig](../ContextCacheConfig.html)



# Uses of Record Class  
com.google.adk.agents.ContextCacheConfig

Packages that use [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.runner

 

  * ## Uses of [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")>`

InvocationContext.`[contextCacheConfig](../InvocationContext.html#contextCacheConfig\(\))()`

Returns the context cache configuration for the current agent run.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[contextCacheConfig](../InvocationContext.Builder.html#contextCacheConfig\(com.google.adk.agents.ContextCacheConfig\))([ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Sets the context cache configuration for the current agent run.

  * ## Uses of [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") in [com.google.adk.apps](../../apps/package-summary.html)

Methods in [com.google.adk.apps](../../apps/package-summary.html) that return [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")`

App.`[contextCacheConfig](../../apps/App.html#contextCacheConfig\(\))()`

 

Methods in [com.google.adk.apps](../../apps/package-summary.html) with parameters of type [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[contextCacheConfig](../../apps/App.Builder.html#contextCacheConfig\(com.google.adk.agents.ContextCacheConfig\))([ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

 

  * ## Uses of [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents")

Modifier

Constructor

Description

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, [ContextCacheConfig](../ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.




* * *

Copyright (C) 1980\. All rights reserved.
