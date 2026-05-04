JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolConfirmation.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](package-summary.html)
  2. [ToolConfirmation](ToolConfirmation.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ToolConfirmation()
  6. Method Details
     1. hint()
     2. confirmed()
     3. payload()
     4. builder()
     5. toBuilder()

Hide sidebar  Show sidebar

# Class ToolConfirmation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.events.ToolConfirmation

* * *

public abstract class ToolConfirmation extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Represents a tool confirmation configuration.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ToolConfirmation.Builder](ToolConfirmation.Builder.html "class in com.google.adk.events")`

Builder for [`ToolConfirmation`](ToolConfirmation.html "class in com.google.adk.events").

  * ## Constructor Summary

Constructors

Constructor

Description

`ToolConfirmation()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ToolConfirmation.Builder](ToolConfirmation.Builder.html "class in com.google.adk.events")`

`builder()`

 

`abstract boolean`

`confirmed()`

 

`abstract @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`hint()`

 

`abstract @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`

`payload()`

 

`abstract [ToolConfirmation.Builder](ToolConfirmation.Builder.html "class in com.google.adk.events")`

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




  * ## Constructor Details

    * ### ToolConfirmation

public ToolConfirmation()

  * ## Method Details

    * ### hint

public abstract @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint()

    * ### confirmed

public abstract boolean confirmed()

    * ### payload

public abstract @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") payload()

    * ### builder

public static [ToolConfirmation.Builder](ToolConfirmation.Builder.html "class in com.google.adk.events") builder()

    * ### toBuilder

public abstract [ToolConfirmation.Builder](ToolConfirmation.Builder.html "class in com.google.adk.events") toBuilder()




* * *

Copyright (C) 1980\. All rights reserved.
