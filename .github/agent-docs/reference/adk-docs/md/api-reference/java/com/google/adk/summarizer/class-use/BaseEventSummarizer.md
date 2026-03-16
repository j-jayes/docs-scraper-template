JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseEventSummarizer.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.summarizer](../package-summary.html)
  2. [BaseEventSummarizer](../BaseEventSummarizer.html)



# Uses of Interface  
com.google.adk.summarizer.BaseEventSummarizer

Packages that use [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")

Package

Description

com.google.adk.summarizer

 

  * ## Uses of [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer") in [com.google.adk.summarizer](../package-summary.html)

Classes in [com.google.adk.summarizer](../package-summary.html) that implement [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")

Modifier and Type

Class

Description

`final class `

`[LlmEventSummarizer](../LlmEventSummarizer.html "class in com.google.adk.summarizer")`

An LLM-based event summarizer for sliding window compaction.

Methods in [com.google.adk.summarizer](../package-summary.html) that return [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")

Modifier and Type

Method

Description

`[BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")`

EventsCompactionConfig.`[summarizer](../EventsCompactionConfig.html#summarizer\(\))()`

Returns the value of the [`summarizer`](../../../../../com/google/adk/summarizer/EventsCompactionConfig.html#param-summarizer) record component.

Methods in [com.google.adk.summarizer](../package-summary.html) with parameters of type [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")

Modifier and Type

Method

Description

`abstract [EventsCompactionConfig.Builder](../EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

EventsCompactionConfig.Builder.`[summarizer](../EventsCompactionConfig.Builder.html#summarizer\(com.google.adk.summarizer.BaseEventSummarizer\))([BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)`

 

Constructors in [com.google.adk.summarizer](../package-summary.html) with parameters of type [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer")

Modifier

Constructor

Description

` `

`[EventsCompactionConfig](../EventsCompactionConfig.html#%3Cinit%3E\(int,int,com.google.adk.summarizer.BaseEventSummarizer\))(int compactionInterval, int overlapSize, [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)`

 

` `

`[EventsCompactionConfig](../EventsCompactionConfig.html#%3Cinit%3E\(java.lang.Integer,java.lang.Integer,com.google.adk.summarizer.BaseEventSummarizer,java.lang.Integer,java.lang.Integer\))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize, [BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize)`

Creates an instance of a `EventsCompactionConfig` record class.

` `

`[TailRetentionEventCompactor](../TailRetentionEventCompactor.html#%3Cinit%3E\(com.google.adk.summarizer.BaseEventSummarizer,int,int\))([BaseEventSummarizer](../BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer, int retentionSize, int tokenThreshold)`

 




* * *

Copyright (C) 1980\. All rights reserved.
