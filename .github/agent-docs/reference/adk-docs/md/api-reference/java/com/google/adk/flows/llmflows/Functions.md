JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Functions.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [Functions](Functions.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. REQUEST_CONFIRMATION_FUNCTION_CALL_NAME
     2. TOOL_CALL_SECURITY_STATES
  5. Method Details
     1. generateClientFunctionCallId()
     2. populateClientFunctionCallId(Event)
     3. handleFunctionCalls(InvocationContext, Event, Map)
     4. handleFunctionCalls(InvocationContext, Event, Map, Map)
     5. handleFunctionCallsLive(InvocationContext, Event, Map)
     6. handleFunctionCallsLive(InvocationContext, Event, Map, Map)
     7. getLongRunningFunctionCalls(List, Map)
     8. findMatchingFunctionCallEvent(List)
     9. hasPendingLongRunningCall(Event)
     10. generateRequestConfirmationEvent(InvocationContext, Event, Event)
     11. getAskUserConfirmationFunctionCalls(Event)

Hide sidebar  Show sidebar

# Class Functions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.Functions

* * *

public final class Functions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for handling function calls.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`REQUEST_CONFIRMATION_FUNCTION_CALL_NAME`

The function call name for the request confirmation function.

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`TOOL_CALL_SECURITY_STATES`

Session state key for storing the security policy outcomes for tool calls.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`findMatchingFunctionCallEvent([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

Returns the most recent function-call event whose call id matches a function response in the last event, or empty.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`generateClientFunctionCallId()`

Generates a unique ID for a function call.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`generateRequestConfirmationEvent([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Event](../../events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Generates a request confirmation event from a function response event.

`static com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall>`

`getAskUserConfirmationFunctionCalls([Event](../../events/Event.html "class in com.google.adk.events") event)`

Gets the ask user confirmation function calls from the event.

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getLongRunningFunctionCalls([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.FunctionCall> functionCalls, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

`handleFunctionCalls([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles standard, non-streaming function calls.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

`handleFunctionCalls([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles standard, non-streaming function calls with tool confirmations.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

`handleFunctionCallsLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)`

Handles function calls in a live/streaming context, supporting background execution and stream termination.

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

`handleFunctionCallsLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)`

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

`static boolean`

`hasPendingLongRunningCall([Event](../../events/Event.html "class in com.google.adk.events") event)`

Returns whether the event emits a long-running function call still awaiting a response (e.g.

`static void`

`populateClientFunctionCallId([Event](../../events/Event.html "class in com.google.adk.events") modelResponseEvent)`

Populates missing function call IDs in the provided event's content.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### REQUEST_CONFIRMATION_FUNCTION_CALL_NAME

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") REQUEST_CONFIRMATION_FUNCTION_CALL_NAME

The function call name for the request confirmation function.

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.flows.llmflows.Functions.REQUEST_CONFIRMATION_FUNCTION_CALL_NAME)

    * ### TOOL_CALL_SECURITY_STATES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") TOOL_CALL_SECURITY_STATES

Session state key for storing the security policy outcomes for tool calls.

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.flows.llmflows.Functions.TOOL_CALL_SECURITY_STATES)

  * ## Method Details

    * ### generateClientFunctionCallId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") generateClientFunctionCallId()

Generates a unique ID for a function call.

    * ### populateClientFunctionCallId

public static void populateClientFunctionCallId([Event](../../events/Event.html "class in com.google.adk.events") modelResponseEvent)

Populates missing function call IDs in the provided event's content. 

If the event contains function calls without an ID, this method generates a unique client-side ID for each and updates the event content.

Parameters:
    `modelResponseEvent` \- The event potentially containing function calls.

    * ### handleFunctionCalls

public static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")> handleFunctionCalls([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)

Handles standard, non-streaming function calls.

    * ### handleFunctionCalls

public static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")> handleFunctionCalls([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)

Handles standard, non-streaming function calls with tool confirmations.

    * ### handleFunctionCallsLive

public static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")> handleFunctionCallsLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)

Handles function calls in a live/streaming context, supporting background execution and stream termination.

    * ### handleFunctionCallsLive

public static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")> handleFunctionCallsLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](../../events/ToolConfirmation.html "class in com.google.adk.events")> toolConfirmations)

Handles function calls in a live/streaming context with tool confirmations, supporting background execution and stream termination.

    * ### getLongRunningFunctionCalls

public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getLongRunningFunctionCalls([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.FunctionCall> functionCalls, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")> tools)

    * ### findMatchingFunctionCallEvent

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> findMatchingFunctionCallEvent([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> events)

Returns the most recent function-call event whose call id matches a function response in the last event, or empty. Mirrors Python ADK's `find_matching_function_call`.

    * ### hasPendingLongRunningCall

public static boolean hasPendingLongRunningCall([Event](../../events/Event.html "class in com.google.adk.events") event)

Returns whether the event emits a long-running function call still awaiting a response (e.g. a HITL request). Mirrors Python ADK v1's `should_pause_invocation`.

    * ### generateRequestConfirmationEvent

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> generateRequestConfirmationEvent([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Event](../../events/Event.html "class in com.google.adk.events") functionResponseEvent)

Generates a request confirmation event from a function response event.

Parameters:
    `invocationContext` \- The invocation context.
    `functionCallEvent` \- The event containing the original function call.
    `functionResponseEvent` \- The event containing the function response.
Returns:
    An optional event containing the request confirmation function call.

    * ### getAskUserConfirmationFunctionCalls

public static com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall> getAskUserConfirmationFunctionCalls([Event](../../events/Event.html "class in com.google.adk.events") event)

Gets the ask user confirmation function calls from the event.

Parameters:
    `event` \- The event to extract function calls from.
Returns:
    A list of function calls for asking user confirmation.




* * *

Copyright (C) 1980\. All rights reserved.
