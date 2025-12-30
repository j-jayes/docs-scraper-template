JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/MemoryEntry.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [MemoryEntry](MemoryEntry.html)
  3. [Builder](MemoryEntry.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. setContent(Content)
     2. setAuthor(String)
     3. setTimestamp(String)
     4. setTimestamp(Instant)
     5. build()



# Class MemoryEntry.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.memory.MemoryEntry.Builder

Enclosing class:
    `[MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")`

* * *

public abstract static class MemoryEntry.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [MemoryEntry](MemoryEntry.html "class in com.google.adk.memory")`

`build()`

Builds the immutable [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory") object.

`abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author)`

Sets the author of the memory.

`abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`setContent(com.google.genai.types.Content content)`

Sets the main content of the memory.

`abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`setTimestamp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") timestamp)`

Sets the timestamp when the original content of this memory happened.

`[MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`setTimestamp([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") instant)`

A convenience method to set the timestamp from an [`Instant`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") object, formatted as an ISO 8601 string.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setContent

public abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") setContent(com.google.genai.types.Content content)

Sets the main content of the memory. 

This is a required field.

    * ### setAuthor

public abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") setAuthor(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author)

Sets the author of the memory.

    * ### setTimestamp

public abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") setTimestamp(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") timestamp)

Sets the timestamp when the original content of this memory happened.

    * ### setTimestamp

public [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") setTimestamp([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") instant)

A convenience method to set the timestamp from an [`Instant`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") object, formatted as an ISO 8601 string.

Parameters:
    `instant` \- The timestamp as an Instant object.

    * ### build

public abstract [MemoryEntry](MemoryEntry.html "class in com.google.adk.memory") build()

Builds the immutable [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory") object.




* * *

Copyright (C) 2025\. All rights reserved.
