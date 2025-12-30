JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SearchMemoryResponse.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [SearchMemoryResponse](SearchMemoryResponse.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SearchMemoryResponse()
  6. Method Details
     1. memories()
     2. builder()



# Class SearchMemoryResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.memory.SearchMemoryResponse

* * *

public abstract class SearchMemoryResponse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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

Copyright (C) 2025\. All rights reserved.
