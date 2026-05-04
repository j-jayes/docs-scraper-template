JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ListSessionsResponse.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.sessions](package-summary.html)
  2. [ListSessionsResponse](ListSessionsResponse.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ListSessionsResponse()
  6. Method Details
     1. sessions()
     2. sessionIds()
     3. builder()

Hide sidebar  Show sidebar

# Class ListSessionsResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.sessions.ListSessionsResponse

* * *

public abstract class ListSessionsResponse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Response for listing sessions.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ListSessionsResponse.Builder](ListSessionsResponse.Builder.html "class in com.google.adk.sessions")`

Builder for [`ListSessionsResponse`](ListSessionsResponse.html "class in com.google.adk.sessions").

  * ## Constructor Summary

Constructors

Constructor

Description

`ListSessionsResponse()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ListSessionsResponse.Builder](ListSessionsResponse.Builder.html "class in com.google.adk.sessions")`

`builder()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`sessionIds()`

 

`abstract com.google.common.collect.ImmutableList<[Session](Session.html "class in com.google.adk.sessions")>`

`sessions()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ListSessionsResponse

public ListSessionsResponse()

  * ## Method Details

    * ### sessions

public abstract com.google.common.collect.ImmutableList<[Session](Session.html "class in com.google.adk.sessions")> sessions()

    * ### sessionIds

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> sessionIds()

    * ### builder

public static [ListSessionsResponse.Builder](ListSessionsResponse.Builder.html "class in com.google.adk.sessions") builder()




* * *

Copyright (C) 1980\. All rights reserved.
