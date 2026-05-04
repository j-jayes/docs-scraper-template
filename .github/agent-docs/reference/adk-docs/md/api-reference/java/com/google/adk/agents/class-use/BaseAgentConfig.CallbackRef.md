JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseAgentConfig.CallbackRef.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [BaseAgentConfig](../BaseAgentConfig.html)
  3. [CallbackRef](../BaseAgentConfig.CallbackRef.html)



# Uses of Class  
com.google.adk.agents.BaseAgentConfig.CallbackRef

Packages that use [BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

BaseAgentConfig.`[afterAgentCallbacks](../BaseAgentConfig.html#afterAgentCallbacks\(\))()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

LlmAgentConfig.`[afterModelCallbacks](../LlmAgentConfig.html#afterModelCallbacks\(\))()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

LlmAgentConfig.`[afterToolCallbacks](../LlmAgentConfig.html#afterToolCallbacks\(\))()`

 

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

BaseAgentConfig.`[beforeAgentCallbacks](../BaseAgentConfig.html#beforeAgentCallbacks\(\))()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

LlmAgentConfig.`[beforeModelCallbacks](../LlmAgentConfig.html#beforeModelCallbacks\(\))()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

LlmAgentConfig.`[beforeToolCallbacks](../LlmAgentConfig.html#beforeToolCallbacks\(\))()`

 

Method parameters in [com.google.adk.agents](../package-summary.html) with type arguments of type [BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static <T> void`

ConfigAgentUtils.`[resolveAndSetCallback](../ConfigAgentUtils.html#resolveAndSetCallback\(java.util.List,java.lang.Class,java.lang.String,java.util.function.Consumer\))(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> refs, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> callbackBaseClass, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") callbackTypeName, [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "interface in java.util.function")<com.google.common.collect.ImmutableList<T>> builderSetter)`

Resolves and sets callbacks from configuration.

`void`

BaseAgentConfig.`[setAfterAgentCallbacks](../BaseAgentConfig.html#setAfterAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterAgentCallbacks)`

 

`void`

LlmAgentConfig.`[setAfterModelCallbacks](../LlmAgentConfig.html#setAfterModelCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterModelCallbacks)`

 

`void`

LlmAgentConfig.`[setAfterToolCallbacks](../LlmAgentConfig.html#setAfterToolCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterToolCallbacks)`

 

`void`

BaseAgentConfig.`[setBeforeAgentCallbacks](../BaseAgentConfig.html#setBeforeAgentCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeAgentCallbacks)`

 

`void`

LlmAgentConfig.`[setBeforeModelCallbacks](../LlmAgentConfig.html#setBeforeModelCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeModelCallbacks)`

 

`void`

LlmAgentConfig.`[setBeforeToolCallbacks](../LlmAgentConfig.html#setBeforeToolCallbacks\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](../BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeToolCallbacks)`

 




* * *

Copyright (C) 1980\. All rights reserved.
