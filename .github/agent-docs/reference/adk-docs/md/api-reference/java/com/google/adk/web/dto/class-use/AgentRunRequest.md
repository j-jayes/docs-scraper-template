JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../AgentRunRequest.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.dto](../package-summary.html)
  2. [AgentRunRequest](../AgentRunRequest.html)



# Uses of Class  
com.google.adk.web.dto.AgentRunRequest

Packages that use [AgentRunRequest](../AgentRunRequest.html "class in com.google.adk.web.dto")

Package

Description

com.google.adk.web.controller

 

  * ## Uses of [AgentRunRequest](../AgentRunRequest.html "class in com.google.adk.web.dto") in [com.google.adk.web.controller](../../controller/package-summary.html)

Methods in [com.google.adk.web.controller](../../controller/package-summary.html) with parameters of type [AgentRunRequest](../AgentRunRequest.html "class in com.google.adk.web.dto")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../../../events/Event.html "class in com.google.adk.events")>`

ExecutionController.`[agentRun](../../controller/ExecutionController.html#agentRun\(com.google.adk.web.dto.AgentRunRequest\))([AgentRunRequest](../AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes a non-streaming agent run for a given session and message.

`org.springframework.web.servlet.mvc.method.annotation.SseEmitter`

ExecutionController.`[agentRunSse](../../controller/ExecutionController.html#agentRunSse\(com.google.adk.web.dto.AgentRunRequest\))([AgentRunRequest](../AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes an agent run and streams the resulting events using Server-Sent Events (SSE).




* * *

Copyright (C) 1980\. All rights reserved.
