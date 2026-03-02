JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../../index.html)
  * [Class](../SpringAIObservabilityHandler.RequestContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../../deprecated-list.html)
  * [Index](../../../../../../../index-all.html)
  * [Search](../../../../../../../search.html)



  1. [com.google.adk.models.springai.observability](../package-summary.html)
  2. [SpringAIObservabilityHandler](../SpringAIObservabilityHandler.html)
  3. [RequestContext](../SpringAIObservabilityHandler.RequestContext.html)



# Uses of Class  
com.google.adk.models.springai.observability.SpringAIObservabilityHandler.RequestContext

Packages that use [SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")

Package

Description

com.google.adk.models.springai.observability

 

  * ## Uses of [SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") in [com.google.adk.models.springai.observability](../package-summary.html)

Methods in [com.google.adk.models.springai.observability](../package-summary.html) that return [SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")

Modifier and Type

Method

Description

`[SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")`

SpringAIObservabilityHandler.`[startRequest](../SpringAIObservabilityHandler.html#startRequest\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") requestType)`

Records the start of a request.

Methods in [com.google.adk.models.springai.observability](../package-summary.html) with parameters of type [SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")

Modifier and Type

Method

Description

`void`

SpringAIObservabilityHandler.`[recordError](../SpringAIObservabilityHandler.html#recordError\(com.google.adk.models.springai.observability.SpringAIObservabilityHandler.RequestContext,java.lang.Throwable\))([SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Records a failed request.

`void`

SpringAIObservabilityHandler.`[recordSuccess](../SpringAIObservabilityHandler.html#recordSuccess\(com.google.adk.models.springai.observability.SpringAIObservabilityHandler.RequestContext,int,int,int\))([SpringAIObservabilityHandler.RequestContext](../SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, int tokenCount, int inputTokens, int outputTokens)`

Records the completion of a successful request.




* * *

Copyright (C) 1980\. All rights reserved.
