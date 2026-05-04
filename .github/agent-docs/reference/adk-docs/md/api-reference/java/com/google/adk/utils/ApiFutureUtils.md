JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ApiFutureUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [ApiFutureUtils](ApiFutureUtils.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. toSingle(ApiFuture)
     2. toMaybe(ApiFuture)

Hide sidebar  Show sidebar

# Class ApiFutureUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.ApiFutureUtils

* * *

public class ApiFutureUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for converting ApiFuture to RxJava Single and Maybe types.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static <T> io.reactivex.rxjava3.core.Maybe<T>`

`toMaybe(com.google.api.core.ApiFuture<T> future)`

Converts an ApiFuture to an RxJava Maybe.

`static <T> io.reactivex.rxjava3.core.Single<T>`

`toSingle(com.google.api.core.ApiFuture<T> future)`

Converts an ApiFuture to an RxJava Single.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### toSingle

public static <T> io.reactivex.rxjava3.core.Single<T> toSingle(com.google.api.core.ApiFuture<T> future)

Converts an ApiFuture to an RxJava Single.

Type Parameters:
    `T` \- the type of the result
Parameters:
    `future` \- the ApiFuture to convert
Returns:
    a Single that emits the result of the ApiFuture

    * ### toMaybe

public static <T> io.reactivex.rxjava3.core.Maybe<T> toMaybe(com.google.api.core.ApiFuture<T> future)

Converts an ApiFuture to an RxJava Maybe.

Type Parameters:
    `T` \- the type of the result
Parameters:
    `future` \- the ApiFuture to convert
Returns:
    a Maybe that emits the result of the ApiFuture or completes if the future fails




* * *

Copyright (C) 1980\. All rights reserved.
