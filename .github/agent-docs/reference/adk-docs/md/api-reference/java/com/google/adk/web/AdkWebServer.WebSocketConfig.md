JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.WebSocketConfig.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [WebSocketConfig](AdkWebServer.WebSocketConfig.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. WebSocketConfig(AdkWebServer.LiveWebSocketHandler)
  5. Method Details
     1. registerWebSocketHandlers(WebSocketHandlerRegistry)



# Class AdkWebServer.WebSocketConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer.WebSocketConfig

All Implemented Interfaces:
    `org.springframework.web.socket.config.annotation.WebSocketConfigurer`

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

@Configuration @EnableWebSocket public static class AdkWebServer.WebSocketConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements org.springframework.web.socket.config.annotation.WebSocketConfigurer

Configuration class for WebSocket handling.

  * ## Constructor Summary

Constructors

Constructor

Description

`WebSocketConfig([AdkWebServer.LiveWebSocketHandler](AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web") liveWebSocketHandler)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`registerWebSocketHandlers(org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry registry)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### WebSocketConfig

@Autowired public WebSocketConfig([AdkWebServer.LiveWebSocketHandler](AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web") liveWebSocketHandler)

  * ## Method Details

    * ### registerWebSocketHandlers

public void registerWebSocketHandlers(org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry registry)

Specified by:
    `registerWebSocketHandlers` in interface `org.springframework.web.socket.config.annotation.WebSocketConfigurer`




* * *

Copyright (C) 2025\. All rights reserved.
