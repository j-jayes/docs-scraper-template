JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIAutoConfiguration.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.models.springai.autoconfigure](package-summary.html)
  2. [SpringAIAutoConfiguration](SpringAIAutoConfiguration.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SpringAIAutoConfiguration()
  5. Method Details
     1. springAIWithBothModels(ChatModel, StreamingChatModel, SpringAIProperties)
     2. springAIWithChatModel(ChatModel, SpringAIProperties)
     3. springAIWithStreamingModel(StreamingChatModel, SpringAIProperties)
     4. springAIEmbedding(EmbeddingModel, SpringAIProperties)

Hide sidebar  Show sidebar

# Class SpringAIAutoConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.autoconfigure.SpringAIAutoConfiguration

* * *

@AutoConfiguration @ConditionalOnClass({[SpringAI](../SpringAI.html "class in com.google.adk.models.springai").class,org.springframework.ai.chat.model.ChatModel.class}) @ConditionalOnProperty(prefix="adk.spring-ai.auto-configuration", name="enabled", havingValue="true", matchIfMissing=true) @EnableConfigurationProperties([SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties").class) public class SpringAIAutoConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Auto-configuration for Spring AI integration with ADK. 

This auto-configuration automatically creates SpringAI beans when Spring AI ChatModel beans are available in the application context. It supports both regular ChatModel and StreamingChatModel instances. 

The auto-configuration can be disabled by setting: 
    
    
    adk.spring-ai.auto-configuration.enabled=false
    

Example usage in application.properties: 
    
    
    # OpenAI configuration
    spring.ai.openai.api-key=${OPENAI_API_KEY}
    spring.ai.openai.chat.options.model=gpt-4o-mini
    spring.ai.openai.chat.options.temperature=0.7
    
    # ADK Spring AI configuration
    adk.spring-ai.default-model=gpt-4o-mini
    adk.spring-ai.validation.enabled=true
    

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAIAutoConfiguration()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[SpringAIEmbedding](../SpringAIEmbedding.html "class in com.google.adk.models.springai")`

`springAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)`

Creates a SpringAIEmbedding bean when EmbeddingModel is available.

`[SpringAI](../SpringAI.html "class in com.google.adk.models.springai")`

`springAIWithBothModels(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)`

Creates a SpringAI bean when both ChatModel and StreamingChatModel are available.

`[SpringAI](../SpringAI.html "class in com.google.adk.models.springai")`

`springAIWithChatModel(org.springframework.ai.chat.model.ChatModel chatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)`

Creates a SpringAI bean when only ChatModel is available.

`[SpringAI](../SpringAI.html "class in com.google.adk.models.springai")`

`springAIWithStreamingModel(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)`

Creates a SpringAI bean when only StreamingChatModel is available.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SpringAIAutoConfiguration

public SpringAIAutoConfiguration()

  * ## Method Details

    * ### springAIWithBothModels

@Bean @Primary @ConditionalOnMissingBean([SpringAI](../SpringAI.html "class in com.google.adk.models.springai").class) @ConditionalOnBean({org.springframework.ai.chat.model.ChatModel.class,org.springframework.ai.chat.model.StreamingChatModel.class}) public [SpringAI](../SpringAI.html "class in com.google.adk.models.springai") springAIWithBothModels(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)

Creates a SpringAI bean when both ChatModel and StreamingChatModel are available.

Parameters:
    `chatModel` \- the Spring AI ChatModel
    `streamingChatModel` \- the Spring AI StreamingChatModel
    `properties` \- the ADK Spring AI properties
Returns:
    configured SpringAI instance

    * ### springAIWithChatModel

@Bean @ConditionalOnMissingBean([SpringAI](../SpringAI.html "class in com.google.adk.models.springai").class) @ConditionalOnBean(org.springframework.ai.chat.model.ChatModel.class) public [SpringAI](../SpringAI.html "class in com.google.adk.models.springai") springAIWithChatModel(org.springframework.ai.chat.model.ChatModel chatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)

Creates a SpringAI bean when only ChatModel is available.

Parameters:
    `chatModel` \- the Spring AI ChatModel
    `properties` \- the ADK Spring AI properties
Returns:
    configured SpringAI instance

    * ### springAIWithStreamingModel

@Bean @ConditionalOnMissingBean({[SpringAI](../SpringAI.html "class in com.google.adk.models.springai").class,org.springframework.ai.chat.model.ChatModel.class}) @ConditionalOnBean(org.springframework.ai.chat.model.StreamingChatModel.class) public [SpringAI](../SpringAI.html "class in com.google.adk.models.springai") springAIWithStreamingModel(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)

Creates a SpringAI bean when only StreamingChatModel is available.

Parameters:
    `streamingChatModel` \- the Spring AI StreamingChatModel
    `properties` \- the ADK Spring AI properties
Returns:
    configured SpringAI instance

    * ### springAIEmbedding

@Bean @ConditionalOnMissingBean([SpringAIEmbedding](../SpringAIEmbedding.html "class in com.google.adk.models.springai").class) @ConditionalOnBean(org.springframework.ai.embedding.EmbeddingModel.class) public [SpringAIEmbedding](../SpringAIEmbedding.html "class in com.google.adk.models.springai") springAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [SpringAIProperties](../properties/SpringAIProperties.html "class in com.google.adk.models.springai.properties") properties)

Creates a SpringAIEmbedding bean when EmbeddingModel is available.

Parameters:
    `embeddingModel` \- the Spring AI EmbeddingModel
    `properties` \- the ADK Spring AI properties
Returns:
    configured SpringAIEmbedding instance




* * *

Copyright (C) 1980\. All rights reserved.
