JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventCompaction.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](package-summary.html)
  2. [EventCompaction](EventCompaction.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. EventCompaction()
  6. Method Details
     1. startTimestamp()
     2. endTimestamp()
     3. compactedContent()
     4. builder()

Hide sidebar  Show sidebar

# Class EventCompaction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.events.EventCompaction

* * *

public abstract class EventCompaction extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

The compaction of the events.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[EventCompaction.Builder](EventCompaction.Builder.html "class in com.google.adk.events")`

Builder for [`EventCompaction`](EventCompaction.html "class in com.google.adk.events").

  * ## Constructor Summary

Constructors

Constructor

Description

`EventCompaction()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [EventCompaction.Builder](EventCompaction.Builder.html "class in com.google.adk.events")`

`builder()`

 

`abstract com.google.genai.types.Content`

`compactedContent()`

 

`abstract long`

`endTimestamp()`

 

`abstract long`

`startTimestamp()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### EventCompaction

public EventCompaction()

  * ## Method Details

    * ### startTimestamp

public abstract long startTimestamp()

    * ### endTimestamp

public abstract long endTimestamp()

    * ### compactedContent

public abstract com.google.genai.types.Content compactedContent()

    * ### builder

public static [EventCompaction.Builder](EventCompaction.Builder.html "class in com.google.adk.events") builder()




* * *

Copyright (C) 1980\. All rights reserved.
