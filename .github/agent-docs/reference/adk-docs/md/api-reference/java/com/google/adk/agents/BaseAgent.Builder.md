JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [BaseAgent](BaseAgent.html)
  3. [Builder](BaseAgent.Builder.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. name
     2. description
     3. subAgents
     4. beforeAgentCallback
     5. afterAgentCallback
  6. Constructor Details
     1. Builder()
  7. Method Details
     1. self()
     2. name(String)
     3. description(String)
     4. subAgents(List)
     5. subAgents(BaseAgent...)
     6. beforeAgentCallback(Callbacks.BeforeAgentCallback)
     7. beforeAgentCallback(List)
     8. afterAgentCallback(Callbacks.AfterAgentCallback)
     9. afterAgentCallback(List)
     10. build()

Hide sidebar  Show sidebar

# Class BaseAgent.Builder<B extends BaseAgent.Builder<B>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.BaseAgent.Builder<B>

Type Parameters:
    `B` \- The concrete builder type.

Direct Known Subclasses:
    `[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents"), [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents"), [ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents"), [PlannerAgent.Builder](PlannerAgent.Builder.html "class in com.google.adk.agents"), [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

Enclosing class:
    `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

* * *

public abstract static class BaseAgent.Builder<B extends BaseAgent.Builder<B>> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Base Builder for all agents.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected com.google.common.collect.ImmutableList<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`afterAgentCallback`

 

`protected com.google.common.collect.ImmutableList<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`beforeAgentCallback`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`description`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name`

 

`protected com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`subAgents`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`B`

`afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`B`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`B`

`beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`B`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`abstract [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`build()`

 

`B`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`B`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`protected B`

`self()`

This is a safe cast to the concrete builder type.

`B`

`subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`B`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### name

protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name

    * ### description

protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description

    * ### subAgents

protected com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents

    * ### beforeAgentCallback

protected com.google.common.collect.ImmutableList<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> beforeAgentCallback

    * ### afterAgentCallback

protected com.google.common.collect.ImmutableList<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> afterAgentCallback

  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### self

protected B self()

This is a safe cast to the concrete builder type.

    * ### name

@CanIgnoreReturnValue public B name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### description

@CanIgnoreReturnValue public B description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

    * ### subAgents

@CanIgnoreReturnValue public B subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### subAgents

@CanIgnoreReturnValue public B subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public B beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public B beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public B afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public B afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)

    * ### build

public abstract [BaseAgent](BaseAgent.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 1980\. All rights reserved.
