JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FunctionCallingUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [FunctionCallingUtils](FunctionCallingUtils.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. buildFunctionDeclaration(Method, List)
     2. buildSchemaFromType(Type)
     3. buildSchemaFromType(Type, ObjectMapper)

Hide sidebar  Show sidebar

# Class FunctionCallingUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.FunctionCallingUtils

* * *

public final class FunctionCallingUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for function calling.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.genai.types.FunctionDeclaration`

`buildFunctionDeclaration([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> ignoreParams)`

Builds a FunctionDeclaration from a Java Method, ignoring parameters with the given names.

`static com.google.genai.types.Schema`

`buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") type)`

Builds a Schema from a Java Type, creating a new context for the generation process.

`static com.google.genai.types.Schema`

`buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") type, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Builds a Schema from a Java Type, creating a new context for the generation process.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### buildFunctionDeclaration

public static com.google.genai.types.FunctionDeclaration buildFunctionDeclaration([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> ignoreParams)

Builds a FunctionDeclaration from a Java Method, ignoring parameters with the given names.

Parameters:
    `func` \- The Java [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") to convert into a FunctionDeclaration.
    `ignoreParams` \- The names of parameters to ignore.
Returns:
    The generated `FunctionDeclaration`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.

    * ### buildSchemaFromType

public static com.google.genai.types.Schema buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") type)

Builds a Schema from a Java Type, creating a new context for the generation process.

Parameters:
    `type` \- The Java [`Type`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") to convert into a Schema.
Returns:
    The generated `Schema`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.

    * ### buildSchemaFromType

public static com.google.genai.types.Schema buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") type, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Builds a Schema from a Java Type, creating a new context for the generation process.

Parameters:
    `type` \- The Java [`Type`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "interface in java.lang.reflect") to convert into a Schema.
    `objectMapper` \- The `ObjectMapper` to use for introspecting types.
Returns:
    The generated `Schema`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.




* * *

Copyright (C) 1980\. All rights reserved.
