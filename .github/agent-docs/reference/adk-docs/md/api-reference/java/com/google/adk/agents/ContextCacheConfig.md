JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContextCacheConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [ContextCacheConfig](ContextCacheConfig.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ContextCacheConfig()
     2. ContextCacheConfig(int, Duration, int)
  5. Method Details
     1. getTtlString()
     2. toString()
     3. hashCode()
     4. equals(Object)
     5. maxInvocations()
     6. ttl()
     7. minTokens()

Hide sidebar  Show sidebar

# Record Class ContextCacheConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.agents.ContextCacheConfig

Record Components:
    `maxInvocations` \- Maximum number of invocations to reuse the same cache before refreshing it. Defaults to 10.
    `ttl` \- Time-to-live for cache. Defaults to 1800 seconds (30 minutes).
    `minTokens` \- Minimum estimated request tokens required to enable caching. This compares against the estimated total tokens of the request (system instruction + tools + contents). Context cache storage may have cost. Set higher to avoid caching small requests where overhead may exceed benefits. Defaults to 0.

* * *

public record ContextCacheConfig(int maxInvocations, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

Configuration for context caching across all agents in an app. 

This configuration enables and controls context caching behavior for all LLM agents in an app. When this config is present on an app, context caching is enabled for all agents. When absent (null), context caching is disabled. 

Context caching can significantly reduce costs and improve response times by reusing previously processed context across multiple requests.

  * ## Constructor Summary

Constructors

Constructor

Description

`ContextCacheConfig()`

 

`ContextCacheConfig(int maxInvocations, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens)`

Creates an instance of a `ContextCacheConfig` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getTtlString()`

Returns TTL as string format for cache creation.

`final int`

`hashCode()`

Returns a hash code value for this object.

`int`

`maxInvocations()`

Returns the value of the `maxInvocations` record component.

`int`

`minTokens()`

Returns the value of the `minTokens` record component.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

`[Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`ttl()`

Returns the value of the `ttl` record component.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ContextCacheConfig

public ContextCacheConfig()

    * ### ContextCacheConfig

public ContextCacheConfig(int maxInvocations, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens)

Creates an instance of a `ContextCacheConfig` record class.

Parameters:
    `maxInvocations` \- the value for the `maxInvocations` record component
    `ttl` \- the value for the `ttl` record component
    `minTokens` \- the value for the `minTokens` record component

  * ## Method Details

    * ### getTtlString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getTtlString()

Returns TTL as string format for cache creation.

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. Reference components are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\)); primitive components are compared with the `compare` method from their corresponding wrapper classes.

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### maxInvocations

public int maxInvocations()

Returns the value of the `maxInvocations` record component.

Returns:
    the value of the `maxInvocations` record component

    * ### ttl

public [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl()

Returns the value of the `ttl` record component.

Returns:
    the value of the `ttl` record component

    * ### minTokens

public int minTokens()

Returns the value of the `minTokens` record component.

Returns:
    the value of the `minTokens` record component




* * *

Copyright (C) 1980\. All rights reserved.
