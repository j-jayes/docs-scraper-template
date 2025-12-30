JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LiveRequest.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LiveRequest](LiveRequest.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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



# Class LiveRequest

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Blob>`

`blob()`

Returns the blob of the request.

`static [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`close()`

Returns whether the connection should be closed.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`content()`

Returns the content of the request.

`static [LiveRequest](LiveRequest.html "class in com.google.adk.agents")`

`fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)`

Deserializes a Json string to a [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") object.

`boolean`

`shouldClose()`

Extracts boolean value from the close field or returns false if unset.

`abstract [LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")`

`toBuilder()`

 

### Methods inherited from class com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\)), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\)), [getMapper](../JsonBaseModel.html#getMapper\(\)), [toJson](../JsonBaseModel.html#toJson\(\)), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\)), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### content

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content()

Returns the content of the request. 

If set, send the content to the model in turn-by-turn mode.

Returns:
    An optional `Content` object containing the content of the request.

    * ### blob

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Blob> blob()

Returns the blob of the request. 

If set, send the blob to the model in realtime mode.

Returns:
    An optional `Blob` object containing the blob of the request.

    * ### close

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> close()

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

public static [LiveRequest](LiveRequest.html "class in com.google.adk.agents") fromJsonString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)

Deserializes a Json string to a [`LiveRequest`](LiveRequest.html "class in com.google.adk.agents") object.




* * *

Copyright (C) 2025\. All rights reserved.
