JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../MemoryEntry.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.memory](../package-summary.html)
  2. [MemoryEntry](../MemoryEntry.html)
  3. [Builder](../MemoryEntry.Builder.html)



# Uses of Class  
com.google.adk.memory.MemoryEntry.Builder

Packages that use [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")

Package

Description

com.google.adk.memory

 

  * ## Uses of [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory") in [com.google.adk.memory](../package-summary.html)

Methods in [com.google.adk.memory](../package-summary.html) that return [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")

Modifier and Type

Method

Description

`static [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.`[builder](../MemoryEntry.html#builder\(\))()`

Returns a new builder for creating a [`MemoryEntry`](../MemoryEntry.html "class in com.google.adk.memory").

`abstract [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.Builder.`[setAuthor](../MemoryEntry.Builder.html#setAuthor\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author)`

Sets the author of the memory.

`abstract [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.Builder.`[setContent](../MemoryEntry.Builder.html#setContent\(com.google.genai.types.Content\))(com.google.genai.types.Content content)`

Sets the main content of the memory.

`abstract [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.Builder.`[setTimestamp](../MemoryEntry.Builder.html#setTimestamp\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") timestamp)`

Sets the timestamp when the original content of this memory happened.

`[MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.Builder.`[setTimestamp](../MemoryEntry.Builder.html#setTimestamp\(java.time.Instant\))([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") instant)`

A convenience method to set the timestamp from an [`Instant`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class or interface in java.time") object, formatted as an ISO 8601 string.

`abstract [MemoryEntry.Builder](../MemoryEntry.Builder.html "class in com.google.adk.memory")`

MemoryEntry.`[toBuilder](../MemoryEntry.html#toBuilder\(\))()`

Creates a new builder with a copy of this entry's values.




* * *

Copyright (C) 2025\. All rights reserved.
