JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GcsArtifactService.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.artifacts](package-summary.html)
  2. [GcsArtifactService](GcsArtifactService.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. GcsArtifactService(String, Storage)
  5. Method Details
     1. saveArtifact(String, String, String, String, Part)
     2. loadArtifact(String, String, String, String, Optional)
     3. listArtifactKeys(String, String, String)
     4. deleteArtifact(String, String, String, String)
     5. listVersions(String, String, String, String)



# Class GcsArtifactService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.artifacts.GcsArtifactService

All Implemented Interfaces:
    `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`

* * *

public final class GcsArtifactService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")

An artifact service implementation using Google Cloud Storage (GCS).

  * ## Constructor Summary

Constructors

Constructor

Description

`GcsArtifactService([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") bucketName, com.google.cloud.storage.Storage storageClient)`

Initializes the GcsArtifactService.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

Deletes all versions of the specified artifact from GCS.

`io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

`listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists artifact filenames for a user and session.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>>`

`listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

Lists all available versions for a given artifact.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)`

Loads an artifact from GCS.

`io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

`saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact to GCS and assigns a new version.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### GcsArtifactService

public GcsArtifactService([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") bucketName, com.google.cloud.storage.Storage storageClient)

Initializes the GcsArtifactService.

Parameters:
    `bucketName` \- The name of the GCS bucket to use.
    `storageClient` \- The GCS storage client instance.

  * ## Method Details

    * ### saveArtifact

public io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> saveArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)

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

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part> loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> version)

Loads an artifact from GCS.

Specified by:
    `[loadArtifact](BaseArtifactService.html#loadArtifact\(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.util.Optional\))` in interface `[BaseArtifactService](BaseArtifactService.html "interface in com.google.adk.artifacts")`
Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `filename` \- Artifact filename.
    `version` \- Optional version to load. Loads latest if empty.
Returns:
    Maybe with loaded artifact, or empty if not found.

    * ### listArtifactKeys

public io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](ListArtifactsResponse.html "class in com.google.adk.artifacts")> listArtifactKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

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

public io.reactivex.rxjava3.core.Completable deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)

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

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>> listVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)

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




* * *

Copyright (C) 2025\. All rights reserved.
