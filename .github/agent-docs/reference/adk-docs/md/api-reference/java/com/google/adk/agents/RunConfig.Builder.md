JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RunConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [RunConfig](RunConfig.html)
  3. [Builder](RunConfig.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. setSpeechConfig(SpeechConfig)
     2. setResponseModalities(Iterable)
     3. setSaveInputBlobsAsArtifacts(boolean)
     4. setStreamingMode(RunConfig.StreamingMode)
     5. setToolExecutionMode(RunConfig.ToolExecutionMode)
     6. setOutputAudioTranscription(AudioTranscriptionConfig)
     7. setInputAudioTranscription(AudioTranscriptionConfig)
     8. setMaxLlmCalls(int)
     9. build()

Hide sidebar  Show sidebar

# Class RunConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.RunConfig.Builder

Enclosing class:
    `[RunConfig](RunConfig.html "class in com.google.adk.agents")`

* * *

public abstract static class RunConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

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

`[RunConfig](RunConfig.html "class in com.google.adk.agents")`

`build()`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setInputAudioTranscription(com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setMaxLlmCalls(int maxLlmCalls)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setOutputAudioTranscription(com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setResponseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<com.google.genai.types.Modality> responseModalities)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setSaveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setSpeechConfig(com.google.genai.types.SpeechConfig speechConfig)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setStreamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setToolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setSpeechConfig

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setSpeechConfig(@Nullable com.google.genai.types.SpeechConfig speechConfig)

    * ### setResponseModalities

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setResponseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<com.google.genai.types.Modality> responseModalities)

    * ### setSaveInputBlobsAsArtifacts

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setSaveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)

    * ### setStreamingMode

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setStreamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)

    * ### setToolExecutionMode

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setToolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)

    * ### setOutputAudioTranscription

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setOutputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)

    * ### setInputAudioTranscription

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setInputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)

    * ### setMaxLlmCalls

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setMaxLlmCalls(int maxLlmCalls)

    * ### build

public [RunConfig](RunConfig.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 1980\. All rights reserved.
