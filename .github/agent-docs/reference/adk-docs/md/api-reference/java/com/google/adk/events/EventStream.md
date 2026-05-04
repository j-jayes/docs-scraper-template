JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventStream.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](package-summary.html)
  2. [EventStream](EventStream.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. EventStream(Supplier)
  5. Method Details
     1. iterator()

Hide sidebar  Show sidebar

# Class EventStream

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.events.EventStream

All Implemented Interfaces:
    `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>`

* * *

public class EventStream extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>

Iterable stream of [`Event`](Event.html "class in com.google.adk.events") objects. 

NOTE: This class is not thread-safe. Concurrent iteration from multiple threads should be avoided or externally synchronized.

  * ## Constructor Summary

Constructors

Constructor

Description

`EventStream([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "interface in java.util.function")<[Event](Event.html "class in com.google.adk.events")> eventSupplier)`

Constructs a new event stream.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "interface in java.util")<[Event](Event.html "class in com.google.adk.events")>`

`iterator()`

Returns an iterator that fetches events lazily.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#method-summary "interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach\(java.util.function.Consumer\) "forEach\(Consumer\)"), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#spliterator\(\) "spliterator\(\)")`




  * ## Constructor Details

    * ### EventStream

public EventStream([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "interface in java.util.function")<[Event](Event.html "class in com.google.adk.events")> eventSupplier)

Constructs a new event stream.

  * ## Method Details

    * ### iterator

public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "interface in java.util")<[Event](Event.html "class in com.google.adk.events")> iterator()

Returns an iterator that fetches events lazily.

Specified by:
    `[iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#iterator\(\))` in interface `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>`




* * *

Copyright (C) 1980\. All rights reserved.
