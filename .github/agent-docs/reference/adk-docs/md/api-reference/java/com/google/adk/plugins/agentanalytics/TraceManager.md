JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/TraceManager.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [TraceManager](TraceManager.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getRootAgentName()
     2. initTrace(InvocationContext)
     3. getTraceId(InvocationContext)
     4. hasAmbientSpan()
     5. pushSpan(String)
     6. attachCurrentSpan()
     7. ensureInvocationSpan(InvocationContext)
     8. popSpan()
     9. clearStack()
     10. getCurrentSpanAndParent()
     11. getCurrentSpanId()
     12. recordFirstToken(String)
     13. getStartTime(String)
     14. getFirstTokenTime(String)

Hide sidebar  Show sidebar

# Class TraceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.agentanalytics.TraceManager

* * *

public final class TraceManager extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Manages OpenTelemetry-style trace and span context using InvocationContext callback data. 

Uses a stack of SpanRecord objects to keep span, ID, ownership, and timing in sync.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`attachCurrentSpan()`

 

`void`

`clearStack()`

 

`void`

`ensureInvocationSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`com.google.adk.plugins.agentanalytics.TraceManager.SpanIds`

`getCurrentSpanAndParent()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getCurrentSpanId()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")>`

`getFirstTokenTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getRootAgentName()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")>`

`getStartTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getTraceId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`boolean`

`hasAmbientSpan()`

 

`void`

`initTrace([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData>`

`popSpan()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`pushSpan([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanName)`

 

`void`

`recordFirstToken([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### getRootAgentName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getRootAgentName()

    * ### initTrace

public void initTrace([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### getTraceId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getTraceId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### hasAmbientSpan

public boolean hasAmbientSpan()

    * ### pushSpan

@CanIgnoreReturnValue public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pushSpan([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanName)

    * ### attachCurrentSpan

@CanIgnoreReturnValue public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") attachCurrentSpan()

    * ### ensureInvocationSpan

public void ensureInvocationSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### popSpan

@CanIgnoreReturnValue public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData> popSpan()

    * ### clearStack

public void clearStack()

    * ### getCurrentSpanAndParent

public com.google.adk.plugins.agentanalytics.TraceManager.SpanIds getCurrentSpanAndParent()

    * ### getCurrentSpanId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getCurrentSpanId()

    * ### recordFirstToken

public void recordFirstToken([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)

    * ### getStartTime

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")> getStartTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)

    * ### getFirstTokenTime

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")> getFirstTokenTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)




* * *

Copyright (C) 1980\. All rights reserved.
