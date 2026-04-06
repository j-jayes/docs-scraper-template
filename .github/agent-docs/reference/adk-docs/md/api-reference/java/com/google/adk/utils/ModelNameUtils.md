JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ModelNameUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.utils](package-summary.html)
  2. [ModelNameUtils](ModelNameUtils.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. isGeminiModel(String)
     2. isGemini2Model(String)
     3. isInstanceOfGemini(Object)
     4. canUseOutputSchemaWithTools(String)

Hide sidebar  Show sidebar

# Class ModelNameUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.utils.ModelNameUtils

* * *

public final class ModelNameUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for model names.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static boolean`

`canUseOutputSchemaWithTools([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)`

Returns true if the model supports using output schema together with tools.

`static boolean`

`isGemini2Model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)`

 

`static boolean`

`isGeminiModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)`

 

`static boolean`

`isInstanceOfGemini([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

Checks whether an object is an instance of [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), by searching through its class hierarchy for a class whose name equals the hardcoded String name of Gemini class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### isGeminiModel

public static boolean isGeminiModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)

    * ### isGemini2Model

public static boolean isGemini2Model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)

    * ### isInstanceOfGemini

public static boolean isInstanceOfGemini([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Checks whether an object is an instance of [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), by searching through its class hierarchy for a class whose name equals the hardcoded String name of Gemini class. 

This method can be used where the "real" instanceof check is not possible because the Gemini type is not known at compile time.

Parameters:
    `o` \- The object to check.
Returns:
    true if object's class is [`Gemini`](../models/Gemini.html "class in com.google.adk.models"), false otherwise.

    * ### canUseOutputSchemaWithTools

public static boolean canUseOutputSchemaWithTools([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelString)

Returns true if the model supports using output schema together with tools.

Parameters:
    `modelString` \- The model name or path.
Returns:
    true if output schema with tools is supported, false otherwise.




* * *

Copyright (C) 1980\. All rights reserved.
