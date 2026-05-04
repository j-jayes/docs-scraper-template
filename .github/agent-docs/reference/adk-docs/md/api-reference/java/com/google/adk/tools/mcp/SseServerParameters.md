JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SseServerParameters.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [SseServerParameters](SseServerParameters.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SseServerParameters()
  6. Method Details
     1. url()
     2. sseEndpoint()
     3. headers()
     4. timeout()
     5. sseReadTimeout()
     6. builder()

Hide sidebar  Show sidebar

# Class SseServerParameters

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.SseServerParameters

* * *

public abstract class SseServerParameters extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`abstract @Nullable com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`headers()`

Optional headers to include in the SSE connection request.

`abstract @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`sseEndpoint()`

The endpoint to connect to on the SSE server.

`abstract @Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`sseReadTimeout()`

The timeout for reading data from the SSE stream.

`abstract @Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`timeout()`

The timeout for the initial connection attempt.

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`url()`

The URL of the SSE server.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### SseServerParameters

public SseServerParameters()

  * ## Method Details

    * ### url

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url()

The URL of the SSE server.

    * ### sseEndpoint

public abstract @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sseEndpoint()

The endpoint to connect to on the SSE server.

    * ### headers

public abstract @Nullable com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> headers()

Optional headers to include in the SSE connection request.

    * ### timeout

public abstract @Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") timeout()

The timeout for the initial connection attempt.

    * ### sseReadTimeout

public abstract @Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") sseReadTimeout()

The timeout for reading data from the SSE stream.

    * ### builder

public static [SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") builder()

Creates a new builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").




* * *

Copyright (C) 1980\. All rights reserved.
