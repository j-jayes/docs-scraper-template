JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ModelNameUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [ModelNameUtils](ModelNameUtils.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. isGeminiModel(String)
     2. isGemini2Model(String)
     3. isGemini2OrAbove(String)
     4. isInstanceOfGemini(Object)
     5. canUseOutputSchemaWithTools(String)

Hide sidebar  Show sidebar

# Class ModelNameUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.ModelNameUtils

* * *

public final class ModelNameUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for model names.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static boolean`

`canUseOutputSchemaWithTools([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)`

Returns true if the model supports using output schema together with tools.

`static boolean`

`isGemini2Model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)`

 

`static boolean`

`isGemini2OrAbove(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)`

 

`static boolean`

`isGeminiModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)`

 

`static boolean`

`isInstanceOfGemini([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Checks whether an object is an instance of [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), by searching through its class hierarchy for a class whose name equals the hardcoded String name of Gemini class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### isGeminiModel

public static boolean isGeminiModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)

    * ### isGemini2Model

public static boolean isGemini2Model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)

    * ### isGemini2OrAbove

public static boolean isGemini2OrAbove(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)

    * ### isInstanceOfGemini

public static boolean isInstanceOfGemini([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)

Checks whether an object is an instance of [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), by searching through its class hierarchy for a class whose name equals the hardcoded String name of Gemini class. 

This method can be used where the "real" instanceof check is not possible because the Gemini type is not known at compile time.

Parameters:
    `o` \- The object to check.
Returns:
    true if object's class is [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), false otherwise.

    * ### canUseOutputSchemaWithTools

public static boolean canUseOutputSchemaWithTools([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelString)

Returns true if the model supports using output schema together with tools.

Parameters:
    `modelString` \- The model name or path.
Returns:
    true if output schema with tools is supported, false otherwise.




* * *

Copyright (C) 1980\. All rights reserved.
