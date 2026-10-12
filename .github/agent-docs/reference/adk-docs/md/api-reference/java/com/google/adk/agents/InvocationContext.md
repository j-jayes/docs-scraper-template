JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InvocationContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [InvocationContext](InvocationContext.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. InvocationContext(InvocationContext.Builder)
  6. Method Details
     1. builder()
     2. toBuilder()
     3. sessionService()
     4. artifactService()
     5. memoryService()
     6. pluginManager()
     7. activeStreamingTools()
     8. liveRequestQueue()
     9. invocationId()
     10. branch(String)
     11. branch()
     12. agent()
     13. session()
     14. eventsOnCurrentBranch()
     15. userContent()
     16. runConfig()
     17. callbackContextData()
     18. endInvocation()
     19. setEndInvocation(boolean)
     20. appName()
     21. userId()
     22. newInvocationContextId()
     23. incrementLlmCallsCount()
     24. eventsCompactionConfig()
     25. contextCacheConfig()
     26. isResumable()
     27. isLegacyResumability()
     28. agentStates()
     29. endOfAgents()
     30. populateInvocationAgentStates()
     31. events(boolean, boolean)
     32. shouldPauseInvocation(Event)
     33. equals(Object)
     34. hashCode()

Hide sidebar  Show sidebar

# Class InvocationContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.InvocationContext

* * *

public class InvocationContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

The context for an agent invocation.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

Builder for [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`InvocationContext([InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ActiveStreamingTool](ActiveStreamingTool.html "class in com.google.adk.agents")>`

`activeStreamingTools()`

Returns a map of tool call IDs to active streaming tools for the current invocation.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`agent()`

Returns the agent being invoked.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`agentStates()`

Returns an unmodifiable view of the per-agent resumability checkpoint states for this invocation, keyed by agent name.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`appName()`

Returns the application name associated with the session.

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

Returns the artifact service for persisting artifacts.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`branch()`

Returns the branch ID for the current invocation, if one is set.

`void`

`branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") branch)`

Sets the [branch] ID for the current invocation.

`static [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`builder()`

Returns a new [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") for creating [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instances.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`callbackContextData()`

Returns a map for storing temporary context data that can be shared between different parts of the invocation (e.g., before/on/after model callbacks).

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents")>`

`contextCacheConfig()`

Returns the context cache configuration for the current agent run.

`boolean`

`endInvocation()`

Returns whether this invocation should be ended, e.g., due to reaching a terminal state or error.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`endOfAgents()`

Returns an unmodifiable view of the per-agent end-of-agent flags for this invocation, keyed by agent name.

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

 

`com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>`

`events(boolean currentInvocation, boolean currentBranch)`

Returns the current session's events, optionally filtered to the current invocation and/or the current branch.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer")>`

`eventsCompactionConfig()`

Returns the events compaction configuration for the current agent run.

`com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>`

`eventsOnCurrentBranch()`

Returns a snapshot of the session's events, keeping only those on the branch this invocation is running on.

`int`

`hashCode()`

 

`void`

`incrementLlmCallsCount()`

Increments the count of LLM calls made during this invocation and throws an exception if the limit defined in [`RunConfig`](RunConfig.html "class in com.google.adk.agents") is exceeded.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`invocationId()`

Returns the unique ID for this invocation.

`boolean`

`isLegacyResumability()`

Deprecated.

Reports the deprecated plain-text continuation shim and goes away with it; use `isResumable()`.

`boolean`

`isResumable()`

Returns whether the current invocation is resumable.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")>`

`liveRequestQueue()`

Returns the queue for managing live requests, if available for this invocation.

`[BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory")`

`memoryService()`

Returns the memory service for accessing agent memory.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`newInvocationContextId()`

Generates a new unique ID for an invocation context.

`[Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")`

`pluginManager()`

Returns the plugin manager for accessing tools and plugins.

`void`

`populateInvocationAgentStates()`

Rehydrates `agentStates()` and `endOfAgents()` from the current invocation's history when this invocation is resumable.

`[RunConfig](RunConfig.html "class in com.google.adk.agents")`

`runConfig()`

Returns the configuration for the current agent run.

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`session()`

Returns the session associated with this invocation.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

Returns the session service for managing session state.

`void`

`setEndInvocation(boolean endInvocation)`

Sets whether this invocation should be ended.

`boolean`

`shouldPauseInvocation([Event](../events/Event.html "class in com.google.adk.events") event)`

Returns whether to pause the invocation right after this event: it is resumable and the event carries a long-running function call, including a synthetic `adk_request_confirmation` HITL request.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`toBuilder()`

Returns a [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") initialized with the values of this instance.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`userContent()`

Returns the user content that triggered this invocation, if any.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`userId()`

Returns the user ID associated with the session.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### InvocationContext

protected InvocationContext([InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder)

  * ## Method Details

    * ### builder

public static [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder()

Returns a new [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") for creating [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instances.

    * ### toBuilder

public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") toBuilder()

Returns a [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") initialized with the values of this instance.

    * ### sessionService

public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

Returns the session service for managing session state.

    * ### artifactService

public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

Returns the artifact service for persisting artifacts.

    * ### memoryService

public [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService()

Returns the memory service for accessing agent memory.

    * ### pluginManager

public [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager()

Returns the plugin manager for accessing tools and plugins.

    * ### activeStreamingTools

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ActiveStreamingTool](ActiveStreamingTool.html "class in com.google.adk.agents")> activeStreamingTools()

Returns a map of tool call IDs to active streaming tools for the current invocation.

    * ### liveRequestQueue

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue()

Returns the queue for managing live requests, if available for this invocation.

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId()

Returns the unique ID for this invocation.

    * ### branch

public void branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") branch)

Sets the [branch] ID for the current invocation. A branch represents a fork in the conversation history.

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> branch()

Returns the branch ID for the current invocation, if one is set. A branch represents a fork in the conversation history.

    * ### agent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent()

Returns the agent being invoked.

    * ### session

public [Session](../sessions/Session.html "class in com.google.adk.sessions") session()

Returns the session associated with this invocation.

    * ### eventsOnCurrentBranch

public com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")> eventsOnCurrentBranch()

Returns a snapshot of the session's events, keeping only those on the branch this invocation is running on. 

The rule is author-asymmetric on purpose, so a confirmation the user answered on a sub-branch stays visible while a descendant agent's own events do not.

    * ### userContent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content> userContent()

Returns the user content that triggered this invocation, if any.

    * ### runConfig

public [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig()

Returns the configuration for the current agent run.

    * ### callbackContextData

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> callbackContextData()

Returns a map for storing temporary context data that can be shared between different parts of the invocation (e.g., before/on/after model callbacks).

    * ### endInvocation

public boolean endInvocation()

Returns whether this invocation should be ended, e.g., due to reaching a terminal state or error.

    * ### setEndInvocation

public void setEndInvocation(boolean endInvocation)

Sets whether this invocation should be ended.

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName()

Returns the application name associated with the session.

    * ### userId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId()

Returns the user ID associated with the session.

    * ### newInvocationContextId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") newInvocationContextId()

Generates a new unique ID for an invocation context.

    * ### incrementLlmCallsCount

public void incrementLlmCallsCount() throws [LlmCallsLimitExceededException](../models/LlmCallsLimitExceededException.html "class in com.google.adk.models")

Increments the count of LLM calls made during this invocation and throws an exception if the limit defined in [`RunConfig`](RunConfig.html "class in com.google.adk.agents") is exceeded.

Throws:
    `[LlmCallsLimitExceededException](../models/LlmCallsLimitExceededException.html "class in com.google.adk.models")` \- if the call limit is exceeded

    * ### eventsCompactionConfig

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer")> eventsCompactionConfig()

Returns the events compaction configuration for the current agent run.

    * ### contextCacheConfig

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents")> contextCacheConfig()

Returns the context cache configuration for the current agent run.

    * ### isResumable

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public boolean isResumable()

Returns whether the current invocation is resumable.

    * ### isLegacyResumability

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public boolean isLegacyResumability()

Deprecated.

Reports the deprecated plain-text continuation shim and goes away with it; use `isResumable()`.

Returns whether the invocation runs the legacy resumption flow: the behavior `isResumable()` had before durable checkpoints existed. It is a separate flow, not a weaker `isResumable()`, so a caller wanting either has to ask for both.

    * ### agentStates

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> agentStates()

Returns an unmodifiable view of the per-agent resumability checkpoint states for this invocation, keyed by agent name. The backing map is shared by reference across derived contexts within the invocation; mutate it only through `setAgentState(String, Map, boolean)`.

    * ### endOfAgents

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> endOfAgents()

Returns an unmodifiable view of the per-agent end-of-agent flags for this invocation, keyed by agent name.

    * ### populateInvocationAgentStates

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public void populateInvocationAgentStates()

Rehydrates `agentStates()` and `endOfAgents()` from the current invocation's history when this invocation is resumable. For each event carrying agent-state information, sets the authoring agent's checkpoint; for a non-workflow author that already produced content, seeds an empty state so it is treated as mid-run.

    * ### events

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")> events(boolean currentInvocation, boolean currentBranch)

Returns the current session's events, optionally filtered to the current invocation and/or the current branch. Reads the in-memory [`Session.events()`](../sessions/Session.html#events\(\)) list, which [`BaseSessionService.appendEvent(Session, Event)`](../sessions/BaseSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\)) keeps in sync. A `null`-branch event is visible on any branch.

Parameters:
    `currentInvocation` \- whether to filter to events from this invocation.
    `currentBranch` \- whether to filter to events on this branch (or with no branch).

    * ### shouldPauseInvocation

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public boolean shouldPauseInvocation([Event](../events/Event.html "class in com.google.adk.events") event)

Returns whether to pause the invocation right after this event: it is resumable and the event carries a long-running function call, including a synthetic `adk_request_confirmation` HITL request. Pausing, unlike ending, leaves the invocation resumable.

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
