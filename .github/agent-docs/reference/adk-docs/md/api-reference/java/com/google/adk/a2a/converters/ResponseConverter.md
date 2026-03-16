JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ResponseConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [ResponseConverter](ResponseConverter.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. clientEventToEvent(ClientEvent, InvocationContext)
     2. artifactToEvent(Artifact, InvocationContext)
     3. messageToFailedEvent(Message, InvocationContext)
     4. messageToEvent(Message, InvocationContext)
     5. messageToEvent(Message, InvocationContext, boolean)
     6. taskToEvent(Task, InvocationContext)

Hide sidebar  Show sidebar

# Class ResponseConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.ResponseConverter

* * *

public final class ResponseConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility for converting ADK events to A2A spec messages (and back).

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Event](../../events/Event.html "class in com.google.adk.events")`

`artifactToEvent(io.a2a.spec.Artifact artifact, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an artifact to an ADK event.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`clientEventToEvent(io.a2a.client.ClientEvent event, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts a A2A `ClientEvent` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events"), based on the event type.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

`messageToEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message back to ADK events.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

`messageToEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, boolean isPending)`

Converts an A2A message back to ADK events.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

`messageToFailedEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A message for a failed task to ADK event filling in the error message.

`static [Event](../../events/Event.html "class in com.google.adk.events")`

`taskToEvent(io.a2a.spec.Task task, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Converts an A2A `Task` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### clientEventToEvent

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> clientEventToEvent(io.a2a.client.ClientEvent event, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Converts a A2A `ClientEvent` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events"), based on the event type. Returns an empty optional if the event should be ignored (e.g. if the event is not a final update for TaskArtifactUpdateEvent or if the message is empty for TaskStatusUpdateEvent).

Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the event type is not supported.

    * ### artifactToEvent

public static [Event](../../events/Event.html "class in com.google.adk.events") artifactToEvent(io.a2a.spec.Artifact artifact, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Converts an artifact to an ADK event.

    * ### messageToFailedEvent

public static [Event](../../events/Event.html "class in com.google.adk.events") messageToFailedEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Converts an A2A message for a failed task to ADK event filling in the error message.

    * ### messageToEvent

public static [Event](../../events/Event.html "class in com.google.adk.events") messageToEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Converts an A2A message back to ADK events.

    * ### messageToEvent

public static [Event](../../events/Event.html "class in com.google.adk.events") messageToEvent(io.a2a.spec.Message message, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, boolean isPending)

Converts an A2A message back to ADK events. For streaming task in pending state it sets the thought field to true, to mark them as thought updates.

    * ### taskToEvent

public static [Event](../../events/Event.html "class in com.google.adk.events") taskToEvent(io.a2a.spec.Task task, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Converts an A2A `Task` to an ADK [`Event`](../../events/Event.html "class in com.google.adk.events"). If the artifacts are present, the last artifact is used. If not, the status message is used. If not, the last history message is used. If none of these are present, an empty event is returned.




* * *

Copyright (C) 1980\. All rights reserved.
