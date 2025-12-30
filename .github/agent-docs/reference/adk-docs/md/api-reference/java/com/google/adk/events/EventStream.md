JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventStream.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [EventStream](EventStream.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. EventStream(Supplier)
  5. Method Details
     1. iterator()



# Class EventStream

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.events.EventStream

All Implemented Interfaces:
    `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>`

* * *

public class EventStream extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>

Iterable stream of [`Event`](Event.html "class in com.google.adk.events") objects.

  * ## Constructor Summary

Constructors

Constructor

Description

`EventStream([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<[Event](Event.html "class in com.google.adk.events")> eventSupplier)`

Constructs a new event stream.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[Event](Event.html "class in com.google.adk.events")>`

`iterator()`

Returns an iterator that fetches events lazily.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")

`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach\(java.util.function.Consumer\) "class or interface in java.lang"), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#spliterator\(\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### EventStream

public EventStream([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<[Event](Event.html "class in com.google.adk.events")> eventSupplier)

Constructs a new event stream.

  * ## Method Details

    * ### iterator

public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[Event](Event.html "class in com.google.adk.events")> iterator()

Returns an iterator that fetches events lazily.

Specified by:
    `[iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#iterator\(\) "class or interface in java.lang")` in interface `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](Event.html "class in com.google.adk.events")>`




* * *

Copyright (C) 2025\. All rights reserved.
