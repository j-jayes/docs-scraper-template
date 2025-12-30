JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmResponse.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [LlmResponse](LlmResponse.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. content()
     2. groundingMetadata()
     3. partial()
     4. turnComplete()
     5. errorCode()
     6. errorMessage()
     7. interrupted()
     8. usageMetadata()
     9. toBuilder()
     10. builder()
     11. create(List)
     12. create(GenerateContentResponse)



# Class LlmResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.models.LlmResponse

* * *

public abstract class LlmResponse extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Represents a response received from the LLM.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

Builder for constructing [`LlmResponse`](LlmResponse.html "class in com.google.adk.models") instances.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`content()`

Returns the content of the first candidate in the response, if available.

`static [LlmResponse](LlmResponse.html "class in com.google.adk.models")`

`create(com.google.genai.types.GenerateContentResponse response)`

 

`static [LlmResponse](LlmResponse.html "class in com.google.adk.models")`

`create([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Candidate> candidates)`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason>`

`errorCode()`

Error code if the response is an error.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`errorMessage()`

Error message if the response is an error.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata>`

`groundingMetadata()`

Returns the grounding metadata of the first candidate in the response, if available.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`interrupted()`

Indicates that LLM was interrupted when generating the content.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`partial()`

Indicates whether the text content is part of a unfinished text stream.

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`toBuilder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`turnComplete()`

Indicates whether the response from the model is complete.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata>`

`usageMetadata()`

Usage metadata about the response(s).

### Methods inherited from class com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\)), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\)), [getMapper](../JsonBaseModel.html#getMapper\(\)), [toJson](../JsonBaseModel.html#toJson\(\)), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\)), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### content

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content()

Returns the content of the first candidate in the response, if available.

Returns:
    An `Content` of the first `Candidate` in the `GenerateContentResponse` if the response contains at least one candidate., or an empty optional if no candidates are present in the response.

    * ### groundingMetadata

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata()

Returns the grounding metadata of the first candidate in the response, if available.

Returns:
    An [`Optional`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util") containing `GroundingMetadata` or empty.

    * ### partial

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial()

Indicates whether the text content is part of a unfinished text stream. 

Only used for streaming mode and when the content is plain text.

    * ### turnComplete

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete()

Indicates whether the response from the model is complete. 

Only used for streaming mode.

    * ### errorCode

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode()

Error code if the response is an error. Code varies by model.

    * ### errorMessage

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage()

Error message if the response is an error.

    * ### interrupted

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted()

Indicates that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

    * ### usageMetadata

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata> usageMetadata()

Usage metadata about the response(s).

    * ### toBuilder

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") toBuilder()

    * ### builder

public static [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") builder()

    * ### create

public static [LlmResponse](LlmResponse.html "class in com.google.adk.models") create([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Candidate> candidates)

    * ### create

public static [LlmResponse](LlmResponse.html "class in com.google.adk.models") create(com.google.genai.types.GenerateContentResponse response)




* * *

Copyright (C) 2025\. All rights reserved.
