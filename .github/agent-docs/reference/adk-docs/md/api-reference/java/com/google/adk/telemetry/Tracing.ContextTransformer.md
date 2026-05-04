JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Tracing.ContextTransformer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Tracing](Tracing.html)
  3. [ContextTransformer](Tracing.ContextTransformer.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. apply(Flowable)
     2. apply(Single)
     3. apply(Maybe)
     4. apply(Completable)

Hide sidebar  Show sidebar

# Class Tracing.ContextTransformer<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Tracing.ContextTransformer<T>

Type Parameters:
    `T` \- The type of the stream.

All Implemented Interfaces:
    `io.reactivex.rxjava3.core.CompletableTransformer, io.reactivex.rxjava3.core.FlowableTransformer<T,T>, io.reactivex.rxjava3.core.MaybeTransformer<T,T>, io.reactivex.rxjava3.core.SingleTransformer<T,T>`

Enclosing class:
    `[Tracing](Tracing.html "class in com.google.adk.telemetry")`

* * *

public static final class Tracing.ContextTransformer<T> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements io.reactivex.rxjava3.core.FlowableTransformer<T,T>, io.reactivex.rxjava3.core.SingleTransformer<T,T>, io.reactivex.rxjava3.core.MaybeTransformer<T,T>, io.reactivex.rxjava3.core.CompletableTransformer

A transformer that re-activates a given context for the duration of the stream's subscription.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.CompletableSource`

`apply(io.reactivex.rxjava3.core.Completable upstream)`

 

`org.reactivestreams.Publisher<T>`

`apply(io.reactivex.rxjava3.core.Flowable<T> upstream)`

 

`io.reactivex.rxjava3.core.MaybeSource<T>`

`apply(io.reactivex.rxjava3.core.Maybe<T> upstream)`

 

`io.reactivex.rxjava3.core.SingleSource<T>`

`apply(io.reactivex.rxjava3.core.Single<T> upstream)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### apply

public org.reactivestreams.Publisher<T> apply(io.reactivex.rxjava3.core.Flowable<T> upstream)

Specified by:
    `apply` in interface `io.reactivex.rxjava3.core.FlowableTransformer<T,T>`

    * ### apply

public io.reactivex.rxjava3.core.SingleSource<T> apply(io.reactivex.rxjava3.core.Single<T> upstream)

Specified by:
    `apply` in interface `io.reactivex.rxjava3.core.SingleTransformer<T,T>`

    * ### apply

public io.reactivex.rxjava3.core.MaybeSource<T> apply(io.reactivex.rxjava3.core.Maybe<T> upstream)

Specified by:
    `apply` in interface `io.reactivex.rxjava3.core.MaybeTransformer<T,T>`

    * ### apply

public io.reactivex.rxjava3.core.CompletableSource apply(io.reactivex.rxjava3.core.Completable upstream)

Specified by:
    `apply` in interface `io.reactivex.rxjava3.core.CompletableTransformer`




* * *

Copyright (C) 1980\. All rights reserved.
