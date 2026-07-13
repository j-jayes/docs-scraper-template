JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/WebSocketConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.websocket](package-summary.html)
  2. [WebSocketConfig](WebSocketConfig.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. WebSocketConfig(LiveWebSocketHandler, AdkWebCorsProperties)
  5. Method Details
     1. registerWebSocketHandlers(WebSocketHandlerRegistry)

Hide sidebar  Show sidebar

# Class WebSocketConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.websocket.WebSocketConfig

All Implemented Interfaces:
    `org.springframework.web.socket.config.annotation.WebSocketConfigurer`

* * *

@Configuration @EnableWebSocket public class WebSocketConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements org.springframework.web.socket.config.annotation.WebSocketConfigurer

Configuration class for WebSocket handling.

  * ## Constructor Summary

Constructors

Constructor

Description

`WebSocketConfig([LiveWebSocketHandler](LiveWebSocketHandler.html "class in com.google.adk.web.websocket") liveWebSocketHandler, [AdkWebCorsProperties](../config/AdkWebCorsProperties.html "class in com.google.adk.web.config") corsProperties)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`registerWebSocketHandlers(org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry registry)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### WebSocketConfig

@Autowired public WebSocketConfig([LiveWebSocketHandler](LiveWebSocketHandler.html "class in com.google.adk.web.websocket") liveWebSocketHandler, [AdkWebCorsProperties](../config/AdkWebCorsProperties.html "class in com.google.adk.web.config") corsProperties)

  * ## Method Details

    * ### registerWebSocketHandlers

public void registerWebSocketHandlers(org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry registry)

Specified by:
    `registerWebSocketHandlers` in interface `org.springframework.web.socket.config.annotation.WebSocketConfigurer`




* * *

Copyright (C) 1980\. All rights reserved.
