JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)
  3. [Builder](LlmAgent.Builder.html)



Contents 

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Builder()
  6. Method Details
     1. model(String)
     2. model(BaseLlm)
     3. instruction(Instruction)
     4. instruction(String)
     5. globalInstruction(Instruction)
     6. globalInstruction(String)
     7. tools(List)
     8. tools(Object...)
     9. generateContentConfig(GenerateContentConfig)
     10. exampleProvider(BaseExampleProvider)
     11. exampleProvider(List)
     12. exampleProvider(Example...)
     13. includeContents(LlmAgent.IncludeContents)
     14. planning(boolean)
     15. maxSteps(int)
     16. disallowTransferToParent(boolean)
     17. disallowTransferToPeers(boolean)
     18. beforeModelCallback(Callbacks.BeforeModelCallback)
     19. beforeModelCallback(List)
     20. beforeModelCallbackSync(Callbacks.BeforeModelCallbackSync)
     21. afterModelCallback(Callbacks.AfterModelCallback)
     22. afterModelCallback(List)
     23. afterModelCallbackSync(Callbacks.AfterModelCallbackSync)
     24. beforeAgentCallbackSync(Callbacks.BeforeAgentCallbackSync)
     25. afterAgentCallbackSync(Callbacks.AfterAgentCallbackSync)
     26. beforeToolCallback(Callbacks.BeforeToolCallback)
     27. beforeToolCallback(List)
     28. beforeToolCallbackSync(Callbacks.BeforeToolCallbackSync)
     29. afterToolCallback(Callbacks.AfterToolCallback)
     30. afterToolCallback(List)
     31. afterToolCallbackSync(Callbacks.AfterToolCallbackSync)
     32. inputSchema(Schema)
     33. outputSchema(Schema)
     34. executor(Executor)
     35. outputKey(String)
     36. codeExecutor(BaseCodeExecutor)
     37. validate()
     38. build()

Hide sidebar  Show sidebar

# Class LlmAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")>

com.google.adk.agents.LlmAgent.Builder

Enclosing class:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

* * *

public static class LlmAgent.Builder extends [BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")>

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

  * ## Field Summary

### Fields inherited from class [BaseAgent.Builder](BaseAgent.Builder.html#field-summary "class in com.google.adk.agents")

`[callbackPluginBuilder](BaseAgent.Builder.html#callbackPluginBuilder), [description](BaseAgent.Builder.html#description), [name](BaseAgent.Builder.html#name), [subAgents](BaseAgent.Builder.html#subAgents)`

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

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") afterAgentCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") afterModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterModelCallbackBase> afterModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") afterModelCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") afterToolCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterToolCallbackBase> afterToolCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") afterToolCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") beforeAgentCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") beforeModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeModelCallbackBase> beforeModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") beforeModelCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") beforeToolCallbackSync)`

 

`[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

`build()`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`codeExecutor([BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors") codeExecutor)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`disallowTransferToParent(boolean disallowTransferToParent)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`disallowTransferToPeers(boolean disallowTransferToPeers)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`exampleProvider([BaseExampleProvider](../examples/BaseExampleProvider.html "interface in com.google.adk.examples") exampleProvider)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`exampleProvider([Example](../examples/Example.html "class in com.google.adk.examples")... examples)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`exampleProvider([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Example](../examples/Example.html "class in com.google.adk.examples")> examples)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`executor([Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent") executor)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`generateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`globalInstruction([Instruction](Instruction.html "interface in com.google.adk.agents") globalInstruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`globalInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") globalInstruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`includeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`inputSchema(com.google.genai.types.Schema inputSchema)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`instruction([Instruction](Instruction.html "interface in com.google.adk.agents") instruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`instruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`maxSteps(int maxSteps)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`model([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputSchema(com.google.genai.types.Schema outputSchema)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`planning(boolean planning)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")... tools)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<?> tools)`

 

`protected void`

`validate()`

 

### Methods inherited from class [BaseAgent.Builder](BaseAgent.Builder.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\) "afterAgentCallback\(Callbacks.AfterAgentCallback\)"), [afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(java.util.List\) "afterAgentCallback\(List\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\) "beforeAgentCallback\(Callbacks.BeforeAgentCallback\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(java.util.List\) "beforeAgentCallback\(List\)"), [callbackPluginBuilder](BaseAgent.Builder.html#callbackPluginBuilder\(\) "callbackPluginBuilder\(\)"), [description](BaseAgent.Builder.html#description\(java.lang.String\) "description\(String\)"), [name](BaseAgent.Builder.html#name\(java.lang.String\) "name\(String\)"), [self](BaseAgent.Builder.html#self\(\) "self\(\)"), [subAgents](BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\) "subAgents\(BaseAgent...\)"), [subAgents](BaseAgent.Builder.html#subAgents\(java.util.List\) "subAgents\(List\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### model

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)

    * ### model

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") model([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model)

    * ### instruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") instruction([Instruction](Instruction.html "interface in com.google.adk.agents") instruction)

    * ### instruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") instruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)

    * ### globalInstruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") globalInstruction([Instruction](Instruction.html "interface in com.google.adk.agents") globalInstruction)

    * ### globalInstruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") globalInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") globalInstruction)

    * ### tools

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") tools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<?> tools)

    * ### tools

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") tools([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")... tools)

    * ### generateContentConfig

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") generateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)

    * ### exampleProvider

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") exampleProvider([BaseExampleProvider](../examples/BaseExampleProvider.html "interface in com.google.adk.examples") exampleProvider)

    * ### exampleProvider

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") exampleProvider([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Example](../examples/Example.html "class in com.google.adk.examples")> examples)

    * ### exampleProvider

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") exampleProvider([Example](../examples/Example.html "class in com.google.adk.examples")... examples)

    * ### includeContents

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") includeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)

    * ### planning

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") planning(boolean planning)

    * ### maxSteps

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") maxSteps(int maxSteps)

    * ### disallowTransferToParent

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") disallowTransferToParent(boolean disallowTransferToParent)

    * ### disallowTransferToPeers

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") disallowTransferToPeers(boolean disallowTransferToPeers)

    * ### beforeModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") beforeModelCallback)

    * ### beforeModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeModelCallbackBase> beforeModelCallback)

    * ### beforeModelCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") beforeModelCallbackSync)

    * ### afterModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") afterModelCallback)

    * ### afterModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterModelCallbackBase> afterModelCallback)

    * ### afterModelCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") afterModelCallbackSync)

    * ### beforeAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") beforeAgentCallbackSync)

    * ### afterAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") afterAgentCallbackSync)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)

    * ### beforeToolCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") beforeToolCallbackSync)

    * ### afterToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") afterToolCallback)

    * ### afterToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterToolCallbackBase> afterToolCallbacks)

    * ### afterToolCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") afterToolCallbackSync)

    * ### inputSchema

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") inputSchema(com.google.genai.types.Schema inputSchema)

    * ### outputSchema

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") outputSchema(com.google.genai.types.Schema outputSchema)

    * ### executor

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") executor([Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "class or interface in java.util.concurrent") executor)

    * ### outputKey

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") outputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey)

    * ### codeExecutor

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") codeExecutor([BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors") codeExecutor)

    * ### validate

protected void validate()

    * ### build

public [LlmAgent](LlmAgent.html "class in com.google.adk.agents") build()

Specified by:
    `[build](BaseAgent.Builder.html#build\(\))` in class `[BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")>`




* * *

Copyright (C) 1980\. All rights reserved.
