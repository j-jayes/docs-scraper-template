JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [ToolContext](ToolContext.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Method Summary
  5. Method Details
     1. setActions(EventActions)
     2. builder(InvocationContext)
     3. toBuilder()
     4. toString()

Hide sidebar  Show sidebar

# Class ToolContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")

[com.google.adk.agents.Context](../agents/Context.html "class in com.google.adk.agents")

[com.google.adk.agents.CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

com.google.adk.tools.ToolContext

* * *

public class ToolContext extends [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents")

ToolContext object provides a structured context for executing tools or functions. 

Extends [`CallbackContext`](../agents/CallbackContext.html "class in com.google.adk.agents") (and through it [`Context`](../agents/Context.html "class in com.google.adk.agents")); [`BaseTool.runAsync(Map, ToolContext)`](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\)) and tool callbacks take this type.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

Builder for [`ToolContext`](ToolContext.html "class in com.google.adk.tools").

  * ## Field Summary

### Fields inherited from class [Context](../agents/Context.html#field-summary "class in com.google.adk.agents")

`[eventActions](../agents/Context.html#eventActions)`

Modifier and Type

Field

Description

`protected [EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[eventActions](../agents/Context.html#eventActions)`

The event actions that record this context's changes.

### Fields inherited from class [ReadonlyContext](../agents/ReadonlyContext.html#field-summary "class in com.google.adk.agents")

`[invocationContext](../agents/ReadonlyContext.html#invocationContext)`

Modifier and Type

Field

Description

`protected final [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents")`

`[invocationContext](../agents/ReadonlyContext.html#invocationContext)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

`builder([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`void`

`setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)`

 

`[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")`

`toBuilder()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

 

### Methods inherited from class [Context](../agents/Context.html#method-summary "class in com.google.adk.agents")

`[actions](../agents/Context.html#actions\(\) "actions\(\)"), [eventActions](../agents/Context.html#eventActions\(\) "eventActions\(\)"), [eventId](../agents/Context.html#eventId\(\) "eventId\(\)"), [functionCallId](../agents/Context.html#functionCallId\(\) "functionCallId\(\)"), [functionCallId](../agents/Context.html#functionCallId\(java.lang.String\) "functionCallId\(String\)"), [listArtifacts](../agents/Context.html#listArtifacts\(\) "listArtifacts\(\)"), [loadArtifact](../agents/Context.html#loadArtifact\(java.lang.String\) "loadArtifact\(String\)"), [loadArtifact](../agents/Context.html#loadArtifact\(java.lang.String,int\) "loadArtifact\(String, int\)"), [requestConfirmation](../agents/Context.html#requestConfirmation\(\) "requestConfirmation\(\)"), [requestConfirmation](../agents/Context.html#requestConfirmation\(java.lang.String\) "requestConfirmation\(String\)"), [requestConfirmation](../agents/Context.html#requestConfirmation\(java.lang.String,java.lang.Object\) "requestConfirmation\(String, Object\)"), [saveArtifact](../agents/Context.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\) "saveArtifact\(String, Part\)"), [searchMemory](../agents/Context.html#searchMemory\(java.lang.String\) "searchMemory\(String\)"), [state](../agents/Context.html#state\(\) "state\(\)"), [toolConfirmation](../agents/Context.html#toolConfirmation\(\) "toolConfirmation\(\)"), [toolConfirmation](../agents/Context.html#toolConfirmation\(com.google.adk.events.ToolConfirmation\) "toolConfirmation\(ToolConfirmation\)")`

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[actions](../agents/Context.html#actions\(\))()`

Returns the same [`EventActions`](../events/EventActions.html "class in com.google.adk.events") as [`Context.eventActions()`](../agents/Context.html#eventActions\(\)).

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[eventActions](../agents/Context.html#eventActions\(\))()`

Returns the [`EventActions`](../events/EventActions.html "class in com.google.adk.events") associated with this context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[eventId](../agents/Context.html#eventId\(\))()`

Returns the ID of the event associated with this context, or null if there is none.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[functionCallId](../agents/Context.html#functionCallId\(\))()`

Returns the ID of the function call that invoked the current tool, if any.

`void`

`[functionCallId](../agents/Context.html#functionCallId\(java.lang.String\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") functionCallId)`

Sets the ID of the function call that invoked the current tool, or clears it if null.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`[listArtifacts](../agents/Context.html#listArtifacts\(\))()`

Lists the filenames of the artifacts attached to the current session.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](../agents/Context.html#loadArtifact\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](../agents/Context.html#loadArtifact\(java.lang.String,int\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`void`

`[requestConfirmation](../agents/Context.html#requestConfirmation\(\))()`

Requests confirmation for the current function call.

`void`

`[requestConfirmation](../agents/Context.html#requestConfirmation\(java.lang.String\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint)`

Requests confirmation for the current function call.

`void`

`[requestConfirmation](../agents/Context.html#requestConfirmation\(java.lang.String,java.lang.Object\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") payload)`

Requests confirmation for the current function call.

`io.reactivex.rxjava3.core.Completable`

`[saveArtifact](../agents/Context.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and records it as a delta for the current session.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")>`

`[searchMemory](../agents/Context.html#searchMemory\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") query)`

Searches the memory of the current user.

`[State](../sessions/State.html "class in com.google.adk.sessions")`

`[state](../agents/Context.html#state\(\))()`

Returns the delta-aware state of the current context.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")>`

`[toolConfirmation](../agents/Context.html#toolConfirmation\(\))()`

Returns the confirmation of the current tool call, if any.

`void`

`[toolConfirmation](../agents/Context.html#toolConfirmation\(com.google.adk.events.ToolConfirmation\))(@Nullable [ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)`

Sets the confirmation of the current tool call, or clears it if null.

### Methods inherited from class [ReadonlyContext](../agents/ReadonlyContext.html#method-summary "class in com.google.adk.agents")

`[agentName](../agents/ReadonlyContext.html#agentName\(\) "agentName\(\)"), [branch](../agents/ReadonlyContext.html#branch\(\) "branch\(\)"), [events](../agents/ReadonlyContext.html#events\(\) "events\(\)"), [invocationContext](../agents/ReadonlyContext.html#invocationContext\(\) "invocationContext\(\)"), [invocationId](../agents/ReadonlyContext.html#invocationId\(\) "invocationId\(\)"), [sessionId](../agents/ReadonlyContext.html#sessionId\(\) "sessionId\(\)"), [userContent](../agents/ReadonlyContext.html#userContent\(\) "userContent\(\)"), [userId](../agents/ReadonlyContext.html#userId\(\) "userId\(\)")`

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[agentName](../agents/ReadonlyContext.html#agentName\(\))()`

Returns the name of the agent currently running.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[branch](../agents/ReadonlyContext.html#branch\(\))()`

Returns the branch of the current invocation, if present.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`[events](../agents/ReadonlyContext.html#events\(\))()`

Returns an unmodifiable view of the events of the session.

`[InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents")`

`[invocationContext](../agents/ReadonlyContext.html#invocationContext\(\))()`

Returns the invocation context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[invocationId](../agents/ReadonlyContext.html#invocationId\(\))()`

Returns the ID of the current invocation.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[sessionId](../agents/ReadonlyContext.html#sessionId\(\))()`

Returns the session ID.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`[userContent](../agents/ReadonlyContext.html#userContent\(\))()`

Returns the user content that initiated this invocation.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[userId](../agents/ReadonlyContext.html#userId\(\))()`

Returns the user ID.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### setActions

public void setActions([EventActions](../events/EventActions.html "class in com.google.adk.events") actions)

    * ### builder

public static [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") builder([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

    * ### toBuilder

public [ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools") toBuilder()

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
