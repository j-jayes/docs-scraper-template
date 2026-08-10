toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

commonJvmAndroid

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.artifacts](../index.html)/FileArtifactService

# FileArtifactService

commonJvmAndroid

class [FileArtifactService](index.html)(baseDir: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)) : [ArtifactService](../-artifact-service/index.html)

An [ArtifactService](../-artifact-service/index.html) that persists artifacts on the local filesystem.

The on-disk layout mirrors the other ADK file-backed artifact services so the same directory can be opened interchangeably across language ports. Each artifact version is a directory holding the raw payload (named after the artifact's basename) plus a `metadata.json` sidecar:
    
    
    <baseDir>/users/<userId>/sessions/<sessionId>/artifacts/<artifactPath>/versions/<v>/<basename>  
    <baseDir>/users/<userId>/sessions/<sessionId>/artifacts/<artifactPath>/versions/<v>/metadata.json  
    <baseDir>/users/<userId>/artifacts/<artifactPath>/versions/<v>/<basename>            # user-scoped

Content copied to clipboard

An artifact is user-scoped when the session id is `null` or the filename starts with `user:` (the prefix is stripped from the path and preserved in metadata). `<artifactPath>` is derived from the filename, so nested names such as `images/photo.png` create nested directories; absolute paths and names that traverse outside the storage scope (e.g. `../secret`) are rejected.

Versions are 0-based and increase monotonically. A version is published atomically by staging its payload and metadata in a temporary directory and renaming it into place, so concurrent readers only ever observe complete versions (payload and metadata together). Writes to the same artifact are additionally serialized by an in-process per-artifact lock; this does not coordinate across separate OS processes.

This impl lives in `commonJvmAndroidMain` because it only needs java.io.File, so the same code serves both Android and the JVM. On Android, prefer the `fromContext` factory (in the `androidMain` source set) which roots [baseDir](../../../google-adk-kotlin-core/com.google.adk.kt.artifacts/-file-artifact-service/base-dir.html) at the app-specific external files directory.

Members

## Constructors

[FileArtifactService](-file-artifact-service.html)

Link copied to clipboard

commonJvmAndroid

constructor(baseDir: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

## Types

[Companion](-companion/index.html)

Link copied to clipboard

commonJvmAndroid

object [Companion](-companion/index.html)

## Functions

[deleteArtifact](delete-artifact.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [deleteArtifact](delete-artifact.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html), filename: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

Deletes an artifact.

[listArtifactKeys](list-artifact-keys.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [listArtifactKeys](list-artifact-keys.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>

Lists the filenames of all artifacts within a session.

[listVersions](list-versions.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [listVersions](list-versions.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html), filename: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)>

Lists all the versions (as revision IDs) of an artifact.

[loadArtifact](load-artifact.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [loadArtifact](load-artifact.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html), filename: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)?): [Part](../../com.google.adk.kt.types/-part/index.html)?

Gets an artifact.

[saveAndReloadArtifact](save-and-reload-artifact.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [saveAndReloadArtifact](save-and-reload-artifact.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html), filename: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Part](../../com.google.adk.kt.types/-part/index.html)

Saves an artifact and returns it with fileData if available.

[saveArtifact](save-artifact.html)

Link copied to clipboard

commonJvmAndroid

open suspend override fun [saveArtifact](save-artifact.html)(sessionKey: [SessionKey](../../com.google.adk.kt.sessions/-session-key/index.html), filename: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)

Saves an artifact.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
