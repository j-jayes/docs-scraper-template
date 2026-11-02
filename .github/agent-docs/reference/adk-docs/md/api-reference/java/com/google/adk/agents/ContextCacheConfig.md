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
     1. ContextCacheConfig(int, Duration, int, HttpOptions)
     2. ContextCacheConfig()
     3. ContextCacheConfig(int, Duration, int)
  5. Method Details
     1. maxInvocations()
     2. getTtlString()
     3. toString()
     4. hashCode()
     5. equals(Object)
     6. cacheIntervals()
     7. ttl()
     8. minTokens()
     9. createHttpOptions()

Hide sidebar  Show sidebar

# Record Class ContextCacheConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.agents.ContextCacheConfig

Record Components:
    `cacheIntervals` \- maximum number of invocations that reuse the same cache before it is refreshed; must be from 1 to 100
    `ttl` \- time-to-live of the cache; must be a whole number of seconds, at least one
    `minTokens` \- minimum prompt token count of the agent's previous request needed to create a cache; raise it to skip small requests, where cache storage can cost more than it saves; must not be negative
    `createHttpOptions` \- HTTP options, such as a timeout, for the call that creates a cache, or `null` to use the client's defaults; if that call fails, the request is sent without a cache

* * *

public record ContextCacheConfig(int cacheIntervals, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens, @Nullable com.google.genai.types.HttpOptions createHttpOptions) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

Configures context caching for all agents in an app. Without it, nothing is cached.

  * ## Constructor Summary

Constructors

Constructor

Description

`ContextCacheConfig()`

Creates a config with the defaults: `cacheIntervals` of 10, `ttl` of 30 minutes, `minTokens` of 0, and the client's default HTTP options (`createHttpOptions` is `null`).

`ContextCacheConfig(int cacheIntervals, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens)`

Creates a config that creates caches with the client's default HTTP options.

`ContextCacheConfig(int cacheIntervals, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens, @Nullable com.google.genai.types.HttpOptions createHttpOptions)`

Creates a config.

  * ## Method Summary

All MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`int`

`cacheIntervals()`

Returns the value of the `cacheIntervals` record component.

`@Nullable com.google.genai.types.HttpOptions`

`createHttpOptions()`

Returns the value of the `createHttpOptions` record component.

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getTtlString()`

Returns the TTL in the `"<seconds>s"` form that the Gemini API uses.

`final int`

`hashCode()`

Returns a hash code value for this object.

`int`

`maxInvocations()`

Deprecated.

Use `cacheIntervals()`, the name ADK Python and ADK Kotlin use.

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

public ContextCacheConfig(int cacheIntervals, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens, @Nullable com.google.genai.types.HttpOptions createHttpOptions)

Creates a config.

Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if a value is out of range

    * ### ContextCacheConfig

public ContextCacheConfig()

Creates a config with the defaults: `cacheIntervals` of 10, `ttl` of 30 minutes, `minTokens` of 0, and the client's default HTTP options (`createHttpOptions` is `null`).

    * ### ContextCacheConfig

public ContextCacheConfig(int cacheIntervals, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") ttl, int minTokens)

Creates a config that creates caches with the client's default HTTP options.

  * ## Method Details

    * ### maxInvocations

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") @InlineMe(replacement="this.cacheIntervals()") public int maxInvocations()

Deprecated.

Use `cacheIntervals()`, the name ADK Python and ADK Kotlin use.

Returns `cacheIntervals()`.

    * ### getTtlString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getTtlString()

Returns the TTL in the `"<seconds>s"` form that the Gemini API uses.

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

    * ### cacheIntervals

public int cacheIntervals()

Returns the value of the `cacheIntervals` record component.

Returns:
    the value of the `cacheIntervals` record component

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

    * ### createHttpOptions

public @Nullable com.google.genai.types.HttpOptions createHttpOptions()

Returns the value of the `createHttpOptions` record component.

Returns:
    the value of the `createHttpOptions` record component




* * *

Copyright (C) 1980\. All rights reserved.
