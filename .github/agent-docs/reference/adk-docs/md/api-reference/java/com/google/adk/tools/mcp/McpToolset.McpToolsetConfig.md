JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpToolset.McpToolsetConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`setToolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolFilter)`

 

`[SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")`

`sseServerParams()`

 

`[StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp")`

`stdioConnectionParams()`

 

`[StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp")`

`stdioServerParams()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`toolFilter()`

 

### Methods inherited from class [JsonBaseModel](../../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolFilter()

    * ### setToolFilter

public void setToolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolFilter)




* * *

Copyright (C) 1980\. All rights reserved.
