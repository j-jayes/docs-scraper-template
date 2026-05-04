JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ComputerUseTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.computeruse](package-summary.html)
  2. [ComputerUseTool](ComputerUseTool.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ComputerUseTool(Object, Method, int[], int[])
  6. Method Details
     1. runAsync(Map, ToolContext)

Hide sidebar  Show sidebar

# Class ComputerUseTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.FunctionTool](../FunctionTool.html "class in com.google.adk.tools")

com.google.adk.tools.computeruse.ComputerUseTool

* * *

public class ComputerUseTool extends [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")

A tool that wraps computer control functions for use with LLMs. 

This tool automatically normalizes coordinates from a virtual coordinate space (by default 1000x1000) to the actual screen size.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](../BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Modifier and Type

Class

Description

`static class `

`[BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")`

Configuration class for tool arguments that allows arbitrary key-value pairs.

`static class `

`[BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Configuration class for a tool definition in YAML/JSON.

  * ## Constructor Summary

Constructors

Constructor

Description

`ComputerUseTool([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, int[] screenSize, int[] virtualScreenSize)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class [FunctionTool](../FunctionTool.html#method-summary "class in com.google.adk.tools")

`[callLive](../FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\) "callLive\(Map, ToolContext, InvocationContext\)"), [create](../FunctionTool.html#create\(java.lang.Class,java.lang.String\) "create\(Class, String\)"), [create](../FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean\) "create\(Class, String, boolean\)"), [create](../FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\) "create\(Class, String, boolean, boolean\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method\) "create\(Object, Method\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean\) "create\(Object, Method, boolean\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\) "create\(Object, Method, boolean, boolean\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.String\) "create\(Object, String\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean\) "create\(Object, String, boolean\)"), [create](../FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\) "create\(Object, String, boolean, boolean\)"), [create](../FunctionTool.html#create\(java.lang.reflect.Method\) "create\(Method\)"), [create](../FunctionTool.html#create\(java.lang.reflect.Method,boolean\) "create\(Method, boolean\)"), [create](../FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\) "create\(Method, boolean, boolean\)"), [declaration](../FunctionTool.html#declaration\(\) "declaration\(\)"), [func](../FunctionTool.html#func\(\) "func\(\)"), [isStreaming](../FunctionTool.html#isStreaming\(\) "isStreaming\(\)")`

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[callLive](../FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Class,java.lang.String\))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean\))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.String\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.reflect.Method\))([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.reflect.Method,boolean\))([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

`[create](../FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\))([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FunctionDeclaration>`

`[declaration](../FunctionTool.html#declaration\(\))()`

Gets the `FunctionDeclaration` representation of this tool.

`[Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect")`

`[func](../FunctionTool.html#func\(\))()`

Returns the underlying function [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect").

`boolean`

`[isStreaming](../FunctionTool.html#isStreaming\(\))()`

Returns true if the wrapped function returns a Flowable and can be used for streaming.

### Methods inherited from class [BaseTool](../BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](../BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](../BaseTool.html#description\(\) "description\(\)"), [fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](../BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](../BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](../BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[customMetadata](../BaseTool.html#customMetadata\(\))()`

Returns a read-only view of the tool metadata.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](../BaseTool.html#description\(\))()`

 

`static [BaseTool](../BaseTool.html "class in com.google.adk.tools")`

`[fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a tool instance from a config.

`boolean`

`[longRunning](../BaseTool.html#longRunning\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](../BaseTool.html#name\(\))()`

 

`io.reactivex.rxjava3.core.Completable`

`[processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments, returning the results converted to a specified class.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool with generic arguments and returns a map of results.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results.

`void`

`[setCustomMetadata](../BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") key, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)`

Sets custom metadata to the tool associated with a key.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ComputerUseTool

public ComputerUseTool([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, int[] screenSize, int[] virtualScreenSize)

  * ## Method Details

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](../FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
