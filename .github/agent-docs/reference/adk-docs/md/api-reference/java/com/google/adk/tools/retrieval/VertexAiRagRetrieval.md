JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/VertexAiRagRetrieval.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.retrieval](package-summary.html)
  2. [VertexAiRagRetrieval](VertexAiRagRetrieval.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. VertexAiRagRetrieval(String, String, VertexRagServiceClient, String, List, Double)
  5. Method Details
     1. processLlmRequest(LlmRequest.Builder, ToolContext)
     2. runAsync(Map, ToolContext)



# Class VertexAiRagRetrieval

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.retrieval.BaseRetrievalTool](BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")

com.google.adk.tools.retrieval.VertexAiRagRetrieval

* * *

public class VertexAiRagRetrieval extends [BaseRetrievalTool](BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")

A retrieval tool that fetches context from Vertex AI RAG. 

This tool allows to retrieve relevant information based on a query using Vertex AI RAG service. It supports configuration of rag resources and a vector distance threshold.

  * ## Constructor Summary

Constructors

Constructor

Description

`VertexAiRagRetrieval([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, com.google.cloud.aiplatform.v1.VertexRagServiceClient vertexRagServiceClient, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") parent, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.cloud.aiplatform.v1.RetrieveContextsRequest.VertexRagStore.RagResource> ragResources, [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") vectorDistanceThreshold)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class com.google.adk.tools.retrieval.[BaseRetrievalTool](BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")

`[declaration](BaseRetrievalTool.html#declaration\(\))`

### Methods inherited from class com.google.adk.tools.[BaseTool](../BaseTool.html "class in com.google.adk.tools")

`[description](../BaseTool.html#description\(\)), [longRunning](../BaseTool.html#longRunning\(\)), [name](../BaseTool.html#name\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### VertexAiRagRetrieval

public VertexAiRagRetrieval(@Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, @Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, @Nonnull com.google.cloud.aiplatform.v1.VertexRagServiceClient vertexRagServiceClient, @Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") parent, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.cloud.aiplatform.v1.RetrieveContextsRequest.VertexRagStore.RagResource> ragResources, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") vectorDistanceThreshold)

  * ## Method Details

    * ### processLlmRequest

@CanIgnoreReturnValue public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's [`BaseTool.declaration()`](../BaseTool.html#declaration\(\)) to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.

Overrides:
    `[processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 2025\. All rights reserved.
