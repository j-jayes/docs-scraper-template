JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FunctionCallingUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.FunctionCallingUtils

* * *

public final class FunctionCallingUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for function calling.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.genai.types.FunctionDeclaration`

`buildFunctionDeclaration([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> ignoreParams)`

Builds a FunctionDeclaration from a Java Method, ignoring parameters with the given names.

`static com.google.genai.types.Schema`

`buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") type)`

Builds a Schema from a Java Type, creating a new context for the generation process.

`static com.google.genai.types.Schema`

`buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") type, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Builds a Schema from a Java Type, creating a new context for the generation process.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### buildFunctionDeclaration

public static com.google.genai.types.FunctionDeclaration buildFunctionDeclaration([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> ignoreParams)

Builds a FunctionDeclaration from a Java Method, ignoring parameters with the given names.

Parameters:
    `func` \- The Java [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") to convert into a FunctionDeclaration.
    `ignoreParams` \- The names of parameters to ignore.
Returns:
    The generated `FunctionDeclaration`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.

    * ### buildSchemaFromType

public static com.google.genai.types.Schema buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") type)

Builds a Schema from a Java Type, creating a new context for the generation process.

Parameters:
    `type` \- The Java [`Type`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") to convert into a Schema.
Returns:
    The generated `Schema`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.

    * ### buildSchemaFromType

public static com.google.genai.types.Schema buildSchemaFromType([Type](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") type, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Builds a Schema from a Java Type, creating a new context for the generation process.

Parameters:
    `type` \- The Java [`Type`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Type.html "class or interface in java.lang.reflect") to convert into a Schema.
    `objectMapper` \- The `ObjectMapper` to use for introspecting types.
Returns:
    The generated `Schema`.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if a type is encountered that cannot be serialized by Jackson.




* * *

Copyright (C) 1980\. All rights reserved.
