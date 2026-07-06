JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ApiServerSpanExporter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.service](package-summary.html)
  2. [ApiServerSpanExporter](ApiServerSpanExporter.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ApiServerSpanExporter()
     2. ApiServerSpanExporter(ApiServerSpanExporterConfig)
  5. Method Details
     1. getEventTraceAttributes(String)
     2. getSessionToTraceIdsMap()
     3. getAllExportedSpans()
     4. export(Collection)
     5. flush()
     6. shutdown()

Hide sidebar  Show sidebar

# Class ApiServerSpanExporter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.service.ApiServerSpanExporter

All Implemented Interfaces:
    `io.opentelemetry.sdk.trace.export.SpanExporter, [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html "interface in java.io"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

* * *

public class ApiServerSpanExporter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements io.opentelemetry.sdk.trace.export.SpanExporter

A custom SpanExporter that stores relevant span data. It handles two types of trace data storage: 1\. Event-ID based: Stores attributes of specific spans (call_llm, send_data, tool_response) keyed by `gcp.vertex.agent.event_id`. This is used for debugging individual events. 2. Session-ID based: Stores all exported spans and maintains a mapping from `session_id` (extracted from `call_llm` spans) to a list of `trace_id`s. This is used for retrieving all spans related to a session.

  * ## Constructor Summary

Constructors

Constructor

Description

`ApiServerSpanExporter()`

 

`ApiServerSpanExporter([ApiServerSpanExporterConfig](ApiServerSpanExporterConfig.html "class in com.google.adk.web.service") config)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.opentelemetry.sdk.common.CompletableResultCode`

`export([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> spans)`

 

`io.opentelemetry.sdk.common.CompletableResultCode`

`flush()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData>`

`getAllExportedSpans()`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`getEventTraceAttributes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`getSessionToTraceIdsMap()`

 

`io.opentelemetry.sdk.common.CompletableResultCode`

`shutdown()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface io.opentelemetry.sdk.trace.export.SpanExporter

`close`




  * ## Constructor Details

    * ### ApiServerSpanExporter

public ApiServerSpanExporter()

    * ### ApiServerSpanExporter

public ApiServerSpanExporter([ApiServerSpanExporterConfig](ApiServerSpanExporterConfig.html "class in com.google.adk.web.service") config)

  * ## Method Details

    * ### getEventTraceAttributes

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> getEventTraceAttributes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)

    * ### getSessionToTraceIdsMap

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> getSessionToTraceIdsMap()

    * ### getAllExportedSpans

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> getAllExportedSpans()

    * ### export

public io.opentelemetry.sdk.common.CompletableResultCode export([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<io.opentelemetry.sdk.trace.data.SpanData> spans)

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

Copyright (C) 1980\. All rights reserved.
