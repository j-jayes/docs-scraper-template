JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FunctionTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [FunctionTool](FunctionTool.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BaseTool
     2. Methods inherited from class Object
  5. Constructor Details
     1. FunctionTool(Object, Method, boolean)
     2. FunctionTool(Object, Method, boolean, boolean)
     3. FunctionTool(Object, Method, boolean, ObjectMapper)
     4. FunctionTool(Object, Method, boolean, boolean, ObjectMapper)
  6. Method Details
     1. create(Object, Method)
     2. create(Object, Method, boolean)
     3. create(Object, Method, boolean, boolean)
     4. create(Method)
     5. create(Method, boolean)
     6. create(Method, boolean, boolean)
     7. create(Class, String)
     8. create(Class, String, boolean)
     9. create(Class, String, boolean, boolean)
     10. create(Object, String)
     11. create(Object, String, boolean)
     12. create(Object, String, boolean, boolean)
     13. declaration()
     14. func()
     15. isStreaming()
     16. runAsync(Map, ToolContext)
     17. callLive(Map, ToolContext, InvocationContext)

Hide sidebar  Show sidebar

# Class FunctionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.FunctionTool

Direct Known Subclasses:
    `[ComputerUseTool](computeruse/ComputerUseTool.html "class in com.google.adk.tools.computeruse"), [LoadMemoryTool](LoadMemoryTool.html "class in com.google.adk.tools"), [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

* * *

public class FunctionTool extends [BaseTool](BaseTool.html "class in com.google.adk.tools")

FunctionTool implements a customized function calling tool.

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

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning)`

 

`protected `

`FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, boolean requireConfirmation)`

 

`protected `

`FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, boolean requireConfirmation, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

`protected `

`FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`callLive([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`[Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect")`

`func()`

Returns the underlying function [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect").

`boolean`

`isStreaming()`

Returns true if the wrapped function returns a Flowable and can be used for streaming.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

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




  * ## Constructor Details

    * ### FunctionTool

protected FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning)

    * ### FunctionTool

protected FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, boolean requireConfirmation)

    * ### FunctionTool

protected FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

    * ### FunctionTool

protected FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean isLongRunning, boolean requireConfirmation, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

  * ## Method Details

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func, boolean requireConfirmation, boolean isLongRunning)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") methodName, boolean requireConfirmation, boolean isLongRunning)

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Description copied from class: `[BaseTool](BaseTool.html#declaration\(\))`

Gets the `FunctionDeclaration` representation of this tool.

Overrides:
    `[declaration](BaseTool.html#declaration\(\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`

    * ### func

public [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect") func()

Returns the underlying function [`Method`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class in java.lang.reflect").

    * ### isStreaming

public boolean isStreaming()

Returns true if the wrapped function returns a Flowable and can be used for streaming.

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`

    * ### callLive

public io.reactivex.rxjava3.core.Flowable<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> callLive([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext) throws [IllegalAccessException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalAccessException.html "class in java.lang"), [InvocationTargetException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/InvocationTargetException.html "class in java.lang.reflect")

Throws:
    `[IllegalAccessException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalAccessException.html "class in java.lang")`
    `[InvocationTargetException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/InvocationTargetException.html "class in java.lang.reflect")`




* * *

Copyright (C) 1980\. All rights reserved.
