JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/ContextCachingRun.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.contextcaching](package-summary.html)
  2. [ContextCachingRun](ContextCachingRun.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. main(String[])

Hide sidebar  Show sidebar

# Class ContextCachingRun

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.contextcaching.ContextCachingRun

* * *

public final class ContextCachingRun extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Runs several turns of one session against [`ContextCachingAgent`](ContextCachingAgent.html "class in com.example.contextcaching") and prints what the cache does on each turn. It pauses once so the cache expires, and the next turn creates a new one. Exact turn-by-turn output depends on model latency, since a slow turn can outlast the TTL.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### main

public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args) throws [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class in java.lang")

Throws:
    `[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
