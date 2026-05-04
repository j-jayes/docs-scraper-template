JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SlidingWindowEventCompactor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.summarizer](package-summary.html)
  2. [SlidingWindowEventCompactor](SlidingWindowEventCompactor.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SlidingWindowEventCompactor(EventsCompactionConfig)
  5. Method Details
     1. compact(Session, BaseSessionService)

Hide sidebar  Show sidebar

# Class SlidingWindowEventCompactor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.summarizer.SlidingWindowEventCompactor

All Implemented Interfaces:
    `[EventCompactor](EventCompactor.html "interface in com.google.adk.summarizer")`

* * *

public final class SlidingWindowEventCompactor extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [EventCompactor](EventCompactor.html "interface in com.google.adk.summarizer")

This class performs events compaction in a sliding window fashion based on the [`EventsCompactionConfig`](EventsCompactionConfig.html "class in com.google.adk.summarizer").

  * ## Constructor Summary

Constructors

Constructor

Description

`SlidingWindowEventCompactor([EventsCompactionConfig](EventsCompactionConfig.html "class in com.google.adk.summarizer") config)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`compact([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Runs compaction for SlidingWindowCompactor.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### SlidingWindowEventCompactor

public SlidingWindowEventCompactor([EventsCompactionConfig](EventsCompactionConfig.html "class in com.google.adk.summarizer") config)

  * ## Method Details

    * ### compact

public io.reactivex.rxjava3.core.Completable compact([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

Runs compaction for SlidingWindowCompactor. 

This method implements the sliding window compaction logic. It determines if enough new invocations have occurred since the last compaction based on [`EventsCompactionConfig.compactionInterval()`](EventsCompactionConfig.html#compactionInterval\(\)). If so, it selects a range of events to compact based on [`EventsCompactionConfig.overlapSize()`](EventsCompactionConfig.html#overlapSize\(\)), and calls [`BaseEventSummarizer.summarizeEvents(List)`](BaseEventSummarizer.html#summarizeEvents\(java.util.List\)). 

The compaction process is controlled by two parameters: 

1\. [`EventsCompactionConfig.compactionInterval()`](EventsCompactionConfig.html#compactionInterval\(\)): The number of *new* user-initiated invocations that, once fully represented in the session's events, will trigger a compaction. 2. `overlap_size`: The number of preceding invocations to include from the end of the last compacted range. This creates an overlap between consecutive compacted summaries, maintaining context. 

The compactor is called after an agent has finished processing a turn and all its events have been added to the session. It checks if a new compaction is needed. 

When a compaction is triggered: - The compactor identifies the range of `invocation_id`s to be summarized. - This range starts `overlap_size` invocations before the beginning of the new block of `compaction_invocation_threshold` invocations and ends with the last invocation in the current block. - A `CompactedEvent` is created, summarizing all events within this determined `invocation_id` range. This `CompactedEvent` is then appended to the session. 

Here is an example with `compaction_invocation_threshold = 2` and `overlap_size = 1`: Let's assume events are added for `invocation_id`s 1, 2, 3, and 4 in order. 

1\. **After `invocation_id` 2 events are added:** - The session now contains events for invocations 1 and 2. This fulfills the `compaction_invocation_threshold = 2` criteria. - Since this is the first compaction, the range starts from the beginning. - A `CompactedEvent` is generated, summarizing events within `invocation_id` range [1, 2]. - The session now contains: `[ E(inv=1, role=user), E(inv=1, role=model), E(inv=2, role=user), E(inv=2, role=model), CompactedEvent(inv=[1, 2])]`. 

2\. **After `invocation_id` 3 events are added:** - No compaction happens yet, because only 1 new invocation (`inv=3`) has been completed since the last compaction, and `compaction_invocation_threshold` is 2. 

3\. **After `invocation_id` 4 events are added:** - The session now contains new events for invocations 3 and 4, again fulfilling `compaction_invocation_threshold = 2`. - The last `CompactedEvent` covered up to `invocation_id` 2. With `overlap_size = 1`, the new compaction range will start one invocation before the new block (inv 3), which is `invocation_id` 2. - The new compaction range is from `invocation_id` 2 to 4. - A new `CompactedEvent` is generated, summarizing events within `invocation_id` range [2, 4]. - The session now contains: `[ E(inv=1, role=user), E(inv=1, role=model), E(inv=2, role=user), E(inv=2, role=model), CompactedEvent(inv=[1, 2]), E(inv=3, role=user), E(inv=3, role=model), E(inv=4, role=user), E(inv=4, role=model), CompactedEvent(inv=[2, 4])]`.

Specified by:
    `[compact](EventCompactor.html#compact\(com.google.adk.sessions.Session,com.google.adk.sessions.BaseSessionService\))` in interface `[EventCompactor](EventCompactor.html "interface in com.google.adk.summarizer")`
Parameters:
    `session` \- the session containing the events to be compacted.
    `sessionService` \- the session service for appending the new compaction event.
Returns:
    the [`Event`](../events/Event.html "class in com.google.adk.events") containing the events summary.




* * *

Copyright (C) 1980\. All rights reserved.
