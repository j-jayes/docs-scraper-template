JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../AgentLoader.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web](../package-summary.html)
  2. [AgentLoader](../AgentLoader.html)



# Uses of Interface  
com.google.adk.web.AgentLoader

Packages that use [AgentLoader](../AgentLoader.html "interface in com.google.adk.web")

Package

Description

com.google.adk.maven

 

com.google.adk.web

 

com.google.adk.web.controller

 

com.google.adk.web.service

 

  * ## Uses of [AgentLoader](../AgentLoader.html "interface in com.google.adk.web") in [com.google.adk.maven](../../maven/package-summary.html)

Classes in [com.google.adk.maven](../../maven/package-summary.html) that implement [AgentLoader](../AgentLoader.html "interface in com.google.adk.web")

Modifier and Type

Class

Description

`class `

`[ConfigAgentLoader](../../maven/ConfigAgentLoader.html "class in com.google.adk.maven")`

Configuration-based AgentLoader that loads agents from YAML configuration files.

  * ## Uses of [AgentLoader](../AgentLoader.html "interface in com.google.adk.web") in [com.google.adk.web](../package-summary.html)

Classes in [com.google.adk.web](../package-summary.html) that implement [AgentLoader](../AgentLoader.html "interface in com.google.adk.web")

Modifier and Type

Class

Description

`class `

`[AgentStaticLoader](../AgentStaticLoader.html "class in com.google.adk.web")`

Static Agent Loader for programmatically provided agents.

`class `

`[CompiledAgentLoader](../CompiledAgentLoader.html "class in com.google.adk.web")`

CompiledAgentLoader implementation for the dev environment.

  * ## Uses of [AgentLoader](../AgentLoader.html "interface in com.google.adk.web") in [com.google.adk.web.controller](../controller/package-summary.html)

Constructors in [com.google.adk.web.controller](../controller/package-summary.html) with parameters of type [AgentLoader](../AgentLoader.html "interface in com.google.adk.web")

Modifier

Constructor

Description

` `

`[AgentController](../controller/AgentController.html#%3Cinit%3E\(com.google.adk.web.AgentLoader\))([AgentLoader](../AgentLoader.html "interface in com.google.adk.web") agentProvider)`

Constructs the AgentController.

` `

`[GraphController](../controller/GraphController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.web.AgentLoader\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [AgentLoader](../AgentLoader.html "interface in com.google.adk.web") agentProvider)`

 

  * ## Uses of [AgentLoader](../AgentLoader.html "interface in com.google.adk.web") in [com.google.adk.web.service](../service/package-summary.html)

Constructors in [com.google.adk.web.service](../service/package-summary.html) with parameters of type [AgentLoader](../AgentLoader.html "interface in com.google.adk.web")

Modifier

Constructor

Description

` `

`[RunnerService](../service/RunnerService.html#%3Cinit%3E\(com.google.adk.web.AgentLoader,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([AgentLoader](../AgentLoader.html "interface in com.google.adk.web") agentProvider, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> extraPlugins)`

 




* * *

Copyright (C) 1980\. All rights reserved.
