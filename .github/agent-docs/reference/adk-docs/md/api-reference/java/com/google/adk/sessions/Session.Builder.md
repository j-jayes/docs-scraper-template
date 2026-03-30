JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Session.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [Session](Session.html)
  3. [Builder](Session.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder(String)
     2. Builder(SessionKey)
  5. Method Details
     1. id(String)
     2. sessionKey(SessionKey)
     3. state(State)
     4. state(Map)
     5. appName(String)
     6. userId(String)
     7. events(List)
     8. lastUpdateTime(Instant)
     9. lastUpdateTimeSeconds(double)
     10. build()

Hide sidebar  Show sidebar

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

`Builder([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new [`Session.Builder`](Session.Builder.html "class in com.google.adk.sessions") with the given session key.

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

`sessionKey([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Sets the session key.

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`state([State](State.html "class in com.google.adk.sessions") state)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`state([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

 

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`userId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)

    * ### Builder

public Builder([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)

Creates a new [`Session.Builder`](Session.Builder.html "class in com.google.adk.sessions") with the given session key.

  * ## Method Details

    * ### id

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)

    * ### sessionKey

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") sessionKey([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)

Sets the session key.

    * ### state

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") state([State](State.html "class in com.google.adk.sessions") state)

    * ### state

@CanIgnoreReturnValue public [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") state([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)

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

Copyright (C) 1980\. All rights reserved.
