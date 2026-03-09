JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ExampleTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [ExampleTool](ExampleTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. processLlmRequest(LlmRequest.Builder, ToolContext)
     2. fromConfig(BaseTool.ToolArgsConfig, String)
     3. fromConfig(BaseTool.ToolArgsConfig)
     4. builder()

Hide sidebar  Show sidebar

# Class ExampleTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.ExampleTool

* * *

public final class ExampleTool extends [BaseTool](BaseTool.html "class in com.google.adk.tools")

A tool that injects (few-shot) examples into the outgoing LLM request as system instructions. 

Configuration (args) options for YAML: 

  * **examples** : Either a fully-qualified reference to a [`BaseExampleProvider`](../examples/BaseExampleProvider.html "interface in com.google.adk.examples") instance (e.g., `com.example.MyExamples.INSTANCE`) or a list of examples with fields `input` and `output` (array of messages). 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[ExampleTool.Builder](ExampleTool.Builder.html "class in com.google.adk.tools")`

 

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ExampleTool.Builder](ExampleTool.Builder.html "class in com.google.adk.tools")`

`builder()`

 

`static [ExampleTool](ExampleTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args)`

Overload to match resolver which passes only ToolArgsConfig.

`static [ExampleTool](ExampleTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Factory from YAML tool args.

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [declaration](BaseTool.html#declaration\(\) "declaration\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [runAsync](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\) "runAsync\(Map, ToolContext\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### processLlmRequest

public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's [`BaseTool.declaration()`](BaseTool.html#declaration\(\)) to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.

Overrides:
    `[processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`

    * ### fromConfig

public static [ExampleTool](ExampleTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Factory from YAML tool args.

Throws:
    `[ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")`

    * ### fromConfig

public static [ExampleTool](ExampleTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") args) throws [ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Overload to match resolver which passes only ToolArgsConfig.

Throws:
    `[ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")`

    * ### builder

public static [ExampleTool.Builder](ExampleTool.Builder.html "class in com.google.adk.tools") builder()




* * *

Copyright (C) 1980\. All rights reserved.
