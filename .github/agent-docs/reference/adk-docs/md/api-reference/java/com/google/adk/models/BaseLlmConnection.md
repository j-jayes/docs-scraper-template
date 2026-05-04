JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseLlmConnection.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [BaseLlmConnection](BaseLlmConnection.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. sendHistory(List)
     2. sendContent(Content)
     3. sendRealtime(Blob)
     4. receive()
     5. close()
     6. close(Throwable)

Hide sidebar  Show sidebar

# Interface BaseLlmConnection

All Known Implementing Classes:
    `[GeminiLlmConnection](GeminiLlmConnection.html "class in com.google.adk.models")`

* * *

public interface BaseLlmConnection

The base class for a live model connection.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`void`

`close()`

Closes the connection.

`void`

`close([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") throwable)`

Closes the connection with an error.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")>`

`receive()`

Receives the model responses.

`io.reactivex.rxjava3.core.Completable`

`sendContent(com.google.genai.types.Content content)`

Sends a user content to the model.

`io.reactivex.rxjava3.core.Completable`

`sendHistory([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content> history)`

Sends the conversation history to the model.

`io.reactivex.rxjava3.core.Completable`

`sendRealtime(com.google.genai.types.Blob blob)`

Sends a chunk of audio or a frame of video to the model in realtime.




  * ## Method Details

    * ### sendHistory

io.reactivex.rxjava3.core.Completable sendHistory([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content> history)

Sends the conversation history to the model. 

You call this method right after setting up the model connection. The model will respond if the last content is from user, otherwise it will wait for new user input before responding.

    * ### sendContent

io.reactivex.rxjava3.core.Completable sendContent(com.google.genai.types.Content content)

Sends a user content to the model. 

The model will respond immediately upon receiving the content. If you send function responses, all parts in the content should be function responses.

    * ### sendRealtime

io.reactivex.rxjava3.core.Completable sendRealtime(com.google.genai.types.Blob blob)

Sends a chunk of audio or a frame of video to the model in realtime. 

The model may not respond immediately upon receiving the blob. It will do voice activity detection and decide when to respond.

    * ### receive

io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")> receive()

Receives the model responses.

    * ### close

void close()

Closes the connection.

    * ### close

void close([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") throwable)

Closes the connection with an error.




* * *

Copyright (C) 1980\. All rights reserved.
