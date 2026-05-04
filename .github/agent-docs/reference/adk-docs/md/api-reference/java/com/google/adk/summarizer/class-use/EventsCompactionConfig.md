JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../EventsCompactionConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.summarizer](../package-summary.html)
  2. [EventsCompactionConfig](../EventsCompactionConfig.html)



# Uses of Record Class  
com.google.adk.summarizer.EventsCompactionConfig

Packages that use [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Package

Description

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.runner

 

com.google.adk.summarizer

 

  * ## Uses of [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")>`

InvocationContext.`[eventsCompactionConfig](../../agents/InvocationContext.html#eventsCompactionConfig\(\))()`

Returns the events compaction configuration for the current agent run.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[eventsCompactionConfig](../../agents/InvocationContext.Builder.html#eventsCompactionConfig\(com.google.adk.summarizer.EventsCompactionConfig\))(@Nullable [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)`

Sets the events compaction configuration for the current agent run.

  * ## Uses of [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") in [com.google.adk.apps](../../apps/package-summary.html)

Methods in [com.google.adk.apps](../../apps/package-summary.html) that return [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier and Type

Method

Description

`@Nullable [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")`

App.`[eventsCompactionConfig](../../apps/App.html#eventsCompactionConfig\(\))()`

 

Methods in [com.google.adk.apps](../../apps/package-summary.html) with parameters of type [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[eventsCompactionConfig](../../apps/App.Builder.html#eventsCompactionConfig\(com.google.adk.summarizer.EventsCompactionConfig\))([EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)`

 

  * ## Uses of [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") in [com.google.adk.runner](../../runner/package-summary.html)

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier

Constructor

Description

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

  * ## Uses of [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") in [com.google.adk.summarizer](../package-summary.html)

Methods in [com.google.adk.summarizer](../package-summary.html) that return [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier and Type

Method

Description

`abstract [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")`

EventsCompactionConfig.Builder.`[build](../EventsCompactionConfig.Builder.html#build\(\))()`

 

Constructors in [com.google.adk.summarizer](../package-summary.html) with parameters of type [EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer")

Modifier

Constructor

Description

` `

`[SlidingWindowEventCompactor](../SlidingWindowEventCompactor.html#%3Cinit%3E\(com.google.adk.summarizer.EventsCompactionConfig\))([EventsCompactionConfig](../EventsCompactionConfig.html "class in com.google.adk.summarizer") config)`

 




* * *

Copyright (C) 1980\. All rights reserved.
