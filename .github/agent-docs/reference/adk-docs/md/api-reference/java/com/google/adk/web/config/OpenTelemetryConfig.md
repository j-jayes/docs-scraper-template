JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/OpenTelemetryConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.config](package-summary.html)
  2. [OpenTelemetryConfig](OpenTelemetryConfig.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. OpenTelemetryConfig()
  5. Method Details
     1. apiServerSpanExporter()
     2. sdkTracerProvider(ApiServerSpanExporter)
     3. openTelemetrySdk(SdkTracerProvider)

Hide sidebar  Show sidebar

# Class OpenTelemetryConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.config.OpenTelemetryConfig

* * *

@Configuration public class OpenTelemetryConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`[ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service")`

`apiServerSpanExporter()`

 

`io.opentelemetry.api.OpenTelemetry`

`openTelemetrySdk(io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider)`

 

`io.opentelemetry.sdk.trace.SdkTracerProvider`

`sdkTracerProvider([ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### OpenTelemetryConfig

public OpenTelemetryConfig()

  * ## Method Details

    * ### apiServerSpanExporter

@Bean public [ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter()

    * ### sdkTracerProvider

@Bean(destroyMethod="shutdown") public io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider([ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter)

    * ### openTelemetrySdk

@Bean public io.opentelemetry.api.OpenTelemetry openTelemetrySdk(io.opentelemetry.sdk.trace.SdkTracerProvider sdkTracerProvider)




* * *

Copyright (C) 1980\. All rights reserved.
