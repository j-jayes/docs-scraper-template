JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Context.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Context](Context.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
     1. Methods inherited from class ReadonlyContext
     2. Methods inherited from class Object
  4. Field Details
     1. eventActions
  5. Method Details
     1. state()
     2. eventActions()
     3. actions()
     4. eventId()
     5. functionCallId()
     6. functionCallId(String)
     7. toolConfirmation()
     8. toolConfirmation(ToolConfirmation)
     9. listArtifacts()
     10. loadArtifact(String)
     11. loadArtifact(String, int)
     12. saveArtifact(String, Part)
     13. requestConfirmation(String, Object)
     14. requestConfirmation(String)
     15. requestConfirmation()
     16. searchMemory(String)

Hide sidebar  Show sidebar

# Class Context

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

com.google.adk.agents.Context

Direct Known Subclasses:
    `[CallbackContext](CallbackContext.html "class in com.google.adk.agents")`

* * *

public class Context extends [ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

The context passed to callbacks and tools during an invocation. 

Agent and model callbacks receive a [`CallbackContext`](CallbackContext.html "class in com.google.adk.agents"), and tools and tool callbacks a [`ToolContext`](../tools/ToolContext.html "class in com.google.adk.tools"); both extend this class, so a helper that serves both, or a function tool's `toolContext` parameter, can take a `Context`. `requestConfirmation()` needs a function call ID, which only a tool call has.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected [EventActions](../events/EventActions.html "class in com.google.adk.events")`

`eventActions`

The event actions that record this context's changes.

### Fields inherited from class [ReadonlyContext](ReadonlyContext.html#field-summary "class in com.google.adk.agents")

`[invocationContext](ReadonlyContext.html#invocationContext)`

Modifier and Type

Field

Description

`protected final [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`[invocationContext](ReadonlyContext.html#invocationContext)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`actions()`

Returns the same [`EventActions`](../events/EventActions.html "class in com.google.adk.events") as `eventActions()`.

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`eventActions()`

Returns the [`EventActions`](../events/EventActions.html "class in com.google.adk.events") associated with this context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventId()`

Returns the ID of the event associated with this context, or null if there is none.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`functionCallId()`

Returns the ID of the function call that invoked the current tool, if any.

`void`

`functionCallId(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") functionCallId)`

Sets the ID of the function call that invoked the current tool, or clears it if null.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`listArtifacts()`

Lists the filenames of the artifacts attached to the current session.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`void`

`requestConfirmation()`

Requests confirmation for the current function call.

`void`

`requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint)`

Requests confirmation for the current function call.

`void`

`requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") payload)`

Requests confirmation for the current function call.

`io.reactivex.rxjava3.core.Completable`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and records it as a delta for the current session.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")>`

`searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") query)`

Searches the memory of the current user.

`[State](../sessions/State.html "class in com.google.adk.sessions")`

`state()`

Returns the delta-aware state of the current context.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")>`

`toolConfirmation()`

Returns the confirmation of the current tool call, if any.

`void`

`toolConfirmation(@Nullable [ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)`

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




  * ## Field Details

    * ### eventActions

protected [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions

The event actions that record this context's changes.

  * ## Method Details

    * ### state

public [State](../sessions/State.html "class in com.google.adk.sessions") state()

Returns the delta-aware state of the current context.

Overrides:
    `[state](ReadonlyContext.html#state\(\))` in class `[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")`

    * ### eventActions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions()

Returns the [`EventActions`](../events/EventActions.html "class in com.google.adk.events") associated with this context.

    * ### actions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") actions()

Returns the same [`EventActions`](../events/EventActions.html "class in com.google.adk.events") as `eventActions()`.

    * ### eventId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId()

Returns the ID of the event associated with this context, or null if there is none.

    * ### functionCallId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> functionCallId()

Returns the ID of the function call that invoked the current tool, if any.

    * ### functionCallId

public void functionCallId(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") functionCallId)

Sets the ID of the function call that invoked the current tool, or clears it if null.

    * ### toolConfirmation

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmation()

Returns the confirmation of the current tool call, if any.

    * ### toolConfirmation

public void toolConfirmation(@Nullable [ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events") toolConfirmation)

Sets the confirmation of the current tool call, or clears it if null.

    * ### listArtifacts

public io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> listArtifacts()

Lists the filenames of the artifacts attached to the current session.

Returns:
    the list of artifact filenames

    * ### loadArtifact

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Loads the latest version of an artifact from the service.

    * ### loadArtifact

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)

Loads a specific version of an artifact from the service.

    * ### saveArtifact

public io.reactivex.rxjava3.core.Completable saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact and records it as a delta for the current session.

Parameters:
    `filename` \- Artifact file name.
    `artifact` \- Artifact content to save.
Returns:
    a `Completable` that completes when the artifact is saved.
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if the artifact service is not initialized.

    * ### requestConfirmation

public void requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") payload)

Requests confirmation for the current function call.

Parameters:
    `hint` \- A hint to the user on how to confirm the tool call.
    `payload` \- The payload used to confirm the tool call.
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if this context has no function call ID.

    * ### requestConfirmation

public void requestConfirmation(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") hint)

Requests confirmation for the current function call.

Parameters:
    `hint` \- A hint to the user on how to confirm the tool call.
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if this context has no function call ID.

    * ### requestConfirmation

public void requestConfirmation()

Requests confirmation for the current function call.

Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if this context has no function call ID.

    * ### searchMemory

public io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](../memory/SearchMemoryResponse.html "class in com.google.adk.memory")> searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") query)

Searches the memory of the current user.




* * *

Copyright (C) 1980\. All rights reserved.
