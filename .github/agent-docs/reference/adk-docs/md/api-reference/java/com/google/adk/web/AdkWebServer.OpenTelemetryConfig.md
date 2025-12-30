JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.OpenTelemetryConfig.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [OpenTelemetryConfig](AdkWebServer.OpenTelemetryConfig.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. OpenTelemetryConfig()
  5. Method Details
     1. apiServerSpanExporter()
     2. sdkTracerProvider(AdkWebServer.ApiServerSpanExporter)
     3. openTelemetrySdk(SdkTracerProvider)



# Class AdkWebServer.OpenTelemetryConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer.OpenTelemetryConfig

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

@Configuration public static class AdkWebServer.OpenTelemetryConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Configuration class for OpenTelemetry, setting up the tracer provider and span exporter.

  * ## Constructor Summary

Constructors

Constructor

Description

`OpenTelemetryConfig()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web")`

`apiServerSpanExporter()`

 

`io.opentelemetry.api.OpenTelemetry`

`openTelemetrySdk(io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider)`

 

`io.opentelemetry.sdk.trace.SdkTracerProvider`

`sdkTracerProvider([AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### OpenTelemetryConfig

public OpenTelemetryConfig()

  * ## Method Details

    * ### apiServerSpanExporter

@Bean public [AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter()

    * ### sdkTracerProvider

@Bean(destroyMethod="shutdown") public io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider([AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter)

    * ### openTelemetrySdk

@Bean public io.opentelemetry.api.OpenTelemetry openTelemetrySdk(io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider)




* * *

Copyright (C) 2025\. All rights reserved.
