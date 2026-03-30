JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)



Contents 

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
     7. canonicalTools()
     8. canonicalTools(ReadonlyContext)
     9. instruction()
     10. globalInstruction()
     11. model()
     12. planning()
     13. maxSteps()
     14. generateContentConfig()
     15. includeContents()
     16. tools()
     17. toolsUnion()
     18. toolsets()
     19. disallowTransferToParent()
     20. disallowTransferToPeers()
     21. beforeModelCallback()
     22. afterModelCallback()
     23. beforeToolCallback()
     24. afterToolCallback()
     25. onModelErrorCallback()
     26. onToolErrorCallback()
     27. canonicalBeforeModelCallbacks()
     28. canonicalAfterModelCallbacks()
     29. canonicalOnModelErrorCallbacks()
     30. canonicalBeforeToolCallbacks()
     31. canonicalAfterToolCallbacks()
     32. canonicalOnToolErrorCallbacks()
     33. inputSchema()
     34. outputSchema()
     35. executor()
     36. outputKey()
     37. codeExecutor()
     38. resolvedModel()
     39. fromConfig(LlmAgentConfig, String)
     40. close()

Hide sidebar  Show sidebar

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

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

`afterModelCallback()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>`

`afterToolCallback()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>`

`beforeModelCallback()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

`beforeToolCallback()`

 

`static [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

Returns a [`LlmAgent.Builder`](LlmAgent.Builder.html "class in com.google.adk.agents") for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

`canonicalAfterModelCallbacks()`

The resolved afterModelCallback field as a list.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>`

`canonicalAfterToolCallbacks()`

The resolved afterToolCallback field as a list.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>`

`canonicalBeforeModelCallbacks()`

The resolved beforeModelCallback field as a list.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

`canonicalBeforeToolCallbacks()`

The resolved beforeToolCallback field as a list.

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

`canonicalGlobalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text global instruction for this agent based on the `globalInstruction` field.

`io.reactivex.rxjava3.core.Single<[Map.Entry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.Entry.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>>`

`canonicalInstruction([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the text instruction for this agent based on the `instruction` field.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")>`

`canonicalOnModelErrorCallbacks()`

The resolved onModelErrorCallback field as a list.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")>`

`canonicalOnToolErrorCallbacks()`

The resolved onToolErrorCallback field as a list.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`canonicalTools()`

Constructs the list of tools for this agent based on the `tools()` field.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`canonicalTools([ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)`

Constructs the list of tools for this agent based on the `tools()` field.

`io.reactivex.rxjava3.core.Completable`

`close()`

Closes all sub-agents.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors")>`

`codeExecutor()`

 

`protected [BaseLlmFlow](../flows/llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows")`

`determineLlmFlow()`

 

`boolean`

`disallowTransferToParent()`

 

`boolean`

`disallowTransferToPeers()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent")>`

`executor()`

 

`static [LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

`fromConfig([LlmAgentConfig](LlmAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

Creates an LlmAgent from configuration with full subagent support.

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

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")>`

`onModelErrorCallback()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")>`

`onToolErrorCallback()`

 

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

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>>`

`tools()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>`

`toolsets()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`toolsUnion()`

 

### Methods inherited from class [BaseAgent](BaseAgent.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\) "afterAgentCallback\(\)"), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\) "beforeAgentCallback\(\)"), [canonicalAfterAgentCallbacks](BaseAgent.html#canonicalAfterAgentCallbacks\(\) "canonicalAfterAgentCallbacks\(\)"), [canonicalBeforeAgentCallbacks](BaseAgent.html#canonicalBeforeAgentCallbacks\(\) "canonicalBeforeAgentCallbacks\(\)"), [description](BaseAgent.html#description\(\) "description\(\)"), [findAgent](BaseAgent.html#findAgent\(java.lang.String\) "findAgent\(String\)"), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\) "findSubAgent\(String\)"), [fromConfig](BaseAgent.html#fromConfig\(com.google.adk.agents.BaseAgentConfig,java.lang.String\) "fromConfig\(BaseAgentConfig, String\)"), [name](BaseAgent.html#name\(\) "name\(\)"), [parentAgent](BaseAgent.html#parentAgent\(\) "parentAgent\(\)"), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\) "parentAgent\(BaseAgent\)"), [rootAgent](BaseAgent.html#rootAgent\(\) "rootAgent\(\)"), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\) "runAsync\(InvocationContext\)"), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)"), [subAgents](BaseAgent.html#subAgents\(\) "subAgents\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

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

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> canonicalTools()

Constructs the list of tools for this agent based on the `tools()` field.

Returns:
    The resolved list of tools as a `Single` wrapped list of [`BaseTool`](../tools/BaseTool.html "class in com.google.adk.tools").

    * ### canonicalTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> canonicalTools(@Nullable [ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents") context)

Constructs the list of tools for this agent based on the `tools()` field.

Parameters:
    `context` \- The context to retrieve the session state.
Returns:
    The resolved list of tools as a `Single` wrapped list of [`BaseTool`](../tools/BaseTool.html "class in com.google.adk.tools").

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

    * ### includeContents

public [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents()

    * ### tools

public io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>> tools()

    * ### toolsUnion

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolsUnion()

    * ### toolsets

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")> toolsets()

    * ### disallowTransferToParent

public boolean disallowTransferToParent()

    * ### disallowTransferToPeers

public boolean disallowTransferToPeers()

    * ### beforeModelCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")> beforeModelCallback()

    * ### afterModelCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")> afterModelCallback()

    * ### beforeToolCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")> beforeToolCallback()

    * ### afterToolCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")> afterToolCallback()

    * ### onModelErrorCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")> onModelErrorCallback()

    * ### onToolErrorCallback

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")> onToolErrorCallback()

    * ### canonicalBeforeModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")> canonicalBeforeModelCallbacks()

The resolved beforeModelCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalAfterModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")> canonicalAfterModelCallbacks()

The resolved afterModelCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalOnModelErrorCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")> canonicalOnModelErrorCallbacks()

The resolved onModelErrorCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalBeforeToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")> canonicalBeforeToolCallbacks()

The resolved beforeToolCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalAfterToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")> canonicalAfterToolCallbacks()

The resolved afterToolCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### canonicalOnToolErrorCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")> canonicalOnToolErrorCallbacks()

The resolved onToolErrorCallback field as a list. 

This method is only for use by Agent Development Kit.

    * ### inputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema> inputSchema()

    * ### outputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Schema> outputSchema()

    * ### executor

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent")> executor()

    * ### outputKey

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> outputKey()

    * ### codeExecutor

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors")> codeExecutor()

    * ### resolvedModel

public [Model](../models/Model.html "class in com.google.adk.models") resolvedModel()

    * ### fromConfig

public static [LlmAgent](LlmAgent.html "class in com.google.adk.agents") fromConfig([LlmAgentConfig](LlmAgentConfig.html "class in com.google.adk.agents") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Creates an LlmAgent from configuration with full subagent support.

Parameters:
    `config` \- the agent configuration
    `configAbsPath` \- The absolute path to the agent config file. This is needed for resolving relative paths for e.g. tools and subagents.
Returns:
    the configured LlmAgent
Throws:
    `[ConfigAgentUtils.ConfigurationException](ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the configuration is invalid

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Description copied from class: `[BaseAgent](BaseAgent.html#close\(\))`

Closes all sub-agents.

Overrides:
    `[close](BaseAgent.html#close\(\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Returns:
    a `Completable` that completes when all sub-agents are closed.




* * *

Copyright (C) 1980\. All rights reserved.
