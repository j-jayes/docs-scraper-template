JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseAgentConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [BaseAgentConfig](../BaseAgentConfig.html)



# Uses of Class  
com.google.adk.agents.BaseAgentConfig

Packages that use [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Subclasses of [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[LlmAgentConfig](../LlmAgentConfig.html "class in com.google.adk.agents")`

Configuration for LlmAgent.

`class `

`[LoopAgentConfig](../LoopAgentConfig.html "class in com.google.adk.agents")`

Configuration for LoopAgent.

`class `

`[ParallelAgentConfig](../ParallelAgentConfig.html "class in com.google.adk.agents")`

Configuration for ParallelAgent.

`class `

`[SequentialAgentConfig](../SequentialAgentConfig.html "class in com.google.adk.agents")`

Configuration for SequentialAgent.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

BaseAgent.`[fromConfig](../BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a new agent instance from a configuration object.

`static void`

ConfigAgentUtils.`[resolveAndSetCommonAgentFields](../ConfigAgentUtils.html#resolveAndSetCommonAgentFields\(com.google.adk.agents.BaseAgent.Builder,com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgent.Builder](../BaseAgent.Builder.html "class in com.google.adk.agents")<?> builder, [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Configures the common properties of an agent builder from the configuration.

`static void`

ConfigAgentUtils.`[setBaseAgentCallbacks](../ConfigAgentUtils.html#setBaseAgentCallbacks\(com.google.adk.agents.BaseAgentConfig,java.util.function.Consumer,java.util.function.Consumer\))([BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase>> beforeSetter, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.AfterAgentCallbackBase>> afterSetter)`

Sets the common agent callbacks (before/after agent) from the config to the builder setters.




* * *

Copyright (C) 1980\. All rights reserved.
