JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/HttpClientFactory.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.internal.http](package-summary.html)
  2. [HttpClientFactory](HttpClientFactory.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getOrCreateSharedHttpClient(String)
     2. createHttpClient(ExecutorService)
     3. daemonExecutor(String)

Hide sidebar  Show sidebar

# Class HttpClientFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.internal.http.HttpClientFactory

* * *

public final class HttpClientFactory extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Creates `OkHttpClient`s for the ADK. The default clients are cached per name so the dispatcher and connection pool are reused across the ADK; a caller that supplies its own executor gets a fresh, non-cached client it owns.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static okhttp3.OkHttpClient`

`createHttpClient([ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent") executorService)`

Returns a new `OkHttpClient` whose dispatcher runs on `executorService`.

`static [ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent")`

`daemonExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns an unbounded pool of daemon threads, matching OkHttp's own dispatcher pool but with daemon threads so a standalone JVM can exit once work is done.

`static okhttp3.OkHttpClient`

`getOrCreateSharedHttpClient([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the shared `OkHttpClient` cached by `name`, using OkHttp's default threading.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### getOrCreateSharedHttpClient

public static okhttp3.OkHttpClient getOrCreateSharedHttpClient([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Returns the shared `OkHttpClient` cached by `name`, using OkHttp's default threading.

    * ### createHttpClient

public static okhttp3.OkHttpClient createHttpClient([ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent") executorService)

Returns a new `OkHttpClient` whose dispatcher runs on `executorService`. Pass `daemonExecutor(String)` so a standalone JVM can exit once work is done, or a container-managed executor in a managed environment. The client is not cached: the caller owns the executor and the returned client.

Parameters:
    `executorService` \- executor for the dispatcher.

    * ### daemonExecutor

public static [ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent") daemonExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Returns an unbounded pool of daemon threads, matching OkHttp's own dispatcher pool but with daemon threads so a standalone JVM can exit once work is done. Managed container environments should inject their own executor instead of calling this.

Parameters:
    `name` \- prefix for the dispatcher thread names.




* * *

Copyright (C) 1980\. All rights reserved.
