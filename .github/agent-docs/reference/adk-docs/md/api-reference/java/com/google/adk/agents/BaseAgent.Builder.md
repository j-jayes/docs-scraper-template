JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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
     4. callbackPluginBuilder
  6. Constructor Details
     1. Builder()
  7. Method Details
     1. callbackPluginBuilder()
     2. self()
     3. name(String)
     4. description(String)
     5. subAgents(List)
     6. subAgents(BaseAgent...)
     7. beforeAgentCallback(Callbacks.BeforeAgentCallback)
     8. beforeAgentCallback(List)
     9. afterAgentCallback(Callbacks.AfterAgentCallback)
     10. afterAgentCallback(List)
     11. build()

Hide sidebar  Show sidebar

# Class BaseAgent.Builder<B extends BaseAgent.Builder<B>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.BaseAgent.Builder<B>

Type Parameters:
    `B` \- The concrete builder type.

Direct Known Subclasses:
    `[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents"), [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents"), [ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents"), [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

Enclosing class:
    `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

* * *

public abstract static class BaseAgent.Builder<B extends BaseAgent.Builder<B>> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Base Builder for all agents.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected final [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`callbackPluginBuilder`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`description`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

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

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`B`

`beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`B`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`abstract [BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`build()`

 

`protected [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`callbackPluginBuilder()`

 

`B`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`B`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`protected B`

`self()`

This is a safe cast to the concrete builder type.

`B`

`subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`B`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### name

protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name

    * ### description

protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description

    * ### subAgents

protected com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents

    * ### callbackPluginBuilder

protected final [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") callbackPluginBuilder

  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### callbackPluginBuilder

protected [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") callbackPluginBuilder()

    * ### self

protected B self()

This is a safe cast to the concrete builder type.

    * ### name

@CanIgnoreReturnValue public B name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### description

@CanIgnoreReturnValue public B description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### subAgents

@CanIgnoreReturnValue public B subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### subAgents

@CanIgnoreReturnValue public B subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public B beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public B beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public B afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public B afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)

    * ### build

public abstract [BaseAgent](BaseAgent.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 1980\. All rights reserved.
