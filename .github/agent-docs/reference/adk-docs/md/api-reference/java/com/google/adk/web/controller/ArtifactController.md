JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ArtifactController.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.controller](package-summary.html)
  2. [ArtifactController](ArtifactController.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ArtifactController(BaseArtifactService)
  5. Method Details
     1. loadArtifact(String, String, String, String, Integer)
     2. loadArtifactVersion(String, String, String, String, int)
     3. listArtifactNames(String, String, String)
     4. listArtifactVersions(String, String, String, String)
     5. deleteArtifact(String, String, String, String)

Hide sidebar  Show sidebar

# Class ArtifactController

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.controller.ArtifactController

* * *

@RestController public class ArtifactController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Controller handling artifact-related API endpoints.

  * ## Constructor Summary

Constructors

Constructor

Description

`ArtifactController([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")>`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName)`

Deletes an artifact and all its versions.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`listArtifactNames([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Lists the names of all artifacts associated with a session.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`listArtifactVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName)`

Lists the available versions for a specific artifact.

`com.google.genai.types.Part`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)`

Loads the latest or a specific version of an artifact associated with a session.

`com.google.genai.types.Part`

`loadArtifactVersion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName, int versionId)`

Loads a specific version of an artifact.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ArtifactController

@Autowired public ArtifactController([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)

  * ## Method Details

    * ### loadArtifact

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}") public com.google.genai.types.Part loadArtifact(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName, @RequestParam(required=false) [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") version)

Loads the latest or a specific version of an artifact associated with a session.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
    `version` \- Optional specific version number. If null, loads the latest.
Returns:
    The artifact content as a Part object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the artifact is not found (NOT_FOUND).

    * ### loadArtifactVersion

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}/versions/{versionId}") public com.google.genai.types.Part loadArtifactVersion(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName, @PathVariable int versionId)

Loads a specific version of an artifact.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
    `versionId` \- The specific version number.
Returns:
    The artifact content as a Part object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the artifact version is not found (NOT_FOUND).

    * ### listArtifactNames

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> listArtifactNames(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Lists the names of all artifacts associated with a session.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
Returns:
    A list of artifact names.

    * ### listArtifactVersions

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}/versions") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> listArtifactVersions(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName)

Lists the available versions for a specific artifact.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
Returns:
    A list of version numbers (integers).

    * ### deleteArtifact

@DeleteMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}") public org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class in java.lang")> deleteArtifact(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") artifactName)

Deletes an artifact and all its versions.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact to delete.
Returns:
    A ResponseEntity with status NO_CONTENT on success.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if deletion fails (INTERNAL_SERVER_ERROR).




* * *

Copyright (C) 1980\. All rights reserved.
