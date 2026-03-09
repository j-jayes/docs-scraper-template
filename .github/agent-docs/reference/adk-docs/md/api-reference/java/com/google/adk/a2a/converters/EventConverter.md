JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/EventConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [EventConverter](EventConverter.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. convertEventToA2AMessage(Event)
     2. convertEventsToA2AMessage(InvocationContext)
     3. convertEventsToA2AMessage(InvocationContext, EventConverter.AggregationMode)

Hide sidebar  Show sidebar

# Class EventConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.EventConverter

* * *

public final class EventConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Converter for ADK Events to A2A Messages. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static enum `

`[EventConverter.AggregationMode](EventConverter.AggregationMode.html "enum class in com.google.adk.a2a.converters")`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message>`

`convertEventsToA2AMessage([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message>`

`convertEventsToA2AMessage([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [EventConverter.AggregationMode](EventConverter.AggregationMode.html "enum class in com.google.adk.a2a.converters") mode)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message>`

`convertEventToA2AMessage([Event](../../events/Event.html "class in com.google.adk.events") event)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### convertEventToA2AMessage

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message> convertEventToA2AMessage([Event](../../events/Event.html "class in com.google.adk.events") event)

    * ### convertEventsToA2AMessage

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message> convertEventsToA2AMessage([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### convertEventsToA2AMessage

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Message> convertEventsToA2AMessage([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [EventConverter.AggregationMode](EventConverter.AggregationMode.html "enum class in com.google.adk.a2a.converters") mode)




* * *

Copyright (C) 1980\. All rights reserved.
