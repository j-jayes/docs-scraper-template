JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ToolConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai](package-summary.html)
  2. [ToolConverter](ToolConverter.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ToolConverter()
  6. Method Details
     1. createToolRegistry(Map)
     2. convertSchemaToSpringAi(Schema)
     3. convertToSpringAiTools(Map)

Hide sidebar  Show sidebar

# Class ToolConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.ToolConverter

* * *

public class ToolConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Converts between ADK and Spring AI tool/function formats. 

This converter handles the translation between ADK's BaseTool/FunctionDeclaration format and Spring AI tool representations. This is a simplified initial version that focuses on basic schema conversion and tool metadata handling.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")`

Simple metadata holder for tool information.

  * ## Constructor Summary

Constructors

Constructor

Description

`ToolConverter()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`convertSchemaToSpringAi(com.google.genai.types.Schema schema)`

Converts ADK Schema to Spring AI compatible parameter schema.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<org.springframework.ai.tool.ToolCallback>`

`convertToSpringAiTools([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Converts ADK tools to Spring AI ToolCallback format for tool calling.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")>`

`createToolRegistry([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Creates a tool registry from ADK tools for internal tracking.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ToolConverter

public ToolConverter()

  * ## Method Details

    * ### createToolRegistry

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")> createToolRegistry([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)

Creates a tool registry from ADK tools for internal tracking. 

This method provides a way to track available tools, though Spring AI tool calling integration will be enhanced in subsequent iterations.

Parameters:
    `tools` \- Map of ADK tools to process
Returns:
    Map of tool names to their metadata

    * ### convertSchemaToSpringAi

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> convertSchemaToSpringAi(com.google.genai.types.Schema schema)

Converts ADK Schema to Spring AI compatible parameter schema. 

This provides basic schema conversion for tool parameters.

Parameters:
    `schema` \- The ADK schema to convert
Returns:
    A Map representing the Spring AI compatible schema

    * ### convertToSpringAiTools

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<org.springframework.ai.tool.ToolCallback> convertToSpringAiTools([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)

Converts ADK tools to Spring AI ToolCallback format for tool calling.

Parameters:
    `tools` \- Map of ADK tools to convert
Returns:
    List of Spring AI ToolCallback objects




* * *

Copyright (C) 1980\. All rights reserved.
