JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PlanningContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [PlanningContext](PlanningContext.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. PlanningContext(InvocationContext, ImmutableList)
  5. Method Details
     1. state()
     2. events()
     3. availableAgents()
     4. userContent()
     5. findAgent(String)
     6. invocationContext()

Hide sidebar  Show sidebar

# Class PlanningContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.PlanningContext

* * *

public class PlanningContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Context provided to a [`Planner`](Planner.html "interface in com.google.adk.agents") during the planning loop. 

Wraps an [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") to expose the session state (world state), events, and available sub-agents. Planners use this to inspect the current state and decide which agent(s) to run next.

  * ## Constructor Summary

Constructors

Constructor

Description

`PlanningContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> availableAgents)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`availableAgents()`

Returns the sub-agents available for the planner to select from.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`events()`

Returns all events in the current session.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Finds an available agent by name.

`[InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`invocationContext()`

Returns the full [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") for advanced use cases.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`state()`

Returns the session state — the shared "world state" that agents read and write.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`userContent()`

Returns the user content that initiated this invocation, if any.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### PlanningContext

public PlanningContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> availableAgents)

  * ## Method Details

    * ### state

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state()

Returns the session state — the shared "world state" that agents read and write.

    * ### events

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events()

Returns all events in the current session.

    * ### availableAgents

public com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> availableAgents()

Returns the sub-agents available for the planner to select from.

    * ### userContent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content> userContent()

Returns the user content that initiated this invocation, if any.

    * ### findAgent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") findAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Finds an available agent by name.

Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if no agent with the given name is found.

    * ### invocationContext

public [InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext()

Returns the full [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") for advanced use cases.




* * *

Copyright (C) 1980\. All rights reserved.
