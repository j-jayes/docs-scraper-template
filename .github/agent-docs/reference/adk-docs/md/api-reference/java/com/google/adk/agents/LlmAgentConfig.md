JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgentConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgentConfig](LlmAgentConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BaseAgentConfig
     2. Methods inherited from class Object
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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

com.google.adk.agents.LlmAgentConfig

* * *

public class LlmAgentConfig extends [BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

Configuration for LlmAgent. 

TODO: Config agent features are not yet ready for public use.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseAgentConfig](BaseAgentConfig.html#nested-class-summary "class in com.google.adk.agents")

`[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents"), [BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")`

Modifier and Type

Class

Description

`static class `

`[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")`

Configuration for referencing other agents (subagents).

`static class `

`[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")`

Reference to a callback stored in the ComponentRegistry.

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

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`afterModelCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`afterToolCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`beforeModelCallbacks()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`beforeToolCallbacks()`

 

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`disallowTransferToParent()`

 

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`disallowTransferToPeers()`

 

`com.google.genai.types.GenerateContentConfig`

`generateContentConfig()`

 

`[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")`

`includeContents()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`instruction()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`outputKey()`

 

`void`

`setAfterModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks)`

 

`void`

`setAfterToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks)`

 

`void`

`setBeforeModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks)`

 

`void`

`setBeforeToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks)`

 

`void`

`setDisallowTransferToParent([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToParent)`

 

`void`

`setDisallowTransferToPeers([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToPeers)`

 

`void`

`setGenerateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)`

 

`void`

`setIncludeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)`

 

`void`

`setInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instruction)`

 

`void`

`setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)`

 

`void`

`setOutputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") outputKey)`

 

`void`

`setTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools)`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")>`

`tools()`

 

### Methods inherited from class [BaseAgentConfig](BaseAgentConfig.html#method-summary "class in com.google.adk.agents")

`[afterAgentCallbacks](BaseAgentConfig.html#afterAgentCallbacks\(\) "afterAgentCallbacks\(\)"), [agentClass](BaseAgentConfig.html#agentClass\(\) "agentClass\(\)"), [beforeAgentCallbacks](BaseAgentConfig.html#beforeAgentCallbacks\(\) "beforeAgentCallbacks\(\)"), [description](BaseAgentConfig.html#description\(\) "description\(\)"), [name](BaseAgentConfig.html#name\(\) "name\(\)"), [setAfterAgentCallbacks](BaseAgentConfig.html#setAfterAgentCallbacks\(java.util.List\) "setAfterAgentCallbacks\(List\)"), [setAgentClass](BaseAgentConfig.html#setAgentClass\(java.lang.String\) "setAgentClass\(String\)"), [setBeforeAgentCallbacks](BaseAgentConfig.html#setBeforeAgentCallbacks\(java.util.List\) "setBeforeAgentCallbacks\(List\)"), [setDescription](BaseAgentConfig.html#setDescription\(java.lang.String\) "setDescription\(String\)"), [setName](BaseAgentConfig.html#setName\(java.lang.String\) "setName\(String\)"), [setSubAgents](BaseAgentConfig.html#setSubAgents\(java.util.List\) "setSubAgents\(List\)"), [subAgents](BaseAgentConfig.html#subAgents\(\) "subAgents\(\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`[afterAgentCallbacks](BaseAgentConfig.html#afterAgentCallbacks\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[agentClass](BaseAgentConfig.html#agentClass\(\))()`

 

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`[beforeAgentCallbacks](BaseAgentConfig.html#beforeAgentCallbacks\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](BaseAgentConfig.html#description\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BaseAgentConfig.html#name\(\))()`

 

`void`

`[setAfterAgentCallbacks](BaseAgentConfig.html#setAfterAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterAgentCallbacks)`

 

`void`

`[setAgentClass](BaseAgentConfig.html#setAgentClass\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)`

 

`void`

`[setBeforeAgentCallbacks](BaseAgentConfig.html#setBeforeAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeAgentCallbacks)`

 

`void`

`[setDescription](BaseAgentConfig.html#setDescription\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`void`

`[setName](BaseAgentConfig.html#setName\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`void`

`[setSubAgents](BaseAgentConfig.html#setSubAgents\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgents)`

 

`com.google.common.collect.ImmutableList<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")>`

`[subAgents](BaseAgentConfig.html#subAgents\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### LlmAgentConfig

public LlmAgentConfig()

  * ## Method Details

    * ### model

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model()

    * ### setModel

public void setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model)

    * ### instruction

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instruction()

    * ### setInstruction

public void setInstruction([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instruction)

    * ### disallowTransferToParent

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToParent()

    * ### setDisallowTransferToParent

public void setDisallowTransferToParent([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToParent)

    * ### disallowTransferToPeers

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToPeers()

    * ### setDisallowTransferToPeers

public void setDisallowTransferToPeers([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") disallowTransferToPeers)

    * ### outputKey

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") outputKey()

    * ### setOutputKey

public void setOutputKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") outputKey)

    * ### tools

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools()

    * ### setTools

public void setTools([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")> tools)

    * ### includeContents

public [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents()

    * ### setIncludeContents

public void setIncludeContents([LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") includeContents)

    * ### generateContentConfig

public com.google.genai.types.GenerateContentConfig generateContentConfig()

    * ### setGenerateContentConfig

public void setGenerateContentConfig(com.google.genai.types.GenerateContentConfig generateContentConfig)

    * ### beforeModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks()

    * ### setBeforeModelCallbacks

public void setBeforeModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks)

    * ### afterModelCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks()

    * ### setAfterModelCallbacks

public void setAfterModelCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks)

    * ### beforeToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks()

    * ### setBeforeToolCallbacks

public void setBeforeToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks)

    * ### afterToolCallbacks

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks()

    * ### setAfterToolCallbacks

public void setAfterToolCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks)




* * *

Copyright (C) 1980\. All rights reserved.
