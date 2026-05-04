JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpToolset.McpToolsetConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpToolset](McpToolset.html)
  3. [McpToolsetConfig](McpToolset.McpToolsetConfig.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. McpToolsetConfig()
  5. Method Details
     1. stdioConnectionParams()
     2. setStdioConnectionParams(StdioConnectionParameters)
     3. stdioServerParams()
     4. setStdioServerParams(StdioServerParameters)
     5. sseServerParams()
     6. setSseServerParams(SseServerParameters)
     7. toolFilter()
     8. setToolFilter(List)

Hide sidebar  Show sidebar

# Class McpToolset.McpToolsetConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")

com.google.adk.tools.mcp.McpToolset.McpToolsetConfig

Enclosing class:
    `[McpToolset](McpToolset.html "class in com.google.adk.tools.mcp")`

* * *

public static class McpToolset.McpToolsetConfig extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")

Configuration class for MCPToolset.

  * ## Constructor Summary

Constructors

Constructor

Description

`McpToolsetConfig()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`setSseServerParams([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") sseServerParams)`

 

`void`

`setStdioConnectionParams([StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp") stdioConnectionParams)`

 

`void`

`setStdioServerParams([StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp") stdioServerParams)`

 

`void`

`setToolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolFilter)`

 

`[SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")`

`sseServerParams()`

 

`[StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp")`

`stdioConnectionParams()`

 

`[StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp")`

`stdioServerParams()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`toolFilter()`

 

### Methods inherited from class [JsonBaseModel](../../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### McpToolsetConfig

public McpToolsetConfig()

  * ## Method Details

    * ### stdioConnectionParams

public [StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp") stdioConnectionParams()

    * ### setStdioConnectionParams

public void setStdioConnectionParams([StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp") stdioConnectionParams)

    * ### stdioServerParams

public [StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp") stdioServerParams()

    * ### setStdioServerParams

public void setStdioServerParams([StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp") stdioServerParams)

    * ### sseServerParams

public [SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") sseServerParams()

    * ### setSseServerParams

public void setSseServerParams([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") sseServerParams)

    * ### toolFilter

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolFilter()

    * ### setToolFilter

public void setToolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolFilter)




* * *

Copyright (C) 1980\. All rights reserved.
