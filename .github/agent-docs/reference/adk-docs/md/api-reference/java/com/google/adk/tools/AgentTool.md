JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AgentTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [AgentTool](AgentTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AgentTool(BaseAgent, boolean)
  6. Method Details
     1. fromConfig(BaseTool.ToolArgsConfig, String)
     2. create(BaseAgent, boolean)
     3. create(BaseAgent)
     4. declaration()
     5. runAsync(Map, ToolContext)

Hide sidebar  Show sidebar

# Class AgentTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.AgentTool

Direct Known Subclasses:
    `[GoogleSearchAgentTool](GoogleSearchAgentTool.html "class in com.google.adk.tools"), [VertexAiSearchAgentTool](VertexAiSearchAgentTool.html "class in com.google.adk.tools")`

* * *

public class AgentTool extends [BaseTool](BaseTool.html "class in com.google.adk.tools")

AgentTool implements a tool that allows an agent to call another agent.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`AgentTool([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [AgentTool](AgentTool.html "class in com.google.adk.tools")`

`create([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`static [AgentTool](AgentTool.html "class in com.google.adk.tools")`

`create([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`static [BaseTool](BaseTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentTool

protected AgentTool([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)

  * ## Method Details

    * ### fromConfig

public static [BaseTool](BaseTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Throws:
    `[ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")`

    * ### create

public static [AgentTool](AgentTool.html "class in com.google.adk.tools") create([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, boolean skipSummarization)

    * ### create

public static [AgentTool](AgentTool.html "class in com.google.adk.tools") create([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Description copied from class: `[BaseTool](BaseTool.html#declaration\(\))`

Gets the `FunctionDeclaration` representation of this tool.

Overrides:
    `[declaration](BaseTool.html#declaration\(\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
