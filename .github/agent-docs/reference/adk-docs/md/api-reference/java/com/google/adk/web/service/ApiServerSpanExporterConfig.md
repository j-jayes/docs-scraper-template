JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ApiServerSpanExporterConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.service](package-summary.html)
  2. [ApiServerSpanExporterConfig](ApiServerSpanExporterConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ApiServerSpanExporterConfig()
  6. Method Details
     1. maxSpansToKeep()
     2. builder()

Hide sidebar  Show sidebar

# Class ApiServerSpanExporterConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.service.ApiServerSpanExporterConfig

* * *

public abstract class ApiServerSpanExporterConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration for [`ApiServerSpanExporter`](ApiServerSpanExporter.html "class in com.google.adk.web.service").

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ApiServerSpanExporterConfig.Builder](ApiServerSpanExporterConfig.Builder.html "class in com.google.adk.web.service")`

Builder for [`ApiServerSpanExporterConfig`](ApiServerSpanExporterConfig.html "class in com.google.adk.web.service").

  * ## Constructor Summary

Constructors

Constructor

Description

`ApiServerSpanExporterConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ApiServerSpanExporterConfig.Builder](ApiServerSpanExporterConfig.Builder.html "class in com.google.adk.web.service")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`maxSpansToKeep()`

The maximum number of spans to keep in memory.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ApiServerSpanExporterConfig

public ApiServerSpanExporterConfig()

  * ## Method Details

    * ### maxSpansToKeep

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> maxSpansToKeep()

The maximum number of spans to keep in memory. When the limit is reached, the oldest spans are evicted (FIFO). If empty, no limit is enforced and spans accumulate without bound. 

When set, the value must be a positive integer (`>= 1`).

    * ### builder

public static [ApiServerSpanExporterConfig.Builder](ApiServerSpanExporterConfig.Builder.html "class in com.google.adk.web.service") builder()




* * *

Copyright (C) 1980\. All rights reserved.
