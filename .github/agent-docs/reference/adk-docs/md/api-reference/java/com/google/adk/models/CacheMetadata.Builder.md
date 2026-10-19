JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CacheMetadata.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [CacheMetadata](CacheMetadata.html)
  3. [Builder](CacheMetadata.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. fingerprint(String)
     2. contentsCount(int)
     3. cacheName(String)
     4. expireTime(Instant)
     5. invocationsUsed(Integer)
     6. createdAt(Instant)
     7. build()

Hide sidebar  Show sidebar

# Class CacheMetadata.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.CacheMetadata.Builder

Enclosing class:
    `[CacheMetadata](CacheMetadata.html "class in com.google.adk.models")`

* * *

public abstract static class CacheMetadata.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`CacheMetadata`](CacheMetadata.html "class in com.google.adk.models"). The snake_case aliases read metadata that ADK Python wrote.

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

`[CacheMetadata](CacheMetadata.html "class in com.google.adk.models")`

`build()`

Builds the metadata.

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`cacheName(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") cacheName)`

 

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`contentsCount(int contentsCount)`

 

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`createdAt(@Nullable [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") createdAt)`

 

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`expireTime(@Nullable [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") expireTime)`

 

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`fingerprint([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") fingerprint)`

 

`abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models")`

`invocationsUsed(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") invocationsUsed)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### fingerprint

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") fingerprint([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") fingerprint)

    * ### contentsCount

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") contentsCount(int contentsCount)

    * ### cacheName

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") cacheName(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") cacheName)

    * ### expireTime

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") expireTime(@Nullable [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") expireTime)

    * ### invocationsUsed

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") invocationsUsed(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") invocationsUsed)

    * ### createdAt

public abstract [CacheMetadata.Builder](CacheMetadata.Builder.html "class in com.google.adk.models") createdAt(@Nullable [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") createdAt)

    * ### build

public [CacheMetadata](CacheMetadata.html "class in com.google.adk.models") build()

Builds the metadata.

Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if a count is negative, or if only some of `cacheName`, `expireTime` and `invocationsUsed` are set




* * *

Copyright (C) 1980\. All rights reserved.
