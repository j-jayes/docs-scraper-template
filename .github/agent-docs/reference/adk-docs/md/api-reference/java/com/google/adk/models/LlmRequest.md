JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmRequest.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [LlmRequest](LlmRequest.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LlmRequest()
  6. Method Details
     1. model()
     2. contents()
     3. config()
     4. liveConnectConfig()
     5. tools()
     6. getFirstSystemInstruction()
     7. getSystemInstructions()
     8. builder()
     9. toBuilder()



# Class LlmRequest

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.models.LlmRequest

* * *

public abstract class LlmRequest extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Represents a request to be sent to the LLM.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

Builder for constructing [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") instances.

  * ## Constructor Summary

Constructors

Constructor

Description

`LlmRequest()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig>`

`config()`

Returns the configuration for content generation.

`abstract [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content>`

`contents()`

Returns the list of content sent to the LLM.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`getFirstSystemInstruction()`

returns the first system instruction text from the request if present.

`com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`getSystemInstructions()`

Returns all system instruction texts from the request as an immutable list.

`abstract com.google.genai.types.LiveConnectConfig`

`liveConnectConfig()`

Returns the configuration for live connections.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`model()`

Returns the name of the LLM model to be used.

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`toBuilder()`

 

`abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`tools()`

Returns a map of tools available to the LLM.

### Methods inherited from class com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\)), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\)), [getMapper](../JsonBaseModel.html#getMapper\(\)), [toJson](../JsonBaseModel.html#toJson\(\)), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\)), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LlmRequest

public LlmRequest()

  * ## Method Details

    * ### model

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> model()

Returns the name of the LLM model to be used. If not set, the default model of the LLM class will be used.

Returns:
    An optional string representing the model name.

    * ### contents

public abstract [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> contents()

Returns the list of content sent to the LLM.

Returns:
    A list of `Content` objects.

    * ### config

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config()

Returns the configuration for content generation.

Returns:
    An optional `GenerateContentConfig` object containing the generation settings.

    * ### liveConnectConfig

public abstract com.google.genai.types.LiveConnectConfig liveConnectConfig()

Returns the configuration for live connections. Populated using the RunConfig in the InvocationContext.

Returns:
    An optional `LiveConnectConfig` object containing the live connection settings.

    * ### tools

public abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools()

Returns a map of tools available to the LLM.

Returns:
    A map where keys are tool names and values are [`BaseTool`](../tools/BaseTool.html "class in com.google.adk.tools") instances.

    * ### getFirstSystemInstruction

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getFirstSystemInstruction()

returns the first system instruction text from the request if present.

    * ### getSystemInstructions

public com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> getSystemInstructions()

Returns all system instruction texts from the request as an immutable list.

    * ### builder

public static [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") builder()

    * ### toBuilder

public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") toBuilder()




* * *

Copyright (C) 2025\. All rights reserved.
