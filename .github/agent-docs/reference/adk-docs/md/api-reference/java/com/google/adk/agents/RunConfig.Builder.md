JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RunConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     2. speechConfig(SpeechConfig)
     3. setResponseModalities(Iterable)
     4. responseModalities(Iterable)
     5. setSaveInputBlobsAsArtifacts(boolean)
     6. saveInputBlobsAsArtifacts(boolean)
     7. setStreamingMode(RunConfig.StreamingMode)
     8. streamingMode(RunConfig.StreamingMode)
     9. setToolExecutionMode(RunConfig.ToolExecutionMode)
     10. toolExecutionMode(RunConfig.ToolExecutionMode)
     11. setOutputAudioTranscription(AudioTranscriptionConfig)
     12. outputAudioTranscription(AudioTranscriptionConfig)
     13. setInputAudioTranscription(AudioTranscriptionConfig)
     14. inputAudioTranscription(AudioTranscriptionConfig)
     15. setMaxLlmCalls(int)
     16. maxLlmCalls(int)
     17. setAutoCreateSession(boolean)
     18. autoCreateSession(boolean)
     19. build()

Hide sidebar  Show sidebar

# Class RunConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.RunConfig.Builder

Enclosing class:
    `[RunConfig](RunConfig.html "class in com.google.adk.agents")`

* * *

public abstract static class RunConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`RunConfig`](RunConfig.html "class in com.google.adk.agents").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`autoCreateSession(boolean autoCreateSession)`

 

`[RunConfig](RunConfig.html "class in com.google.adk.agents")`

`build()`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`inputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`maxLlmCalls(int maxLlmCalls)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`outputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`responseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<com.google.genai.types.Modality> responseModalities)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`saveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)`

 

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setAutoCreateSession(boolean autoCreateSession)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setInputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setMaxLlmCalls(int maxLlmCalls)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setOutputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setResponseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<com.google.genai.types.Modality> responseModalities)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setSaveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setSpeechConfig(@Nullable com.google.genai.types.SpeechConfig speechConfig)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setStreamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)`

Deprecated.

`final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`setToolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)`

Deprecated.

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`speechConfig(@Nullable com.google.genai.types.SpeechConfig speechConfig)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`streamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)`

 

`abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")`

`toolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setSpeechConfig

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setSpeechConfig(@Nullable com.google.genai.types.SpeechConfig speechConfig)

Deprecated.

    * ### speechConfig

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") speechConfig(@Nullable com.google.genai.types.SpeechConfig speechConfig)

    * ### setResponseModalities

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setResponseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<com.google.genai.types.Modality> responseModalities)

Deprecated.

    * ### responseModalities

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") responseModalities([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<com.google.genai.types.Modality> responseModalities)

    * ### setSaveInputBlobsAsArtifacts

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setSaveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)

Deprecated.

    * ### saveInputBlobsAsArtifacts

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") saveInputBlobsAsArtifacts(boolean saveInputBlobsAsArtifacts)

    * ### setStreamingMode

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setStreamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)

Deprecated.

    * ### streamingMode

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") streamingMode([RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") streamingMode)

    * ### setToolExecutionMode

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setToolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)

Deprecated.

    * ### toolExecutionMode

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") toolExecutionMode([RunConfig.ToolExecutionMode](RunConfig.ToolExecutionMode.html "enum class in com.google.adk.agents") toolExecutionMode)

    * ### setOutputAudioTranscription

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setOutputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)

Deprecated.

    * ### outputAudioTranscription

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") outputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig outputAudioTranscription)

    * ### setInputAudioTranscription

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setInputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)

Deprecated.

    * ### inputAudioTranscription

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") inputAudioTranscription(@Nullable com.google.genai.types.AudioTranscriptionConfig inputAudioTranscription)

    * ### setMaxLlmCalls

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setMaxLlmCalls(int maxLlmCalls)

Deprecated.

    * ### maxLlmCalls

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") maxLlmCalls(int maxLlmCalls)

    * ### setAutoCreateSession

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") setAutoCreateSession(boolean autoCreateSession)

Deprecated.

    * ### autoCreateSession

@CanIgnoreReturnValue public abstract [RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents") autoCreateSession(boolean autoCreateSession)

    * ### build

public [RunConfig](RunConfig.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 1980\. All rights reserved.
