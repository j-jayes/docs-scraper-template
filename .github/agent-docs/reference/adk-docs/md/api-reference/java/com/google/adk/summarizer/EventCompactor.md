JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventCompactor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.summarizer](package-summary.html)
  2. [EventCompactor](EventCompactor.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. compact(Session, BaseSessionService)

Hide sidebar  Show sidebar

# Interface EventCompactor

All Known Implementing Classes:
    `[SlidingWindowEventCompactor](SlidingWindowEventCompactor.html "class in com.google.adk.summarizer")`

* * *

public interface EventCompactor

Base interface for compacting events.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`compact([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Compacts events in the given session.




  * ## Method Details

    * ### compact

io.reactivex.rxjava3.core.Completable compact([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

Compacts events in the given session. If there is compaction happened, the new compaction event will be appended to the given [`BaseSessionService`](../sessions/BaseSessionService.html "interface in com.google.adk.sessions").

Parameters:
    `session` \- the session containing the events to be compacted.
    `sessionService` \- the session service for appending the new compaction event.
Returns:
    the [`Event`](../events/Event.html "class in com.google.adk.events") containing the events summary.




* * *

Copyright (C) 1980\. All rights reserved.
