JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseArtifactService.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.artifacts](package-summary.html)
  2. [BaseArtifactService](BaseArtifactService.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. saveArtifact(String, String, String, String, Part)
     2. loadArtifact(String, String, String, String, Optional)
     3. listArtifactKeys(String, String, String)
     4. deleteArtifact(String, String, String, String)
     5. listVersions(String, String, String, String)



# Interface BaseArtifactService

All Known Implementing Classes:
    `[GcsArtifactService](GcsArtifactService.html "class in com.google.adk.artifacts")`, `[InMemoryArtifactService](InMemoryArtifactService.html "class in com.google.adk.artifacts")`

* * *

public interface BaseArtifactService

Base interface for artifact services.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

Deletes an artifact.

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists all the artifact filenames within a session.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>>`

`listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

Lists all the versions (as revision IDs) of an artifact.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)`

Gets an artifact.

`io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact.




  * ## Method Details

    * ### saveArtifact

io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename
    `artifact` \- the artifact
Returns:
    the revision ID (version) of the saved artifact.

    * ### loadArtifact

io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)

Gets an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename
    `version` \- Optional version number. If null, loads the latest version.
Returns:
    the artifact or empty if not found

    * ### listArtifactKeys

io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")> listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Lists all the artifact filenames within a session.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
Returns:
    the list artifact response containing filenames

    * ### deleteArtifact

io.reactivex.rxjava3.core.Completable deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)

Deletes an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename

    * ### listVersions

io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>> listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)

Lists all the versions (as revision IDs) of an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the artifact filename
Returns:
    A list of integer version numbers.




* * *

Copyright (C) 2025\. All rights reserved.
