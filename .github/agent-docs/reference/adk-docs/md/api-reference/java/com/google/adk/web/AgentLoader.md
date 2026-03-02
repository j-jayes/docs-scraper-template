JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AgentLoader.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AgentLoader](AgentLoader.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. listAgents()
     2. loadAgent(String)

Hide sidebar  Show sidebar

# Interface AgentLoader

All Known Implementing Classes:
    `[AgentStaticLoader](AgentStaticLoader.html "class in com.google.adk.web"), [CompiledAgentLoader](CompiledAgentLoader.html "class in com.google.adk.web"), [ConfigAgentLoader](../maven/ConfigAgentLoader.html "class in com.google.adk.maven")`

* * *

@ThreadSafe public interface AgentLoader

Interface for loading agents to the ADK Web Server. 

Users implement this interface to register their agents with ADK Web Server. 

**Thread Safety:** Implementation must be thread-safe as it will be used as Spring singleton beans and accessed concurrently by multiple HTTP requests. 

Example usage: 
    
    
    public class MyAgentLoader implements AgentLoader {
      @Override
      public ImmutableList<String> listAgents() {
        return ImmutableList.of("chat_bot", "code_assistant");
      }
    
      @Override
      public BaseAgent loadAgent(String name) {
        switch (name) {
          case "chat_bot": return createChatBot();
          case "code_assistant": return createCodeAssistant();
          default: throw new java.util.NoSuchElementException("Agent not found: " + name);
        }
      }
    }
    

Then use with Maven plugin: 
    
    
    mvn google-adk:web -Dagents=com.acme.MyAgentLoader
    

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listAgents()`

Returns a list of available agent names.

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`loadAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Loads the BaseAgent instance for the specified agent name.




  * ## Method Details

    * ### listAgents

@Nonnull com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listAgents()

Returns a list of available agent names.

Returns:
    ImmutableList of agent names. Must not return null - return an empty list if no agents are available.

    * ### loadAgent

[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") loadAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Loads the BaseAgent instance for the specified agent name.

Parameters:
    `name` \- the name of the agent to load
Returns:
    BaseAgent instance for the given name
Throws:
    `[NoSuchElementException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "class or interface in java.util")` \- if the agent doesn't exist
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class or interface in java.lang")` \- if the agent exists but fails to load




* * *

Copyright (C) 1980\. All rights reserved.
