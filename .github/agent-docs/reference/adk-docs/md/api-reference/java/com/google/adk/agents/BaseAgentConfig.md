JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseAgentConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [BaseAgentConfig](BaseAgentConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. BaseAgentConfig()
     2. BaseAgentConfig(String)
     3. BaseAgentConfig(String, String, String)
  6. Method Details
     1. name()
     2. setName(String)
     3. description()
     4. setDescription(String)
     5. setAgentClass(String)
     6. agentClass()
     7. subAgents()
     8. setSubAgents(List)
     9. beforeAgentCallbacks()
     10. setBeforeAgentCallbacks(List)
     11. afterAgentCallbacks()
     12. setAfterAgentCallbacks(List)

Hide sidebar  Show sidebar

# Class BaseAgentConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.BaseAgentConfig

Direct Known Subclasses:
    `[LlmAgentConfig](LlmAgentConfig.html "class in com.google.adk.agents"), [LoopAgentConfig](LoopAgentConfig.html "class in com.google.adk.agents"), [ParallelAgentConfig](ParallelAgentConfig.html "class in com.google.adk.agents"), [SequentialAgentConfig](SequentialAgentConfig.html "class in com.google.adk.agents")`

* * *

public class BaseAgentConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Base configuration for all agents with subagent support. 

TODO: Config agent features are not yet ready for public use.

  * ## Nested Class Summary

Nested Classes

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

`BaseAgentConfig()`

 

`BaseAgentConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)`

 

`BaseAgentConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)`

Constructor with basic fields.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`afterAgentCallbacks()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`agentClass()`

 

`com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")>`

`beforeAgentCallbacks()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`description()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

 

`void`

`setAfterAgentCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterAgentCallbacks)`

 

`void`

`setAgentClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)`

 

`void`

`setBeforeAgentCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeAgentCallbacks)`

 

`void`

`setDescription([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`void`

`setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`void`

`setSubAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgents)`

 

`com.google.common.collect.ImmutableList<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")>`

`subAgents()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### BaseAgentConfig

public BaseAgentConfig()

    * ### BaseAgentConfig

public BaseAgentConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)

    * ### BaseAgentConfig

public BaseAgentConfig([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)

Constructor with basic fields.

Parameters:
    `name` \- The agent name
    `description` \- The agent description
    `agentClass` \- The agent class name

  * ## Method Details

    * ### name

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

    * ### setName

public void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### description

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description()

    * ### setDescription

public void setDescription([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

    * ### setAgentClass

public void setAgentClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass)

    * ### agentClass

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClass()

    * ### subAgents

public com.google.common.collect.ImmutableList<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgents()

    * ### setSubAgents

public void setSubAgents([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.AgentRefConfig](BaseAgentConfig.AgentRefConfig.html "class in com.google.adk.agents")> subAgents)

    * ### beforeAgentCallbacks

public com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeAgentCallbacks()

    * ### setBeforeAgentCallbacks

public void setBeforeAgentCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> beforeAgentCallbacks)

    * ### afterAgentCallbacks

public com.google.common.collect.ImmutableList<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterAgentCallbacks()

    * ### setAfterAgentCallbacks

public void setAfterAgentCallbacks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BaseAgentConfig.CallbackRef](BaseAgentConfig.CallbackRef.html "class in com.google.adk.agents")> afterAgentCallbacks)




* * *

Copyright (C) 1980\. All rights reserved.
