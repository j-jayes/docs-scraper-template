JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SseServerParameters.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [SseServerParameters](SseServerParameters.html)
  3. [Builder](SseServerParameters.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. url(String)
     2. headers(Map)
     3. timeout(Duration)
     4. sseReadTimeout(Duration)
     5. build()



# Class SseServerParameters.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.SseServerParameters.Builder

Enclosing class:
    `[SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")`

* * *

public abstract static class SseServerParameters.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`headers([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> headers)`

Sets the headers for the SSE connection request.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`sseReadTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") sseReadTimeout)`

Sets the timeout for reading data from the SSE stream.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`timeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") timeout)`

Sets the timeout for the initial connection attempt.

`abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`url([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") url)`

Sets the URL of the SSE server.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### url

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") url([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") url)

Sets the URL of the SSE server.

    * ### headers

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") headers(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> headers)

Sets the headers for the SSE connection request.

    * ### timeout

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") timeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") timeout)

Sets the timeout for the initial connection attempt.

    * ### sseReadTimeout

public abstract [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") sseReadTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") sseReadTimeout)

Sets the timeout for reading data from the SSE stream.

    * ### build

public abstract [SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") build()

Builds a new [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp") instance.




* * *

Copyright (C) 2025\. All rights reserved.
