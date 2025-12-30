JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LoopAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LoopAgent](LoopAgent.html)
  3. [Builder](LoopAgent.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. name(String)
     2. description(String)
     3. subAgents(List)
     4. subAgents(BaseAgent...)
     5. maxIterations(int)
     6. maxIterations(Optional)
     7. beforeAgentCallback(Callbacks.BeforeAgentCallback)
     8. beforeAgentCallback(List)
     9. afterAgentCallback(Callbacks.AfterAgentCallback)
     10. afterAgentCallback(List)
     11. build()



# Class LoopAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.LoopAgent.Builder

Enclosing class:
    `[LoopAgent](LoopAgent.html "class in com.google.adk.agents")`

* * *

public static class LoopAgent.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

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

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`[LoopAgent](LoopAgent.html "class in com.google.adk.agents")`

`build()`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`maxIterations(int maxIterations)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`maxIterations([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxIterations)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### description

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### subAgents

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### subAgents

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)

    * ### maxIterations

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") maxIterations(int maxIterations)

    * ### maxIterations

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") maxIterations([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxIterations)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)

    * ### build

public [LoopAgent](LoopAgent.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 2025\. All rights reserved.
