JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LoopAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LoopAgent](LoopAgent.html)
  3. [Builder](LoopAgent.Builder.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Builder()
  6. Method Details
     1. maxIterations(Integer)
     2. build()

Hide sidebar  Show sidebar

# Class LoopAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")>

com.google.adk.agents.LoopAgent.Builder

Enclosing class:
    `[LoopAgent](LoopAgent.html "class in com.google.adk.agents")`

* * *

public static class LoopAgent.Builder extends [BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")>

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

  * ## Field Summary

### Fields inherited from class [BaseAgent.Builder](BaseAgent.Builder.html#field-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback), [description](BaseAgent.Builder.html#description), [name](BaseAgent.Builder.html#name), [subAgents](BaseAgent.Builder.html#subAgents)`

Modifier and Type

Field

Description

`protected com.google.common.collect.ImmutableList<[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback)`

 

`protected com.google.common.collect.ImmutableList<[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`[beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback)`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](BaseAgent.Builder.html#description)`

 

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BaseAgent.Builder.html#name)`

 

`protected com.google.common.collect.ImmutableList<[BaseAgent](BaseAgent.html "class in com.google.adk.agents")>`

`[subAgents](BaseAgent.Builder.html#subAgents)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[LoopAgent](LoopAgent.html "class in com.google.adk.agents")`

`build()`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`maxIterations(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxIterations)`

 

### Methods inherited from class [BaseAgent.Builder](BaseAgent.Builder.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\) "afterAgentCallback\(Callbacks.AfterAgentCallback\)"), [afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(java.util.List\) "afterAgentCallback\(List\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\) "beforeAgentCallback\(Callbacks.BeforeAgentCallback\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(java.util.List\) "beforeAgentCallback\(List\)"), [description](BaseAgent.Builder.html#description\(java.lang.String\) "description\(String\)"), [name](BaseAgent.Builder.html#name\(java.lang.String\) "name\(String\)"), [self](BaseAgent.Builder.html#self\(\) "self\(\)"), [subAgents](BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\) "subAgents\(BaseAgent...\)"), [subAgents](BaseAgent.Builder.html#subAgents\(java.util.List\) "subAgents\(List\)")`

Modifier and Type

Method

Description

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[description](BaseAgent.Builder.html#description\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[name](BaseAgent.Builder.html#name\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`protected [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[self](BaseAgent.Builder.html#self\(\))()`

This is a safe cast to the concrete builder type.

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[subAgents](BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`[subAgents](BaseAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### maxIterations

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") maxIterations(@Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxIterations)

    * ### build

public [LoopAgent](LoopAgent.html "class in com.google.adk.agents") build()

Specified by:
    `[build](BaseAgent.Builder.html#build\(\))` in class `[BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")>`




* * *

Copyright (C) 1980\. All rights reserved.
