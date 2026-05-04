JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LiveRequest.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LiveRequest](LiveRequest.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. content()
     2. blob()
     3. close()
     4. shouldClose()
     5. builder()
     6. toBuilder()
     7. fromJsonString(String)

Hide sidebar  Show sidebar

# Class LiveRequest

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.agents.LiveRequest

* * *

public abstract class LiveRequest extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Represents a request to be sent to a live connection to the LLM model.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")`

Builder for constructing [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") instances.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Blob>`

`blob()`

Returns the blob of the request.

`static [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`close()`

Returns whether the connection should be closed.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`content()`

Returns the content of the request.

`static [LiveRequest](LiveRequest.html "class in com.google.adk.agents")`

`fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)`

Deserializes a Json string to a [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") object.

`boolean`

`shouldClose()`

Extracts boolean value from the close field or returns false if unset.

`abstract [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")`

`toBuilder()`

 

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### content

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content> content()

Returns the content of the request. 

If set, send the content to the model in turn-by-turn mode.

Returns:
    An optional `Content` object containing the content of the request.

    * ### blob

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Blob> blob()

Returns the blob of the request. 

If set, send the blob to the model in realtime mode.

Returns:
    An optional `Blob` object containing the blob of the request.

    * ### close

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> close()

Returns whether the connection should be closed. 

If set to true, the connection will be closed after the request is sent.

Returns:
    A boolean indicating whether the connection should be closed.

    * ### shouldClose

public boolean shouldClose()

Extracts boolean value from the close field or returns false if unset.

    * ### builder

public static [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents") builder()

    * ### toBuilder

public abstract [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents") toBuilder()

    * ### fromJsonString

public static [LiveRequest](LiveRequest.html "class in com.google.adk.agents") fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)

Deserializes a Json string to a [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") object.




* * *

Copyright (C) 1980\. All rights reserved.
