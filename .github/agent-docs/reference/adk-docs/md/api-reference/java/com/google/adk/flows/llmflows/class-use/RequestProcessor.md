JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../RequestProcessor.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.flows.llmflows](../package-summary.html)
  2. [RequestProcessor](../RequestProcessor.html)



# Uses of Interface  
com.google.adk.flows.llmflows.RequestProcessor

Packages that use [RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")

Package

Description

com.google.adk.flows.llmflows

 

  * ## Uses of [RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") in [com.google.adk.flows.llmflows](../package-summary.html)

Classes in [com.google.adk.flows.llmflows](../package-summary.html) that implement [RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")

Modifier and Type

Class

Description

`final class `

`[AgentTransfer](../AgentTransfer.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles agent transfer for LLM flow.

`final class `

`[Basic](../Basic.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles basic information to build the LLM request.

`final class `

`[Contents](../Contents.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that populates content in request for LLM flows.

`final class `

`[Examples](../Examples.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that populates examples in LLM request.

`final class `

`[Identity](../Identity.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that gives the agent identity from the framework

`final class `

`[Instructions](../Instructions.html "class in com.google.adk.flows.llmflows")`

[`RequestProcessor`](../RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles instructions and global instructions for LLM flows.

Fields in [com.google.adk.flows.llmflows](../package-summary.html) with type parameters of type [RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")

Modifier and Type

Field

Description

`protected static final com.google.common.collect.ImmutableList<[RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")>`

SingleFlow.`[REQUEST_PROCESSORS](../SingleFlow.html#REQUEST_PROCESSORS)`

 

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[requestProcessors](../BaseLlmFlow.html#requestProcessors)`

 

Constructor parameters in [com.google.adk.flows.llmflows](../package-summary.html) with type arguments of type [RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")

Modifier

Constructor

Description

` `

`[BaseLlmFlow](../BaseLlmFlow.html#%3Cinit%3E\(java.util.List,java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](../ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors)`

 

` `

`[BaseLlmFlow](../BaseLlmFlow.html#%3Cinit%3E\(java.util.List,java.util.List,java.util.Optional\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](../ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)`

 

`protected `

`[SingleFlow](../SingleFlow.html#%3Cinit%3E\(java.util.List,java.util.List,java.util.Optional\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](../RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](../ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)`

 




* * *

Copyright (C) 2025\. All rights reserved.
