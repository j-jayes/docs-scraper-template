JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ResumabilityConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.apps](package-summary.html)
  2. [ResumabilityConfig](ResumabilityConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ResumabilityConfig()
  6. Method Details
     1. isResumable()
     2. builder()

Hide sidebar  Show sidebar

# Class ResumabilityConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.apps.ResumabilityConfig

* * *

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public abstract class ResumabilityConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Deprecated.

Partial feature: only event-reconstruction-based pause/resume for ` SequentialAgent` is implemented. Full session resumability (persisted agent state, durable resume, other workflow agents) is not yet available. Forward-compatible: the same config will drive full resumability once it lands.

App resumability config, mirroring Python ADK v1's `ResumabilityConfig`: pause on a long-running call and resume from the last event. Applies to all agents in the app.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps")`

Deprecated.

Builder for [`ResumabilityConfig`](ResumabilityConfig.html "class in com.google.adk.apps").

  * ## Constructor Summary

Constructors

Constructor

Description

`ResumabilityConfig()`

Deprecated.

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`static [ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps")`

`builder()`

Deprecated.

 

`abstract boolean`

`isResumable()`

Deprecated.

Whether the app supports agent resumption.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ResumabilityConfig

public ResumabilityConfig()

Deprecated.

  * ## Method Details

    * ### isResumable

public abstract boolean isResumable()

Deprecated.

Whether the app supports agent resumption.

    * ### builder

public static [ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps") builder()

Deprecated.




* * *

Copyright (C) 1980\. All rights reserved.
