JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/NodeConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [NodeConfig](NodeConfig.html)
  3. [Builder](NodeConfig.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. retryConfig(RetryConfig)
     2. timeout(Duration)
     3. build()

Hide sidebar  Show sidebar

# Class NodeConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.NodeConfig.Builder

Enclosing class:
    `[NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

* * *

public abstract static class NodeConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`NodeConfig`](NodeConfig.html "class in com.google.adk.workflow").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`final [NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

`build()`

 

`abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")`

`retryConfig(@Nullable [RetryConfig](RetryConfig.html "class in com.google.adk.workflow") retryConfig)`

 

`abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")`

`timeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") timeout)`

Sets the timeout, which must be positive; null imposes no limit.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### retryConfig

@CanIgnoreReturnValue public abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow") retryConfig(@Nullable [RetryConfig](RetryConfig.html "class in com.google.adk.workflow") retryConfig)

    * ### timeout

@CanIgnoreReturnValue public abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow") timeout(@Nullable [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") timeout)

Sets the timeout, which must be positive; null imposes no limit.

    * ### build

public final [NodeConfig](NodeConfig.html "class in com.google.adk.workflow") build()




* * *

Copyright (C) 1980\. All rights reserved.
