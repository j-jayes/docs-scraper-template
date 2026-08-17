JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RunConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [RunConfig](RunConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. RunConfig()
  6. Method Details
     1. speechConfig()
     2. responseModalities()
     3. avatarConfig()
     4. saveInputBlobsAsArtifacts()
     5. streamingMode()
     6. toolExecutionMode()
     7. outputAudioTranscription()
     8. inputAudioTranscription()
     9. maxLlmCalls()
     10. autoCreateSession()
     11. groupFunctionResponsesInHistoryOverride()
     12. groupFunctionResponsesInHistory()
     13. customMetadata()
     14. toBuilder()
     15. builder()
     16. builder(RunConfig)

Hide sidebar  Show sidebar

# Class RunConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.RunConfig

* * *

public abstract class RunConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration to modify an agent's LLM's underlying behavior.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

`static enum `

`[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")`

Streaming mode for the runner.

`static enum `

`[RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents")`

Execution mode when the model requests multiple tools.

  * ## Constructor Summary

Constructors

Constructor

Description

`RunConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`abstract boolean`

`autoCreateSession()`

 

`abstract @Nullable com.google.genai.types.AvatarConfig`

`avatarConfig()`

 

`static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`builder([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`customMetadata()`

 

`final boolean`

`groupFunctionResponsesInHistory()`

Deprecated.

Expected only for specific model endpoints.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`groupFunctionResponsesInHistoryOverride()`

Deprecated.

Expected only for specific model endpoints.

`abstract @Nullable com.google.genai.types.AudioTranscriptionConfig`

`inputAudioTranscription()`

 

`abstract int`

`maxLlmCalls()`

 

`abstract @Nullable com.google.genai.types.AudioTranscriptionConfig`

`outputAudioTranscription()`

 

`abstract com.google.common.collect.ImmutableList<com.google.genai.types.Modality>`

`responseModalities()`

 

`abstract boolean`

`saveInputBlobsAsArtifacts()`

 

`abstract @Nullable com.google.genai.types.SpeechConfig`

`speechConfig()`

 

`abstract [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")`

`streamingMode()`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`toBuilder()`

 

`abstract [RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents")`

`toolExecutionMode()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### RunConfig

public RunConfig()

  * ## Method Details

    * ### speechConfig

public abstract @Nullable com.google.genai.types.SpeechConfig speechConfig()

    * ### responseModalities

public abstract com.google.common.collect.ImmutableList<com.google.genai.types.Modality> responseModalities()

    * ### avatarConfig

public abstract @Nullable com.google.genai.types.AvatarConfig avatarConfig()

    * ### saveInputBlobsAsArtifacts

public abstract boolean saveInputBlobsAsArtifacts()

    * ### streamingMode

public abstract [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode()

    * ### toolExecutionMode

public abstract [RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode()

    * ### outputAudioTranscription

public abstract @Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription()

    * ### inputAudioTranscription

public abstract @Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription()

    * ### maxLlmCalls

public abstract int maxLlmCalls()

    * ### autoCreateSession

public abstract boolean autoCreateSession()

    * ### groupFunctionResponsesInHistoryOverride

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> groupFunctionResponsesInHistoryOverride()

Deprecated.

Expected only for specific model endpoints.

Three-state override for grouping function calls before function responses in history (FC1, FC2, FR1, FR2) instead of pairing each response with its call (FC1, FR1, FC2, FR2). 

Empty (default) groups only for models that require it (Gemini 3); when present the value applies to all models. 

Not needed for the core ADK Gemini implementation, which already groups automatically for Gemini 3. Kept for backwards compatibility with other model implementations that route to endpoints requiring the grouped form.

    * ### groupFunctionResponsesInHistory

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public final boolean groupFunctionResponsesInHistory()

Deprecated.

Expected only for specific model endpoints.

Whether grouping is explicitly enabled; equivalent to ` groupFunctionResponsesInHistoryOverride().orElse(false)`. Retained for backwards compatibility.

    * ### customMetadata

public abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> customMetadata()

    * ### toBuilder

public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") toBuilder()

    * ### builder

public static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") builder()

    * ### builder

public static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") builder([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)




* * *

Copyright (C) 1980\. All rights reserved.
