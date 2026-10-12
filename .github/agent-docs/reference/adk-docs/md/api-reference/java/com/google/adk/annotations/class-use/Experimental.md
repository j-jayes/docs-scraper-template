JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Experimental.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.annotations](../package-summary.html)
  2. [Experimental](../Experimental.html)



# Uses of Annotation Interface  
com.google.adk.annotations.Experimental

Packages that use [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations")

Package

Description

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.runner

 

  * ## Uses of [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with annotations of type [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations")

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

InvocationContext.`[agentStates](../../agents/InvocationContext.html#agentStates\(\))()`

Returns an unmodifiable view of the per-agent resumability checkpoint states for this invocation, keyed by agent name.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

InvocationContext.`[endOfAgents](../../agents/InvocationContext.html#endOfAgents\(\))()`

Returns an unmodifiable view of the per-agent end-of-agent flags for this invocation, keyed by agent name.

`com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")>`

InvocationContext.`[events](../../agents/InvocationContext.html#events\(boolean,boolean\))(boolean currentInvocation, boolean currentBranch)`

Returns the current session's events, optionally filtered to the current invocation and/or the current branch.

`boolean`

InvocationContext.`[isResumable](../../agents/InvocationContext.html#isResumable\(\))()`

Returns whether the current invocation is resumable.

`void`

InvocationContext.`[populateInvocationAgentStates](../../agents/InvocationContext.html#populateInvocationAgentStates\(\))()`

Rehydrates [`InvocationContext.agentStates()`](../../agents/InvocationContext.html#agentStates\(\)) and [`InvocationContext.endOfAgents()`](../../agents/InvocationContext.html#endOfAgents\(\)) from the current invocation's history when this invocation is resumable.

`boolean`

InvocationContext.`[shouldPauseInvocation](../../agents/InvocationContext.html#shouldPauseInvocation\(com.google.adk.events.Event\))([Event](../../events/Event.html "class in com.google.adk.events") event)`

Returns whether to pause the invocation right after this event: it is resumable and the event carries a long-running function call, including a synthetic `adk_request_confirmation` HITL request.

  * ## Uses of [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations") in [com.google.adk.apps](../../apps/package-summary.html)

Classes in [com.google.adk.apps](../../apps/package-summary.html) with annotations of type [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations")

Modifier and Type

Class

Description

`class `

`[ResumabilityConfig](../../apps/ResumabilityConfig.html "class in com.google.adk.apps")`

Resumability config for every agent in an app: pause on a long-running call and resume from the last event.

Methods in [com.google.adk.apps](../../apps/package-summary.html) with annotations of type [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[resumabilityConfig](../../apps/App.Builder.html#resumabilityConfig\(com.google.adk.apps.ResumabilityConfig\))([ResumabilityConfig](../../apps/ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

 

`@Nullable [ResumabilityConfig](../../apps/ResumabilityConfig.html "class in com.google.adk.apps")`

App.`[resumabilityConfig](../../apps/App.html#resumabilityConfig\(\))()`

 

  * ## Uses of [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with annotations of type [Experimental](../Experimental.html "annotation interface in com.google.adk.annotations")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId, @Nullable com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent, resuming an existing invocation instead of starting a new one.




* * *

Copyright (C) 1980\. All rights reserved.
