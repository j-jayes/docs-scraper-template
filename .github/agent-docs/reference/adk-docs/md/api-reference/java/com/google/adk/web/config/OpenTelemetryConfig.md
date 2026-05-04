JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/OpenTelemetryConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.config.OpenTelemetryConfig

* * *

@Configuration public class OpenTelemetryConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




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
