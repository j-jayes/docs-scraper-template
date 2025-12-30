JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SequentialAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [SequentialAgent](SequentialAgent.html)
  3. [Builder](SequentialAgent.Builder.html)



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
     5. beforeAgentCallback(Callbacks.BeforeAgentCallback)
     6. beforeAgentCallback(List)
     7. afterAgentCallback(Callbacks.AfterAgentCallback)
     8. afterAgentCallback(List)
     9. build()



# Class SequentialAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.SequentialAgent.Builder

Enclosing class:
    `[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

* * *

public static class SequentialAgent.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

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

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")`

`build()`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### description

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### subAgents

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### subAgents

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)

    * ### build

public [SequentialAgent](SequentialAgent.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 2025\. All rights reserved.
