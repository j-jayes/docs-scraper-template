JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Recordings.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins.recordings](package-summary.html)
  2. [Recordings](Recordings.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Recordings()
  6. Method Details
     1. recordings()
     2. builder()
     3. of(List)

Hide sidebar  Show sidebar

# Class Recordings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.recordings.Recordings

* * *

public abstract class Recordings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

All recordings in chronological order.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[Recordings.Builder](Recordings.Builder.html "class in com.google.adk.plugins.recordings")`

Builder for Recordings.

  * ## Constructor Summary

Constructors

Constructor

Description

`Recordings()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Recordings.Builder](Recordings.Builder.html "class in com.google.adk.plugins.recordings")`

`builder()`

 

`static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings")`

`of([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Recording](Recording.html "class in com.google.adk.plugins.recordings")> recordings)`

 

`abstract com.google.common.collect.ImmutableList<[Recording](Recording.html "class in com.google.adk.plugins.recordings")>`

`recordings()`

Chronological list of all recordings.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Recordings

public Recordings()

  * ## Method Details

    * ### recordings

public abstract com.google.common.collect.ImmutableList<[Recording](Recording.html "class in com.google.adk.plugins.recordings")> recordings()

Chronological list of all recordings.

    * ### builder

public static [Recordings.Builder](Recordings.Builder.html "class in com.google.adk.plugins.recordings") builder()

    * ### of

public static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings") of([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Recording](Recording.html "class in com.google.adk.plugins.recordings")> recordings)




* * *

Copyright (C) 1980\. All rights reserved.
