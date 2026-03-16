JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [ToolContext](ToolContext.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Method Summary
  5. Method Details
     1. actions()
     2. setActions(EventActions)
     3. functionCallId()
     4. functionCallId(String)
     5. toolConfirmation()
     6. toolConfirmation(ToolConfirmation)
     7. requestConfirmation(String, Object)
     8. requestConfirmation(String)
     9. requestConfirmation()
     10. searchMemory(String)
     11. builder(InvocationContext)
     12. toBuilder()
     13. toString()

Hide sidebar  Show sidebar

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

### Fields inherited from class [CallbackContext](../agents/CallbackContext.html#field-summary "class in com.google.adk.agents")

`[eventActions](../agents/CallbackContext.html#eventActions)`

### Fields inherited from class [ReadonlyContext](../agents/ReadonlyContext.html#field-summary "class in com.google.adk.agents")

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

 

`void`

`requestConfirmation()`

Requests confirmation for the given function call.

`void`

`requestConfirmation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hint)`

Requests confirmation for the given function call.

`void`

`requestConfirmation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hint, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") payload)`

Requests confirmation for the given function call.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")>`

`searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)`

Searches the memory of the current user.

`void`

`setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)`

 

`[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

`toBuilder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")>`

`toolConfirmation()`

 

`void`

`toolConfirmation([ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

 

### Methods inherited from class [CallbackContext](../agents/CallbackContext.html#method-summary "class in com.google.adk.agents")

`[eventActions](../agents/CallbackContext.html#eventActions\(\) "eventActions\(\)"), [eventId](../agents/CallbackContext.html#eventId\(\) "eventId\(\)"), [listArtifacts](../agents/CallbackContext.html#listArtifacts\(\) "listArtifacts\(\)"), [loadArtifact](../agents/CallbackContext.html#loadArtifact\(java.lang.String\) "loadArtifact\(String\)"), [loadArtifact](../agents/CallbackContext.html#loadArtifact\(java.lang.String,int\) "loadArtifact\(String, int\)"), [saveArtifact](../agents/CallbackContext.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\) "saveArtifact\(String, Part\)"), [state](../agents/CallbackContext.html#state\(\) "state\(\)")`

### Methods inherited from class [ReadonlyContext](../agents/ReadonlyContext.html#method-summary "class in com.google.adk.agents")

`[agentName](../agents/ReadonlyContext.html#agentName\(\) "agentName\(\)"), [branch](../agents/ReadonlyContext.html#branch\(\) "branch\(\)"), [events](../agents/ReadonlyContext.html#events\(\) "events\(\)"), [invocationContext](../agents/ReadonlyContext.html#invocationContext\(\) "invocationContext\(\)"), [invocationId](../agents/ReadonlyContext.html#invocationId\(\) "invocationId\(\)"), [sessionId](../agents/ReadonlyContext.html#sessionId\(\) "sessionId\(\)"), [userContent](../agents/ReadonlyContext.html#userContent\(\) "userContent\(\)"), [userId](../agents/ReadonlyContext.html#userId\(\) "userId\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### actions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") actions()

    * ### setActions

public void setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)

    * ### functionCallId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> functionCallId()

    * ### functionCallId

public void functionCallId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") functionCallId)

    * ### toolConfirmation

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmation()

    * ### toolConfirmation

public void toolConfirmation([ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)

    * ### requestConfirmation

public void requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hint, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") payload)

Requests confirmation for the given function call.

Parameters:
    `hint` \- A hint to the user on how to confirm the tool call.
    `payload` \- The payload used to confirm the tool call.

    * ### requestConfirmation

public void requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") hint)

Requests confirmation for the given function call.

Parameters:
    `hint` \- A hint to the user on how to confirm the tool call.

    * ### requestConfirmation

public void requestConfirmation()

Requests confirmation for the given function call.

    * ### searchMemory

public io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")> searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)

Searches the memory of the current user.

    * ### builder

public static [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") builder([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

    * ### toBuilder

public [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") toBuilder()

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
