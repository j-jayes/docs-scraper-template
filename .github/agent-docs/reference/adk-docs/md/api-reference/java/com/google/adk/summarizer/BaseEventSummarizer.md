JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseEventSummarizer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.summarizer](package-summary.html)
  2. [BaseEventSummarizer](BaseEventSummarizer.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. summarizeEvents(List)

Hide sidebar  Show sidebar

# Interface BaseEventSummarizer

All Known Implementing Classes:
    `[LlmEventSummarizer](LlmEventSummarizer.html "class in com.google.adk.summarizer")`

* * *

public interface BaseEventSummarizer

Base interface for producing events summary.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`summarizeEvents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.




  * ## Method Details

    * ### summarizeEvents

io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> summarizeEvents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

Compact a list of events into a single event. 

If compaction failed, return `Maybe.empty()`. Otherwise, compact into a content and return it. 

This method will summarize the events and return a new summary event indicating the range of events it summarized.

Parameters:
    `events` \- Events to compact.
Returns:
    The new compacted event, or `Maybe.empty()` if no compaction happened.




* * *

Copyright (C) 1980\. All rights reserved.
