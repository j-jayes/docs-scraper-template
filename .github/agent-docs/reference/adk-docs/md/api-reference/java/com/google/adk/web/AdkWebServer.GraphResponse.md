JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.GraphResponse.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [GraphResponse](AdkWebServer.GraphResponse.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. dotSrc
  6. Constructor Details
     1. GraphResponse(String)
     2. GraphResponse()
  7. Method Details
     1. getDotSrc()



# Class AdkWebServer.GraphResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer.GraphResponse

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

public static class AdkWebServer.GraphResponse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

DTO for the response of GET /apps/{appName}/users/{userId}/sessions/{sessionId}/events/{eventId}/graph. Contains the graph representation (e.g., DOT source).

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`dotSrc`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`GraphResponse()`

 

`GraphResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dotSrc)`

Constructs a GraphResponse.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getDotSrc()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### dotSrc

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dotSrc

  * ## Constructor Details

    * ### GraphResponse

public GraphResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dotSrc)

Constructs a GraphResponse.

Parameters:
    `dotSrc` \- The graph source string (e.g., in DOT format).

    * ### GraphResponse

public GraphResponse()

  * ## Method Details

    * ### getDotSrc

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getDotSrc()




* * *

Copyright (C) 2025\. All rights reserved.
