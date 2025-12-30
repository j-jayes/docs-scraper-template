JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ReadonlyContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [ReadonlyContext](../ReadonlyContext.html)



# Uses of Class  
com.google.adk.agents.ReadonlyContext

Packages that use [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.mcp

 

  * ## Uses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Subclasses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[CallbackContext](../CallbackContext.html "class in com.google.adk.agents")`

The context of various callbacks for an agent invocation.

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "class or interface in java.util.function")<[ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`

Instruction.Provider.`[getInstruction](../Instruction.Provider.html#getInstruction\(\))()`

Returns the value of the `getInstruction` record component.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

LlmAgent.`[canonicalGlobalInstruction](../LlmAgent.html#canonicalGlobalInstruction\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text global instruction for this agent based on the `LlmAgent.globalInstruction` field.

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

LlmAgent.`[canonicalInstruction](../LlmAgent.html#canonicalInstruction\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text instruction for this agent based on the `LlmAgent.instruction` field.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../LlmAgent.html#canonicalTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") context)`

Convenience overload of canonicalTools that accepts a non-optional ReadonlyContext.

Method parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../LlmAgent.html#canonicalTools\(java.util.Optional\))([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")> context)`

Constructs the list of tools for this agent based on the [`LlmAgent.tools()`](../LlmAgent.html#tools\(\)) field.

Constructor parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[Provider](../Instruction.Provider.html#%3Cinit%3E\(java.util.function.Function\))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "class or interface in java.util.function")<[ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> getInstruction)`

Creates an instance of a `Provider` record class.

  * ## Uses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Subclasses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Modifier and Type

Class

Description

`class `

`[ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools")`

ToolContext object provides a structured context for executing tools or functions.

Methods in [com.google.adk.tools](../../tools/package-summary.html) with parameters of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")>`

BaseToolset.`[getTools](../../tools/BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

Method parameters in [com.google.adk.tools](../../tools/package-summary.html) with type arguments of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`boolean`

ToolPredicate.`[test](../../tools/ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Decides if the given tool is selected.

  * ## Uses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.tools.applicationintegrationtoolset](../../tools/applicationintegrationtoolset/package-summary.html)

Methods in [com.google.adk.tools.applicationintegrationtoolset](../../tools/applicationintegrationtoolset/package-summary.html) with parameters of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")>`

ApplicationIntegrationToolset.`[getTools](../../tools/applicationintegrationtoolset/ApplicationIntegrationToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))(@Nullable [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

  * ## Uses of [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") in [com.google.adk.tools.mcp](../../tools/mcp/package-summary.html)

Methods in [com.google.adk.tools.mcp](../../tools/mcp/package-summary.html) with parameters of type [ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools")>`

McpToolset.`[getTools](../../tools/mcp/McpToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 




* * *

Copyright (C) 2025\. All rights reserved.
