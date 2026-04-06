JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ConfigAgentUtils.ConfigurationException.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [ConfigAgentUtils](../ConfigAgentUtils.html)
  3. [ConfigurationException](../ConfigAgentUtils.ConfigurationException.html)



# Uses of Class  
com.google.adk.agents.ConfigAgentUtils.ConfigurationException

Packages that use [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.tools

 

com.google.adk.tools.mcp

 

  * ## Uses of [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that throw [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [BaseAgent](../BaseAgent.html "class in com.google.adk.agents")`

ConfigAgentUtils.`[fromConfig](../ConfigAgentUtils.html#fromConfig\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configPath)`

Load agent from a YAML config file path.

`static [LlmAgent](../LlmAgent.html "class in com.google.adk.agents")`

LlmAgent.`[fromConfig](../LlmAgent.html#fromConfig\(com.google.adk.agents.LlmAgentConfig,java.lang.String\))([LlmAgentConfig](../LlmAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates an LlmAgent from configuration with full subagent support.

`static [LoopAgent](../LoopAgent.html "class in com.google.adk.agents")`

LoopAgent.`[fromConfig](../LoopAgent.html#fromConfig\(com.google.adk.agents.LoopAgentConfig,java.lang.String\))([LoopAgentConfig](../LoopAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a LoopAgent from configuration.

`static [ParallelAgent](../ParallelAgent.html "class in com.google.adk.agents")`

ParallelAgent.`[fromConfig](../ParallelAgent.html#fromConfig\(com.google.adk.agents.ParallelAgentConfig,java.lang.String\))([ParallelAgentConfig](../ParallelAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a ParallelAgent from configuration.

`static [SequentialAgent](../SequentialAgent.html "class in com.google.adk.agents")`

SequentialAgent.`[fromConfig](../SequentialAgent.html#fromConfig\(com.google.adk.agents.SequentialAgentConfig,java.lang.String\))([SequentialAgentConfig](../SequentialAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a SequentialAgent from configuration.

`static <T> void`

ConfigAgentUtils.`[resolveAndSetCallback](../ConfigAgentUtils.html#resolveAndSetCallback\(java.util.List,java.lang.Class,java.lang.String,java.util.function.Consumer\))(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> refs, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> callbackBaseClass, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") callbackTypeName, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "class or interface in java.util.function")<com.google.common.collect.ImmutableList<T>> builderSetter)`

Resolves and sets callbacks from configuration.

`static void`

ConfigAgentUtils.`[resolveAndSetCommonAgentFields](../ConfigAgentUtils.html#resolveAndSetCommonAgentFields\(com.google.adk.agents.BaseAgent.Builder,com.google.adk.agents.BaseAgentConfig,java.lang.String\))([BaseAgent.Builder](../BaseAgent.Builder.html "class in com.google.adk.agents")<?> builder, [BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Configures the common properties of an agent builder from the configuration.

`static com.google.common.collect.ImmutableList<[BaseAgent](../BaseAgent.html "class in com.google.adk.agents")>`

ConfigAgentUtils.`[resolveSubAgents](../ConfigAgentUtils.html#resolveSubAgents\(java.util.List,java.lang.String\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.AgentRefConfig](../BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgentConfigs, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Resolves subagent configurations into actual BaseAgent instances.

`static void`

ConfigAgentUtils.`[setBaseAgentCallbacks](../ConfigAgentUtils.html#setBaseAgentCallbacks\(com.google.adk.agents.BaseAgentConfig,java.util.function.Consumer,java.util.function.Consumer\))([BaseAgentConfig](../BaseAgentConfig.html "class in com.google.adk.agents") config, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "class or interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase>> beforeSetter, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "class or interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.AfterAgentCallbackBase>> afterSetter)`

Sets the common agent callbacks (before/after agent) from the config to the builder setters.

  * ## Uses of [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) that throw [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")`

AgentTool.`[fromConfig](../../tools/AgentTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolArgsConfig,java.lang.String\))([BaseTool.ToolArgsConfig](../../tools/BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

 

`static [BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")`

BaseTool.`[fromConfig](../../tools/BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](../../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a tool instance from a config.

`static [ExampleTool](../../tools/ExampleTool.html "class in com.google.adk.tools")`

ExampleTool.`[fromConfig](../../tools/ExampleTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolArgsConfig\))([BaseTool.ToolArgsConfig](../../tools/BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args)`

Overload to match resolver which passes only ToolArgsConfig.

`static [ExampleTool](../../tools/ExampleTool.html "class in com.google.adk.tools")`

ExampleTool.`[fromConfig](../../tools/ExampleTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolArgsConfig,java.lang.String\))([BaseTool.ToolArgsConfig](../../tools/BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Factory from YAML tool args.

  * ## Uses of [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents") in [com.google.adk.tools.mcp](../../tools/mcp/package-summary.html)

Methods in [com.google.adk.tools.mcp](../../tools/mcp/package-summary.html) that throw [ConfigAgentUtils.ConfigurationException](../ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [McpToolset](../../tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp")`

McpToolset.`[fromConfig](../../tools/mcp/McpToolset.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](../../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a McpToolset instance from a config.




* * *

Copyright (C) 1980\. All rights reserved.
