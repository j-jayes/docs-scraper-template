JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ResumabilityConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.apps](../package-summary.html)
  2. [ResumabilityConfig](../ResumabilityConfig.html)



# Uses of Class  
com.google.adk.apps.ResumabilityConfig

Packages that use [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")

Package

Description

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.runner

 

  * ## Uses of [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[resumabilityConfig](../../agents/InvocationContext.Builder.html#resumabilityConfig\(com.google.adk.apps.ResumabilityConfig\))(@Nullable [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

Sets the resumability configuration for the invocation.

  * ## Uses of [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") in [com.google.adk.apps](../package-summary.html)

Methods in [com.google.adk.apps](../package-summary.html) that return [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")

Modifier and Type

Method

Description

`abstract [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")`

ResumabilityConfig.Builder.`[build](../ResumabilityConfig.Builder.html#build\(\))()`

 

`@Nullable [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")`

App.`[resumabilityConfig](../App.html#resumabilityConfig\(\))()`

 

Methods in [com.google.adk.apps](../package-summary.html) with parameters of type [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")

Modifier and Type

Method

Description

`[App.Builder](../App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[resumabilityConfig](../App.Builder.html#resumabilityConfig\(com.google.adk.apps.ResumabilityConfig\))([ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

Deprecated.

See [`ResumabilityConfig`](../ResumabilityConfig.html "class in com.google.adk.apps"): partial feature, full resumability not yet available.

  * ## Uses of [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") in [com.google.adk.runner](../../runner/package-summary.html)

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps")

Modifier

Constructor

Description

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig,com.google.adk.apps.ResumabilityConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig, @Nullable [ResumabilityConfig](../ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.




* * *

Copyright (C) 1980\. All rights reserved.
