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
     3. saveInputBlobsAsArtifacts()
     4. streamingMode()
     5. toolExecutionMode()
     6. outputAudioTranscription()
     7. inputAudioTranscription()
     8. maxLlmCalls()
     9. autoCreateSession()
     10. toBuilder()
     11. builder()
     12. builder(RunConfig)

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

Tool execution mode for the runner, when they are multiple tools requested (by the models or callbacks).

  * ## Constructor Summary

Constructors

Constructor

Description

`RunConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract boolean`

`autoCreateSession()`

 

`static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`builder([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

 

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

    * ### toBuilder

public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") toBuilder()

    * ### builder

public static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") builder()

    * ### builder

public static [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") builder([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)




* * *

Copyright (C) 1980\. All rights reserved.
