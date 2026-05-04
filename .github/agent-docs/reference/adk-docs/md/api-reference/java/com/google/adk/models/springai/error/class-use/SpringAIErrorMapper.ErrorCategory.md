JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../../index.html)
  * [Class](../SpringAIErrorMapper.ErrorCategory.html)
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
  3. [ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html)



# Uses of Enum Class  
com.google.adk.models.springai.error.SpringAIErrorMapper.ErrorCategory

Packages that use [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")

Package

Description

com.google.adk.models.springai.error

 

  * ## Uses of [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") in [com.google.adk.models.springai.error](../package-summary.html)

Subclasses with type arguments of type [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") in [com.google.adk.models.springai.error](../package-summary.html)

Modifier and Type

Class

Description

`static enum `

`[SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

Error categories for different types of failures.

Methods in [com.google.adk.models.springai.error](../package-summary.html) that return [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")

Modifier and Type

Method

Description

`[SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

SpringAIErrorMapper.MappedError.`[getCategory](../SpringAIErrorMapper.MappedError.html#getCategory\(\))()`

 

`static [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

SpringAIErrorMapper.ErrorCategory.`[valueOf](../SpringAIErrorMapper.ErrorCategory.html#valueOf\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")[]`

SpringAIErrorMapper.ErrorCategory.`[values](../SpringAIErrorMapper.ErrorCategory.html#values\(\))()`

Returns an array containing the constants of this enum class, in the order they are declared.

Methods in [com.google.adk.models.springai.error](../package-summary.html) with parameters of type [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")

Modifier and Type

Method

Description

`static boolean`

SpringAIErrorMapper.`[isRetryable](../SpringAIErrorMapper.html#isRetryable\(com.google.adk.models.springai.error.SpringAIErrorMapper.ErrorCategory\))([SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category)`

Determines if an error is retryable based on its category.

Constructors in [com.google.adk.models.springai.error](../package-summary.html) with parameters of type [SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")

Modifier

Constructor

Description

` `

`[MappedError](../SpringAIErrorMapper.MappedError.html#%3Cinit%3E\(com.google.adk.models.springai.error.SpringAIErrorMapper.ErrorCategory,com.google.adk.models.springai.error.SpringAIErrorMapper.RetryStrategy,java.lang.String\))([SpringAIErrorMapper.ErrorCategory](../SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](../SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") normalizedMessage)`

 




* * *

Copyright (C) 1980\. All rights reserved.
