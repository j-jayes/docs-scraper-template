JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LlmAgent(LlmAgent.Builder)
  6. Method Details
     1. builder()
     2. determineLlmFlow()
     3. runAsyncImpl(InvocationContext)
     4. runLiveImpl(InvocationContext)
     5. canonicalInstruction(ReadonlyContext)
     6. canonicalGlobalInstruction(ReadonlyContext)
     7. canonicalTools(Optional)
     8. canonicalTools()
     9. canonicalTools(ReadonlyContext)
     10. instruction()
     11. globalInstruction()
     12. model()
     13. planning()
     14. maxSteps()
     15. generateContentConfig()
     16. exampleProvider()
     17. includeContents()
     18. tools()
     19. toolsUnion()
     20. disallowTransferToParent()
     21. disallowTransferToPeers()
     22. beforeModelCallback()
     23. afterModelCallback()
     24. beforeToolCallback()
     25. afterToolCallback()
     26. inputSchema()
     27. outputSchema()
     28. executor()
     29. outputKey()
     30. resolvedModel()



# Class LlmAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.LlmAgent

* * *

public class LlmAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

The LLM-based agent.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

`static enum `

`[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")`

Enum to define if contents of previous events should be included in requests to the underlying LLM.

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`LlmAgent([LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") builder)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>>`

`afterModelCallback()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>>`

`afterToolCallback()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>>`

`beforeModelCallback()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>>`

`beforeToolCallback()`

 

`static [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

Returns a [`LlmAgent.Builder`](LlmAgent.Builder.html "class in com.google.adk.agents") for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

`canonicalGlobalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text global instruction for this agent based on the `globalInstruction` field.

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

`canonicalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text instruction for this agent based on the `instruction` field.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`canonicalTools()`

Overload of canonicalTools that defaults to an empty context.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`canonicalTools([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Convenience overload of canonicalTools that accepts a non-optional ReadonlyContext.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`canonicalTools([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")> context)`

Constructs the list of tools for this agent based on the `tools()` field.

`protected [BaseLlmFlow](../flows/llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows")`

`determineLlmFlow()`

 

`boolean`

`disallowTransferToParent()`

 

`boolean`

`disallowTransferToPeers()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseExampleProvider](../examples/BaseExampleProvider.html "interface in com.google.adk.examples")>`

`exampleProvider()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent")>`

`executor()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig>`

`generateContentConfig()`

 

`[Instruction](Instruction.html "interface in com.google.adk.agents")`

`globalInstruction()`

 

`[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")`

`includeContents()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema>`

`inputSchema()`

 

`[Instruction](Instruction.html "interface in com.google.adk.agents")`

`instruction()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

`maxSteps()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Model](../models/Model.html "class in com.google.adk.models")>`

`model()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`outputKey()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema>`

`outputSchema()`

 

`boolean`

`planning()`

 

`[Model](../models/Model.html "class in com.google.adk.models")`

`resolvedModel()`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`tools()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`toolsUnion()`

 

### Methods inherited from class com.google.adk.agents.[BaseAgent](BaseAgent.html "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\)), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\)), [description](BaseAgent.html#description\(\)), [findAgent](BaseAgent.html#findAgent\(java.lang.String\)), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\)), [name](BaseAgent.html#name\(\)), [parentAgent](BaseAgent.html#parentAgent\(\)), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\)), [rootAgent](BaseAgent.html#rootAgent\(\)), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\)), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\)), [subAgents](BaseAgent.html#subAgents\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LlmAgent

protected LlmAgent([LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") builder)

  * ## Method Details

    * ### builder

public static [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") builder()

Returns a [`LlmAgent.Builder`](LlmAgent.Builder.html "class in com.google.adk.agents") for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

    * ### determineLlmFlow

protected [BaseLlmFlow](../flows/llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows") determineLlmFlow()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific asynchronous logic.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific synchronous logic.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### canonicalInstruction

public io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>> canonicalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)

Constructs the text instruction for this agent based on the `instruction` field. Also returns a boolean indicating that state injection should be bypassed when the instruction is constructed with an [`Instruction.Provider`](Instruction.Provider.html "class in com.google.adk.agents"). 

This method is only for use by Agent Development Kit.

Parameters:
    `context` \- The context to retrieve the session state.
Returns:
    The resolved instruction as a `Single` wrapped Map.Entry. The key is the instruction string and the value is a boolean indicating if state injection should be bypassed.

    * ### canonicalGlobalInstruction

public io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>> canonicalGlobalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)

Constructs the text global instruction for this agent based on the `globalInstruction` field. Also returns a boolean indicating that state injection should be bypassed when the instruction is constructed with an [`Instruction.Provider`](Instruction.Provider.html "class in com.google.adk.agents"). 

This method is only for use by Agent Development Kit.

Parameters:
    `context` \- The context to retrieve the session state.
Returns:
    The resolved global instruction as a `Single` wrapped Map.Entry. The key is the instruction string and the value is a boolean indicating if state injection should be bypassed.

    * ### canonicalTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> canonicalTools([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")> context)

Constructs the list of tools for this agent based on the `tools()` field. 

This method is only for use by Agent Development Kit.

Parameters:
    `context` \- The context to retrieve the session state.
Returns:
    The resolved list of tools as a `Single` wrapped list of [`BaseTool`](../tools/BaseTool.html "class in com.google.adk.tools").

    * ### canonicalTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> canonicalTools()

Overload of canonicalTools that defaults to an empty context.

    * ### canonicalTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> canonicalTools([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)

Convenience overload of canonicalTools that accepts a non-optional ReadonlyContext.

    * ### instruction

public [Instruction](Instruction.html "interface in com.google.adk.agents") instruction()

    * ### globalInstruction

public [Instruction](Instruction.html "interface in com.google.adk.agents") globalInstruction()

    * ### model

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Model](../models/Model.html "class in com.google.adk.models")> model()

    * ### planning

public boolean planning()

    * ### maxSteps

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps()

    * ### generateContentConfig

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> generateContentConfig()

    * ### exampleProvider

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseExampleProvider](../examples/BaseExampleProvider.html "interface in com.google.adk.examples")> exampleProvider()

    * ### includeContents

public [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents()

    * ### tools

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> tools()

    * ### toolsUnion

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolsUnion()

    * ### disallowTransferToParent

public boolean disallowTransferToParent()

    * ### disallowTransferToPeers

public boolean disallowTransferToPeers()

    * ### beforeModelCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>> beforeModelCallback()

    * ### afterModelCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>> afterModelCallback()

    * ### beforeToolCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>> beforeToolCallback()

    * ### afterToolCallback

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>> afterToolCallback()

    * ### inputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema> inputSchema()

    * ### outputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema> outputSchema()

    * ### executor

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent")> executor()

    * ### outputKey

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> outputKey()

    * ### resolvedModel

public [Model](../models/Model.html "class in com.google.adk.models") resolvedModel()




* * *

Copyright (C) 2025\. All rights reserved.
