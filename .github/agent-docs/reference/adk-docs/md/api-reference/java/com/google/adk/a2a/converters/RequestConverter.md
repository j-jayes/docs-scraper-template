JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RequestConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [RequestConverter](RequestConverter.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. convertA2aMessageToAdkEvent(Message, String)
     2. convertAggregatedA2aMessageToAdkEvents(Message, String)

Hide sidebar  Show sidebar

# Class RequestConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.RequestConverter

* * *

public final class RequestConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

rfe Converter for A2A Messages to ADK Events. This is used on the A2A service side to convert incoming A2A requests to ADK Events. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`convertA2aMessageToAdkEvent(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Convert an A2A Message to an ADK Event.

`static com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")>`

`convertAggregatedA2aMessageToAdkEvents(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Convert an aggregated A2A Message to multiple ADK Events.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### convertA2aMessageToAdkEvent

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> convertA2aMessageToAdkEvent(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)

Convert an A2A Message to an ADK Event. This is used when the A2A service receives a request and needs to process it with ADK.

Parameters:
    `message` \- The A2A message to convert.
    `invocationId` \- The invocation ID for the event.
Returns:
    Optional containing the converted ADK Event, or empty if conversion fails.

    * ### convertAggregatedA2aMessageToAdkEvents

public static com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")> convertAggregatedA2aMessageToAdkEvents(io.a2a.spec.Message message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)

Convert an aggregated A2A Message to multiple ADK Events. This reconstructs the original event sequence from an aggregated message.

Parameters:
    `message` \- The aggregated A2A message to convert.
    `invocationId` \- The invocation ID for the events.
Returns:
    List of ADK Events representing the conversation history.




* * *

Copyright (C) 1980\. All rights reserved.
