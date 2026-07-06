JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/PersistBarrier.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [PersistBarrier](PersistBarrier.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. enable(InvocationContext)
     2. awaitPersisted(InvocationContext, List)
     3. markPersisted(InvocationContext, String)
     4. markFailed(InvocationContext, String, Throwable)

Hide sidebar  Show sidebar

# Class PersistBarrier

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.PersistBarrier

* * *

public final class PersistBarrier extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Lets [`BaseLlmFlow`](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")'s multi-step loop wait until the `Runner` \-- the sole event persister -- has appended the current step's events, so the next step's request (built from `session.events()` by [`Contents`](Contents.html "class in com.google.adk.flows.llmflows")) is not assembled from a stale session. The ` Runner` calls `markPersisted(InvocationContext, String)` (or `markFailed(InvocationContext, String, Throwable)`) after each append; the flow calls `awaitPersisted(InvocationContext, List)` between steps. State lives in the per-invocation [`InvocationContext.callbackContextData()`](../../agents/InvocationContext.html#callbackContextData\(\)) map, shared across the agent tree. 

Each event id maps to a `CompletableSubject`: pending until its append finishes, then terminally completed or failed. The subject retains its terminal state, so ` awaitPersisted`/`mark*` may happen in any order and a late await -- e.g. at a higher flow level across an agent transfer -- resolves immediately. If an append fails, the matching await fails with that error rather than blocking forever. 

Thread-safe and lock-free: `markPersisted`/`markFailed` may run off-thread (async `appendEvent`) concurrently with `awaitPersisted`; [`ConcurrentHashMap.computeIfAbsent(K, Function)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html#computeIfAbsent\(K,java.util.function.Function\)) hands both sides the same subject, which itself serializes its terminal signal against subscription.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Completable`

`awaitPersisted([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

Completes once every event in `events` has been `markPersisted(InvocationContext, String)`, or fails if any was `markFailed(InvocationContext, String, Throwable)`; completes immediately if the barrier was never `enable(InvocationContext)`d.

`static void`

`enable([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

Marks that a `Runner` is driving this invocation and will resolve each appended event.

`static void`

`markFailed([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Signals that persisting the event with the given id failed, so an await on it fails with ` error` instead of blocking forever.

`static void`

`markPersisted([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

Signals that the `Runner` persisted the event with the given id.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### enable

public static void enable([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

Marks that a `Runner` is driving this invocation and will resolve each appended event. Otherwise (flow run directly, e.g. unit tests) `awaitPersisted(InvocationContext, List)` is a no-op, avoiding a deadlock waiting for a signal that never comes.

    * ### awaitPersisted

public static io.reactivex.rxjava3.core.Completable awaitPersisted([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)

Completes once every event in `events` has been `markPersisted(InvocationContext, String)`, or fails if any was `markFailed(InvocationContext, String, Throwable)`; completes immediately if the barrier was never `enable(InvocationContext)`d. Already-resolved events resolve immediately, so the order of `awaitPersisted`/` mark*` does not matter.

    * ### markPersisted

public static void markPersisted([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)

Signals that the `Runner` persisted the event with the given id.

    * ### markFailed

public static void markFailed([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Signals that persisting the event with the given id failed, so an await on it fails with ` error` instead of blocking forever.




* * *

Copyright (C) 1980\. All rights reserved.
