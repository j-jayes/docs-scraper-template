JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ExecutionController.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.controller](package-summary.html)
  2. [ExecutionController](ExecutionController.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ExecutionController(RunnerService)
  5. Method Details
     1. agentRun(AgentRunRequest)
     2. agentRunSse(AgentRunRequest)

Hide sidebar  Show sidebar

# Class ExecutionController

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.controller.ExecutionController

* * *

@RestController public class ExecutionController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Controller handling agent execution endpoints.

  * ## Constructor Summary

Constructors

Constructor

Description

`ExecutionController([RunnerService](../service/RunnerService.html "class in com.google.adk.web.service") runnerService)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`agentRun([AgentRunRequest](../dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes a non-streaming agent run for a given session and message.

`org.springframework.web.servlet.mvc.method.annotation.SseEmitter`

`agentRunSse([AgentRunRequest](../dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)`

Executes an agent run and streams the resulting events using Server-Sent Events (SSE).

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ExecutionController

@Autowired public ExecutionController([RunnerService](../service/RunnerService.html "class in com.google.adk.web.service") runnerService)

  * ## Method Details

    * ### agentRun

@PostMapping("/run") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> agentRun(@RequestBody [AgentRunRequest](../dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)

Executes a non-streaming agent run for a given session and message.

Parameters:
    `request` \- The AgentRunRequest containing run details.
Returns:
    A list of events generated during the run.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the session is not found or the run fails.

    * ### agentRunSse

@PostMapping(value="/run_sse", produces="text/event-stream") public org.springframework.web.servlet.mvc.method.annotation.SseEmitter agentRunSse(@RequestBody [AgentRunRequest](../dto/AgentRunRequest.html "class in com.google.adk.web.dto") request)

Executes an agent run and streams the resulting events using Server-Sent Events (SSE).

Parameters:
    `request` \- The AgentRunRequest containing run details.
Returns:
    A Flux that will stream events to the client.




* * *

Copyright (C) 1980\. All rights reserved.
