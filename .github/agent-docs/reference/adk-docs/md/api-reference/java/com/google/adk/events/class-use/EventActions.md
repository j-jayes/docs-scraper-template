JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../EventActions.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](../package-summary.html)
  2. [EventActions](../EventActions.html)



# Uses of Class  
com.google.adk.events.EventActions

Packages that use [EventActions](../EventActions.html "class in com.google.adk.events")

Package

Description

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.tools

 

  * ## Uses of [EventActions](../EventActions.html "class in com.google.adk.events") in [com.google.adk.agents](../../agents/package-summary.html)

Fields in [com.google.adk.agents](../../agents/package-summary.html) declared as [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier and Type

Field

Description

`protected [EventActions](../EventActions.html "class in com.google.adk.events")`

Context.`[eventActions](../../agents/Context.html#eventActions)`

The event actions that record this context's changes.

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[EventActions](../EventActions.html "class in com.google.adk.events")`

Context.`[actions](../../agents/Context.html#actions\(\))()`

Returns the same [`EventActions`](../EventActions.html "class in com.google.adk.events") as [`Context.eventActions()`](../../agents/Context.html#eventActions\(\)).

`[EventActions](../EventActions.html "class in com.google.adk.events")`

Context.`[eventActions](../../agents/Context.html#eventActions\(\))()`

Returns the [`EventActions`](../EventActions.html "class in com.google.adk.events") associated with this context.

Constructors in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier

Constructor

Description

` `

`[CallbackContext](../../agents/CallbackContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext,com.google.adk.events.EventActions\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../EventActions.html "class in com.google.adk.events") eventActions)`

Initializes callback context.

` `

`[CallbackContext](../../agents/CallbackContext.html#%3Cinit%3E\(com.google.adk.agents.InvocationContext,com.google.adk.events.EventActions,java.lang.String\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, @Nullable [EventActions](../EventActions.html "class in com.google.adk.events") eventActions, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

Initializes callback context.

  * ## Uses of [EventActions](../EventActions.html "class in com.google.adk.events") in [com.google.adk.events](../package-summary.html)

Methods in [com.google.adk.events](../package-summary.html) that return [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[EventActions](../EventActions.html "class in com.google.adk.events")`

Event.`[actions](../Event.html#actions\(\))()`

 

`[EventActions](../EventActions.html "class in com.google.adk.events")`

EventActions.Builder.`[build](../EventActions.Builder.html#build\(\))()`

 

Methods in [com.google.adk.events](../package-summary.html) with parameters of type [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[Event.Builder](../Event.Builder.html "class in com.google.adk.events")`

Event.Builder.`[actions](../Event.Builder.html#actions\(com.google.adk.events.EventActions\))(@Nullable [EventActions](../EventActions.html "class in com.google.adk.events") value)`

 

`[EventActions.Builder](../EventActions.Builder.html "class in com.google.adk.events")`

EventActions.Builder.`[merge](../EventActions.Builder.html#merge\(com.google.adk.events.EventActions\))([EventActions](../EventActions.html "class in com.google.adk.events") other)`

 

`void`

Event.`[setActions](../Event.html#setActions\(com.google.adk.events.EventActions\))([EventActions](../EventActions.html "class in com.google.adk.events") actions)`

 

  * ## Uses of [EventActions](../EventActions.html "class in com.google.adk.events") in [com.google.adk.tools](../../tools/package-summary.html)

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [EventActions](../EventActions.html "class in com.google.adk.events")

Modifier and Type

Method

Description

`[ToolContext.Builder](../../tools/ToolContext.Builder.html "class in com.google.adk.tools")`

ToolContext.Builder.`[actions](../../tools/ToolContext.Builder.html#actions\(com.google.adk.events.EventActions\))([EventActions](../EventActions.html "class in com.google.adk.events") actions)`

 

`void`

ToolContext.`[setActions](../../tools/ToolContext.html#setActions\(com.google.adk.events.EventActions\))([EventActions](../EventActions.html "class in com.google.adk.events") actions)`

 




* * *

Copyright (C) 1980\. All rights reserved.
