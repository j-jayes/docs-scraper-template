JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ListEventsResponse.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [ListEventsResponse](ListEventsResponse.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ListEventsResponse()
  6. Method Details
     1. events()
     2. nextPageToken()
     3. builder()



# Class ListEventsResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.sessions.ListEventsResponse

* * *

public abstract class ListEventsResponse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Response for listing events.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ListEventsResponse.Builder](ListEventsResponse.Builder.html "class in com.google.adk.sessions")`

Builder for [`ListEventsResponse`](ListEventsResponse.html "class in com.google.adk.sessions").

  * ## Constructor Summary

Constructors

Constructor

Description

`ListEventsResponse()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ListEventsResponse.Builder](ListEventsResponse.Builder.html "class in com.google.adk.sessions")`

`builder()`

 

`abstract com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>`

`events()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`nextPageToken()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ListEventsResponse

public ListEventsResponse()

  * ## Method Details

    * ### events

public abstract com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")> events()

    * ### nextPageToken

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> nextPageToken()

    * ### builder

public static [ListEventsResponse.Builder](ListEventsResponse.Builder.html "class in com.google.adk.sessions") builder()




* * *

Copyright (C) 2025\. All rights reserved.
