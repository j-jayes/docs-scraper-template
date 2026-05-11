JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmRegistry.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [LlmRegistry](LlmRegistry.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. registerLlm(String, LlmRegistry.LlmFactory)
     2. getLlm(String)

Hide sidebar  Show sidebar

# Class LlmRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.LlmRegistry

* * *

public final class LlmRegistry extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Central registry for managing Large Language Model (LLM) instances.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static interface `

`[LlmRegistry.LlmFactory](LlmRegistry.LlmFactory.html "interface in com.google.adk.models")`

The factory interface for creating LLM instances.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [BaseLlm](BaseLlm.html "class in com.google.adk.models")`

`getLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)`

Returns an LLM instance for the given model name, using a cached or new factory-created instance.

`static void`

`registerLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelNamePattern, [LlmRegistry.LlmFactory](LlmRegistry.LlmFactory.html "interface in com.google.adk.models") factory)`

Registers a factory for model names matching the given regex pattern.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### registerLlm

public static void registerLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelNamePattern, [LlmRegistry.LlmFactory](LlmRegistry.LlmFactory.html "interface in com.google.adk.models") factory)

Registers a factory for model names matching the given regex pattern.

Parameters:
    `modelNamePattern` \- Regex pattern for matching model names.
    `factory` \- Factory to create LLM instances.

    * ### getLlm

public static [BaseLlm](BaseLlm.html "class in com.google.adk.models") getLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)

Returns an LLM instance for the given model name, using a cached or new factory-created instance.

Parameters:
    `modelName` \- Model name to look up.
Returns:
    Matching [`BaseLlm`](BaseLlm.html "class in com.google.adk.models") instance.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- If no factory matches the model name.




* * *

Copyright (C) 1980\. All rights reserved.
