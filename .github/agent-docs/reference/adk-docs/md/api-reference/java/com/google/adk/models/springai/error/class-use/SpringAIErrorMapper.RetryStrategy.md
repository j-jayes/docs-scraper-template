JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../../index.html)
  * [Class](../SpringAIErrorMapper.RetryStrategy.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../../deprecated-list.html)
  * [Index](../../../../../../../index-all.html)
  * [Search](../../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai.error](../package-summary.html)
  2. [SpringAIErrorMapper](../SpringAIErrorMapper.html)
  3. [RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html)



# Uses of Enum Class  
com.google.adk.models.springai.error.SpringAIErrorMapper.RetryStrategy

Packages that use [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")

Package

Description

com.google.adk.models.springai.error

 

  * ## Uses of [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") in [com.google.adk.models.springai.error](../package-summary.html)

Subclasses with type arguments of type [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") in [com.google.adk.models.springai.error](../package-summary.html)

Modifier and Type

Class

Description

`static enum `

`[SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

Retry strategy recommendations.

Methods in [com.google.adk.models.springai.error](../package-summary.html) that return [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")

Modifier and Type

Method

Description

`[SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

SpringAIErrorMapper.MappedError.`[getRetryStrategy](../SpringAIErrorMapper.MappedError.html#getRetryStrategy\(\))()`

 

`static [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

SpringAIErrorMapper.RetryStrategy.`[valueOf](../SpringAIErrorMapper.RetryStrategy.html#valueOf\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")[]`

SpringAIErrorMapper.RetryStrategy.`[values](../SpringAIErrorMapper.RetryStrategy.html#values\(\))()`

Returns an array containing the constants of this enum class, in the order they are declared.

Methods in [com.google.adk.models.springai.error](../package-summary.html) with parameters of type [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")

Modifier and Type

Method

Description

`static long`

SpringAIErrorMapper.`[getRetryDelay](../SpringAIErrorMapper.html#getRetryDelay\(com.google.adk.models.springai.error.SpringAIErrorMapper.RetryStrategy,int\))([SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") strategy, int attempt)`

Gets the recommended delay before retrying based on the retry strategy.

Constructors in [com.google.adk.models.springai.error](../package-summary.html) with parameters of type [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")

Modifier

Constructor

Description

` `

`[MappedError](../SpringAIErrorMapper.MappedError.html#%3Cinit%3E\(com.google.adk.models.springai.error.SpringAIErrorMapper.ErrorCategory,com.google.adk.models.springai.error.SpringAIErrorMapper.RetryStrategy,java.lang.String\))([SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") normalizedMessage)`

 




* * *

Copyright (C) 1980\. All rights reserved.
