JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [BaseTool](BaseTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. BaseTool(String, String)
     2. BaseTool(String, String, boolean)
  6. Method Details
     1. name()
     2. description()
     3. longRunning()
     4. declaration()
     5. customMetadata()
     6. setCustomMetadata(String, Object)
     7. runAsync(Map, ToolContext)
     8. runAsync(T, ToolContext)
     9. runAsync(T, ToolContext, ObjectMapper)
     10. runAsync(I, ToolContext, ObjectMapper, Class)
     11. runAsync(I, ToolContext, ObjectMapper, TypeReference)
     12. runAsync(I, ToolContext, Class)
     13. runAsync(I, ToolContext, TypeReference)
     14. processLlmRequest(LlmRequest.Builder, ToolContext)
     15. fromConfig(BaseTool.ToolConfig, String)

Hide sidebar  Show sidebar

# Class BaseTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.BaseTool

Direct Known Subclasses:
    `[AbstractMcpTool](mcp/AbstractMcpTool.html "class in com.google.adk.tools.mcp"), [AgentTool](AgentTool.html "class in com.google.adk.tools"), [BaseRetrievalTool](retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval"), [BuiltInCodeExecutionTool](BuiltInCodeExecutionTool.html "class in com.google.adk.tools"), [ExampleTool](ExampleTool.html "class in com.google.adk.tools"), [FunctionTool](FunctionTool.html "class in com.google.adk.tools"), [GoogleMapsTool](GoogleMapsTool.html "class in com.google.adk.tools"), [GoogleSearchTool](GoogleSearchTool.html "class in com.google.adk.tools"), [IntegrationConnectorTool](applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset"), [LoadArtifactsTool](LoadArtifactsTool.html "class in com.google.adk.tools"), [SetModelResponseTool](SetModelResponseTool.html "class in com.google.adk.tools"), [UrlContextTool](UrlContextTool.html "class in com.google.adk.tools"), [VertexAiSearchTool](VertexAiSearchTool.html "class in com.google.adk.tools")`

* * *

public abstract class BaseTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The base class for all ADK tools.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")`

Configuration class for tool arguments that allows arbitrary key-value pairs.

`static class `

`[BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Configuration class for a tool definition in YAML/JSON.

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`protected `

`BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`customMetadata()`

Returns a read-only view of the tool metadata.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`description()`

 

`static [BaseTool](BaseTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates a tool instance from a config.

`boolean`

`longRunning()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`name()`

 

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments, returning the results converted to a specified class.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool with generic arguments and returns a map of results.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results.

`void`

`setCustomMetadata([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") value)`

Sets custom metadata to the tool associated with a key.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseTool

protected BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### BaseTool

protected BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)

  * ## Method Details

    * ### name

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name()

    * ### description

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description()

    * ### longRunning

public boolean longRunning()

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Gets the `FunctionDeclaration` representation of this tool.

    * ### customMetadata

public com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customMetadata()

Returns a read-only view of the tool metadata.

    * ### setCustomMetadata

public void setCustomMetadata([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") key, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") value)

Sets custom metadata to the tool associated with a key.

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Calls a tool.

    * ### runAsync

public final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Calls a tool with generic arguments and returns a map of results. The args type `T` need to be serializable with [`JsonBaseModel.getMapper()`](../JsonBaseModel.html#getMapper\(\))

    * ### runAsync

public final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results. The args type `T` needs to be serializable with the provided `ObjectMapper`.

    * ### runAsync

public final <I,O> io.reactivex.rxjava3.core.Single<O> runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends O> oClass)

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class. The input type `I` needs to be serializable and the output type `O` needs to be deserializable with the provided `ObjectMapper`.

    * ### runAsync

public final <I,O> io.reactivex.rxjava3.core.Single<O> runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference. The input type `I` needs to be serializable and the output type `O` needs to be deserializable with the provided `ObjectMapper`.

    * ### runAsync

public final <I,O> io.reactivex.rxjava3.core.Single<O> runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends O> oClass)

Calls a tool with generic arguments, returning the results converted to a specified class. The input type `I` needs to be serializable and the output type `O` needs to be deserializable with [`JsonBaseModel.getMapper()`](../JsonBaseModel.html#getMapper\(\))

    * ### runAsync

public final <I,O> io.reactivex.rxjava3.core.Single<O> runAsync(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)

Calls a tool with generic arguments, returning the results converted to a specified type reference. The input type needs to be serializable and the output type needs to be deserializable with [`JsonBaseModel.getMapper()`](../JsonBaseModel.html#getMapper\(\))

    * ### processLlmRequest

@CanIgnoreReturnValue public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's `declaration()` to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.

    * ### fromConfig

public static [BaseTool](BaseTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Creates a tool instance from a config. 

Subclasses should override and implement this method to do custom initialization from a config.

Parameters:
    `config` \- The config for the tool.
    `configAbsPath` \- The absolute path to the config file that contains the tool config.
Returns:
    The tool instance.
Throws:
    `[ConfigAgentUtils.ConfigurationException](../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the tool cannot be created from the config.




* * *

Copyright (C) 1980\. All rights reserved.
