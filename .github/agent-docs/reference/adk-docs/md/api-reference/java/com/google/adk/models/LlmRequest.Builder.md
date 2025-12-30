JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmRequest.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [LlmRequest](LlmRequest.html)
  3. [Builder](LlmRequest.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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
     6. appendInstructions(List)
     7. appendTools(List)
     8. outputSchema(Schema)
     9. build()



# Class LlmRequest.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.LlmRequest.Builder

Enclosing class:
    `[LlmRequest](LlmRequest.html "class in com.google.adk.models")`

* * *

public abstract static class LlmRequest.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`appendInstructions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> instructions)`

 

`final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`appendTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`abstract [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`build()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig>`

`config()`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`config(com.google.genai.types.GenerateContentConfig config)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`contents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> contents)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`liveConnectConfig(com.google.genai.types.LiveConnectConfig liveConnectConfig)`

 

`abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

`final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models")`

`outputSchema(com.google.genai.types.Schema schema)`

Sets the output schema for the LLM response.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### model

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)

    * ### contents

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") contents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> contents)

    * ### config

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") config(com.google.genai.types.GenerateContentConfig config)

    * ### config

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config()

    * ### liveConnectConfig

@CanIgnoreReturnValue public abstract [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") liveConnectConfig(com.google.genai.types.LiveConnectConfig liveConnectConfig)

    * ### appendInstructions

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") appendInstructions([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> instructions)

    * ### appendTools

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") appendTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools)

    * ### outputSchema

@CanIgnoreReturnValue public final [LlmRequest.Builder](LlmRequest.Builder.html "class in com.google.adk.models") outputSchema(com.google.genai.types.Schema schema)

Sets the output schema for the LLM response. If set, The output content will always be a JSON string that conforms to the schema.

    * ### build

public abstract [LlmRequest](LlmRequest.html "class in com.google.adk.models") build()




* * *

Copyright (C) 2025\. All rights reserved.
