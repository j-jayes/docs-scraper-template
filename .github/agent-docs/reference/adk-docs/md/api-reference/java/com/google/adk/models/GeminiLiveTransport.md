JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GeminiLiveTransport.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [GeminiLiveTransport](GeminiLiveTransport.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. sendClientContent(LiveSendClientContentParameters)
     2. sendRealtimeInput(LiveSendRealtimeInputParameters)
     3. sendToolResponse(LiveSendToolResponseParameters)
     4. receive(Consumer, Runnable)
     5. close()

Hide sidebar  Show sidebar

# Interface GeminiLiveTransport

* * *

public interface GeminiLiveTransport

The bidirectional live transport that [`GeminiLlmConnection`](GeminiLlmConnection.html "class in com.google.adk.models") drives. 

[`GeminiLlmConnection`](GeminiLlmConnection.html "class in com.google.adk.models") holds the translation logic; this is the transport beneath it, so the connection can drive any implementation. The default one delegates to a genai live session.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`close()`

Closes the transport.

`[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`receive([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.genai.types.LiveServerMessage> onMessage, [Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html "interface in java.lang") onStreamEnd)`

Registers the callback for messages the transport yields and a callback for when its receive stream ends.

`[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`sendClientContent(com.google.genai.types.LiveSendClientContentParameters params)`

Sends a client-content turn to the transport.

`[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`sendRealtimeInput(com.google.genai.types.LiveSendRealtimeInputParameters params)`

Sends realtime input (audio, video, or text) to the transport.

`[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`sendToolResponse(com.google.genai.types.LiveSendToolResponseParameters params)`

Sends a tool response to the transport.




  * ## Method Details

    * ### sendClientContent

[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> sendClientContent(com.google.genai.types.LiveSendClientContentParameters params)

Sends a client-content turn to the transport.

    * ### sendRealtimeInput

[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> sendRealtimeInput(com.google.genai.types.LiveSendRealtimeInputParameters params)

Sends realtime input (audio, video, or text) to the transport.

    * ### sendToolResponse

[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> sendToolResponse(com.google.genai.types.LiveSendToolResponseParameters params)

Sends a tool response to the transport.

    * ### receive

[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> receive([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.genai.types.LiveServerMessage> onMessage, [Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html "interface in java.lang") onStreamEnd)

Registers the callback for messages the transport yields and a callback for when its receive stream ends. An implementation whose stream ends only when the client closes never invokes `onStreamEnd`; one backed by a finite script invokes it when the script is exhausted, so the run can end.

    * ### close

[CompletableFuture](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CompletableFuture.html "class in java.util.concurrent")<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> close()

Closes the transport.




* * *

Copyright (C) 1980\. All rights reserved.
