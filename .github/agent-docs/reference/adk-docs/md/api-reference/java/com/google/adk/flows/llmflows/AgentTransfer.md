JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentTransfer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [AgentTransfer](AgentTransfer.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AgentTransfer()
  6. Method Details
     1. processRequest(InvocationContext, LlmRequest)
     2. transferToAgent(String, ToolContext)
     3. legacyTransferToAgent(String, ToolContext)

Hide sidebar  Show sidebar

# Class AgentTransfer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.AgentTransfer

All Implemented Interfaces:
    `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public final class AgentTransfer extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")

[`RequestProcessor`](RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles agent transfer for LLM flow.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [RequestProcessor](RequestProcessor.html#nested-class-summary "interface in com.google.adk.flows.llmflows")

`[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentTransfer()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`legacyTransferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Backwards compatible transferToAgent that uses camel-case naming instead of the ADK's snake_case convention.

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

`static void`

`transferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentTransfer

public AgentTransfer()

  * ## Method Details

    * ### processRequest

public io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")> processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)

Description copied from interface: `[RequestProcessor](RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))`

Process the LLM request as part of the pre-processing stage.

Specified by:
    `[processRequest](RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))` in interface `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`
Parameters:
    `context` \- the invocation context.
    `request` \- the LLM request to process.
Returns:
    a list of events generated during processing (if any).

    * ### transferToAgent

public static void transferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

    * ### legacyTransferToAgent

public static void legacyTransferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Backwards compatible transferToAgent that uses camel-case naming instead of the ADK's snake_case convention. 

It exists only to support users who already use literal "transferToAgent" function call to instruct ADK to transfer the question to another agent.




* * *

Copyright (C) 1980\. All rights reserved.
