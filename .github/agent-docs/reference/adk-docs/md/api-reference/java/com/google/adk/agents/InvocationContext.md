JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InvocationContext.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [InvocationContext](InvocationContext.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. create(BaseSessionService, BaseArtifactService, String, BaseAgent, Session, Content, RunConfig)
     2. create(BaseSessionService, BaseArtifactService, BaseAgent, Session, LiveRequestQueue, RunConfig)
     3. copyOf(InvocationContext)
     4. sessionService()
     5. artifactService()
     6. liveRequestQueue()
     7. invocationId()
     8. branch(String)
     9. branch()
     10. agent()
     11. agent(BaseAgent)
     12. session()
     13. userContent()
     14. runConfig()
     15. endInvocation()
     16. setEndInvocation(boolean)
     17. appName()
     18. userId()
     19. newInvocationContextId()
     20. incrementLlmCallsCount()
     21. equals(Object)
     22. hashCode()



# Class InvocationContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.InvocationContext

* * *

public class InvocationContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The context for an agent invocation.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`agent()`

 

`void`

`agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`appName()`

 

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`branch()`

 

`void`

`branch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

 

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`copyOf([InvocationContext](InvocationContext.html "class in com.google.adk.agents") other)`

 

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`boolean`

`endInvocation()`

 

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

 

`int`

`hashCode()`

 

`void`

`incrementLlmCallsCount()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`invocationId()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")>`

`liveRequestQueue()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`newInvocationContextId()`

 

`[RunConfig](RunConfig.html "class in com.google.adk.agents")`

`runConfig()`

 

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`session()`

 

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

 

`void`

`setEndInvocation(boolean endInvocation)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`userContent()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`userId()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### create

public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)

    * ### create

public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)

    * ### copyOf

public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") copyOf([InvocationContext](InvocationContext.html "class in com.google.adk.agents") other)

    * ### sessionService

public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

    * ### artifactService

public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

    * ### liveRequestQueue

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue()

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId()

    * ### branch

public void branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch()

    * ### agent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent()

    * ### agent

public void agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)

    * ### session

public [Session](../sessions/Session.html "class in com.google.adk.sessions") session()

    * ### userContent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent()

    * ### runConfig

public [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig()

    * ### endInvocation

public boolean endInvocation()

    * ### setEndInvocation

public void setEndInvocation(boolean endInvocation)

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName()

    * ### userId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId()

    * ### newInvocationContextId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newInvocationContextId()

    * ### incrementLlmCallsCount

public void incrementLlmCallsCount() throws [LlmCallsLimitExceededException](../exceptions/LlmCallsLimitExceededException.html "class in com.google.adk.exceptions")

Throws:
    `[LlmCallsLimitExceededException](../exceptions/LlmCallsLimitExceededException.html "class in com.google.adk.exceptions")`

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 2025\. All rights reserved.
