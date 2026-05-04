JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GcsArtifactService.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.artifacts](package-summary.html)
  2. [GcsArtifactService](GcsArtifactService.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. GcsArtifactService(String, Storage)
  5. Method Details
     1. saveArtifact(String, String, String, String, Part)
     2. loadArtifact(String, String, String, String, Integer)
     3. listArtifactKeys(String, String, String)
     4. deleteArtifact(String, String, String, String)
     5. listVersions(String, String, String, String)
     6. saveAndReloadArtifact(String, String, String, String, Part)

Hide sidebar  Show sidebar

# Class GcsArtifactService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.artifacts.GcsArtifactService

All Implemented Interfaces:
    `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`

* * *

public final class GcsArtifactService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")

An artifact service implementation using Google Cloud Storage (GCS).

  * ## Constructor Summary

Constructors

Constructor

Description

`GcsArtifactService([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") bucketName, com.google.cloud.storage.Storage storageClient)`

Initializes the GcsArtifactService.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Deletes all versions of the specified artifact from GCS.

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Lists artifact filenames for a user and session.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>>`

`listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Lists all available versions for a given artifact.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)`

Loads an artifact from GCS.

`io.reactivex.rxjava3.core.Single<com.google.genai.types.Part>`

`saveAndReloadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and returns it with fileData if available.

`io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact to GCS and assigns a new version.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [BaseArtifactService](BaseArtifactService.html#method-summary "interface in com.google.adk.artifacts")

`[deleteArtifact](BaseArtifactService.html#deleteArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\) "deleteArtifact\(SessionKey, String\)"), [listArtifactKeys](BaseArtifactService.html#listArtifactKeys\(com.google.adk.sessions.SessionKey\) "listArtifactKeys\(SessionKey\)"), [listVersions](BaseArtifactService.html#listVersions\(com.google.adk.sessions.SessionKey,java.lang.String\) "listVersions\(SessionKey, String\)"), [loadArtifact](BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\) "loadArtifact\(SessionKey, String\)"), [loadArtifact](BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,int\) "loadArtifact\(SessionKey, String, int\)"), [loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String\) "loadArtifact\(String, String, String, String\)"), [loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,int\) "loadArtifact\(String, String, String, String, int\)"), [saveAndReloadArtifact](BaseArtifactService.html#saveAndReloadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\) "saveAndReloadArtifact\(SessionKey, String, Part\)"), [saveArtifact](BaseArtifactService.html#saveArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\) "saveArtifact\(SessionKey, String, Part\)")`

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Completable`

`[deleteArtifact](BaseArtifactService.html#deleteArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

 

`default io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`[listArtifactKeys](BaseArtifactService.html#listArtifactKeys\(com.google.adk.sessions.SessionKey\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey)`

 

`default io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>>`

`[listVersions](BaseArtifactService.html#listVersions\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,int\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)`

Loads the latest version of an artifact from the service.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`[loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,int\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, int version)`

Loads a specific version of an artifact from the service.

`default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part>`

`[saveAndReloadArtifact](BaseArtifactService.html#saveAndReloadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and returns it with fileData if available.

`default io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`[saveArtifact](BaseArtifactService.html#saveArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact.




  * ## Constructor Details

    * ### GcsArtifactService

public GcsArtifactService([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") bucketName, com.google.cloud.storage.Storage storageClient)

Initializes the GcsArtifactService.

Parameters:
    `bucketName` \- The name of the GCS bucket to use.
    `storageClient` \- The GCS storage client instance.

  * ## Method Details

    * ### saveArtifact

public io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Saves an artifact to GCS and assigns a new version.

Specified by:
    `[saveArtifact](BaseArtifactService.html#saveArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.google.genai.types.Part\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `filename` \- Artifact filename.
    `artifact` \- Artifact content to save.
Returns:
    Single with assigned version number.

    * ### loadArtifact

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)

Loads an artifact from GCS.

Specified by:
    `[loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.Integer\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `filename` \- Artifact filename.
    `version` \- Optional version to load. Loads latest if empty.
Returns:
    Maybe with loaded artifact, or empty if not found.

    * ### listArtifactKeys

public io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")> listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Lists artifact filenames for a user and session.

Specified by:
    `[listArtifactKeys](BaseArtifactService.html#listArtifactKeys\(java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
Returns:
    Single with sorted list of artifact filenames.

    * ### deleteArtifact

public io.reactivex.rxjava3.core.Completable deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Deletes all versions of the specified artifact from GCS.

Specified by:
    `[deleteArtifact](BaseArtifactService.html#deleteArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `filename` \- Artifact filename.
Returns:
    Completable indicating operation completion.

    * ### listVersions

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>> listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename)

Lists all available versions for a given artifact.

Specified by:
    `[listVersions](BaseArtifactService.html#listVersions\(java.lang.String,java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `filename` \- Artifact filename.
Returns:
    Single with sorted list of version numbers.

    * ### saveAndReloadArtifact

public io.reactivex.rxjava3.core.Single<com.google.genai.types.Part> saveAndReloadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") filename, com.google.genai.types.Part artifact)

Description copied from interface: `[BaseArtifactService](BaseArtifactService.html#saveAndReloadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.google.genai.types.Part\))`

Saves an artifact and returns it with fileData if available. 

Implementations should override this default method for efficiency, as the default performs two I/O operations (save then load).

Specified by:
    `[saveAndReloadArtifact](BaseArtifactService.html#saveAndReloadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,com.google.genai.types.Part\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- the app name
    `userId` \- the user ID
    `sessionId` \- the session ID
    `filename` \- the filename
    `artifact` \- the artifact to save
Returns:
    the saved artifact with fileData if available.




* * *

Copyright (C) 1980\. All rights reserved.
