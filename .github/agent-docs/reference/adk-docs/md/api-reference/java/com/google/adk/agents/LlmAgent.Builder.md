JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)
  3. [Builder](LlmAgent.Builder.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BaseAgent.Builder
     2. Methods inherited from class Object
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
     10. includeContents(LlmAgent.IncludeContents)
     11. planning(boolean)
     12. maxSteps(int)
     13. disallowTransferToParent(boolean)
     14. disallowTransferToPeers(boolean)
     15. clearBeforeModelCallbacks()
     16. beforeModelCallback(Callbacks.BeforeModelCallback)
     17. beforeModelCallback(List)
     18. beforeModelCallbackSync(Callbacks.BeforeModelCallbackSync)
     19. afterModelCallback(Callbacks.AfterModelCallback)
     20. afterModelCallback(List)
     21. afterModelCallbackSync(Callbacks.AfterModelCallbackSync)
     22. onModelErrorCallback(Callbacks.OnModelErrorCallback)
     23. onModelErrorCallback(List)
     24. onModelErrorCallbackSync(Callbacks.OnModelErrorCallbackSync)
     25. beforeAgentCallbackSync(Callbacks.BeforeAgentCallbackSync)
     26. afterAgentCallbackSync(Callbacks.AfterAgentCallbackSync)
     27. beforeToolCallback(Callbacks.BeforeToolCallback)
     28. beforeToolCallback(List)
     29. beforeToolCallbackSync(Callbacks.BeforeToolCallbackSync)
     30. afterToolCallback(Callbacks.AfterToolCallback)
     31. afterToolCallback(List)
     32. afterToolCallbackSync(Callbacks.AfterToolCallbackSync)
     33. onToolErrorCallback(Callbacks.OnToolErrorCallback)
     34. onToolErrorCallback(List)
     35. onToolErrorCallbackSync(Callbacks.OnToolErrorCallbackSync)
     36. inputSchema(Schema)
     37. outputSchema(Schema)
     38. executor(Executor)
     39. outputKey(String)
     40. codeExecutor(BaseCodeExecutor)
     41. validate()
     42. build()

Hide sidebar  Show sidebar

# Class LlmAgent.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")>

com.google.adk.agents.LlmAgent.Builder

Enclosing class:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

* * *

public static class LlmAgent.Builder extends [BaseAgent.Builder](BaseAgent.Builder.html "class in com.google.adk.agents")<[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")>

Builder for [`LlmAgent`](LlmAgent.html "class in com.google.adk.agents").

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

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") afterAgentCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") afterModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.AfterModelCallbackBase> afterModelCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") afterModelCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") afterToolCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.AfterToolCallbackBase> afterToolCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`afterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") afterToolCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") beforeAgentCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") beforeModelCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeModelCallbackBase> beforeModelCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") beforeModelCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`beforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") beforeToolCallbackSync)`

 

`[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

`build()`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`clearBeforeModelCallbacks()`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`codeExecutor([BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors") codeExecutor)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`disallowTransferToParent(boolean disallowTransferToParent)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`disallowTransferToPeers(boolean disallowTransferToPeers)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`executor([Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "interface in java.util.concurrent") executor)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`generateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`globalInstruction([Instruction](Instruction.html "interface in com.google.adk.agents") globalInstruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`globalInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") globalInstruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`includeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`inputSchema(com.google.genai.types.Schema inputSchema)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`instruction([Instruction](Instruction.html "interface in com.google.adk.agents") instruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`instruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instruction)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`maxSteps(int maxSteps)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`model([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onModelErrorCallback([Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents") onModelErrorCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onModelErrorCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.OnModelErrorCallbackBase> onModelErrorCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onModelErrorCallbackSync([Callbacks.OnModelErrorCallbackSync](Callbacks.OnModelErrorCallbackSync.html "interface in com.google.adk.agents") onModelErrorCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onToolErrorCallback([Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents") onToolErrorCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onToolErrorCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.OnToolErrorCallbackBase> onToolErrorCallbacks)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`onToolErrorCallbackSync([Callbacks.OnToolErrorCallbackSync](Callbacks.OnToolErrorCallbackSync.html "interface in com.google.adk.agents") onToolErrorCallbackSync)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") outputKey)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`outputSchema(com.google.genai.types.Schema outputSchema)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`planning(boolean planning)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")... tools)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`tools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<?> tools)`

 

`protected void`

`validate()`

 

### Methods inherited from class [BaseAgent.Builder](BaseAgent.Builder.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\) "afterAgentCallback\(Callbacks.AfterAgentCallback\)"), [afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(java.util.List\) "afterAgentCallback\(List\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\) "beforeAgentCallback\(Callbacks.BeforeAgentCallback\)"), [beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(java.util.List\) "beforeAgentCallback\(List\)"), [description](BaseAgent.Builder.html#description\(java.lang.String\) "description\(String\)"), [name](BaseAgent.Builder.html#name\(java.lang.String\) "name\(String\)"), [self](BaseAgent.Builder.html#self\(\) "self\(\)"), [subAgents](BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\) "subAgents\(BaseAgent...\)"), [subAgents](BaseAgent.Builder.html#subAgents\(java.util.List\) "subAgents\(List\)")`

Modifier and Type

Method

Description

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(com.google.adk.agents.Callbacks.AfterAgentCallback\))([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") afterAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[afterAgentCallback](BaseAgent.Builder.html#afterAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.AfterAgentCallbackBase> afterAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(com.google.adk.agents.Callbacks.BeforeAgentCallback\))([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") beforeAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[beforeAgentCallback](BaseAgent.Builder.html#beforeAgentCallback\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.agents.Callbacks.BeforeAgentCallbackBase> beforeAgentCallback)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[description](BaseAgent.Builder.html#description\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[name](BaseAgent.Builder.html#name\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`protected [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[self](BaseAgent.Builder.html#self\(\))()`

This is a safe cast to the concrete builder type.

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[subAgents](BaseAgent.Builder.html#subAgents\(com.google.adk.agents.BaseAgent...\))([BaseAgent](BaseAgent.html "class in com.google.adk.agents")... subAgents)`

 

`[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")`

`[subAgents](BaseAgent.Builder.html#subAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")> subAgents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### model

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") model([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)

    * ### model

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") model([BaseLlm](../models/BaseLlm.html "class in com.google.adk.models") model)

    * ### instruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") instruction([Instruction](Instruction.html "interface in com.google.adk.agents") instruction)

    * ### instruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") instruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instruction)

    * ### globalInstruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") globalInstruction([Instruction](Instruction.html "interface in com.google.adk.agents") globalInstruction)

    * ### globalInstruction

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") globalInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") globalInstruction)

    * ### tools

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") tools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<?> tools)

    * ### tools

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") tools([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")... tools)

    * ### generateContentConfig

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") generateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)

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

    * ### clearBeforeModelCallbacks

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") clearBeforeModelCallbacks()

    * ### beforeModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") beforeModelCallback)

    * ### beforeModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeModelCallbackBase> beforeModelCallbacks)

    * ### beforeModelCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") beforeModelCallbackSync)

    * ### afterModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") afterModelCallback)

    * ### afterModelCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.AfterModelCallbackBase> afterModelCallbacks)

    * ### afterModelCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") afterModelCallbackSync)

    * ### onModelErrorCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onModelErrorCallback([Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents") onModelErrorCallback)

    * ### onModelErrorCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onModelErrorCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.OnModelErrorCallbackBase> onModelErrorCallbacks)

    * ### onModelErrorCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onModelErrorCallbackSync([Callbacks.OnModelErrorCallbackSync](Callbacks.OnModelErrorCallbackSync.html "interface in com.google.adk.agents") onModelErrorCallbackSync)

    * ### beforeAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") beforeAgentCallbackSync)

    * ### afterAgentCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") afterAgentCallbackSync)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") beforeToolCallback)

    * ### beforeToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.BeforeToolCallbackBase> beforeToolCallbacks)

    * ### beforeToolCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") beforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") beforeToolCallbackSync)

    * ### afterToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") afterToolCallback)

    * ### afterToolCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.AfterToolCallbackBase> afterToolCallbacks)

    * ### afterToolCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") afterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") afterToolCallbackSync)

    * ### onToolErrorCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onToolErrorCallback([Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents") onToolErrorCallback)

    * ### onToolErrorCallback

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onToolErrorCallback(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends com.google.adk.agents.Callbacks.OnToolErrorCallbackBase> onToolErrorCallbacks)

    * ### onToolErrorCallbackSync

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") onToolErrorCallbackSync([Callbacks.OnToolErrorCallbackSync](Callbacks.OnToolErrorCallbackSync.html "interface in com.google.adk.agents") onToolErrorCallbackSync)

    * ### inputSchema

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") inputSchema(com.google.genai.types.Schema inputSchema)

    * ### outputSchema

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") outputSchema(com.google.genai.types.Schema outputSchema)

    * ### executor

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") executor([Executor](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Executor.html "interface in java.util.concurrent") executor)

    * ### outputKey

@CanIgnoreReturnValue public [LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents") outputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") outputKey)

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
