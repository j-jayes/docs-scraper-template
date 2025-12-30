JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Package](package-summary.html)
  * [Use](package-use.html)
  * Tree
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)



# Hierarchy For Package com.google.adk.agents

Package Hierarchies:

  * [All Packages](../../../../overview-tree.html)



## Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * com.google.adk.agents.[BaseAgent](BaseAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LlmAgent](LlmAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LoopAgent](LoopAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[ParallelAgent](ParallelAgent.html "class in com.google.adk.agents")
      * com.google.adk.agents.[SequentialAgent](SequentialAgent.html "class in com.google.adk.agents")
    * com.google.adk.agents.[BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")
      * com.google.adk.agents.[LlmAgentConfig](LlmAgentConfig.html "class in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks](Callbacks.html "class in com.google.adk.agents")
    * com.google.adk.agents.[CallbackUtil](CallbackUtil.html "class in com.google.adk.agents")
    * com.google.adk.agents.[InvocationContext](InvocationContext.html "class in com.google.adk.agents")
    * com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")
      * com.google.adk.agents.[LiveRequest](LiveRequest.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LiveRequest.Builder](LiveRequest.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LlmAgent.Builder](LlmAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[ParallelAgent.Builder](ParallelAgent.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents")
      * com.google.adk.agents.[CallbackContext](CallbackContext.html "class in com.google.adk.agents")
    * com.google.adk.agents.[RunConfig](RunConfig.html "class in com.google.adk.agents")
    * com.google.adk.agents.[RunConfig.Builder](RunConfig.Builder.html "class in com.google.adk.agents")
    * com.google.adk.agents.[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")



## Interface Hierarchy

  * com.google.adk.agents.Callbacks.AfterAgentCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.AfterModelCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.AfterToolCallbackBase 
    * com.google.adk.agents.[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeAgentCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeModelCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.Callbacks.BeforeToolCallbackBase 
    * com.google.adk.agents.[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")
    * com.google.adk.agents.[Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")
  * com.google.adk.agents.[Instruction](Instruction.html "interface in com.google.adk.agents")



## Enum Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<E> (implements java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang")<T>, java.lang.constant.[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "class or interface in java.lang.constant"), java.io.[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")) 
      * com.google.adk.agents.[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")
      * com.google.adk.agents.[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")



## Record Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * java.lang.[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")
      * com.google.adk.agents.[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents") (implements com.google.adk.agents.[Instruction](Instruction.html "interface in com.google.adk.agents"))
      * com.google.adk.agents.[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents") (implements com.google.adk.agents.[Instruction](Instruction.html "interface in com.google.adk.agents"))



* * *

Copyright (C) 2025\. All rights reserved.
