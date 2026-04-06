JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventsCompactionConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.summarizer](package-summary.html)
  2. [EventsCompactionConfig](EventsCompactionConfig.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. EventsCompactionConfig(int, int)
     2. EventsCompactionConfig(int, int, BaseEventSummarizer)
     3. EventsCompactionConfig(Integer, Integer, BaseEventSummarizer, Integer, Integer)
  6. Method Details
     1. builder()
     2. toBuilder()
     3. hasSlidingWindowCompactionConfig()
     4. toString()
     5. hashCode()
     6. equals(Object)
     7. compactionInterval()
     8. overlapSize()
     9. summarizer()
     10. tokenThreshold()
     11. eventRetentionSize()

Hide sidebar  Show sidebar

# Record Class EventsCompactionConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

com.google.adk.summarizer.EventsCompactionConfig

Record Components:
    `compactionInterval` \- The number of **new** user-initiated invocations that, once fully represented in the session's events, will trigger a compaction.
    `overlapSize` \- The number of preceding invocations to include from the end of the last compacted range. This creates an overlap between consecutive compacted summaries, maintaining context.
    `summarizer` \- An event summarizer to use for compaction.
    `tokenThreshold` \- The number of tokens above which compaction will be triggered. If null, no token limit will be enforced. It will trigger compaction within the invocation.
    `eventRetentionSize` \- The maximum number of events to retain and preserve from compaction. If null, no event retention limit will be enforced.

* * *

public record EventsCompactionConfig(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize, @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

Configuration for event compaction.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

Builder for [`EventsCompactionConfig`](EventsCompactionConfig.html "class in com.google.adk.summarizer").

  * ## Constructor Summary

Constructors

Constructor

Description

`EventsCompactionConfig(int compactionInterval, int overlapSize)`

 

`EventsCompactionConfig(int compactionInterval, int overlapSize, @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)`

 

`EventsCompactionConfig(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize, @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize)`

Creates an instance of a `EventsCompactionConfig` record class.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`builder()`

 

`@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`compactionInterval()`

Returns the value of the `compactionInterval` record component.

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`eventRetentionSize()`

Returns the value of the `eventRetentionSize` record component.

`final int`

`hashCode()`

Returns a hash code value for this object.

`boolean`

`hasSlidingWindowCompactionConfig()`

 

`@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`overlapSize()`

Returns the value of the `overlapSize` record component.

`@Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer")`

`summarizer()`

Returns the value of the `summarizer` record component.

`[EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer")`

`toBuilder()`

 

`@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`tokenThreshold()`

Returns the value of the `tokenThreshold` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### EventsCompactionConfig

public EventsCompactionConfig(int compactionInterval, int overlapSize)

    * ### EventsCompactionConfig

public EventsCompactionConfig(int compactionInterval, int overlapSize, @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)

    * ### EventsCompactionConfig

public EventsCompactionConfig(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize, @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize)

Creates an instance of a `EventsCompactionConfig` record class.

Parameters:
    `compactionInterval` \- the value for the `compactionInterval` record component
    `overlapSize` \- the value for the `overlapSize` record component
    `summarizer` \- the value for the `summarizer` record component
    `tokenThreshold` \- the value for the `tokenThreshold` record component
    `eventRetentionSize` \- the value for the `eventRetentionSize` record component

  * ## Method Details

    * ### builder

public static [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") builder()

    * ### toBuilder

public [EventsCompactionConfig.Builder](EventsCompactionConfig.Builder.html "class in com.google.adk.summarizer") toBuilder()

    * ### hasSlidingWindowCompactionConfig

public boolean hasSlidingWindowCompactionConfig()

    * ### toString

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\) "class or interface in java.util").

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### compactionInterval

public @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") compactionInterval()

Returns the value of the `compactionInterval` record component.

Returns:
    the value of the `compactionInterval` record component

    * ### overlapSize

public @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") overlapSize()

Returns the value of the `overlapSize` record component.

Returns:
    the value of the `overlapSize` record component

    * ### summarizer

public @Nullable [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer()

Returns the value of the `summarizer` record component.

Returns:
    the value of the `summarizer` record component

    * ### tokenThreshold

public @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") tokenThreshold()

Returns the value of the `tokenThreshold` record component.

Returns:
    the value of the `tokenThreshold` record component

    * ### eventRetentionSize

public @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") eventRetentionSize()

Returns the value of the `eventRetentionSize` record component.

Returns:
    the value of the `eventRetentionSize` record component




* * *

Copyright (C) 1980\. All rights reserved.
