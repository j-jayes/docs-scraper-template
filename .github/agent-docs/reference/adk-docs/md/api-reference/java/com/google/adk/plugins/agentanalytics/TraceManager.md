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
     3. initTraceIfNeeded(InvocationContext)
     4. getTraceId(InvocationContext)
     5. pushSpan(InvocationContext, String)
     6. attachCurrentSpan(InvocationContext)
     7. ensureInvocationSpan(InvocationContext)
     8. popSpan(InvocationContext, String)
     9. popSpan(InvocationContext, String, String)
     10. clearStack()
     11. getCurrentSpanAndParent(InvocationContext)
     12. getCurrentSpanId(InvocationContext)
     13. recordFirstToken(String)
     14. getStartTime(String)
     15. getFirstTokenTime(String)

Hide sidebar  Show sidebar

# Class TraceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.agentanalytics.TraceManager

* * *

public final class TraceManager extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Manages the BQAA-internal execution tree of span IDs for one invocation. 

No OpenTelemetry spans are created: records are ID-only, so a host with an SDK exporter configured never receives a duplicate plugin-owned span tree next to ADK's framework spans. Ambient OpenTelemetry context is still consulted for the `trace_id` (and the invocation root's `span_id`) so BigQuery rows stay joinable to Cloud Trace. 

Span records are kept in per-branch stacks keyed by [`InvocationContext.branch()`](../../agents/InvocationContext.html#branch\(\)). Concurrently scheduled `ParallelAgent` branches (which share an invocation ID but carry distinct branch strings) never touch each other's stacks, so a branch completing first can no longer pop another branch's span. Within one branch, agent and model spans execute sequentially and use top-of-stack semantics, but ADK executes an event's function calls CONCURRENTLY by default: tool spans therefore carry an operation identity (the function-call ID) plus a parent captured at push time, and are popped by identity rather than stack position. Pops additionally verify the record's `kind`, so an error callback firing without its matching push cannot pop an unrelated record.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`attachCurrentSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

Records the ambient OpenTelemetry span's IDs as the invocation root without creating or owning any span, so plugin-emitted rows correlate with the host's existing tracing.

`void`

`clearStack()`

 

`void`

`ensureInvocationSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`com.google.adk.plugins.agentanalytics.TraceManager.SpanIds`

`getCurrentSpanAndParent([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getCurrentSpanId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")>`

`getFirstTokenTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getRootAgentName()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")>`

`getStartTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getTraceId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`void`

`initTrace([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

 

`void`

`initTraceIfNeeded([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

Sets the root agent name from the invocation context if it is still the sentinel default.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData>`

`popSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") expectedKindPrefix)`

Pops the calling branch's top span record if its kind matches `expectedKindPrefix`.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData>`

`popSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") expectedKindPrefix, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") operationId)`

Pops the calling branch's matching span record.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`pushSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanName)`

Pushes an ID-only span record onto the calling branch's stack.

`void`

`recordFirstToken([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### getRootAgentName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getRootAgentName()

    * ### initTrace

public void initTrace([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### initTraceIfNeeded

public void initTraceIfNeeded([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

Sets the root agent name from the invocation context if it is still the sentinel default. Null-safe: workflow-driven callbacks with no current agent leave the sentinel in place for a later event to resolve.

    * ### getTraceId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getTraceId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### pushSpan

@CanIgnoreReturnValue public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pushSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanName)

Pushes an ID-only span record onto the calling branch's stack. No OTel span is created.

    * ### attachCurrentSpan

@CanIgnoreReturnValue public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") attachCurrentSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

Records the ambient OpenTelemetry span's IDs as the invocation root without creating or owning any span, so plugin-emitted rows correlate with the host's existing tracing.

    * ### ensureInvocationSpan

public void ensureInvocationSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### popSpan

@CanIgnoreReturnValue public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData> popSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") expectedKindPrefix)

Pops the calling branch's top span record if its kind matches `expectedKindPrefix`. 

The branch scoping prevents a concurrently completing `ParallelAgent` branch from popping another branch's span; the kind check prevents a mismatched pop (e.g. an error callback firing without its corresponding push) from corrupting the stack.

    * ### popSpan

@CanIgnoreReturnValue public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.adk.plugins.agentanalytics.TraceManager.RecordData> popSpan([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") expectedKindPrefix, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") operationId)

Pops the calling branch's matching span record. 

With an `operationId`, the record is located by kind AND operation identity (newest-first) rather than stack position: ADK executes an event's function calls concurrently by default within one branch, so a completion must remove its own record even when a sibling tool's record sits above it. Without an `operationId`, only the branch's top record is popped, and only when its kind matches.

    * ### clearStack

public void clearStack()

    * ### getCurrentSpanAndParent

public com.google.adk.plugins.agentanalytics.TraceManager.SpanIds getCurrentSpanAndParent([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### getCurrentSpanId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getCurrentSpanId([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

    * ### recordFirstToken

public void recordFirstToken([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)

    * ### getStartTime

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")> getStartTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)

    * ### getFirstTokenTime

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")> getFirstTokenTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spanId)




* * *

Copyright (C) 1980\. All rights reserved.
