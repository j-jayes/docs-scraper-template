JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/VertexAiSearchAgentTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [VertexAiSearchAgentTool](VertexAiSearchAgentTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. VertexAiSearchAgentTool(LlmAgent)
  6. Method Details
     1. create(BaseLlm, VertexAiSearchTool)

Hide sidebar  Show sidebar

# Class VertexAiSearchAgentTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.AgentTool](AgentTool.html "class in com.google.adk.tools")

com.google.adk.tools.VertexAiSearchAgentTool

* * *

public class VertexAiSearchAgentTool extends [AgentTool](AgentTool.html "class in com.google.adk.tools")

A tool that wraps a sub-agent that only uses vertex_ai_search tool. 

This is a workaround to support using [`VertexAiSearchTool`](VertexAiSearchTool.html "class in com.google.adk.tools") tool with other tools.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`VertexAiSearchAgentTool([LlmAgent](../agents/LlmAgent.html "class in com.google.adk.agents") agent)`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [VertexAiSearchAgentTool](VertexAiSearchAgentTool.html "class in com.google.adk.tools")`

`create([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model, [VertexAiSearchTool](VertexAiSearchTool.html "class in com.google.adk.tools") vertexAiSearchTool)`

 

### Methods inherited from class [AgentTool](AgentTool.html#method-summary "class in com.google.adk.tools")

`[create](AgentTool.html#create\(com.google.adk.agents.BaseAgent\) "create\(BaseAgent\)"), [create](AgentTool.html#create\(com.google.adk.agents.BaseAgent,boolean\) "create\(BaseAgent, boolean\)"), [declaration](AgentTool.html#declaration\(\) "declaration\(\)"), [fromConfig](AgentTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolArgsConfig,java.lang.String\) "fromConfig\(BaseTool.ToolArgsConfig, String\)"), [runAsync](AgentTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\) "runAsync\(Map, ToolContext\)")`

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### VertexAiSearchAgentTool

protected VertexAiSearchAgentTool([LlmAgent](../agents/LlmAgent.html "class in com.google.adk.agents") agent)

  * ## Method Details

    * ### create

public static [VertexAiSearchAgentTool](VertexAiSearchAgentTool.html "class in com.google.adk.tools") create([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model, [VertexAiSearchTool](VertexAiSearchTool.html "class in com.google.adk.tools") vertexAiSearchTool)




* * *

Copyright (C) 1980\. All rights reserved.
