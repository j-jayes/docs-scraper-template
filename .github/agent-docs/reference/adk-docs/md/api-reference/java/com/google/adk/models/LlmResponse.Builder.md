JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmResponse.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [LlmResponse](LlmResponse.html)
  3. [Builder](LlmResponse.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. content(Content)
     2. interrupted(Boolean)
     3. groundingMetadata(GroundingMetadata)
     4. customMetadata(List)
     5. partial(Boolean)
     6. turnComplete(Boolean)
     7. errorCode(FinishReason)
     8. finishReason(FinishReason)
     9. avgLogprobs(Double)
     10. errorMessage(String)
     11. usageMetadata(GenerateContentResponseUsageMetadata)
     12. modelVersion(String)
     13. inputTranscription(Transcription)
     14. outputTranscription(Transcription)
     15. response(GenerateContentResponse)
     16. build()

Hide sidebar  Show sidebar

# Class LlmResponse.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.LlmResponse.Builder

Enclosing class:
    `[LlmResponse](LlmResponse.html "class in com.google.adk.models")`

* * *

public abstract static class LlmResponse.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for constructing [`LlmResponse`](LlmResponse.html "class in com.google.adk.models") instances.

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`avgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") avgLogprobs)`

 

`[LlmResponse](LlmResponse.html "class in com.google.adk.models")`

`build()`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`content(@Nullable com.google.genai.types.Content content)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`customMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata> customMetadata)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorCode(@Nullable com.google.genai.types.FinishReason errorCode)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorMessage)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`finishReason(@Nullable com.google.genai.types.FinishReason finishReason)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata groundingMetadata)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`inputTranscription(@Nullable com.google.genai.types.Transcription inputTranscription)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") interrupted)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`modelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelVersion)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`outputTranscription(@Nullable com.google.genai.types.Transcription outputTranscription)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") partial)`

 

`final [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`response(com.google.genai.types.GenerateContentResponse response)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") turnComplete)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`usageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### content

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") content(@Nullable com.google.genai.types.Content content)

    * ### interrupted

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") interrupted)

    * ### groundingMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata groundingMetadata)

    * ### customMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") customMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata> customMetadata)

    * ### partial

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") partial)

    * ### turnComplete

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") turnComplete)

    * ### errorCode

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorCode(@Nullable com.google.genai.types.FinishReason errorCode)

    * ### finishReason

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") finishReason(@Nullable com.google.genai.types.FinishReason finishReason)

    * ### avgLogprobs

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") avgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") avgLogprobs)

    * ### errorMessage

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorMessage)

    * ### usageMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") usageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)

    * ### modelVersion

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") modelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelVersion)

    * ### inputTranscription

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") inputTranscription(@Nullable com.google.genai.types.Transcription inputTranscription)

    * ### outputTranscription

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") outputTranscription(@Nullable com.google.genai.types.Transcription outputTranscription)

    * ### response

@CanIgnoreReturnValue public final [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") response(com.google.genai.types.GenerateContentResponse response)

    * ### build

public [LlmResponse](LlmResponse.html "class in com.google.adk.models") build()




* * *

Copyright (C) 1980\. All rights reserved.
