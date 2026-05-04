JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SseServerParameters.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [SseServerParameters](SseServerParameters.html)
  3. [Builder](SseServerParameters.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. url(String)
     2. sseEndpoint(String)
     3. headers(Map)
     4. timeout(Duration)
     5. sseReadTimeout(Duration)
     6. build()

Hide sidebar  Show sidebar

# Class SseServerParameters.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.SseServerParameters.Builder

Enclosing class:
    `[SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")`

* * *

public abstract static class SseServerParameters.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`abstract [SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")`

`build()`

Builds a new [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp") instance.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`headers(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> headers)`

Sets the headers for the SSE connection request.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`sseEndpoint([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sseEndpoint)`

Sets the endpoint to connect to on the SSE server.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`sseReadTimeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") sseReadTimeout)`

Sets the timeout for reading data from the SSE stream.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`timeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") timeout)`

Sets the timeout for the initial connection attempt.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`url([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)`

Sets the URL of the SSE server.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### url

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") url([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)

Sets the URL of the SSE server.

    * ### sseEndpoint

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") sseEndpoint([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sseEndpoint)

Sets the endpoint to connect to on the SSE server.

    * ### headers

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") headers(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> headers)

Sets the headers for the SSE connection request.

    * ### timeout

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") timeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") timeout)

Sets the timeout for the initial connection attempt.

    * ### sseReadTimeout

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") sseReadTimeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") sseReadTimeout)

Sets the timeout for reading data from the SSE stream.

    * ### build

public abstract [SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") build()

Builds a new [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp") instance.




* * *

Copyright (C) 1980\. All rights reserved.
