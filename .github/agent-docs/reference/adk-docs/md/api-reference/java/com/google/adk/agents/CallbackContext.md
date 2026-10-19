JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CallbackContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [CallbackContext](CallbackContext.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. CallbackContext(InvocationContext, EventActions)
     2. CallbackContext(InvocationContext, EventActions, String)

Hide sidebar  Show sidebar

# Class CallbackContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

[com.google.adk.agents.Context](Context.html "class in com.google.adk.agents")

com.google.adk.agents.CallbackContext

Direct Known Subclasses:
    `[ToolContext](../tools/ToolContext.html "class in com.google.adk.tools")`

* * *

public class CallbackContext extends [Context](Context.html "class in com.google.adk.agents")

The context of various callbacks for an agent invocation. 

Extends [`Context`](Context.html "class in com.google.adk.agents") for backward compatibility; agent and model callback signatures still use this type.

  * ## Field Summary

### Fields inherited from class [Context](Context.html#field-summary "class in com.google.adk.agents")

`[eventActions](Context.html#eventActions)`

Modifier and Type

Field

Description

`protected [EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[eventActions](Context.html#eventActions)`

The event actions that record this context's changes.

### Fields inherited from class [ReadonlyContext](ReadonlyContext.html#field-summary "class in com.google.adk.agents")

`[invocationContext](ReadonlyContext.html#invocationContext)`

Modifier and Type

Field

Description

`protected final [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`[invocationContext](ReadonlyContext.html#invocationContext)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions)`

Initializes callback context.

`CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

Initializes callback context.

  * ## Method Summary

### Methods inherited from class [Context](Context.html#method-summary "class in com.google.adk.agents")

`[actions](Context.html#actions\(\) "actions\(\)"), [eventActions](Context.html#eventActions\(\) "eventActions\(\)"), [eventId](Context.html#eventId\(\) "eventId\(\)"), [functionCallId](Context.html#functionCallId\(\) "functionCallId\(\)"), [functionCallId](Context.html#functionCallId\(java.lang.String\) "functionCallId\(String\)"), [listArtifacts](Context.html#listArtifacts\(\) "listArtifacts\(\)"), [loadArtifact](Context.html#loadArtifact\(java.lang.String\) "loadArtifact\(String\)"), [loadArtifact](Context.html#loadArtifact\(java.lang.String,int\) "loadArtifact\(String, int\)"), [requestConfirmation](Context.html#requestConfirmation\(\) "requestConfirmation\(\)"), [requestConfirmation](Context.html#requestConfirmation\(java.lang.String\) "requestConfirmation\(String\)"), [requestConfirmation](Context.html#requestConfirmation\(java.lang.String,java.lang.Object\) "requestConfirmation\(String, Object\)"), [saveArtifact](Context.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\) "saveArtifact\(String, Part\)"), [searchMemory](Context.html#searchMemory\(java.lang.String\) "searchMemory\(String\)"), [state](Context.html#state\(\) "state\(\)"), [toolConfirmation](Context.html#toolConfirmation\(\) "toolConfirmation\(\)"), [toolConfirmation](Context.html#toolConfirmation\(com.google.adk.events.ToolConfirmation\) "toolConfirmation\(ToolConfirmation\)")`

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[actions](Context.html#actions\(\))()`

Returns the same [`EventActions`](../events/EventActions.html "class in com.google.adk.events") as [`Context.eventActions()`](Context.html#eventActions\(\)).

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`[eventActions](Context.html#eventActions\(\))()`

Returns the [`EventActions`](../events/EventActions.html "class in com.google.adk.events") associated with this context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[eventId](Context.html#eventId\(\))()`

Returns the ID of the event associated with this context, or null if there is none.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[functionCallId](Context.html#functionCallId\(\))()`

Returns the ID of the function call that invoked the current tool, if any.

`void`

`[functionCallId](Context.html#functionCallId\(java.lang.String\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") functionCallId)`

Sets the ID of the function call that invoked the current tool, or clears it if null.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`[listArtifacts](Context.html#listArtifacts\(\))()`

Lists the filenames of the artifacts attached to the current session.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](Context.html#loadArtifact\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](Context.html#loadArtifact\(java.lang.String,int\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`void`

`[requestConfirmation](Context.html#requestConfirmation\(\))()`

Requests confirmation for the current function call.

`void`

`[requestConfirmation](Context.html#requestConfirmation\(java.lang.String\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint)`

Requests confirmation for the current function call.

`void`

`[requestConfirmation](Context.html#requestConfirmation\(java.lang.String,java.lang.Object\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") payload)`

Requests confirmation for the current function call.

`io.reactivex.rxjava3.core.Completable`

`[saveArtifact](Context.html#saveArtifact\(java.lang.String,com.google.genai.types.Part\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and records it as a delta for the current session.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")>`

`[searchMemory](Context.html#searchMemory\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") query)`

Searches the memory of the current user.

`[State](../sessions/State.html "class in com.google.adk.sessions")`

`[state](Context.html#state\(\))()`

Returns the delta-aware state of the current context.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")>`

`[toolConfirmation](Context.html#toolConfirmation\(\))()`

Returns the confirmation of the current tool call, if any.

`void`

`[toolConfirmation](Context.html#toolConfirmation\(com.google.adk.events.ToolConfirmation\))(@Nullable [ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)`

Sets the confirmation of the current tool call, or clears it if null.

### Methods inherited from class [ReadonlyContext](ReadonlyContext.html#method-summary "class in com.google.adk.agents")

`[agentName](ReadonlyContext.html#agentName\(\) "agentName\(\)"), [branch](ReadonlyContext.html#branch\(\) "branch\(\)"), [events](ReadonlyContext.html#events\(\) "events\(\)"), [invocationContext](ReadonlyContext.html#invocationContext\(\) "invocationContext\(\)"), [invocationId](ReadonlyContext.html#invocationId\(\) "invocationId\(\)"), [sessionId](ReadonlyContext.html#sessionId\(\) "sessionId\(\)"), [userContent](ReadonlyContext.html#userContent\(\) "userContent\(\)"), [userId](ReadonlyContext.html#userId\(\) "userId\(\)")`

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[agentName](ReadonlyContext.html#agentName\(\))()`

Returns the name of the agent currently running.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[branch](ReadonlyContext.html#branch\(\))()`

Returns the branch of the current invocation, if present.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`[events](ReadonlyContext.html#events\(\))()`

Returns an unmodifiable view of the events of the session.

`[InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`[invocationContext](ReadonlyContext.html#invocationContext\(\))()`

Returns the invocation context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[invocationId](ReadonlyContext.html#invocationId\(\))()`

Returns the ID of the current invocation.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[sessionId](ReadonlyContext.html#sessionId\(\))()`

Returns the session ID.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`[userContent](ReadonlyContext.html#userContent\(\))()`

Returns the user content that initiated this invocation.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[userId](ReadonlyContext.html#userId\(\))()`

Returns the user ID.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### CallbackContext

public CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions)

Initializes callback context.

Parameters:
    `invocationContext` \- Current invocation context.
    `eventActions` \- Callback event actions, or null for new empty ones.

    * ### CallbackContext

public CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)

Initializes callback context.

Parameters:
    `invocationContext` \- Current invocation context.
    `eventActions` \- Callback event actions, or null for new empty ones.
    `eventId` \- The ID of the event associated with this context, or null if there is none.




* * *

Copyright (C) 1980\. All rights reserved.
