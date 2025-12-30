JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolContext.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [ToolContext](ToolContext.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Method Summary
  5. Method Details
     1. actions()
     2. setActions(EventActions)
     3. functionCallId()
     4. functionCallId(String)
     5. listArtifacts()
     6. builder(InvocationContext)
     7. toBuilder()



# Class ToolContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")

[com.google.adk.agents.CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

com.google.adk.tools.ToolContext

* * *

public class ToolContext extends [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

ToolContext object provides a structured context for executing tools or functions.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

Builder for [`ToolContext`](ToolContext.html "class in com.google.adk.tools").

  * ## Field Summary

### Fields inherited from class com.google.adk.agents.[CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

`[eventActions](../agents/CallbackContext.html#eventActions)`

### Fields inherited from class com.google.adk.agents.[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")

`[invocationContext](../agents/ReadonlyContext.html#invocationContext)`

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`actions()`

 

`static [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

`builder([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`functionCallId()`

 

`void`

`functionCallId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") functionCallId)`

 

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`

`listArtifacts()`

Lists the filenames of the artifacts attached to the current session.

`void`

`setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)`

 

`[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

`toBuilder()`

 

### Methods inherited from class com.google.adk.agents.[CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

`[eventActions](../agents/CallbackContext.html#eventActions\(\)), [loadArtifact](../agents/CallbackContext.html#loadArtifact\(java.lang.String,java.util.Optional\)), [saveArtifact](../agents/CallbackContext.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\)), [state](../agents/CallbackContext.html#state\(\))`

### Methods inherited from class com.google.adk.agents.[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")

`[agentName](../agents/ReadonlyContext.html#agentName\(\)), [branch](../agents/ReadonlyContext.html#branch\(\)), [events](../agents/ReadonlyContext.html#events\(\)), [invocationId](../agents/ReadonlyContext.html#invocationId\(\)), [sessionId](../agents/ReadonlyContext.html#sessionId\(\)), [userContent](../agents/ReadonlyContext.html#userContent\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### actions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") actions()

    * ### setActions

public void setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)

    * ### functionCallId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> functionCallId()

    * ### functionCallId

public void functionCallId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") functionCallId)

    * ### listArtifacts

public io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> listArtifacts()

Lists the filenames of the artifacts attached to the current session.

    * ### builder

public static [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") builder([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

    * ### toBuilder

public [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") toBuilder()




* * *

Copyright (C) 2025\. All rights reserved.
