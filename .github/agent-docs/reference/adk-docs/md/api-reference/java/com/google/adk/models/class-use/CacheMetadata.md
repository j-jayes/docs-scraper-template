JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../CacheMetadata.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](../package-summary.html)
  2. [CacheMetadata](../CacheMetadata.html)



# Uses of Class  
com.google.adk.models.CacheMetadata

Packages that use [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Package

Description

com.google.adk.events

 

com.google.adk.models

 

  * ## Uses of [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") in [com.google.adk.events](../../events/package-summary.html)

Methods in [com.google.adk.events](../../events/package-summary.html) that return types with arguments of type [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")>`

Event.`[cacheMetadata](../../events/Event.html#cacheMetadata\(\))()`

Context cache state of the LLM response this event carries.

Methods in [com.google.adk.events](../../events/package-summary.html) with parameters of type [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[Event.Builder](../../events/Event.Builder.html "class in com.google.adk.events")`

Event.Builder.`[cacheMetadata](../../events/Event.Builder.html#cacheMetadata\(com.google.adk.models.CacheMetadata\))(@Nullable [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") value)`

 

`void`

Event.`[setCacheMetadata](../../events/Event.html#setCacheMetadata\(com.google.adk.models.CacheMetadata\))(@Nullable [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") cacheMetadata)`

 

  * ## Uses of [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Methods in [com.google.adk.models](../package-summary.html) that return [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")`

CacheMetadata.Builder.`[build](../CacheMetadata.Builder.html#build\(\))()`

Builds the metadata.

Methods in [com.google.adk.models](../package-summary.html) that return types with arguments of type [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")>`

LlmRequest.`[cacheMetadata](../LlmRequest.html#cacheMetadata\(\))()`

Cache state from the agent's latest response, used to reuse or refresh the cache.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")>`

LlmResponse.`[cacheMetadata](../LlmResponse.html#cacheMetadata\(\))()`

Context cache state for this response; set only when context caching is enabled.

Methods in [com.google.adk.models](../package-summary.html) with parameters of type [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[cacheMetadata](../LlmRequest.Builder.html#cacheMetadata\(com.google.adk.models.CacheMetadata\))(@Nullable [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") cacheMetadata)`

 

`abstract [LlmResponse.Builder](../LlmResponse.Builder.html "class in com.google.adk.models")`

LlmResponse.Builder.`[cacheMetadata](../LlmResponse.Builder.html#cacheMetadata\(com.google.adk.models.CacheMetadata\))(@Nullable [CacheMetadata](../CacheMetadata.html "class in com.google.adk.models") cacheMetadata)`

 




* * *

Copyright (C) 1980\. All rights reserved.
