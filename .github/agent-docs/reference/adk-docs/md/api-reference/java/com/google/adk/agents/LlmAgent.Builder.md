JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)
  3. [Builder](LlmAgent.Builder.html)



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
     3. model(String)
     4. model(BaseLlm)
     5. instruction(Instruction)
     6. instruction(String)
     7. globalInstruction(Instruction)
     8. globalInstruction(String)
     9. subAgents(List)
     10. subAgents(BaseAgent...)
     11. tools(List)
     12. tools(Object...)
     13. generateContentConfig(GenerateContentConfig)
     14. exampleProvider(BaseExampleProvider)
     15. exampleProvider(List)
     16. exampleProvider(Example...)
     17. includeContents(LlmAgent.IncludeContents)
     18. planning(boolean)
     19. maxSteps(int)
     20. disallowTransferToParent(boolean)
     21. disallowTransferToPeers(boolean)
     22. beforeModelCallback(Callbacks.BeforeModelCallback)
     23. beforeModelCallback(List)
     24. beforeModelCallbackSync(Callbacks.BeforeModelCallbackSync)
     25. afterModelCallback(Callbacks.AfterModelCallback)
     26. afterModelCallback(List)
     27. afterModelCallbackSync(Callbacks.AfterModelCallbackSync)
     28. beforeAgentCallback(Callbacks.BeforeAgentCallback)
     29. beforeAgentCallback(List)
     30. beforeAgentCallbackSync(Callbacks.BeforeAgentCallbackSync)
     31. afterAgentCallback(Callbacks.AfterAgentCallback)
     32. afterAgentCallback(List)
     33. afterAgentCallbackSync(Callbacks.AfterAgentCallbackSync)
     34. beforeToolCallback(Callbacks.BeforeToolCallback)
     35. beforeToolCallback(List)
     36. beforeToolCallbackSync(Callbacks.BeforeToolCallbackSync)
     37. afterToolCallback(Callbacks.AfterToolCallback)
     38. afterToolCallback(List)
     39. afterToolCallbackSync(Callbacks.AfterToolCallbackSync)
     40. inputSchema(Schema)
     41. outputSchema(Schema)
     42. executor(Executor)
     43. outputKey(String)
     44. validate()
     45. build()



# Class LlmAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.LlmAgent.Builder

Enclosing class:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

* * *

public static class LlmAgent.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

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

`afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

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

`beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

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

`beforeToolCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") beforeToolCallbackSync)`

 

`[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

`build()`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

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

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputSchema(com.google.genai.types.Schema outputSchema)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`planning(boolean planning)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")... tools)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<?> tools)`

 

`protected void`

`validate()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### description

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

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

    * ### subAgents

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") subAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)

    * ### subAgents

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") subAgents([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)

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

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)

    * ### beforeAgentCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)

    * ### beforeAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") beforeAgentCallbackSync)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)

    * ### afterAgentCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterAgentCallback([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)

    * ### afterAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") afterAgentCallbackSync)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)

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

    * ### validate

protected void validate()

    * ### build

public [LlmAgent](LlmAgent.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 2025\. All rights reserved.
