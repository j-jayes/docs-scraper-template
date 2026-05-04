JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContextFilterPlugin.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins](package-summary.html)
  2. [ContextFilterPlugin](ContextFilterPlugin.html)
  3. [Builder](ContextFilterPlugin.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. numInvocationsToKeep(int)
     2. customFilter(UnaryOperator)
     3. name(String)
     4. build()

Hide sidebar  Show sidebar

# Class ContextFilterPlugin.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.ContextFilterPlugin.Builder

Enclosing class:
    `[ContextFilterPlugin](ContextFilterPlugin.html "class in com.google.adk.plugins")`

* * *

public static class ContextFilterPlugin.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`ContextFilterPlugin`](ContextFilterPlugin.html "class in com.google.adk.plugins").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[ContextFilterPlugin](ContextFilterPlugin.html "class in com.google.adk.plugins")`

`build()`

 

`[ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")`

`customFilter([UnaryOperator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/UnaryOperator.html "interface in java.util.function")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content>> customFilter)`

 

`[ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`[ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")`

`numInvocationsToKeep(int numInvocationsToKeep)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### numInvocationsToKeep

@CanIgnoreReturnValue public [ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") numInvocationsToKeep(int numInvocationsToKeep)

    * ### customFilter

@CanIgnoreReturnValue public [ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") customFilter([UnaryOperator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/UnaryOperator.html "interface in java.util.function")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content>> customFilter)

    * ### name

@CanIgnoreReturnValue public [ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### build

public [ContextFilterPlugin](ContextFilterPlugin.html "class in com.google.adk.plugins") build()




* * *

Copyright (C) 1980\. All rights reserved.
