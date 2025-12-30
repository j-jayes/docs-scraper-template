JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseLlm.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models](../package-summary.html)
  2. [BaseLlm](../BaseLlm.html)



# Uses of Class  
com.google.adk.models.BaseLlm

Packages that use [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Package

Description

com.google.adk.agents

 

com.google.adk.models

 

com.google.adk.models.langchain4j

 

  * ## Uses of [BaseLlm](../BaseLlm.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[LlmAgent.Builder](../../agents/LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[model](../../agents/LlmAgent.Builder.html#model\(com.google.adk.models.BaseLlm\))([BaseLlm](../BaseLlm.html "class in com.google.adk.models") model)`

 

  * ## Uses of [BaseLlm](../BaseLlm.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Subclasses of [BaseLlm](../BaseLlm.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[Claude](../Claude.html "class in com.google.adk.models")`

Represents the Claude Generative AI model by Anthropic.

`class `

`[Gemini](../Gemini.html "class in com.google.adk.models")`

Represents the Gemini Generative AI model.

Methods in [com.google.adk.models](../package-summary.html) that return [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[BaseLlm](../BaseLlm.html "class in com.google.adk.models")`

LlmRegistry.LlmFactory.`[create](../LlmRegistry.LlmFactory.html#create\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`static [BaseLlm](../BaseLlm.html "class in com.google.adk.models")`

LlmRegistry.`[getLlm](../LlmRegistry.html#getLlm\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

Returns an LLM instance for the given model name, using a cached or new factory-created instance.

Methods in [com.google.adk.models](../package-summary.html) that return types with arguments of type [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[BaseLlm](../BaseLlm.html "class in com.google.adk.models")>`

Model.`[model](../Model.html#model\(\))()`

 

Methods in [com.google.adk.models](../package-summary.html) with parameters of type [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [Model.Builder](../Model.Builder.html "class in com.google.adk.models")`

Model.Builder.`[model](../Model.Builder.html#model\(com.google.adk.models.BaseLlm\))([BaseLlm](../BaseLlm.html "class in com.google.adk.models") model)`

 

  * ## Uses of [BaseLlm](../BaseLlm.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Subclasses of [BaseLlm](../BaseLlm.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Modifier and Type

Class

Description

`class `

`[LangChain4j](../langchain4j/LangChain4j.html "class in com.google.adk.models.langchain4j")`

 




* * *

Copyright (C) 2025\. All rights reserved.
