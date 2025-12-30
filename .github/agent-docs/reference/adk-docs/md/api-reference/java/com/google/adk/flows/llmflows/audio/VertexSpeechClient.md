JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/VertexSpeechClient.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.flows.llmflows.audio](package-summary.html)
  2. [VertexSpeechClient](VertexSpeechClient.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. VertexSpeechClient()
  5. Method Details
     1. recognize(RecognitionConfig, RecognitionAudio)
     2. close()



# Class VertexSpeechClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.audio.VertexSpeechClient

All Implemented Interfaces:
    `[SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

* * *

public class VertexSpeechClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")

Implementation of SpeechClientInterface using Vertex AI SpeechClient.

  * ## Constructor Summary

Constructors

Constructor

Description

`VertexSpeechClient()`

Constructs a VertexSpeechClient, initializing the underlying Google Cloud SpeechClient.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Closes the client and releases any resources.

`com.google.cloud.speech.v1.RecognizeResponse`

`recognize(com.google.cloud.speech.v1.RecognitionConfig config, com.google.cloud.speech.v1.RecognitionAudio audio)`

Performs synchronous speech recognition on the given audio input.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### VertexSpeechClient

public VertexSpeechClient() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")

Constructs a VertexSpeechClient, initializing the underlying Google Cloud SpeechClient.

Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- if SpeechClient creation fails.

  * ## Method Details

    * ### recognize

public com.google.cloud.speech.v1.RecognizeResponse recognize(com.google.cloud.speech.v1.RecognitionConfig config, com.google.cloud.speech.v1.RecognitionAudio audio)

Performs synchronous speech recognition on the given audio input.

Specified by:
    `[recognize](SpeechClientInterface.html#recognize\(com.google.cloud.speech.v1.RecognitionConfig,com.google.cloud.speech.v1.RecognitionAudio\))` in interface `[SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")`
Parameters:
    `config` \- Recognition configuration (e.g., language, encoding).
    `audio` \- Audio data to recognize.
Returns:
    The recognition result.

    * ### close

public void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Description copied from interface: `[SpeechClientInterface](SpeechClientInterface.html#close\(\))`

Closes the client and releases any resources.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Specified by:
    `[close](SpeechClientInterface.html#close\(\))` in interface `[SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")` \- if an error occurs during closing.




* * *

Copyright (C) 2025\. All rights reserved.
