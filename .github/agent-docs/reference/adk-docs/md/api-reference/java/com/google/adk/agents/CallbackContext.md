JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CallbackContext.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [CallbackContext](CallbackContext.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. eventActions
  6. Constructor Details
     1. CallbackContext(InvocationContext, EventActions)
  7. Method Details
     1. state()
     2. eventActions()
     3. loadArtifact(String, Optional)
     4. saveArtifact(String, Part)



# Class CallbackContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

 

### Fields inherited from class com.google.adk.agents.[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

`[invocationContext](ReadonlyContext.html#invocationContext)`

  * ## Constructor Summary

Constructors

Constructor

Description

`CallbackContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions)`

Initializes callback context.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

`eventActions()`

Returns the EventActions associated with this context.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)`

Loads an artifact from the artifact service associated with the current session.

`void`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and records it as a delta for the current session.

`[State](../sessions/State.html "class in com.google.adk.sessions")`

`state()`

Returns the delta-aware state of the current callback.

### Methods inherited from class com.google.adk.agents.[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")

`[agentName](ReadonlyContext.html#agentName\(\)), [branch](ReadonlyContext.html#branch\(\)), [events](ReadonlyContext.html#events\(\)), [invocationId](ReadonlyContext.html#invocationId\(\)), [sessionId](ReadonlyContext.html#sessionId\(\)), [userContent](ReadonlyContext.html#userContent\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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

  * ## Method Details

    * ### state

public [State](../sessions/State.html "class in com.google.adk.sessions") state()

Returns the delta-aware state of the current callback.

Overrides:
    `[state](ReadonlyContext.html#state\(\))` in class `[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")`

    * ### eventActions

public [EventActions](../events/EventActions.html "class in com.google.adk.events") eventActions()

Returns the EventActions associated with this context.

    * ### loadArtifact

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)

Loads an artifact from the artifact service associated with the current session.

Parameters:
    `filename` \- Artifact file name.
    `version` \- Artifact version (optional).
Returns:
    loaded part, or empty if not found.
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class or interface in java.lang")` \- if the artifact service is not initialized.

    * ### saveArtifact

public void saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact and records it as a delta for the current session.

Parameters:
    `filename` \- Artifact file name.
    `artifact` \- Artifact content to save.
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class or interface in java.lang")` \- if the artifact service is not initialized.




* * *

Copyright (C) 2025\. All rights reserved.
