JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GetSessionConfig.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [GetSessionConfig](GetSessionConfig.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. GetSessionConfig()
  6. Method Details
     1. numRecentEvents()
     2. afterTimestamp()
     3. builder()



# Class GetSessionConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.sessions.GetSessionConfig

* * *

public abstract class GetSessionConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Configuration for getting a session.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[GetSessionConfig.Builder](GetSessionConfig.Builder.html "class in com.google.adk.sessions")`

Builder for [`GetSessionConfig`](GetSessionConfig.html "class in com.google.adk.sessions").

  * ## Constructor Summary

Constructors

Constructor

Description

`GetSessionConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time")>`

`afterTimestamp()`

 

`static [GetSessionConfig.Builder](GetSessionConfig.Builder.html "class in com.google.adk.sessions")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

`numRecentEvents()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### GetSessionConfig

public GetSessionConfig()

  * ## Method Details

    * ### numRecentEvents

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> numRecentEvents()

    * ### afterTimestamp

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time")> afterTimestamp()

    * ### builder

public static [GetSessionConfig.Builder](GetSessionConfig.Builder.html "class in com.google.adk.sessions") builder()




* * *

Copyright (C) 2025\. All rights reserved.
