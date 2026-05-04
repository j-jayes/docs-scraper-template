JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmEventSummarizer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.summarizer](package-summary.html)
  2. [LlmEventSummarizer](LlmEventSummarizer.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. LlmEventSummarizer(BaseLlm)
     2. LlmEventSummarizer(BaseLlm, String)
  5. Method Details
     1. summarizeEvents(List)

Hide sidebar  Show sidebar

# Class LlmEventSummarizer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.summarizer.LlmEventSummarizer

All Implemented Interfaces:
    `[BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer")`

* * *

public final class LlmEventSummarizer extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer")

An LLM-based event summarizer for sliding window compaction.

  * ## Constructor Summary

Constructors

Constructor

Description

`LlmEventSummarizer([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") baseLlm)`

 

`LlmEventSummarizer([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") baseLlm, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") promptTemplate)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`summarizeEvents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

Compact a list of events into a single event.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### LlmEventSummarizer

public LlmEventSummarizer([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") baseLlm)

    * ### LlmEventSummarizer

public LlmEventSummarizer([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") baseLlm, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") promptTemplate)

  * ## Method Details

    * ### summarizeEvents

public io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> summarizeEvents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

Description copied from interface: `[BaseEventSummarizer](BaseEventSummarizer.html#summarizeEvents\(java.util.List\))`

Compact a list of events into a single event. 

If compaction failed, return `Maybe.empty()`. Otherwise, compact into a content and return it. 

This method will summarize the events and return a new summary event indicating the range of events it summarized.

Specified by:
    `[summarizeEvents](BaseEventSummarizer.html#summarizeEvents\(java.util.List\))` in interface `[BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer")`
Parameters:
    `events` \- Events to compact.
Returns:
    The new compacted event, or `Maybe.empty()` if no compaction happened.




* * *

Copyright (C) 1980\. All rights reserved.
