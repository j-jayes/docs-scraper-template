JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemoryRunner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.runner](package-summary.html)
  2. [InMemoryRunner](InMemoryRunner.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. InMemoryRunner(BaseAgent)
     2. InMemoryRunner(BaseAgent, String)
     3. InMemoryRunner(BaseAgent, String, List)

Hide sidebar  Show sidebar

# Class InMemoryRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.runner.Runner](Runner.html "class in com.google.adk.runner")

com.google.adk.runner.InMemoryRunner

* * *

public class InMemoryRunner extends [Runner](Runner.html "class in com.google.adk.runner")

The class for the in-memory GenAi runner, using in-memory artifact and session services.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Runner](Runner.html#nested-class-summary "class in com.google.adk.runner")

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

  * ## Constructor Summary

Constructors

Constructor

Description

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins)`

 

  * ## Method Summary

### Methods inherited from class [Runner](Runner.html#method-summary "class in com.google.adk.runner")

`[agent](Runner.html#agent\(\) "agent\(\)"), [appName](Runner.html#appName\(\) "appName\(\)"), [artifactService](Runner.html#artifactService\(\) "artifactService\(\)"), [builder](Runner.html#builder\(\) "builder\(\)"), [memoryService](Runner.html#memoryService\(\) "memoryService\(\)"), [pluginManager](Runner.html#pluginManager\(\) "pluginManager\(\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(Session, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(Session, Content, RunConfig, Map\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\) "runAsync\(String, String, Content\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(String, String, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(String, String, Content, RunConfig, Map\)"), [runLive](Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(Session, LiveRequestQueue, RunConfig\)"), [runLive](Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(String, String, LiveRequestQueue, RunConfig\)"), [runWithSessionId](Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runWithSessionId\(String, Content, RunConfig\)"), [sessionService](Runner.html#sessionService\(\) "sessionService\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins)




* * *

Copyright (C) 1980\. All rights reserved.
