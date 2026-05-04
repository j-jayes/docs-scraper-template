JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LoopAgentConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LoopAgentConfig](LoopAgentConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LoopAgentConfig()
  6. Method Details
     1. maxIterations()
     2. setMaxIterations(Integer)

Hide sidebar  Show sidebar

# Class LoopAgentConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.agents.BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

com.google.adk.agents.LoopAgentConfig

* * *

public class LoopAgentConfig extends [BaseAgentConfig](BaseAgentConfig.html "class in com.google.adk.agents")

Configuration for LoopAgent.

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

`LoopAgentConfig()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")`

`maxIterations()`

 

`void`

`setMaxIterations([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxIterations)`

 

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

    * ### LoopAgentConfig

public LoopAgentConfig()

  * ## Method Details

    * ### maxIterations

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxIterations()

    * ### setMaxIterations

public void setMaxIterations([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxIterations)




* * *

Copyright (C) 1980\. All rights reserved.
