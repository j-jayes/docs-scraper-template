JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmRequest.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models](../package-summary.html)
  2. [LlmRequest](../LlmRequest.html)
  3. [Builder](../LlmRequest.Builder.html)



# Uses of Class  
com.google.adk.models.LlmRequest.Builder

Packages that use [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Package

Description

com.google.adk.models

 

com.google.adk.tools

 

com.google.adk.tools.retrieval

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Methods in [com.google.adk.models](../package-summary.html) that return [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendInstructions](../LlmRequest.Builder.html#appendInstructions\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> instructions)`

 

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendTools](../LlmRequest.Builder.html#appendTools\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.`[builder](../LlmRequest.html#builder\(\))()`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[config](../LlmRequest.Builder.html#config\(com.google.genai.types.GenerateContentConfig\))(com.google.genai.types.GenerateContentConfig config)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[contents](../LlmRequest.Builder.html#contents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> contents)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[liveConnectConfig](../LlmRequest.Builder.html#liveConnectConfig\(com.google.genai.types.LiveConnectConfig\))(com.google.genai.types.LiveConnectConfig liveConnectConfig)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[model](../LlmRequest.Builder.html#model\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[outputSchema](../LlmRequest.Builder.html#outputSchema\(com.google.genai.types.Schema\))(com.google.genai.types.Schema schema)`

Sets the output schema for the LLM response.

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.`[toBuilder](../LlmRequest.html#toBuilder\(\))()`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[appendArtifactsToLlmRequest](../../tools/LoadArtifactsTool.html#appendArtifactsToLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

BaseTool.`[processLlmRequest](../../tools/BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../LlmRequest.Builder.html "class in com.google.adk.models").

`io.reactivex.rxjava3.core.Completable`

BuiltInCodeExecutionTool.`[processLlmRequest](../../tools/BuiltInCodeExecutionTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleSearchTool.`[processLlmRequest](../../tools/GoogleSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[processLlmRequest](../../tools/LoadArtifactsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.tools.retrieval](../../tools/retrieval/package-summary.html)

Methods in [com.google.adk.tools.retrieval](../../tools/retrieval/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

VertexAiRagRetrieval.`[processLlmRequest](../../tools/retrieval/VertexAiRagRetrieval.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 




* * *

Copyright (C) 2025\. All rights reserved.
