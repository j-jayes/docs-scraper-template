JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../index.html)
  * Class
  * [Use](class-use/CustomDemoRegistry.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../deprecated-list.html)
  * [Index](../../index-all.html)
  * [Search](../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example](package-summary.html)
  2. [CustomDemoRegistry](CustomDemoRegistry.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. INSTANCE
  6. Constructor Details
     1. CustomDemoRegistry()

Hide sidebar  Show sidebar

# Class CustomDemoRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.utils.ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils")

com.example.CustomDemoRegistry

* * *

public class CustomDemoRegistry extends [ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils")

Custom ComponentRegistry for the user-defined config agent demo. 

This registry is used to add custom tools and agents to the ADK Web Server.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [CustomDemoRegistry](CustomDemoRegistry.html "class in com.example")`

`INSTANCE`

Singleton instance for easy access

  * ## Constructor Summary

Constructors

Constructor

Description

`CustomDemoRegistry()`

Private constructor to initialize custom components

  * ## Method Summary

### Methods inherited from class [ComponentRegistry](../google/adk/utils/ComponentRegistry.html#method-summary "class in com.google.adk.utils")

`[get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String\) "get\(String\)"), [get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String,java.lang.Class\) "get\(String, Class\)"), [getInstance](../google/adk/utils/ComponentRegistry.html#getInstance\(\) "getInstance\(\)"), [getToolNamesWithPrefix](../google/adk/utils/ComponentRegistry.html#getToolNamesWithPrefix\(java.lang.String\) "getToolNamesWithPrefix\(String\)"), [register](../google/adk/utils/ComponentRegistry.html#register\(java.lang.String,java.lang.Object\) "register\(String, Object\)"), [resolveAfterAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterAgentCallback\(java.lang.String\) "resolveAfterAgentCallback\(String\)"), [resolveAfterModelCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterModelCallback\(java.lang.String\) "resolveAfterModelCallback\(String\)"), [resolveAfterToolCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterToolCallback\(java.lang.String\) "resolveAfterToolCallback\(String\)"), [resolveAgentClass](../google/adk/utils/ComponentRegistry.html#resolveAgentClass\(java.lang.String\) "resolveAgentClass\(String\)"), [resolveAgentInstance](../google/adk/utils/ComponentRegistry.html#resolveAgentInstance\(java.lang.String\) "resolveAgentInstance\(String\)"), [resolveBeforeAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeAgentCallback\(java.lang.String\) "resolveBeforeAgentCallback\(String\)"), [resolveBeforeModelCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeModelCallback\(java.lang.String\) "resolveBeforeModelCallback\(String\)"), [resolveBeforeToolCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeToolCallback\(java.lang.String\) "resolveBeforeToolCallback\(String\)"), [resolveToolClass](../google/adk/utils/ComponentRegistry.html#resolveToolClass\(java.lang.String\) "resolveToolClass\(String\)"), [resolveToolInstance](../google/adk/utils/ComponentRegistry.html#resolveToolInstance\(java.lang.String\) "resolveToolInstance\(String\)"), [resolveToolsetClass](../google/adk/utils/ComponentRegistry.html#resolveToolsetClass\(java.lang.String\) "resolveToolsetClass\(String\)"), [resolveToolsetInstance](../google/adk/utils/ComponentRegistry.html#resolveToolsetInstance\(java.lang.String\) "resolveToolsetInstance\(String\)"), [setInstance](../google/adk/utils/ComponentRegistry.html#setInstance\(com.google.adk.utils.ComponentRegistry\) "setInstance\(ComponentRegistry\)")`

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Retrieves an object by name without type checking.

`<T> [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<T>`

`[get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> type)`

Retrieves an object by name and attempts to cast it to the specified type.

`static [ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils")`

`[getInstance](../google/adk/utils/ComponentRegistry.html#getInstance\(\))()`

Returns the global singleton instance of ComponentRegistry.

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[getToolNamesWithPrefix](../google/adk/utils/ComponentRegistry.html#getToolNamesWithPrefix\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") prefix)`

 

`void`

`[register](../google/adk/utils/ComponentRegistry.html#register\(java.lang.String,java.lang.Object\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)`

Registers an object with the given name.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterAgentCallback](../google/adk/agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[resolveAfterAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterAgentCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterModelCallback](../google/adk/agents/Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

`[resolveAfterModelCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterModelCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterToolCallback](../google/adk/agents/Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>`

`[resolveAfterToolCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterToolCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../google/adk/agents/BaseAgent.html "class in com.google.adk.agents")>`

`[resolveAgentClass](../google/adk/utils/ComponentRegistry.html#resolveAgentClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClassName)`

Resolves the agent class based on the agent class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](../google/adk/agents/BaseAgent.html "class in com.google.adk.agents")>`

`[resolveAgentInstance](../google/adk/utils/ComponentRegistry.html#resolveAgentInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Resolves an agent instance from the registry.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeAgentCallback](../google/adk/agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[resolveBeforeAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeAgentCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeModelCallback](../google/adk/agents/Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>`

`[resolveBeforeModelCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeModelCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeToolCallback](../google/adk/agents/Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

`[resolveBeforeToolCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeToolCallback\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../google/adk/tools/BaseTool.html "class in com.google.adk.tools")>>`

`[resolveToolClass](../google/adk/utils/ComponentRegistry.html#resolveToolClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolClassName)`

Resolves the tool class based on the tool class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseTool](../google/adk/tools/BaseTool.html "class in com.google.adk.tools")>`

`[resolveToolInstance](../google/adk/utils/ComponentRegistry.html#resolveToolInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../google/adk/tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`[resolveToolsetClass](../google/adk/utils/ComponentRegistry.html#resolveToolsetClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolsetClassName)`

Resolves a toolset class by name from the registry or by attempting to load it.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseToolset](../google/adk/tools/BaseToolset.html "interface in com.google.adk.tools")>`

`[resolveToolsetInstance](../google/adk/utils/ComponentRegistry.html#resolveToolsetInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Resolves a toolset instance by name from the registry.

`static void`

`[setInstance](../google/adk/utils/ComponentRegistry.html#setInstance\(com.google.adk.utils.ComponentRegistry\))([ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils") newInstance)`

Updates the global singleton instance with a new ComponentRegistry.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### INSTANCE

public static final [CustomDemoRegistry](CustomDemoRegistry.html "class in com.example") INSTANCE

Singleton instance for easy access

  * ## Constructor Details

    * ### CustomDemoRegistry

public CustomDemoRegistry()

Private constructor to initialize custom components




* * *

Copyright (C) 1980\. All rights reserved.
