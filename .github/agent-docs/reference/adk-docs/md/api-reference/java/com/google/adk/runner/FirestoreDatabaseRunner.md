JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FirestoreDatabaseRunner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.runner](package-summary.html)
  2. [FirestoreDatabaseRunner](FirestoreDatabaseRunner.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. FirestoreDatabaseRunner(BaseAgent, Firestore)
     2. FirestoreDatabaseRunner(BaseAgent, String, Firestore)
     3. FirestoreDatabaseRunner(BaseAgent, String, List, Firestore)

Hide sidebar  Show sidebar

# Class FirestoreDatabaseRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.runner.Runner](Runner.html "class in com.google.adk.runner")

com.google.adk.runner.FirestoreDatabaseRunner

* * *

public class FirestoreDatabaseRunner extends [Runner](Runner.html "class in com.google.adk.runner")

FirestoreDatabaseRunner

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Runner](Runner.html#nested-class-summary "class in com.google.adk.runner")

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

  * ## Constructor Summary

Constructors

Constructor

Description

`FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner

`FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner with appName

`FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner with parent runners

  * ## Method Summary

### Methods inherited from class [Runner](Runner.html#method-summary "class in com.google.adk.runner")

`[agent](Runner.html#agent\(\) "agent\(\)"), [appName](Runner.html#appName\(\) "appName\(\)"), [artifactService](Runner.html#artifactService\(\) "artifactService\(\)"), [builder](Runner.html#builder\(\) "builder\(\)"), [close](Runner.html#close\(\) "close\(\)"), [memoryService](Runner.html#memoryService\(\) "memoryService\(\)"), [pluginManager](Runner.html#pluginManager\(\) "pluginManager\(\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content\) "runAsync\(SessionKey, Content\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(SessionKey, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(SessionKey, Content, RunConfig, Map\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(Session, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(Session, Content, RunConfig, Map\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\) "runAsync\(String, String, Content\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(String, String, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(String, String, Content, RunConfig, Map\)"), [runAsyncImpl](Runner.html#runAsyncImpl\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsyncImpl\(Session, Content, RunConfig, Map\)"), [runLive](Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(SessionKey, LiveRequestQueue, RunConfig\)"), [runLive](Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(Session, LiveRequestQueue, RunConfig\)"), [runLive](Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(String, String, LiveRequestQueue, RunConfig\)"), [runWithSessionId](Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runWithSessionId\(String, Content, RunConfig\)"), [sessionService](Runner.html#sessionService\(\) "sessionService\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### FirestoreDatabaseRunner

public FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, com.google.cloud.firestore.Firestore firestore)

Constructor for FirestoreDatabaseRunner

    * ### FirestoreDatabaseRunner

public FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, com.google.cloud.firestore.Firestore firestore)

Constructor for FirestoreDatabaseRunner with appName

    * ### FirestoreDatabaseRunner

public FirestoreDatabaseRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins, com.google.cloud.firestore.Firestore firestore)

Constructor for FirestoreDatabaseRunner with parent runners




* * *

Copyright (C) 1980\. All rights reserved.
