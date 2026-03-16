JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/EventConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [EventConverter](EventConverter.html)



Contents 

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. ADK_TASK_ID_KEY
     2. ADK_CONTEXT_ID_KEY
  5. Method Details
     1. taskId(Event)
     2. contextId(Event)
     3. findUserFunctionCall(List)
     4. contentToParts(Optional, boolean)
     5. messagePartsFromContext(InvocationContext)

Hide sidebar  Show sidebar

# Class EventConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.EventConverter

* * *

public final class EventConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Converter for ADK Events to A2A Messages.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`ADK_CONTEXT_ID_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`ADK_TASK_ID_KEY`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableList<io.a2a.spec.Part<?>>`

`contentToParts([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content, boolean isPartial)`

Converts a GenAI Content object to a list of A2A Parts.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`contextId([Event](../../events/Event.html "class in com.google.adk.events") event)`

Returns the context ID from the event.

`static @Nullable [Event](../../events/Event.html "class in com.google.adk.events")`

`findUserFunctionCall([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

Returns the last user function call event from the list of events.

`static com.google.common.collect.ImmutableList<io.a2a.spec.Part<?>>`

`messagePartsFromContext([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)`

Returns the parts from the context events that should be sent to the agent.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`taskId([Event](../../events/Event.html "class in com.google.adk.events") event)`

Returns the task ID from the event.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### ADK_TASK_ID_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") ADK_TASK_ID_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.EventConverter.ADK_TASK_ID_KEY)

    * ### ADK_CONTEXT_ID_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") ADK_CONTEXT_ID_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.EventConverter.ADK_CONTEXT_ID_KEY)

  * ## Method Details

    * ### taskId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") taskId([Event](../../events/Event.html "class in com.google.adk.events") event)

Returns the task ID from the event. 

Task ID is stored in the event's custom metadata with the key `ADK_TASK_ID_KEY`.

Parameters:
    `event` \- The event to get the task ID from.
Returns:
    The task ID, or an empty string if not found.

    * ### contextId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") contextId([Event](../../events/Event.html "class in com.google.adk.events") event)

Returns the context ID from the event. 

Context ID is stored in the event's custom metadata with the key `ADK_CONTEXT_ID_KEY`.

Parameters:
    `event` \- The event to get the context ID from.
Returns:
    The context ID, or an empty string if not found.

    * ### findUserFunctionCall

public static @Nullable [Event](../../events/Event.html "class in com.google.adk.events") findUserFunctionCall([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)

Returns the last user function call event from the list of events.

Parameters:
    `events` \- The list of events to find the user function call event from.
Returns:
    The user function call event, or null if not found.

    * ### contentToParts

public static com.google.common.collect.ImmutableList<io.a2a.spec.Part<?>> contentToParts([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content, boolean isPartial)

Converts a GenAI Content object to a list of A2A Parts.

Parameters:
    `content` \- The GenAI Content object to convert.
    `isPartial` \- Whether the content is partial.
Returns:
    A list of A2A Parts.

    * ### messagePartsFromContext

public static com.google.common.collect.ImmutableList<io.a2a.spec.Part<?>> messagePartsFromContext([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context)

Returns the parts from the context events that should be sent to the agent. 

All session events from the previous remote agent response (or the beginning of the session in case of the first agent invocation) are included into the A2A message. Events from other agents are presented as user messages and rephased as if a user was telling what happened in the session up to the point.

Parameters:
    `context` \- The invocation context to get the parts from.
Returns:
    A list of A2A Parts.




* * *

Copyright (C) 1980\. All rights reserved.
