JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SearchMemoryResponse.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.memory](package-summary.html)
  2. [SearchMemoryResponse](SearchMemoryResponse.html)
  3. [Builder](SearchMemoryResponse.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. setMemories(ImmutableList)
     2. setMemories(List)
     3. memories(ImmutableList)
     4. memories(List)
     5. build()

Hide sidebar  Show sidebar

# Class SearchMemoryResponse.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.memory.SearchMemoryResponse.Builder

Enclosing class:
    `[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")`

* * *

public abstract static class SearchMemoryResponse.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`abstract [SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")`

`build()`

Builds the immutable [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory") object.

`abstract [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

`memories(com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)`

 

`[SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

`memories([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)`

 

`final [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

`setMemories(com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)`

Deprecated.

`final [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory")`

`setMemories([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)`

Deprecated.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setMemories

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory") setMemories(com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)

Deprecated.

    * ### setMemories

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @CanIgnoreReturnValue public final [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory") setMemories([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)

Deprecated.

Sets the list of memory entries using a list.

    * ### memories

@CanIgnoreReturnValue public abstract [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory") memories(com.google.common.collect.ImmutableList<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)

    * ### memories

@CanIgnoreReturnValue public [SearchMemoryResponse.Builder](SearchMemoryResponse.Builder.html "class in com.google.adk.memory") memories([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")> memories)

    * ### build

public abstract [SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory") build()

Builds the immutable [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory") object.




* * *

Copyright (C) 1980\. All rights reserved.
