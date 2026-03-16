JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseToolset.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools](../package-summary.html)
  2. [BaseToolset](../BaseToolset.html)



# Uses of Interface  
com.google.adk.tools.BaseToolset

Packages that use [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Package

Description

com.google.adk.agents

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.computeruse

 

com.google.adk.tools.mcp

 

com.google.adk.utils

 

  * ## Uses of [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")>`

LlmAgent.`[toolsets](../../agents/LlmAgent.html#toolsets\(\))()`

 

  * ## Uses of [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Classes in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html) that implement [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Modifier and Type

Class

Description

`class `

`[ApplicationIntegrationToolset](../applicationintegrationtoolset/ApplicationIntegrationToolset.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Application Integration Toolset

  * ## Uses of [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools") in [com.google.adk.tools.computeruse](../computeruse/package-summary.html)

Classes in [com.google.adk.tools.computeruse](../computeruse/package-summary.html) that implement [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Modifier and Type

Class

Description

`class `

`[ComputerUseToolset](../computeruse/ComputerUseToolset.html "class in com.google.adk.tools.computeruse")`

A toolset that provides computer use capabilities.

  * ## Uses of [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Classes in [com.google.adk.tools.mcp](../mcp/package-summary.html) that implement [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Modifier and Type

Class

Description

`class `

`[McpAsyncToolset](../mcp/McpAsyncToolset.html "class in com.google.adk.tools.mcp")`

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools.

`class `

`[McpToolset](../mcp/McpToolset.html "class in com.google.adk.tools.mcp")`

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools.

  * ## Uses of [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools") in [com.google.adk.utils](../../utils/package-summary.html)

Methods in [com.google.adk.utils](../../utils/package-summary.html) that return types with arguments of type [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")>>`

AdditionalAdkComponentProvider.`[getToolsetClasses](../../utils/AdditionalAdkComponentProvider.html#getToolsetClasses\(\))()`

Returns toolset classes for [`McpToolset`](../mcp/McpToolset.html "class in com.google.adk.tools.mcp").

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")>>`

AdkComponentProvider.`[getToolsetClasses](../../utils/AdkComponentProvider.html#getToolsetClasses\(\))()`

Returns a list of toolset classes to register.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")>>`

ComponentRegistry.`[resolveToolsetClass](../../utils/ComponentRegistry.html#resolveToolsetClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolsetClassName)`

Resolves a toolset class by name from the registry or by attempting to load it.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")>`

ComponentRegistry.`[resolveToolsetInstance](../../utils/ComponentRegistry.html#resolveToolsetInstance\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Resolves a toolset instance by name from the registry.




* * *

Copyright (C) 1980\. All rights reserved.
