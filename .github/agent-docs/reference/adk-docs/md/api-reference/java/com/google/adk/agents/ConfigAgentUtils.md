JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ConfigAgentUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [ConfigAgentUtils](ConfigAgentUtils.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. resolveAndSetCommonAgentFields(BaseAgent.Builder, BaseAgentConfig, String)
     2. resolveAndSetCallback(List, Class, String, Consumer)
     3. setBaseAgentCallbacks(BaseAgentConfig, Consumer, Consumer)
     4. fromConfig(String)
     5. resolveSubAgents(List, String)

Hide sidebar  Show sidebar

# Class ConfigAgentUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.ConfigAgentUtils

* * *

public final class ConfigAgentUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for loading agent configurations from YAML files. 

TODO: Config agent features are not yet ready for public use.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")`

Exception thrown when configuration is invalid.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`fromConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configPath)`

Load agent from a YAML config file path.

`static <T> void`

`resolveAndSetCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> refs, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> callbackBaseClass, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") callbackTypeName, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<T>> builderSetter)`

Resolves and sets callbacks from configuration.

`static void`

`resolveAndSetCommonAgentFields([BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<?> builder, [BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Configures the common properties of an agent builder from the configuration.

`static com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`resolveSubAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgentConfigs, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Resolves subagent configurations into actual BaseAgent instances.

`static void`

`setBaseAgentCallbacks([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase>> beforeSetter, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.AfterAgentCallbackBase>> afterSetter)`

Sets the common agent callbacks (before/after agent) from the config to the builder setters.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### resolveAndSetCommonAgentFields

public static void resolveAndSetCommonAgentFields([BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<?> builder, [BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Configures the common properties of an agent builder from the configuration.

Parameters:
    `builder` \- The agent builder.
    `config` \- The agent configuration.
    `configAbsPath` \- The absolute path to the config file (for resolving relative paths).
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the configuration is invalid.

    * ### resolveAndSetCallback

public static <T> void resolveAndSetCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> refs, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> callbackBaseClass, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") callbackTypeName, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<T>> builderSetter) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Resolves and sets callbacks from configuration.

Type Parameters:
    `T` \- The type of the callback.
Parameters:
    `refs` \- The list of callback references from config.
    `callbackBaseClass` \- The base class of the callback.
    `callbackTypeName` \- The name of the callback type for error messages.
    `builderSetter` \- The setter method on the builder to apply the resolved callbacks.
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if a callback cannot be resolved.

    * ### setBaseAgentCallbacks

public static void setBaseAgentCallbacks([BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents") config, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase>> beforeSetter, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<com.google.adk.agents.Callbacks.AfterAgentCallbackBase>> afterSetter) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Sets the common agent callbacks (before/after agent) from the config to the builder setters.

Parameters:
    `config` \- The agent configuration.
    `beforeSetter` \- The setter for before-agent callbacks.
    `afterSetter` \- The setter for after-agent callbacks.
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if a callback cannot be resolved.

    * ### fromConfig

public static [BaseAgent](BaseAgent.html "class in com.google.adk.agents") fromConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Load agent from a YAML config file path.

Parameters:
    `configPath` \- the path to a YAML config file
Returns:
    the created agent instance as a [`BaseAgent`](BaseAgent.html "class in com.google.adk.agents")
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if loading fails

    * ### resolveSubAgents

public static com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> resolveSubAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgentConfigs, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Resolves subagent configurations into actual BaseAgent instances. This method is used by concrete agent implementations to resolve their subagents.

Parameters:
    `subAgentConfigs` \- The list of subagent configurations
    `configAbsPath` \- The absolute path to the parent config file for resolving relative paths
Returns:
    A list of resolved BaseAgent instances
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if any subagent fails to resolve




* * *

Copyright (C) 1980\. All rights reserved.
