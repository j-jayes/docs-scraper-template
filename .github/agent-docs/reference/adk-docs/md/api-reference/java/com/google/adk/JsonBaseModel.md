JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/JsonBaseModel.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk](package-summary.html)
  2. [JsonBaseModel](JsonBaseModel.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. JsonBaseModel()
  5. Method Details
     1. toJsonString(Object)
     2. getMapper()
     3. toJson()
     4. toJsonNode(Object)
     5. fromJsonString(String, Class)
     6. fromJsonNode(JsonNode, Class)

Hide sidebar  Show sidebar

# Class JsonBaseModel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.JsonBaseModel

Direct Known Subclasses:
    `[BaseCodeExecutor](codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors"), [BaseTool.ToolArgsConfig](tools/BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](tools/BaseTool.ToolConfig.html "class in com.google.adk.tools"), [CodeExecutionUtils.CodeExecutionInput](codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors"), [CodeExecutionUtils.CodeExecutionResult](codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors"), [CodeExecutionUtils.File](codeexecutors/CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors"), [Event](events/Event.html "class in com.google.adk.events"), [EventActions](events/EventActions.html "class in com.google.adk.events"), [Example](examples/Example.html "class in com.google.adk.examples"), [Frontmatter](skills/Frontmatter.html "class in com.google.adk.skills"), [LiveRequest](agents/LiveRequest.html "class in com.google.adk.agents"), [LlmRequest](models/LlmRequest.html "class in com.google.adk.models"), [LlmResponse](models/LlmResponse.html "class in com.google.adk.models"), [McpToolset.McpToolsetConfig](tools/mcp/McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp"), [RunEvalResult](web/dto/RunEvalResult.html "class in com.google.adk.web.dto"), [Session](sessions/Session.html "class in com.google.adk.sessions"), [SessionKey](sessions/SessionKey.html "class in com.google.adk.sessions"), [ToolConfirmation](events/ToolConfirmation.html "class in com.google.adk.events")`

* * *

public abstract class JsonBaseModel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

The base class for the types that needs JSON serialization/deserialization capability.

  * ## Constructor Summary

Constructors

Constructor

Description

`JsonBaseModel()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")>  
T`

`fromJsonNode(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")>  
T`

`fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`getMapper()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toJson()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`toJsonNode([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toJsonString([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### JsonBaseModel

public JsonBaseModel()

  * ## Method Details

    * ### toJsonString

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toJsonString([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)

Serializes an object to a Json string.

    * ### getMapper

public static com.fasterxml.jackson.databind.ObjectMapper getMapper()

Returns the mutable ObjectMapper instance used by ADK.

    * ### toJson

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toJson()

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

    * ### toJsonNode

protected static com.fasterxml.jackson.databind.JsonNode toJsonNode([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)

Serializes an object to a JsonNode.

    * ### fromJsonString

public static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")> T fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)

Deserializes a Json string to an object of the given type.

    * ### fromJsonNode

public static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")> T fromJsonNode(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)

Deserializes a JsonNode to an object of the given type.




* * *

Copyright (C) 1980\. All rights reserved.
