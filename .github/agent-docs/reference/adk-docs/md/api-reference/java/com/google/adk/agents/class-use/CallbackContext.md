JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../CallbackContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [CallbackContext](../CallbackContext.html)



# Uses of Class  
com.google.adk.agents.CallbackContext

Packages that use [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.tools

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Callbacks.AfterAgentCallback.`[call](../Callbacks.AfterAgentCallback.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback after agent runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

Callbacks.AfterAgentCallbackSync.`[call](../Callbacks.AfterAgentCallbackSync.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Callbacks.BeforeAgentCallback.`[call](../Callbacks.BeforeAgentCallback.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback before agent runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

Callbacks.BeforeAgentCallbackSync.`[call](../Callbacks.BeforeAgentCallbackSync.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallback.`[call](../Callbacks.OnModelErrorCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

Async callback when model call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallbackSync.`[call](../Callbacks.OnModelErrorCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[afterAgentCallback](../../plugins/LoggingPlugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[afterAgentCallback](../../plugins/Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[afterAgentCallback](../../plugins/PluginManager.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[afterModelCallback](../../plugins/LoggingPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[afterModelCallback](../../plugins/Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[afterModelCallback](../../plugins/PluginManager.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

LoggingPlugin.`[beforeAgentCallback](../../plugins/LoggingPlugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Plugin.`[beforeAgentCallback](../../plugins/Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

PluginManager.`[beforeAgentCallback](../../plugins/PluginManager.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

ContextFilterPlugin.`[beforeModelCallback](../../plugins/ContextFilterPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Filters the LLM request context by trimming recent turns and applying any custom filter.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

GlobalInstructionPlugin.`[beforeModelCallback](../../plugins/GlobalInstructionPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[beforeModelCallback](../../plugins/LoggingPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[beforeModelCallback](../../plugins/Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[beforeModelCallback](../../plugins/PluginManager.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

ReplayPlugin.`[beforeModelCallback](../../plugins/ReplayPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[onModelErrorCallback](../../plugins/LoggingPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[onModelErrorCallback](../../plugins/Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[onModelErrorCallback](../../plugins/PluginManager.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

Constructor parameters in [com.google.adk.plugins](../../plugins/package-summary.html) with type arguments of type [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[GlobalInstructionPlugin](../../plugins/GlobalInstructionPlugin.html#%3Cinit%3E\(java.util.function.Function\))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "class or interface in java.util.function")<[CallbackContext](../CallbackContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Maybe<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> instructionProvider)`

 

` `

`[GlobalInstructionPlugin](../../plugins/GlobalInstructionPlugin.html#%3Cinit%3E\(java.util.function.Function,java.lang.String\))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "class or interface in java.util.function")<[CallbackContext](../CallbackContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Maybe<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> instructionProvider, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[afterAgentCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[afterModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

BigQueryAgentAnalyticsPlugin.`[beforeAgentCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[beforeModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[onModelErrorCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Subclasses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Modifier and Type

Class

Description

`class `

`[ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools")`

ToolContext object provides a structured context for executing tools or functions.




* * *

Copyright (C) 1980\. All rights reserved.
