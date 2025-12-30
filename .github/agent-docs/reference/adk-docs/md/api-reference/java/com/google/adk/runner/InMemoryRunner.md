JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemoryRunner.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.runner](package-summary.html)
  2. [InMemoryRunner](InMemoryRunner.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. InMemoryRunner(BaseAgent)
     2. InMemoryRunner(BaseAgent, String)



# Class InMemoryRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.runner.Runner](Runner.html "class in com.google.adk.runner")

com.google.adk.runner.InMemoryRunner

* * *

public class InMemoryRunner extends [Runner](Runner.html "class in com.google.adk.runner")

The class for the in-memory GenAi runner, using in-memory artifact and session services.

  * ## Constructor Summary

Constructors

Constructor

Description

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

  * ## Method Summary

### Methods inherited from class com.google.adk.runner.[Runner](Runner.html "class in com.google.adk.runner")

`[agent](Runner.html#agent\(\)), [appName](Runner.html#appName\(\)), [artifactService](Runner.html#artifactService\(\)), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\)), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\)), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\)), [runLive](Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\)), [runLive](Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\)), [runWithSessionId](Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\)), [sessionService](Runner.html#sessionService\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)




* * *

Copyright (C) 2025\. All rights reserved.
