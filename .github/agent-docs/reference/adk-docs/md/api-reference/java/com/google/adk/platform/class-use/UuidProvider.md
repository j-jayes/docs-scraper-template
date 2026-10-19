JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../UuidProvider.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.platform](../package-summary.html)
  2. [UuidProvider](../UuidProvider.html)



# Uses of Interface  
com.google.adk.platform.UuidProvider

Packages that use [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.platform

Seams for the system operations behind ADK-generated timestamps and ids.

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.summarizer

 

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Method

Description

`[UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")`

InvocationContext.`[uuidProvider](../../agents/InvocationContext.html#uuidProvider\(\))()`

Returns the [`UuidProvider`](../UuidProvider.html "interface in com.google.adk.platform") for this invocation.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

InvocationContext.`[newInvocationContextId](../../agents/InvocationContext.html#newInvocationContextId\(com.google.adk.platform.UuidProvider\))([UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Generates a new unique ID for an invocation context using the given [`UuidProvider`](../UuidProvider.html "interface in com.google.adk.platform").

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[uuidProvider](../../agents/InvocationContext.Builder.html#uuidProvider\(com.google.adk.platform.UuidProvider\))(@Nullable [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Sets the UUID provider for the invocation; `null` (the default) selects [`UuidProvider.SYSTEM`](../UuidProvider.html#SYSTEM).

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Method

Description

`static void`

Functions.`[populateClientFunctionCallId](../../flows/llmflows/Functions.html#populateClientFunctionCallId\(com.google.adk.events.Event,com.google.adk.platform.UuidProvider\))([Event](../../events/Event.html "class in com.google.adk.events") modelResponseEvent, [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Populates missing function call IDs in the provided event's content using the given [`UuidProvider`](../UuidProvider.html "interface in com.google.adk.platform").

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.models](../../models/package-summary.html)

Methods in [com.google.adk.models](../../models/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

FunctionCallIds.`[generateClientFunctionCallId](../../models/FunctionCallIds.html#generateClientFunctionCallId\(com.google.adk.platform.UuidProvider\))([UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Returns a new client-side function call ID with the ADK prefix, minted from the given [`UuidProvider`](../UuidProvider.html "interface in com.google.adk.platform").

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.platform](../package-summary.html)

Fields in [com.google.adk.platform](../package-summary.html) declared as [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Field

Description

`static final [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")`

UuidProvider.`[SYSTEM](../UuidProvider.html#SYSTEM)`

A provider backed by [`UUID.randomUUID()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#randomUUID\(\)).

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[uuidProvider](../../runner/Runner.Builder.html#uuidProvider\(com.google.adk.platform.UuidProvider\))(@Nullable [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Sets the [`UuidProvider`](../UuidProvider.html "interface in com.google.adk.platform") that supplies every identifier this runner generates: event, invocation, and client function-call ids, and the ids of sessions created by the default in-memory session service, which is created on the first `build()`.

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.sessions](../../sessions/package-summary.html)

Constructors in [com.google.adk.sessions](../../sessions/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier

Constructor

Description

` `

`[FirestoreSessionService](../../sessions/FirestoreSessionService.html#%3Cinit%3E\(com.google.cloud.firestore.Firestore,java.time.InstantSource,com.google.adk.platform.UuidProvider\))(com.google.cloud.firestore.Firestore firestore, [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource, [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Creates a session service whose generated session IDs and `lastUpdateTime` values come from the given providers instead of [`UUID.randomUUID()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#randomUUID\(\)) and the wall clock.

` `

`[InMemorySessionService](../../sessions/InMemorySessionService.html#%3Cinit%3E\(com.google.adk.sessions.InMemorySessionService.DuplicateSessionIdBehavior,java.time.InstantSource,com.google.adk.platform.UuidProvider\))([InMemorySessionService.DuplicateSessionIdBehavior](../../sessions/InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions") duplicateSessionIdBehavior, [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource, [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Creates a new instance of the in-memory session service with empty storage.

  * ## Uses of [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") in [com.google.adk.summarizer](../../summarizer/package-summary.html)

Constructors in [com.google.adk.summarizer](../../summarizer/package-summary.html) with parameters of type [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform")

Modifier

Constructor

Description

` `

`[LlmEventSummarizer](../../summarizer/LlmEventSummarizer.html#%3Cinit%3E\(com.google.adk.models.BaseLlm,java.lang.String,java.time.InstantSource,com.google.adk.platform.UuidProvider\))([BaseLlm](../../models/BaseLlm.html "class in com.google.adk.models") baseLlm, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") promptTemplate, [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource, [UuidProvider](../UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Creates a summarizer whose compaction events draw their id, invocation id, and timestamp from the given sources.




* * *

Copyright (C) 1980\. All rights reserved.
