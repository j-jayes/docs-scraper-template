JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Tracing.TracerProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Tracing](Tracing.html)
  3. [TracerProvider](Tracing.TracerProvider.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. configure(Consumer)
     2. setParent(Context)
     3. onSuccess(BiConsumer)
     4. apply(Flowable)
     5. apply(Single)
     6. apply(Maybe)
     7. apply(Completable)

Hide sidebar  Show sidebar

# Class Tracing.TracerProvider<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Tracing.TracerProvider<T>

Type Parameters:
    `T` \- The type of the stream.

All Implemented Interfaces:
    `io.reactivex.rxjava3.core.CompletableTransformer, io.reactivex.rxjava3.core.FlowableTransformer<T,T>, io.reactivex.rxjava3.core.MaybeTransformer<T,T>, io.reactivex.rxjava3.core.SingleTransformer<T,T>`

Enclosing class:
    `[Tracing](Tracing.html "class in com.google.adk.telemetry")`

* * *

public static final class Tracing.TracerProvider<T> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements io.reactivex.rxjava3.core.FlowableTransformer<T,T>, io.reactivex.rxjava3.core.SingleTransformer<T,T>, io.reactivex.rxjava3.core.MaybeTransformer<T,T>, io.reactivex.rxjava3.core.CompletableTransformer

A transformer that manages an OpenTelemetry span and scope for RxJava streams.

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

 

`[Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`configure([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<io.opentelemetry.api.trace.Span> configurer)`

Configures the span created by this transformer.

`[Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`onSuccess([BiConsumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiConsumer.html "interface in java.util.function")<io.opentelemetry.api.trace.Span, T> consumer)`

Registers a callback to be executed with the span and the result item when the stream emits a success value.

`[Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`setParent(io.opentelemetry.context.Context parentContext)`

Sets an explicit parent context for the span created by this transformer.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### configure

@CanIgnoreReturnValue public [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> configure([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<io.opentelemetry.api.trace.Span> configurer)

Configures the span created by this transformer.

    * ### setParent

@CanIgnoreReturnValue public [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> setParent(io.opentelemetry.context.Context parentContext)

Sets an explicit parent context for the span created by this transformer.

    * ### onSuccess

@CanIgnoreReturnValue public [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> onSuccess([BiConsumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiConsumer.html "interface in java.util.function")<io.opentelemetry.api.trace.Span, T> consumer)

Registers a callback to be executed with the span and the result item when the stream emits a success value.

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
