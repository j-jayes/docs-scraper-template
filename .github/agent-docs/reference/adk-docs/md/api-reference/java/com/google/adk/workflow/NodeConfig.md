JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/NodeConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [NodeConfig](NodeConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. NodeConfig()
  6. Method Details
     1. retryConfig()
     2. timeout()
     3. builder()
     4. toBuilder()

Hide sidebar  Show sidebar

# Class NodeConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.NodeConfig

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public abstract class NodeConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

A node's retry policy and execution timeout.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")`

Builder for [`NodeConfig`](NodeConfig.html "class in com.google.adk.workflow").

  * ## Constructor Summary

Constructors

Constructor

Description

`NodeConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[RetryConfig](RetryConfig.html "class in com.google.adk.workflow")>`

`retryConfig()`

Returns how the node is retried when it fails; empty does not retry.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")>`

`timeout()`

Returns how long an attempt may run before it is cancelled and treated as a failure; empty imposes no limit.

`abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")`

`toBuilder()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### NodeConfig

public NodeConfig()

  * ## Method Details

    * ### retryConfig

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[RetryConfig](RetryConfig.html "class in com.google.adk.workflow")> retryConfig()

Returns how the node is retried when it fails; empty does not retry.

    * ### timeout

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")> timeout()

Returns how long an attempt may run before it is cancelled and treated as a failure; empty imposes no limit.

    * ### builder

public static [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow") builder()

    * ### toBuilder

public abstract [NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow") toBuilder()




* * *

Copyright (C) 1980\. All rights reserved.
