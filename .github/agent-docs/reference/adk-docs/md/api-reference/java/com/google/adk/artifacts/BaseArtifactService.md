JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseArtifactService.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.artifacts](package-summary.html)
  2. [BaseArtifactService](BaseArtifactService.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. saveArtifact(String, String, String, String, Part)
     2. saveArtifact(SessionKey, String, Part)
     3. saveAndReloadArtifact(String, String, String, String, Part)
     4. saveAndReloadArtifact(SessionKey, String, Part)
     5. loadArtifact(String, String, String, String)
     6. loadArtifact(SessionKey, String)
     7. loadArtifact(String, String, String, String, int)
     8. loadArtifact(SessionKey, String, int)
     9. loadArtifact(String, String, String, String, Integer)
     10. listArtifactKeys(String, String, String)
     11. listArtifactKeys(SessionKey)
     12. deleteArtifact(String, String, String, String)
     13. deleteArtifact(SessionKey, String)
     14. listVersions(String, String, String, String)
     15. listVersions(SessionKey, String)

Hide sidebar  Show sidebar

# Interface BaseArtifactService

All Known Implementing Classes:
    `[GcsArtifactService](GcsArtifactService.html "class in com.google.adk.artifacts"), [InMemoryArtifactService](InMemoryArtifactService.html "class in com.google.adk.artifacts")`

* * *

public interface BaseArtifactService

Base interface for artifact services.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Completable`

`deleteArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

 

`io.reactivex.rxjava3.core.Completable`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Deletes an artifact.

`default io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`listArtifactKeys([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey)`

 

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Lists all the artifact filenames within a session.

`default io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>>`

`listVersions([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

 

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>>`

`listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Lists all the versions (as revision IDs) of an artifact.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)`

 

`default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part>`

`saveAndReloadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and returns it with fileData if available.

`default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part>`

`saveAndReloadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and returns it with fileData if available.

`default io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`saveArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact.

`io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact.




  * ## Method Details

    * ### saveArtifact

io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename
    `artifact` \- the artifact
Returns:
    the revision ID (version) of the saved artifact.

    * ### saveArtifact

default io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> saveArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact.

    * ### saveAndReloadArtifact

default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part> saveAndReloadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact and returns it with fileData if available. 

Implementations should override this default method for efficiency, as the default performs two I/O operations (save then load).

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename
    `artifact` \- the artifact to save
Returns:
    the saved artifact with fileData if available.

    * ### saveAndReloadArtifact

default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part> saveAndReloadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact and returns it with fileData if available.

    * ### loadArtifact

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Loads the latest version of an artifact from the service.

    * ### loadArtifact

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Loads the latest version of an artifact from the service.

    * ### loadArtifact

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)

Loads a specific version of an artifact from the service.

    * ### loadArtifact

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)

    * ### loadArtifact

io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)

    * ### listArtifactKeys

io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")> listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Lists all the artifact filenames within a session.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
Returns:
    the list artifact response containing filenames

    * ### listArtifactKeys

default io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")> listArtifactKeys([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey)

    * ### deleteArtifact

io.reactivex.rxjava3.core.Completable deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Deletes an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename

    * ### deleteArtifact

default io.reactivex.rxjava3.core.Completable deleteArtifact([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

    * ### listVersions

io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>> listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Lists all the versions (as revision IDs) of an artifact.

Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the artifact filename
Returns:
    A list of integer version numbers.

    * ### listVersions

default io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>> listVersions([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)




* * *

Copyright (C) 1980\. All rights reserved.
