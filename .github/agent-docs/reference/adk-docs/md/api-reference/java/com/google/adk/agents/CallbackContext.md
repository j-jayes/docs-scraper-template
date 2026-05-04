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
  5. Field Details
     1. eventActions
  6. Constructor Details
     1. CallbackContext(InvocationContext, EventActions)
     2. CallbackContext(InvocationContext, EventActions, String)
  7. Method Details
     1. state()
     2. eventActions()
     3. eventId()
     4. listArtifacts()
     5. loadArtifact(String)
     6. loadArtifact(String, int)
     7. saveArtifact(String, Part)

Hide sidebar  Show sidebar

# Class CallbackContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

com.google.adk.agents.CallbackContext

Direct Known Subclasses:
    `[ToolContext](../tools/ToolContext.html "class in com.google.adk.tools")`

* * *

public class CallbackContext extends [ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

The context of various callbacks for an agent invocation.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected [EventActions](../events/EventActions.html "class in com.google.adk.events")`

`eventActions`

 

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

`CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions)`

Initializes callback context.

`CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

Initializes callback context.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`eventActions()`

Returns the EventActions associated with this context.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventId()`

Returns the ID of the event associated with this context.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`listArtifacts()`

Lists the filenames of the artifacts attached to the current session.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`io.reactivex.rxjava3.core.Completable`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and records it as a delta for the current session.

`[State](../sessions/State.html "class in com.google.adk.sessions")`

`state()`

Returns the delta-aware state of the current callback.

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

  * ## Constructor Details

    * ### CallbackContext

public CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions)

Initializes callback context.

Parameters:
    `invocationContext` \- Current invocation context.
    `eventActions` \- Callback event actions.

    * ### CallbackContext

public CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)

Initializes callback context.

Parameters:
    `invocationContext` \- Current invocation context.
    `eventActions` \- Callback event actions.
    `eventId` \- The ID of the event associated with this context.

  * ## Method Details

    * ### state

public [State](../sessions/State.html "class in com.google.adk.sessions") state()

Returns the delta-aware state of the current callback.

Overrides:
    `[state](ReadonlyContext.html#state\(\))` in class `[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")`

    * ### eventActions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions()

Returns the EventActions associated with this context.

    * ### eventId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId()

Returns the ID of the event associated with this context.

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




* * *

Copyright (C) 1980\. All rights reserved.
