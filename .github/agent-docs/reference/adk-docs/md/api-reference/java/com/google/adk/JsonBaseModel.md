JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/JsonBaseModel.html)
  * [Tree](package-tree.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)



  1. [com.google.adk](package-summary.html)
  2. [JsonBaseModel](JsonBaseModel.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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



# Class JsonBaseModel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.JsonBaseModel

Direct Known Subclasses:
    `[AdkWebServer.RunEvalResult](web/AdkWebServer.RunEvalResult.html "class in com.google.adk.web")`, `[Event](events/Event.html "class in com.google.adk.events")`, `[LiveRequest](agents/LiveRequest.html "class in com.google.adk.agents")`, `[LlmRequest](models/LlmRequest.html "class in com.google.adk.models")`, `[LlmResponse](models/LlmResponse.html "class in com.google.adk.models")`, `[Session](sessions/Session.html "class in com.google.adk.sessions")`

* * *

public abstract class JsonBaseModel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`fromJsonNode(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")>  
T`

`fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`getMapper()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toJson()`

 

`protected static com.fasterxml.jackson.databind.JsonNode`

`toJsonNode([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") object)`

Serializes an object to a JsonNode.

`protected static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toJsonString([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### JsonBaseModel

public JsonBaseModel()

  * ## Method Details

    * ### toJsonString

protected static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toJsonString([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") object)

Serializes an object to a Json string.

    * ### getMapper

public static com.fasterxml.jackson.databind.ObjectMapper getMapper()

    * ### toJson

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toJson()

    * ### toJsonNode

protected static com.fasterxml.jackson.databind.JsonNode toJsonNode([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") object)

Serializes an object to a JsonNode.

    * ### fromJsonString

public static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")> T fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)

Deserializes a Json string to an object of the given type.

    * ### fromJsonNode

public static <T extends [JsonBaseModel](JsonBaseModel.html "class in com.google.adk")> T fromJsonNode(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)

Deserializes a JsonNode to an object of the given type.




* * *

Copyright (C) 2025\. All rights reserved.
