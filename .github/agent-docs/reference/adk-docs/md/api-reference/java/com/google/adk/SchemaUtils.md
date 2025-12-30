JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/SchemaUtils.html)
  * [Tree](package-tree.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)



  1. [com.google.adk](package-summary.html)
  2. [SchemaUtils](SchemaUtils.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. validateMapOnSchema(Map, Schema, Boolean)
     2. validateOutputSchema(String, Schema)



# Class SchemaUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.SchemaUtils

* * *

public final class SchemaUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for validating schemas.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`validateMapOnSchema([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, com.google.genai.types.Schema schema, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") isInput)`

Validates a map against a schema.

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`validateOutputSchema([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") output, com.google.genai.types.Schema schema)`

Validates an output string against a schema.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### validateMapOnSchema

public static void validateMapOnSchema([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, com.google.genai.types.Schema schema, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") isInput)

Validates a map against a schema.

Parameters:
    `args` \- The map to validate.
    `schema` \- The schema to validate against.
    `isInput` \- Whether the map is an input or output.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- If the map does not match the schema.

    * ### validateOutputSchema

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> validateOutputSchema([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") output, com.google.genai.types.Schema schema) throws com.fasterxml.jackson.core.JsonProcessingException

Validates an output string against a schema.

Parameters:
    `output` \- The output string to validate.
    `schema` \- The schema to validate against.
Returns:
    The output map.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- If the output string does not match the schema.
    `com.fasterxml.jackson.core.JsonProcessingException` \- If the output string cannot be parsed.




* * *

Copyright (C) 2025\. All rights reserved.
