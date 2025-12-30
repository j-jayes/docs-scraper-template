JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SseServerParameters.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [SseServerParameters](SseServerParameters.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SseServerParameters()
  6. Method Details
     1. url()
     2. headers()
     3. timeout()
     4. sseReadTimeout()
     5. builder()



# Class SseServerParameters

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.SseServerParameters

* * *

public abstract class SseServerParameters extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Parameters for establishing a MCP Server-Sent Events (SSE) connection.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

Builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").

  * ## Constructor Summary

Constructors

Constructor

Description

`SseServerParameters()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`builder()`

Creates a new builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").

`abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`headers()`

Optional headers to include in the SSE connection request.

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`sseReadTimeout()`

The timeout for reading data from the SSE stream.

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`timeout()`

The timeout for the initial connection attempt.

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`url()`

The URL of the SSE server.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SseServerParameters

public SseServerParameters()

  * ## Method Details

    * ### url

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") url()

The URL of the SSE server.

    * ### headers

@Nullable public abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> headers()

Optional headers to include in the SSE connection request.

    * ### timeout

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") timeout()

The timeout for the initial connection attempt.

    * ### sseReadTimeout

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") sseReadTimeout()

The timeout for reading data from the SSE stream.

    * ### builder

public static [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") builder()

Creates a new builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").




* * *

Copyright (C) 2025\. All rights reserved.
