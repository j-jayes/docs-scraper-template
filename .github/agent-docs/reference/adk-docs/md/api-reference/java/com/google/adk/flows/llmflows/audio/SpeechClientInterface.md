JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpeechClientInterface.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.flows.llmflows.audio](package-summary.html)
  2. [SpeechClientInterface](SpeechClientInterface.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. recognize(RecognitionConfig, RecognitionAudio)
     2. close()



# Interface SpeechClientInterface

All Superinterfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

All Known Implementing Classes:
    `[VertexSpeechClient](VertexSpeechClient.html "class in com.google.adk.flows.llmflows.audio")`

* * *

public interface SpeechClientInterface extends [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")

Interface for a speech-to-text client. Allows for different implementations (e.g., Cloud, Mocks).

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`void`

`close()`

Closes the client and releases any resources.

`com.google.cloud.speech.v1.RecognizeResponse`

`recognize(com.google.cloud.speech.v1.RecognitionConfig config, com.google.cloud.speech.v1.RecognitionAudio audio)`

Performs synchronous speech recognition.




  * ## Method Details

    * ### recognize

com.google.cloud.speech.v1.RecognizeResponse recognize(com.google.cloud.speech.v1.RecognitionConfig config, com.google.cloud.speech.v1.RecognitionAudio audio) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Performs synchronous speech recognition.

Parameters:
    `config` \- The recognition configuration.
    `audio` \- The audio data to transcribe.
Returns:
    The recognition response.
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")` \- if an error occurs during recognition.

    * ### close

void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Closes the client and releases any resources.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")` \- if an error occurs during closing.




* * *

Copyright (C) 2025\. All rights reserved.
