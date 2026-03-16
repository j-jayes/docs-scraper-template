JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventsCompactionConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.summarizer](package-summary.html)
  2. [EventsCompactionConfig](EventsCompactionConfig.html)
  3. [Builder](EventsCompactionConfig.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. compactionInterval(Integer)
     2. overlapSize(Integer)
     3. summarizer(BaseEventSummarizer)
     4. tokenThreshold(Integer)
     5. eventRetentionSize(Integer)
     6. build()

Hide sidebar  Show sidebar

# Class EventsCompactionConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.summarizer.EventsCompactionConfig.Builder

Enclosing class:
    `[EventsCompactionConfig](EventsCompactionConfig.html "class in com.google.adk.summarizer")`

* * *

public abstract static class EventsCompactionConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`EventsCompactionConfig`](EventsCompactionConfig.html "class in com.google.adk.summarizer").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`abstract [EventsCompactionConfig](EventsCompactionConfig.html "class in com.google.adk.summarizer")`

`build()`

 

`abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`compactionInterval([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval)`

 

`abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`eventRetentionSize([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize)`

 

`abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`overlapSize([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize)`

 

`abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`summarizer([BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)`

 

`abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`tokenThreshold([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### compactionInterval

@CanIgnoreReturnValue public abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") compactionInterval(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval)

    * ### overlapSize

@CanIgnoreReturnValue public abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") overlapSize(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize)

    * ### summarizer

@CanIgnoreReturnValue public abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") summarizer(@Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)

    * ### tokenThreshold

@CanIgnoreReturnValue public abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") tokenThreshold(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold)

    * ### eventRetentionSize

@CanIgnoreReturnValue public abstract [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") eventRetentionSize(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize)

    * ### build

public abstract [EventsCompactionConfig](EventsCompactionConfig.html "class in com.google.adk.summarizer") build()




* * *

Copyright (C) 1980\. All rights reserved.
