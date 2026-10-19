JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/UuidProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.platform](package-summary.html)
  2. [UuidProvider](UuidProvider.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. SYSTEM
  5. Method Details
     1. newUuid()

Hide sidebar  Show sidebar

# Interface UuidProvider

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public interface UuidProvider

Supplies new unique identifiers for ADK-generated ids. Implementations must be thread-safe and return a distinct value on every call; configure one with ` Runner.Builder.uuidProvider(UuidProvider)`.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [UuidProvider](UuidProvider.html "interface in com.google.adk.platform")`

`SYSTEM`

A provider backed by [`UUID.randomUUID()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#randomUUID\(\)).

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`newUuid()`

Returns a new unique identifier.




  * ## Field Details

    * ### SYSTEM

static final [UuidProvider](UuidProvider.html "interface in com.google.adk.platform") SYSTEM

A provider backed by [`UUID.randomUUID()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#randomUUID\(\)).

  * ## Method Details

    * ### newUuid

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") newUuid()

Returns a new unique identifier.




* * *

Copyright (C) 1980\. All rights reserved.
