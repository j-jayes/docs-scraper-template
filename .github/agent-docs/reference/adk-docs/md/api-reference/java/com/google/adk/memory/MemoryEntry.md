JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/MemoryEntry.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [MemoryEntry](MemoryEntry.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. MemoryEntry()
  6. Method Details
     1. content()
     2. author()
     3. timestamp()
     4. builder()
     5. toBuilder()



# Class MemoryEntry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.memory.MemoryEntry

* * *

public abstract class MemoryEntry extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Represents one memory entry.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

Builder for [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory").

  * ## Constructor Summary

Constructors

Constructor

Description

`MemoryEntry()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`author()`

Returns the author of the memory, or null if not set.

`static [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`builder()`

Returns a new builder for creating a [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory").

`abstract com.google.genai.types.Content`

`content()`

Returns the main content of the memory.

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`timestamp()`

Returns the timestamp when the original content of this memory happened, or null if not set.

`abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory")`

`toBuilder()`

Creates a new builder with a copy of this entry's values.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### MemoryEntry

public MemoryEntry()

  * ## Method Details

    * ### content

public abstract com.google.genai.types.Content content()

Returns the main content of the memory.

    * ### author

@Nullable public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author()

Returns the author of the memory, or null if not set.

    * ### timestamp

@Nullable public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") timestamp()

Returns the timestamp when the original content of this memory happened, or null if not set. 

This string will be forwarded to LLM. Preferred format is ISO 8601 format

    * ### builder

public static [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") builder()

Returns a new builder for creating a [`MemoryEntry`](MemoryEntry.html "class in com.google.adk.memory").

    * ### toBuilder

public abstract [MemoryEntry.Builder](MemoryEntry.Builder.html "class in com.google.adk.memory") toBuilder()

Creates a new builder with a copy of this entry's values.

Returns:
    a new [`MemoryEntry.Builder`](MemoryEntry.Builder.html "class in com.google.adk.memory") instance.




* * *

Copyright (C) 2025\. All rights reserved.
