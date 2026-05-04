JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmRequest.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](package-summary.html)
  2. [LlmRequest](LlmRequest.html)
  3. [Builder](LlmRequest.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. model(String)
     2. contents(List)
     3. config(GenerateContentConfig)
     4. config()
     5. liveConnectConfig(LiveConnectConfig)
     6. tools(Map)
     7. appendInstructions(List)
     8. appendTools(List)
     9. outputSchema(Schema)
     10. build()

Hide sidebar  Show sidebar

# Class LlmRequest.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.LlmRequest.Builder

Enclosing class:
    `[LlmRequest](LlmRequest.html "class in com.google.adk.models")`

* * *

public abstract static class LlmRequest.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for constructing [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") instances.

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`appendInstructions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> instructions)`

 

`final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`appendTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`abstract [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`build()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GenerateContentConfig>`

`config()`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`config(com.google.genai.types.GenerateContentConfig config)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`contents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content> contents)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`liveConnectConfig(com.google.genai.types.LiveConnectConfig liveConnectConfig)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)`

 

`final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`outputSchema(com.google.genai.types.Schema schema)`

Sets the output schema for the LLM response.

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`tools([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### model

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)

    * ### contents

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") contents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Content> contents)

    * ### config

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") config(com.google.genai.types.GenerateContentConfig config)

    * ### config

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GenerateContentConfig> config()

    * ### liveConnectConfig

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") liveConnectConfig(com.google.genai.types.LiveConnectConfig liveConnectConfig)

    * ### tools

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") tools([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)

    * ### appendInstructions

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") appendInstructions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> instructions)

    * ### appendTools

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") appendTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)

    * ### outputSchema

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") outputSchema(com.google.genai.types.Schema schema)

Sets the output schema for the LLM response. If set, The output content will always be a JSON string that conforms to the schema.

    * ### build

public abstract [LlmRequest](LlmRequest.html "class in com.google.adk.models") build()




* * *

Copyright (C) 1980\. All rights reserved.
