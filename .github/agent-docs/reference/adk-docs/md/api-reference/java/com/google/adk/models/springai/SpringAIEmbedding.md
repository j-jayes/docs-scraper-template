JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIEmbedding.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai](package-summary.html)
  2. [SpringAIEmbedding](SpringAIEmbedding.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SpringAIEmbedding(EmbeddingModel)
     2. SpringAIEmbedding(EmbeddingModel, String)
     3. SpringAIEmbedding(EmbeddingModel, String, SpringAIProperties.Observability)
  5. Method Details
     1. embed(String)
     2. embed(List)
     3. embedForResponse(EmbeddingRequest)
     4. dimensions()
     5. modelName()
     6. getEmbeddingModel()

Hide sidebar  Show sidebar

# Class SpringAIEmbedding

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.SpringAIEmbedding

* * *

public class SpringAIEmbedding extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Spring AI embedding model wrapper that provides ADK-compatible embedding generation. 

This wrapper allows Spring AI embedding models to be used within the ADK framework by providing reactive embedding generation with observability and error handling.

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel)`

 

`SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)`

 

`SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`int`

`dimensions()`

Get the embedding dimensions for this model.

`io.reactivex.rxjava3.core.Single<float[]>`

`embed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") text)`

Generate embeddings for a single text input.

`io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<float[]>>`

`embed([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> texts)`

Generate embeddings for multiple text inputs.

`io.reactivex.rxjava3.core.Single<org.springframework.ai.embedding.EmbeddingResponse>`

`embedForResponse(org.springframework.ai.embedding.EmbeddingRequest request)`

Generate embeddings using a full EmbeddingRequest.

`org.springframework.ai.embedding.EmbeddingModel`

`getEmbeddingModel()`

Get the underlying Spring AI embedding model.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`modelName()`

Get the model name.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### SpringAIEmbedding

public SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel)

    * ### SpringAIEmbedding

public SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)

    * ### SpringAIEmbedding

public SpringAIEmbedding(org.springframework.ai.embedding.EmbeddingModel embeddingModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)

  * ## Method Details

    * ### embed

public io.reactivex.rxjava3.core.Single<float[]> embed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") text)

Generate embeddings for a single text input.

Parameters:
    `text` \- The input text to embed
Returns:
    Single emitting the embedding vector

    * ### embed

public io.reactivex.rxjava3.core.Single<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<float[]>> embed([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> texts)

Generate embeddings for multiple text inputs.

Parameters:
    `texts` \- The input texts to embed
Returns:
    Single emitting the list of embedding vectors

    * ### embedForResponse

public io.reactivex.rxjava3.core.Single<org.springframework.ai.embedding.EmbeddingResponse> embedForResponse(org.springframework.ai.embedding.EmbeddingRequest request)

Generate embeddings using a full EmbeddingRequest.

Parameters:
    `request` \- The embedding request
Returns:
    Single emitting the embedding response

    * ### dimensions

public int dimensions()

Get the embedding dimensions for this model.

Returns:
    The number of dimensions in the embedding vectors

    * ### modelName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName()

Get the model name.

Returns:
    The model name

    * ### getEmbeddingModel

public org.springframework.ai.embedding.EmbeddingModel getEmbeddingModel()

Get the underlying Spring AI embedding model.

Returns:
    The Spring AI EmbeddingModel instance




* * *

Copyright (C) 1980\. All rights reserved.
