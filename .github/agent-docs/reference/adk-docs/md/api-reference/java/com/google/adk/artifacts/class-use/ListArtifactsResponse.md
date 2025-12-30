JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ListArtifactsResponse.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.artifacts](../package-summary.html)
  2. [ListArtifactsResponse](../ListArtifactsResponse.html)



# Uses of Class  
com.google.adk.artifacts.ListArtifactsResponse

Packages that use [ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")

Package

Description

com.google.adk.artifacts

 

  * ## Uses of [ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts") in [com.google.adk.artifacts](../package-summary.html)

Methods in [com.google.adk.artifacts](../package-summary.html) that return [ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")

Modifier and Type

Method

Description

`abstract [ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")`

ListArtifactsResponse.Builder.`[build](../ListArtifactsResponse.Builder.html#build\(\))()`

 

Methods in [com.google.adk.artifacts](../package-summary.html) that return types with arguments of type [ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

BaseArtifactService.`[listArtifactKeys](../BaseArtifactService.html#listArtifactKeys\(java.lang.String,java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists all the artifact filenames within a session.

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

GcsArtifactService.`[listArtifactKeys](../GcsArtifactService.html#listArtifactKeys\(java.lang.String,java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists artifact filenames for a user and session.

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](../ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

InMemoryArtifactService.`[listArtifactKeys](../InMemoryArtifactService.html#listArtifactKeys\(java.lang.String,java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists filenames of stored artifacts for the session.




* * *

Copyright (C) 2025\. All rights reserved.
