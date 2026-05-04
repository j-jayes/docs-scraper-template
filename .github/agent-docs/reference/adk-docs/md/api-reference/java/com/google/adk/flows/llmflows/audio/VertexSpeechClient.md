JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/VertexSpeechClient.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows.audio](package-summary.html)
  2. [VertexSpeechClient](VertexSpeechClient.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. VertexSpeechClient()
  5. Method Details
     1. recognize(RecognitionConfig, RecognitionAudio)
     2. close()

Hide sidebar  Show sidebar

# Class VertexSpeechClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.audio.VertexSpeechClient

All Implemented Interfaces:
    `[SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

* * *

public class VertexSpeechClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")

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

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### VertexSpeechClient

public VertexSpeechClient() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Constructs a VertexSpeechClient, initializing the underlying Google Cloud SpeechClient.

Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- if SpeechClient creation fails.

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

public void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")

Description copied from interface: `[SpeechClientInterface](SpeechClientInterface.html#close\(\))`

Closes the client and releases any resources.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\))` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`
Specified by:
    `[close](SpeechClientInterface.html#close\(\))` in interface `[SpeechClientInterface](SpeechClientInterface.html "interface in com.google.adk.flows.llmflows.audio")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")` \- if an error occurs during closing.




* * *

Copyright (C) 1980\. All rights reserved.
