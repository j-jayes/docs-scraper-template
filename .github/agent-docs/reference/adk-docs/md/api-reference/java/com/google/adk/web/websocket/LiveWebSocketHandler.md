JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/LiveWebSocketHandler.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.websocket](package-summary.html)
  2. [LiveWebSocketHandler](LiveWebSocketHandler.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. LiveWebSocketHandler(ObjectMapper, BaseSessionService, RunnerService)
  5. Method Details
     1. afterConnectionEstablished(WebSocketSession)
     2. handleTextMessage(WebSocketSession, TextMessage)
     3. handleTransportError(WebSocketSession, Throwable)
     4. afterConnectionClosed(WebSocketSession, CloseStatus)

Hide sidebar  Show sidebar

# Class LiveWebSocketHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

org.springframework.web.socket.handler.AbstractWebSocketHandler 

org.springframework.web.socket.handler.TextWebSocketHandler 

com.google.adk.web.websocket.LiveWebSocketHandler

All Implemented Interfaces:
    `org.springframework.web.socket.WebSocketHandler`

* * *

@Component public class LiveWebSocketHandler extends org.springframework.web.socket.handler.TextWebSocketHandler

WebSocket Handler for the /run_live endpoint. 

Manages bidirectional communication for live agent interactions. Assumes the com.google.adk.runner.Runner class has a method: `public Flowable<Event> runLive(Session session, Flowable<LiveRequest> liveRequests, List<String> modalities)`

  * ## Constructor Summary

Constructors

Constructor

Description

`LiveWebSocketHandler(com.fasterxml.jackson.databind.ObjectMapper objectMapper, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [RunnerService](../service/RunnerService.html "class in com.google.adk.web.service") runnerService)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`afterConnectionClosed(org.springframework.web.socket.WebSocketSession wsSession, org.springframework.web.socket.CloseStatus status)`

 

`void`

`afterConnectionEstablished(org.springframework.web.socket.WebSocketSession wsSession)`

 

`protected void`

`handleTextMessage(org.springframework.web.socket.WebSocketSession wsSession, org.springframework.web.socket.TextMessage message)`

 

`void`

`handleTransportError(org.springframework.web.socket.WebSocketSession wsSession, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") exception)`

 

### Methods inherited from class org.springframework.web.socket.handler.TextWebSocketHandler

`handleBinaryMessage`

### Methods inherited from class org.springframework.web.socket.handler.AbstractWebSocketHandler

`handleMessage, handlePongMessage, supportsPartialMessages`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LiveWebSocketHandler

@Autowired public LiveWebSocketHandler(com.fasterxml.jackson.databind.ObjectMapper objectMapper, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [RunnerService](../service/RunnerService.html "class in com.google.adk.web.service") runnerService)

  * ## Method Details

    * ### afterConnectionEstablished

public void afterConnectionEstablished(org.springframework.web.socket.WebSocketSession wsSession) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Specified by:
    `afterConnectionEstablished` in interface `org.springframework.web.socket.WebSocketHandler`
Overrides:
    `afterConnectionEstablished` in class `org.springframework.web.socket.handler.AbstractWebSocketHandler`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`

    * ### handleTextMessage

protected void handleTextMessage(org.springframework.web.socket.WebSocketSession wsSession, org.springframework.web.socket.TextMessage message) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Overrides:
    `handleTextMessage` in class `org.springframework.web.socket.handler.AbstractWebSocketHandler`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`

    * ### handleTransportError

public void handleTransportError(org.springframework.web.socket.WebSocketSession wsSession, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") exception) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Specified by:
    `handleTransportError` in interface `org.springframework.web.socket.WebSocketHandler`
Overrides:
    `handleTransportError` in class `org.springframework.web.socket.handler.AbstractWebSocketHandler`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`

    * ### afterConnectionClosed

public void afterConnectionClosed(org.springframework.web.socket.WebSocketSession wsSession, org.springframework.web.socket.CloseStatus status) throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Specified by:
    `afterConnectionClosed` in interface `org.springframework.web.socket.WebSocketHandler`
Overrides:
    `afterConnectionClosed` in class `org.springframework.web.socket.handler.AbstractWebSocketHandler`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
