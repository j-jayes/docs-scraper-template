JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FunctionCallIds.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [FunctionCallIds](FunctionCallIds.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. generateClientFunctionCallId()
     2. isClientGeneratedFunctionCallId(String)

Hide sidebar  Show sidebar

# Class FunctionCallIds

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.FunctionCallIds

* * *

public final class FunctionCallIds extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Constants and helpers for ADK-generated function call IDs.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`generateClientFunctionCallId()`

Returns a new client-side function call ID with the ADK prefix.

`static boolean`

`isClientGeneratedFunctionCallId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)`

Returns whether `id` was generated client-side by the ADK.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### generateClientFunctionCallId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") generateClientFunctionCallId()

Returns a new client-side function call ID with the ADK prefix.

    * ### isClientGeneratedFunctionCallId

public static boolean isClientGeneratedFunctionCallId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)

Returns whether `id` was generated client-side by the ADK.




* * *

Copyright (C) 1980\. All rights reserved.
