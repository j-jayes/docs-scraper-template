JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LongRunningFunctionTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [LongRunningFunctionTool](LongRunningFunctionTool.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
     1. Methods inherited from class FunctionTool
     2. Methods inherited from class BaseTool
     3. Methods inherited from class Object
  4. Method Details
     1. create(Method)
     2. create(Method, boolean)
     3. create(Class, String)
     4. create(Class, String, boolean)
     5. create(Object, String)
     6. create(Object, String, boolean)
     7. create(Object, Method)
     8. create(Object, Method, boolean)
     9. create(FunctionTool)
     10. fromConfig(BaseTool.ToolArgsConfig, String)

Hide sidebar  Show sidebar

# Class LongRunningFunctionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.FunctionTool](FunctionTool.html "class in com.google.adk.tools")

com.google.adk.tools.LongRunningFunctionTool

* * *

public class LongRunningFunctionTool extends [FunctionTool](FunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Modifier and Type

Class

Description

`static class `

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")`

Configuration class for tool arguments that allows arbitrary key-value pairs.

`static class `

`[BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Configuration class for a tool definition in YAML/JSON.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([FunctionTool](FunctionTool.html "class in com.google.adk.tools") tool)`

Creates a LongRunningFunctionTool from a FunctionTool.

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") method)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") method, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

 

### Methods inherited from class [FunctionTool](FunctionTool.html#method-summary "class in com.google.adk.tools")

`[callLive](FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\) "callLive\(Map, ToolContext, InvocationContext\)"), [create](FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\) "create\(Class, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\) "create\(Object, Method, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\) "create\(Object, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\) "create\(Method, boolean, boolean\)"), [declaration](FunctionTool.html#declaration\(\) "declaration\(\)"), [func](FunctionTool.html#func\(\) "func\(\)"), [isStreaming](FunctionTool.html#isStreaming\(\) "isStreaming\(\)"), [runAsync](FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\) "runAsync\(Map, ToolContext\)")`

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[callLive](FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`[create](FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`[create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`[create](FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`[create](FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\))([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FunctionDeclaration>`

`[declaration](FunctionTool.html#declaration\(\))()`

Gets the `FunctionDeclaration` representation of this tool.

`[Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect")`

`[func](FunctionTool.html#func\(\))()`

Returns the underlying function [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect").

`boolean`

`[isStreaming](FunctionTool.html#isStreaming\(\))()`

Returns true if the wrapped function returns a Flowable and can be used for streaming.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[customMetadata](BaseTool.html#customMetadata\(\))()`

Returns a read-only view of the tool metadata.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](BaseTool.html#description\(\))()`

 

`static [BaseTool](BaseTool.html "class in com.google.adk.tools")`

`[fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a tool instance from a config.

`boolean`

`[longRunning](BaseTool.html#longRunning\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BaseTool.html#name\(\))()`

 

`io.reactivex.rxjava3.core.Completable`

`[processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\))(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\))(I args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments, returning the results converted to a specified class.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\))(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool with generic arguments and returns a map of results.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\))(T args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results.

`void`

`[setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") key, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)`

Sets custom metadata to the tool associated with a key.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") method)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") method, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([FunctionTool](FunctionTool.html "class in com.google.adk.tools") tool)

Creates a LongRunningFunctionTool from a FunctionTool.

    * ### fromConfig

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)




* * *

Copyright (C) 1980\. All rights reserved.
