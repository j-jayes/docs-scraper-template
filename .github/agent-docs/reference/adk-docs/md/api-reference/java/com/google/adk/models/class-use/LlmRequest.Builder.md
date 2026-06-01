JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmRequest.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](../package-summary.html)
  2. [LlmRequest](../LlmRequest.html)
  3. [Builder](../LlmRequest.Builder.html)



# Uses of Class  
com.google.adk.models.LlmRequest.Builder

Packages that use [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Package

Description

com.google.adk.agents

 

com.google.adk.codeexecutors

 

com.google.adk.models

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.tools

 

com.google.adk.tools.computeruse

 

com.google.adk.tools.retrieval

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../../agents/Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../../agents/Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.codeexecutors](../../codeexecutors/package-summary.html)

Methods in [com.google.adk.codeexecutors](../../codeexecutors/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`void`

BuiltInCodeExecutor.`[processLlmRequest](../../codeexecutors/BuiltInCodeExecutor.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

Pre-process the LLM request for Gemini 2.0+ models to use the code execution tool.

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Methods in [com.google.adk.models](../package-summary.html) that return [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendInstructions](../LlmRequest.Builder.html#appendInstructions\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> instructions)`

 

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendTools](../LlmRequest.Builder.html#appendTools\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.`[builder](../LlmRequest.html#builder\(\))()`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[config](../LlmRequest.Builder.html#config\(com.google.genai.types.GenerateContentConfig\))(com.google.genai.types.GenerateContentConfig config)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[contents](../LlmRequest.Builder.html#contents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content> contents)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[liveConnectConfig](../LlmRequest.Builder.html#liveConnectConfig\(com.google.genai.types.LiveConnectConfig\))(com.google.genai.types.LiveConnectConfig liveConnectConfig)`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[model](../LlmRequest.Builder.html#model\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)`

 

`final [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[outputSchema](../LlmRequest.Builder.html#outputSchema\(com.google.genai.types.Schema\))(com.google.genai.types.Schema schema)`

Sets the output schema for the LLM response.

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.`[toBuilder](../LlmRequest.html#toBuilder\(\))()`

 

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[tools](../LlmRequest.Builder.html#tools\(java.util.Map\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ContextFilterPlugin.`[beforeModelCallback](../../plugins/ContextFilterPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Filters the LLM request context by trimming recent turns and applying any custom filter.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

GlobalInstructionPlugin.`[beforeModelCallback](../../plugins/GlobalInstructionPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[beforeModelCallback](../../plugins/LoggingPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[beforeModelCallback](../../plugins/Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[beforeModelCallback](../../plugins/PluginManager.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ReplayPlugin.`[beforeModelCallback](../../plugins/ReplayPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[onModelErrorCallback](../../plugins/LoggingPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[onModelErrorCallback](../../plugins/Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[onModelErrorCallback](../../plugins/PluginManager.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[beforeModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback before LLM call.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[onModelErrorCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

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

ExampleTool.`[processLlmRequest](../../tools/ExampleTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleMapsTool.`[processLlmRequest](../../tools/GoogleMapsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleSearchTool.`[processLlmRequest](../../tools/GoogleSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[processLlmRequest](../../tools/LoadArtifactsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadMemoryTool.`[processLlmRequest](../../tools/LoadMemoryTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

UrlContextTool.`[processLlmRequest](../../tools/UrlContextTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

VertexAiSearchTool.`[processLlmRequest](../../tools/VertexAiSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.tools.computeruse](../../tools/computeruse/package-summary.html)

Methods in [com.google.adk.tools.computeruse](../../tools/computeruse/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

ComputerUseToolset.`[processLlmRequest](../../tools/computeruse/ComputerUseToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Adds computer use configuration to the LLM request.

  * ## Uses of [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") in [com.google.adk.tools.retrieval](../../tools/retrieval/package-summary.html)

Methods in [com.google.adk.tools.retrieval](../../tools/retrieval/package-summary.html) with parameters of type [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

VertexAiRagRetrieval.`[processLlmRequest](../../tools/retrieval/VertexAiRagRetrieval.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 




* * *

Copyright (C) 1980\. All rights reserved.
