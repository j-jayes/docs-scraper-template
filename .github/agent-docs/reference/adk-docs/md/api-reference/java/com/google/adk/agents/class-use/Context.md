JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Context.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [Context](../Context.html)



# Uses of Class  
com.google.adk.agents.Context

Packages that use [Context](../Context.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.tools

 

com.google.adk.workflow

 

  * ## Uses of [Context](../Context.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Subclasses of [Context](../Context.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[CallbackContext](../CallbackContext.html "class in com.google.adk.agents")`

The context of various callbacks for an agent invocation.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Context](../Context.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseAgent.`[runNode](../BaseAgent.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs this agent as a workflow node through its [`BaseAgent.runAsync(InvocationContext)`](../BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\)) lifecycle, including its callbacks.

  * ## Uses of [Context](../Context.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Subclasses of [Context](../Context.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Modifier and Type

Class

Description

`class `

`[ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools")`

ToolContext object provides a structured context for executing tools or functions.

  * ## Uses of [Context](../Context.html "class in com.google.adk.agents") in [com.google.adk.workflow](../../workflow/package-summary.html)

Methods in [com.google.adk.workflow](../../workflow/package-summary.html) with parameters of type [Context](../Context.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<?>`

JoinNode.`[runNode](../../workflow/JoinNode.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Outputs its input unchanged, or nothing when the input is null.

`io.reactivex.rxjava3.core.Flowable<?>`

Node.`[runNode](../../workflow/Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs the node on `nodeInput`, the output it receives from its predecessors.

`io.reactivex.rxjava3.core.Flowable<?>`

Start.`[runNode](../../workflow/Start.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

 

`io.reactivex.rxjava3.core.Flowable<?>`

Workflow.`[runNode](../../workflow/Workflow.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

 




* * *

Copyright (C) 1980\. All rights reserved.
