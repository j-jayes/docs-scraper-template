JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgentConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgentConfig](LlmAgentConfig.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LlmAgentConfig()
  6. Method Details
     1. model()
     2. setModel(String)
     3. instruction()
     4. setInstruction(String)
     5. disallowTransferToParent()
     6. setDisallowTransferToParent(Boolean)
     7. disallowTransferToPeers()
     8. setDisallowTransferToPeers(Boolean)
     9. outputKey()
     10. setOutputKey(String)
     11. tools()
     12. setTools(List)
     13. includeContents()
     14. setIncludeContents(LlmAgent.IncludeContents)
     15. generateContentConfig()
     16. setGenerateContentConfig(GenerateContentConfig)
     17. beforeModelCallbacks()
     18. setBeforeModelCallbacks(List)
     19. afterModelCallbacks()
     20. setAfterModelCallbacks(List)
     21. beforeToolCallbacks()
     22. setBeforeToolCallbacks(List)
     23. afterToolCallbacks()
     24. setAfterToolCallbacks(List)

Hide sidebar  Show sidebar

# Class LlmAgentConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

com.google.adk.agents.LlmAgentConfig

* * *

public class LlmAgentConfig extends [BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

Configuration for LlmAgent. 

TODO: Config agent features are not yet ready for public use.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseAgentConfig](BaseAgentConfig.html#nested-class-summary "class in com.google.adk.agents")

`[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents"), [BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")`

  * ## Constructor Summary

Constructors

Constructor

Description

`LlmAgentConfig()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`afterModelCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`afterToolCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`beforeModelCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`beforeToolCallbacks()`

 

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")`

`disallowTransferToParent()`

 

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")`

`disallowTransferToPeers()`

 

`com.google.genai.types.GenerateContentConfig`

`generateContentConfig()`

 

`[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")`

`includeContents()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`instruction()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`model()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`outputKey()`

 

`void`

`setAfterModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks)`

 

`void`

`setAfterToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks)`

 

`void`

`setBeforeModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks)`

 

`void`

`setBeforeToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks)`

 

`void`

`setDisallowTransferToParent([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToParent)`

 

`void`

`setDisallowTransferToPeers([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToPeers)`

 

`void`

`setGenerateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)`

 

`void`

`setIncludeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)`

 

`void`

`setInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)`

 

`void`

`setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

`void`

`setOutputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey)`

 

`void`

`setTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools)`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")>`

`tools()`

 

### Methods inherited from class [BaseAgentConfig](BaseAgentConfig.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallbacks](BaseAgentConfig.html#afterAgentCallbacks\(\) "afterAgentCallbacks\(\)"), [agentClass](BaseAgentConfig.html#agentClass\(\) "agentClass\(\)"), [beforeAgentCallbacks](BaseAgentConfig.html#beforeAgentCallbacks\(\) "beforeAgentCallbacks\(\)"), [description](BaseAgentConfig.html#description\(\) "description\(\)"), [name](BaseAgentConfig.html#name\(\) "name\(\)"), [setAfterAgentCallbacks](BaseAgentConfig.html#setAfterAgentCallbacks\(java.util.List\) "setAfterAgentCallbacks\(List\)"), [setAgentClass](BaseAgentConfig.html#setAgentClass\(java.lang.String\) "setAgentClass\(String\)"), [setBeforeAgentCallbacks](BaseAgentConfig.html#setBeforeAgentCallbacks\(java.util.List\) "setBeforeAgentCallbacks\(List\)"), [setDescription](BaseAgentConfig.html#setDescription\(java.lang.String\) "setDescription\(String\)"), [setName](BaseAgentConfig.html#setName\(java.lang.String\) "setName\(String\)"), [setSubAgents](BaseAgentConfig.html#setSubAgents\(java.util.List\) "setSubAgents\(List\)"), [subAgents](BaseAgentConfig.html#subAgents\(\) "subAgents\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LlmAgentConfig

public LlmAgentConfig()

  * ## Method Details

    * ### model

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model()

    * ### setModel

public void setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)

    * ### instruction

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction()

    * ### setInstruction

public void setInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)

    * ### disallowTransferToParent

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToParent()

    * ### setDisallowTransferToParent

public void setDisallowTransferToParent([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToParent)

    * ### disallowTransferToPeers

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToPeers()

    * ### setDisallowTransferToPeers

public void setDisallowTransferToPeers([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") disallowTransferToPeers)

    * ### outputKey

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey()

    * ### setOutputKey

public void setOutputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") outputKey)

    * ### tools

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools()

    * ### setTools

public void setTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools)

    * ### includeContents

public [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents()

    * ### setIncludeContents

public void setIncludeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)

    * ### generateContentConfig

public com.google.genai.types.GenerateContentConfig generateContentConfig()

    * ### setGenerateContentConfig

public void setGenerateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)

    * ### beforeModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks()

    * ### setBeforeModelCallbacks

public void setBeforeModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks)

    * ### afterModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks()

    * ### setAfterModelCallbacks

public void setAfterModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks)

    * ### beforeToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks()

    * ### setBeforeToolCallbacks

public void setBeforeToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks)

    * ### afterToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks()

    * ### setAfterToolCallbacks

public void setAfterToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks)




* * *

Copyright (C) 1980\. All rights reserved.
