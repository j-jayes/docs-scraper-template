JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.ApiServerSpanExporter.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ApiServerSpanExporter()
  5. Method Details
     1. getEventTraceAttributes(String)
     2. getSessionToTraceIdsMap()
     3. getAllExportedSpans()
     4. export(Collection)
     5. flush()
     6. shutdown()



# Class AdkWebServer.ApiServerSpanExporter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer.ApiServerSpanExporter

All Implemented Interfaces:
    `io.opentelemetry.sdk.trace.export.SpanExporter`, `[Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html "class or interface in java.io")`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

public static class AdkWebServer.ApiServerSpanExporter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements io.opentelemetry.sdk.trace.export.SpanExporter

A custom SpanExporter that stores relevant span data. It handles two types of trace data storage: 1. Event-ID based: Stores attributes of specific spans (call_llm, send_data, tool_response) keyed by `gcp.vertex.agent.event_id`. This is used for debugging individual events. 2. Session-ID based: Stores all exported spans and maintains a mapping from `session_id` (extracted from `call_llm` spans) to a list of `trace_id`s. This is used for retrieving all spans related to a session.

  * ## Constructor Summary

Constructors

Constructor

Description

`ApiServerSpanExporter()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.opentelemetry.sdk.common.CompletableResultCode`

`export([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> spans)`

 

`io.opentelemetry.sdk.common.CompletableResultCode`

`flush()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData>`

`getAllExportedSpans()`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getEventTraceAttributes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`

`getSessionToTraceIdsMap()`

 

`io.opentelemetry.sdk.common.CompletableResultCode`

`shutdown()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface io.opentelemetry.sdk.trace.export.SpanExporter

`close`




  * ## Constructor Details

    * ### ApiServerSpanExporter

public ApiServerSpanExporter()

  * ## Method Details

    * ### getEventTraceAttributes

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getEventTraceAttributes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)

    * ### getSessionToTraceIdsMap

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> getSessionToTraceIdsMap()

    * ### getAllExportedSpans

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> getAllExportedSpans()

    * ### export

public io.opentelemetry.sdk.common.CompletableResultCode export([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> spans)

Specified by:
    `export` in interface `io.opentelemetry.sdk.trace.export.SpanExporter`

    * ### flush

public io.opentelemetry.sdk.common.CompletableResultCode flush()

Specified by:
    `flush` in interface `io.opentelemetry.sdk.trace.export.SpanExporter`

    * ### shutdown

public io.opentelemetry.sdk.common.CompletableResultCode shutdown()

Specified by:
    `shutdown` in interface `io.opentelemetry.sdk.trace.export.SpanExporter`




* * *

Copyright (C) 2025\. All rights reserved.
