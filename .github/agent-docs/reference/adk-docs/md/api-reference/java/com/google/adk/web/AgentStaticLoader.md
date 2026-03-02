JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AgentStaticLoader.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AgentStaticLoader](AgentStaticLoader.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AgentStaticLoader(BaseAgent...)
  5. Method Details
     1. listAgents()
     2. loadAgent(String)

Hide sidebar  Show sidebar

# Class AgentStaticLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AgentStaticLoader

All Implemented Interfaces:
    `[AgentLoader](AgentLoader.html "interface in com.google.adk.web")`

* * *

public class AgentStaticLoader extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [AgentLoader](AgentLoader.html "interface in com.google.adk.web")

Static Agent Loader for programmatically provided agents. 

This loader takes a static list of pre-created agent instances and makes them available through the AgentLoader interface. Perfect for cases where you already have agent instances and just need a convenient way to wrap them in an AgentLoader. 

This class is not a Spring component by itself - instances are created programmatically and then registered as beans via factory methods.

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentStaticLoader([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")... agents)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listAgents()`

Returns a list of available agent names.

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`loadAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Loads the BaseAgent instance for the specified agent name.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentStaticLoader

public AgentStaticLoader([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")... agents)

  * ## Method Details

    * ### listAgents

@Nonnull public com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listAgents()

Description copied from interface: `[AgentLoader](AgentLoader.html#listAgents\(\))`

Returns a list of available agent names.

Specified by:
    `[listAgents](AgentLoader.html#listAgents\(\))` in interface `[AgentLoader](AgentLoader.html "interface in com.google.adk.web")`
Returns:
    ImmutableList of agent names. Must not return null - return an empty list if no agents are available.

    * ### loadAgent

public [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") loadAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Description copied from interface: `[AgentLoader](AgentLoader.html#loadAgent\(java.lang.String\))`

Loads the BaseAgent instance for the specified agent name.

Specified by:
    `[loadAgent](AgentLoader.html#loadAgent\(java.lang.String\))` in interface `[AgentLoader](AgentLoader.html "interface in com.google.adk.web")`
Parameters:
    `name` \- the name of the agent to load
Returns:
    BaseAgent instance for the given name




* * *

Copyright (C) 1980\. All rights reserved.
