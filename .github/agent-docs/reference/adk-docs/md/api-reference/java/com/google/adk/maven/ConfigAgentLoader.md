JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ConfigAgentLoader.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.maven](package-summary.html)
  2. [ConfigAgentLoader](ConfigAgentLoader.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ConfigAgentLoader(String, boolean)
     2. ConfigAgentLoader(String)
  5. Method Details
     1. listAgents()
     2. loadAgent(String)
     3. stop()

Hide sidebar  Show sidebar

# Class ConfigAgentLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.maven.ConfigAgentLoader

All Implemented Interfaces:
    `[AgentLoader](../web/AgentLoader.html "interface in com.google.adk.web")`

* * *

@ThreadSafe public class ConfigAgentLoader extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [AgentLoader](../web/AgentLoader.html "interface in com.google.adk.web")

Configuration-based AgentLoader that loads agents from YAML configuration files. 

This loader monitors a configured source directory for folders containing `root_agent.yaml` files and automatically reloads agents when the files change (if hot-reloading is enabled). 

The loader treats each subdirectory with a `root_agent.yaml` file as an agent, using the folder name as the agent identifier. Agents are loaded lazily when first requested. 

Directory structure expected: 
    
    
    source-dir/
      ├── agent1/
      │   └── root_agent.yaml
      ├── agent2/
      │   └── root_agent.yaml
      └── ...
    

Hot-reloading can be disabled by setting hotReloadingEnabled to false. 

TODO: Config agent features are not yet ready for public use.

  * ## Constructor Summary

Constructors

Constructor

Description

`ConfigAgentLoader([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sourceDir)`

Creates a new ConfigAgentLoader with hot-reloading enabled.

`ConfigAgentLoader([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sourceDir, boolean hotReloadingEnabled)`

Creates a new ConfigAgentLoader.

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

`void`

`stop()`

Stops the hot-loading service.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ConfigAgentLoader

public ConfigAgentLoader([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sourceDir, boolean hotReloadingEnabled)

Creates a new ConfigAgentLoader.

Parameters:
    `sourceDir` \- The directory to scan for agent configuration files
    `hotReloadingEnabled` \- Controls whether hot-reloading is enabled

    * ### ConfigAgentLoader

public ConfigAgentLoader([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sourceDir)

Creates a new ConfigAgentLoader with hot-reloading enabled.

Parameters:
    `sourceDir` \- The directory to scan for agent configuration files

  * ## Method Details

    * ### listAgents

@Nonnull public com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listAgents()

Description copied from interface: `[AgentLoader](../web/AgentLoader.html#listAgents\(\))`

Returns a list of available agent names.

Specified by:
    `[listAgents](../web/AgentLoader.html#listAgents\(\))` in interface `[AgentLoader](../web/AgentLoader.html "interface in com.google.adk.web")`
Returns:
    ImmutableList of agent names. Must not return null - return an empty list if no agents are available.

    * ### loadAgent

public [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") loadAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Description copied from interface: `[AgentLoader](../web/AgentLoader.html#loadAgent\(java.lang.String\))`

Loads the BaseAgent instance for the specified agent name.

Specified by:
    `[loadAgent](../web/AgentLoader.html#loadAgent\(java.lang.String\))` in interface `[AgentLoader](../web/AgentLoader.html "interface in com.google.adk.web")`
Parameters:
    `name` \- the name of the agent to load
Returns:
    BaseAgent instance for the given name

    * ### stop

public void stop()

Stops the hot-loading service.




* * *

Copyright (C) 1980\. All rights reserved.
