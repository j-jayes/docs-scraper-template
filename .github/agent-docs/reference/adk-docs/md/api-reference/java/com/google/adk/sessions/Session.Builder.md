JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Session.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [Session](Session.html)
  3. [Builder](Session.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder(String)
  5. Method Details
     1. id(String)
     2. state(State)
     3. state(ConcurrentMap)
     4. appName(String)
     5. userId(String)
     6. events(List)
     7. lastUpdateTime(Instant)
     8. lastUpdateTimeSeconds(double)
     9. build()



# Class Session.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.sessions.Session.Builder

Enclosing class:
    `[Session](Session.html "class in com.google.adk.sessions")`

* * *

public static final class Session.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`Session`](Session.html "class in com.google.adk.sessions").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

`[Session](Session.html "class in com.google.adk.sessions")`

`build()`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`events([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`lastUpdateTime([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") lastUpdateTime)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`lastUpdateTimeSeconds(double seconds)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`state([State](State.html "class in com.google.adk.sessions") state)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`state([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`userId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)

  * ## Method Details

    * ### id

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)

    * ### state

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") state([State](State.html "class in com.google.adk.sessions") state)

    * ### state

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") state([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)

    * ### appName

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

    * ### userId

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") userId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)

    * ### events

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") events([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

    * ### lastUpdateTime

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") lastUpdateTime([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") lastUpdateTime)

    * ### lastUpdateTimeSeconds

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") lastUpdateTimeSeconds(double seconds)

    * ### build

public [Session](Session.html "class in com.google.adk.sessions") build()




* * *

Copyright (C) 2025\. All rights reserved.
