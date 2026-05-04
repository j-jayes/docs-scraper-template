JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SearchMemoryResponse.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.memory](package-summary.html)
  2. [SearchMemoryResponse](SearchMemoryResponse.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SearchMemoryResponse()
  6. Method Details
     1. memories()
     2. builder()

Hide sidebar  Show sidebar

# Class SearchMemoryResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.memory.SearchMemoryResponse

* * *

public abstract class SearchMemoryResponse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Represents the response from a memory search.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

Builder for [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory").

  * ## Constructor Summary

Constructors

Constructor

Description

`SearchMemoryResponse()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

`builder()`

Creates a new builder for [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory").

`abstract com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")>`

`memories()`

Returns a list of memory entries that relate to the search query.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### SearchMemoryResponse

public SearchMemoryResponse()

  * ## Method Details

    * ### memories

public abstract com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories()

Returns a list of memory entries that relate to the search query.

    * ### builder

public static [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory") builder()

Creates a new builder for [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory").




* * *

Copyright (C) 1980\. All rights reserved.
