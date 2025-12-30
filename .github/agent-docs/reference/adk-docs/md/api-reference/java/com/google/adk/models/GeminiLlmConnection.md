JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GeminiLlmConnection.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [GeminiLlmConnection](GeminiLlmConnection.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. sendHistory(List)
     2. sendContent(Content)
     3. sendRealtime(Blob)
     4. receive()
     5. close()
     6. close(Throwable)



# Class GeminiLlmConnection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.GeminiLlmConnection

All Implemented Interfaces:
    `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

* * *

public final class GeminiLlmConnection extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")

Manages a persistent, bidirectional connection to the Gemini model via WebSockets for real-time interaction. 

This connection allows sending conversation history, individual messages, function responses, and real-time media blobs (like audio chunks) while continuously receiving responses from the model.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Closes the connection.

`void`

`close([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") throwable)`

Closes the connection with an error.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")>`

`receive()`

Receives the model responses.

`io.reactivex.rxjava3.core.Completable`

`sendContent(com.google.genai.types.Content content)`

Sends a user content to the model.

`io.reactivex.rxjava3.core.Completable`

`sendHistory([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> history)`

Sends the conversation history to the model.

`io.reactivex.rxjava3.core.Completable`

`sendRealtime(com.google.genai.types.Blob blob)`

Sends a chunk of audio or a frame of video to the model in realtime.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### sendHistory

public io.reactivex.rxjava3.core.Completable sendHistory([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> history)

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#sendHistory\(java.util.List\))`

Sends the conversation history to the model. 

You call this method right after setting up the model connection. The model will respond if the last content is from user, otherwise it will wait for new user input before responding.

Specified by:
    `[sendHistory](BaseLlmConnection.html#sendHistory\(java.util.List\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

    * ### sendContent

public io.reactivex.rxjava3.core.Completable sendContent(com.google.genai.types.Content content)

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#sendContent\(com.google.genai.types.Content\))`

Sends a user content to the model. 

The model will respond immediately upon receiving the content. If you send function responses, all parts in the content should be function responses.

Specified by:
    `[sendContent](BaseLlmConnection.html#sendContent\(com.google.genai.types.Content\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

    * ### sendRealtime

public io.reactivex.rxjava3.core.Completable sendRealtime(com.google.genai.types.Blob blob)

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#sendRealtime\(com.google.genai.types.Blob\))`

Sends a chunk of audio or a frame of video to the model in realtime. 

The model may not respond immediately upon receiving the blob. It will do voice activity detection and decide when to respond.

Specified by:
    `[sendRealtime](BaseLlmConnection.html#sendRealtime\(com.google.genai.types.Blob\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

    * ### receive

public io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")> receive()

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#receive\(\))`

Receives the model responses.

Specified by:
    `[receive](BaseLlmConnection.html#receive\(\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

    * ### close

public void close()

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#close\(\))`

Closes the connection.

Specified by:
    `[close](BaseLlmConnection.html#close\(\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

    * ### close

public void close([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") throwable)

Description copied from interface: `[BaseLlmConnection](BaseLlmConnection.html#close\(java.lang.Throwable\))`

Closes the connection with an error.

Specified by:
    `[close](BaseLlmConnection.html#close\(java.lang.Throwable\))` in interface `[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`




* * *

Copyright (C) 2025\. All rights reserved.
