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
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. EventsCompactionConfig(int, int, BaseEventSummarizer)
  5. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. compactionInterval()
     5. overlapSize()
     6. summarizer()

Hide sidebar  Show sidebar

# Record Class EventsCompactionConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

com.google.adk.summarizer.EventsCompactionConfig

Record Components:
    `compactionInterval` \- The number of **new** user-initiated invocations that, once fully represented in the session's events, will trigger a compaction.
    `overlapSize` \- The number of preceding invocations to include from the end of the last compacted range. This creates an overlap between consecutive compacted summaries, maintaining context.
    `summarizer` \- An event summarizer to use for compaction.

* * *

public record EventsCompactionConfig(int compactionInterval, int overlapSize, [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

Configuration for event compaction.

  * ## Constructor Summary

Constructors

Constructor

Description

`EventsCompactionConfig(int compactionInterval, int overlapSize, [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)`

Creates an instance of a `EventsCompactionConfig` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`int`

`compactionInterval()`

Returns the value of the `compactionInterval` record component.

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`final int`

`hashCode()`

Returns a hash code value for this object.

`int`

`overlapSize()`

Returns the value of the `overlapSize` record component.

`[BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer")`

`summarizer()`

Returns the value of the `summarizer` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### EventsCompactionConfig

public EventsCompactionConfig(int compactionInterval, int overlapSize, [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer)

Creates an instance of a `EventsCompactionConfig` record class.

Parameters:
    `compactionInterval` \- the value for the `compactionInterval` record component
    `overlapSize` \- the value for the `overlapSize` record component
    `summarizer` \- the value for the `summarizer` record component

  * ## Method Details

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

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. Reference components are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\) "class or interface in java.util"); primitive components are compared with the `compare` method from their corresponding wrapper classes.

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### compactionInterval

public int compactionInterval()

Returns the value of the `compactionInterval` record component.

Returns:
    the value of the `compactionInterval` record component

    * ### overlapSize

public int overlapSize()

Returns the value of the `overlapSize` record component.

Returns:
    the value of the `overlapSize` record component

    * ### summarizer

public [BaseEventSummarizer](BaseEventSummarizer.html "interface in com.google.adk.summarizer") summarizer()

Returns the value of the `summarizer` record component.

Returns:
    the value of the `summarizer` record component




* * *

Copyright (C) 1980\. All rights reserved.
