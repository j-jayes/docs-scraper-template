[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid jvm

Target filter __

    * commonJvmAndroid 
    * jvm 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.interop

# Package-level declarations

Types

## Types

[AsyncJavaHelpers](-async-java-helpers/index.html)

Link copied to clipboard

commonJvmAndroid

object [AsyncJavaHelpers](-async-java-helpers/index.html)

Entry points for calling the suspending and [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)-returning parts of the ADK from Java, and for bridging a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) to Reactive Streams.

[BaseFutureArtifactService](-base-future-artifact-service/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureArtifactService](-base-future-artifact-service/index.html) : [ArtifactService](../com.google.adk.kt.artifacts/-artifact-service/index.html)

Java-friendly base for implementing an [ArtifactService](../com.google.adk.kt.artifacts/-artifact-service/index.html). The engine's methods are `suspend`; a Java subclass returns [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html)s instead. Return each future promptly and do any blocking work inside it, not before returning it.

[BaseFutureLiveConnection](-base-future-live-connection/index.html)

Link copied to clipboard

commonJvmAndroid

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

abstract class [BaseFutureLiveConnection](-base-future-live-connection/index.html) : [LiveConnection](../com.google.adk.kt.models/-live-connection/index.html)

Java-friendly base for implementing a [LiveConnection](../com.google.adk.kt.models/-live-connection/index.html): override the `...Async` methods, which return a [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html), and [receiveJava](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-live-connection/receive-java.html), which returns a [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html) of one model turn. The base maps these to [LiveConnection](../com.google.adk.kt.models/-live-connection/index.html)'s calls and also enforces two of its rules, one [receive](-base-future-live-connection/receive.html) collector at a time and a [closeSession](-base-future-live-connection/close-session.html) that is safe to call again; apply its content rules yourself. Return a new future from each call, because the base cancels a send's future when its caller is cancelled, and a new publisher from each [receiveJava](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-live-connection/receive-java.html) call; return each promptly, with any blocking work inside it, and fail a future rather than cancel it.

[BaseFutureMemoryService](-base-future-memory-service/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureMemoryService](-base-future-memory-service/index.html) : [MemoryService](../com.google.adk.kt.memory/-memory-service/index.html)

Java-friendly base for implementing a [MemoryService](../com.google.adk.kt.memory/-memory-service/index.html). The engine's methods are `suspend`; a Java subclass returns [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html)s instead. [addEventsToMemoryAsync](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-memory-service/add-events-to-memory-async.html) and [addMemoryAsync](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-memory-service/add-memory-async.html) are optional -- their default throws [UnsupportedOperationException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unsupported-operation-exception/index.html) (as the engine does), so override them only if the service supports those writes. Return each future promptly and do any blocking work inside it, not before returning it.

[BaseFuturePlugin](-base-future-plugin/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFuturePlugin](-base-future-plugin/index.html)(pluginName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [Plugin](../com.google.adk.kt.plugins/-plugin/index.html)

Java-friendly base for implementing a [Plugin](../com.google.adk.kt.plugins/-plugin/index.html) \-- the cross-cutting interception point. The engine's `Plugin` has 13 `suspend` callbacks plus `close()`, every one with a default body. This base final-overrides all 13 and re-exposes each as a [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html)-returning hook whose _result_ is the outcome; each default hook completes with the value that leaves execution unchanged. Return the future promptly and do any blocking work inside it, not before returning it.

[BaseFutureSessionService](-base-future-session-service/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureSessionService](-base-future-session-service/index.html) : [SessionService](../com.google.adk.kt.sessions/-session-service/index.html)

Java-friendly base for implementing a [SessionService](../com.google.adk.kt.sessions/-session-service/index.html). Every method of the engine interface is `suspend`; this base final-overrides each and asks the Java subclass for a [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html) instead. Return each future promptly and do any blocking work inside it, not before returning it. The methods with default bodies ([closeSession](-base-future-session-service/close-session.html), [appendEvent](-base-future-session-service/append-event.html), [flush](-base-future-session-service/flush.html)) keep those defaults reachable: leave the hook unoverridden and the engine's own behaviour runs.

[BaseFutureSkillSource](-base-future-skill-source/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureSkillSource](-base-future-skill-source/index.html) : [SkillSource](../com.google.adk.kt.skills/-skill-source/index.html)

Java-friendly base for implementing a [SkillSource](../com.google.adk.kt.skills/-skill-source/index.html): every engine method is a `suspend` returning a [Result](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/index.html), and this base final-overrides each to await a [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html) from the Java subclass, mapping a completed future to [Result.success](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/-companion/success.html) and any failure to a [Result.failure](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/-companion/failure.html) of [SkillSourceException](../com.google.adk.kt.skills/-skill-source-exception/index.html). Return each future promptly and do any blocking work inside it. Complete the future exceptionally with a [SkillSourceException](../com.google.adk.kt.skills/-skill-source-exception/index.html) to report a skill error whose message reaches the LLM.

[BaseFutureTool](-base-future-tool/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureTool](-base-future-tool/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)

Java-friendly base for implementing a [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html) asynchronously. A Java subclass overrides [declaration](../com.google.adk.kt.tools/-base-tool/declaration.html) and [runAsync](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-tool/run-async.html), which returns a [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html); this base awaits it to satisfy the `suspend` [run](-base-future-tool/run.html) contract that Java cannot express.

[BaseFutureToolset](-base-future-toolset/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseFutureToolset](-base-future-toolset/index.html) : [Toolset](../com.google.adk.kt.tools/-toolset/index.html)

Java-friendly base for implementing a [Toolset](../com.google.adk.kt.tools/-toolset/index.html) \-- a dynamically resolved group of tools. Both engine methods are `suspend`; a Java subclass returns [CompletableFuture](https://developer.android.com/reference/kotlin/java/util/concurrent/CompletableFuture.html)s instead. Return each future promptly and do any blocking work inside it, not before returning it. [processLlmRequest](-base-future-toolset/process-llm-request.html) defaults to returning the request unchanged; override [processLlmRequestAsync](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-future-toolset/process-llm-request-async.html) to rewrite it.

[BaseMillisRetryPolicy](-base-millis-retry-policy/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BaseMillisRetryPolicy](-base-millis-retry-policy/index.html) : [RetryPolicy](../com.google.adk.kt.retry/-retry-policy/index.html)

Java-friendly base for implementing a [RetryPolicy](../com.google.adk.kt.retry/-retry-policy/index.html). Java cannot return the [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) that [nextRetryDelay](-base-millis-retry-policy/next-retry-delay.html) needs, so a Java subclass implements [shouldRetry](../com.google.adk.kt.retry/-retry-policy/should-retry.html) and [nextRetryDelayMillis](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-millis-retry-policy/next-retry-delay-millis.html) instead. Like any [RetryPolicy](../com.google.adk.kt.retry/-retry-policy/index.html), it must be thread-safe and return quickly.

[BasePublisherAgent](-base-publisher-agent/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BasePublisherAgent](-base-publisher-agent/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), disallowTransferToParent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html)

Java-friendly base for implementing a [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html). A Java subclass overrides [runAsyncImplJava](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-agent/run-async-impl-java.html), which returns a Reactive Streams [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html) of the turn's events; this base adapts it to the `Flow`-returning [runAsyncImpl](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-agent/run-async-impl.html) contract that Java cannot express. The publisher is subscribed to lazily and honours backpressure.

[BasePublisherModel](-base-publisher-model/index.html)

Link copied to clipboard

commonJvmAndroid

abstract class [BasePublisherModel](-base-publisher-model/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [Model](../com.google.adk.kt.models/-model/index.html)

Java-friendly base for implementing a [Model](../com.google.adk.kt.models/-model/index.html). A Java subclass overrides [generateContentJava](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-model/generate-content-java.html), which returns a Reactive Streams [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html); this base adapts it to the `Flow`-returning [generateContent](-base-publisher-model/generate-content.html) contract that Java cannot express. Both the unary and streaming cases flow through that one method, exactly as they do for a Kotlin [Model](../com.google.adk.kt.models/-model/index.html); a subclass that supports live connections also overrides [connectAsync](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-model/connect-async.html).

[BasePublisherNode](-base-publisher-node/index.html)

Link copied to clipboard

commonJvmAndroid

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

abstract class [BasePublisherNode](-base-publisher-node/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](../com.google.adk.kt.workflow/-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null) : [BaseNode](../com.google.adk.kt.workflow/-base-node/index.html)

Java-friendly base for implementing a workflow node. A Java subclass overrides [runNodeJava](../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-node/run-node-java.html) to set routes or state on the context and return a Reactive Streams [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html) of node outputs, which this base adapts to the `Flow`-returning [runNode](-base-publisher-node/run-node.html).

[Choices](-choices/index.html)

Link copied to clipboard

commonJvmAndroid

object [Choices](-choices/index.html)

Java factories for the sealed [CallbackChoice](../com.google.adk.kt.callbacks/-callback-choice/index.html).

[FutureAfterAgentCallback](-future-after-agent-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureAfterAgentCallback](-future-after-agent-callback/index.html)

[FutureAfterModelCallback](-future-after-model-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureAfterModelCallback](-future-after-model-callback/index.html)

[FutureAfterToolCallback](-future-after-tool-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureAfterToolCallback](-future-after-tool-callback/index.html)

[FutureBeforeAgentCallback](-future-before-agent-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureBeforeAgentCallback](-future-before-agent-callback/index.html)

[FutureBeforeModelCallback](-future-before-model-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureBeforeModelCallback](-future-before-model-callback/index.html)

[FutureBeforeToolCallback](-future-before-tool-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureBeforeToolCallback](-future-before-tool-callback/index.html)

[FutureCallbacks](-future-callbacks/index.html)

Link copied to clipboard

commonJvmAndroid

object [FutureCallbacks](-future-callbacks/index.html)

Java-friendly adapters for the engine's callback interfaces.

[FutureOnModelErrorCallback](-future-on-model-error-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureOnModelErrorCallback](-future-on-model-error-callback/index.html)

[FutureOnToolErrorCallback](-future-on-tool-error-callback/index.html)

Link copied to clipboard

commonJvmAndroid

@[JvmSuppressWildcards](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html)

fun interface [FutureOnToolErrorCallback](-future-on-tool-error-callback/index.html)

[PublisherRunner](-publisher-runner/index.html)

Link copied to clipboard

commonJvmAndroid

class [PublisherRunner](-publisher-runner/index.html) : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

Java-friendly wrapper around a [Runner](../com.google.adk.kt.runners/-runner/index.html). A run is exposed as a Reactive Streams [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html) of events, so Java callers never touch `Flow`; collect it with `AsyncJavaHelpers.collect`/`forEach` or any Reactive Streams consumer. Session management is not a runner concern -- reach the session service via `asKotlinRunner().sessionService` (or wrap it in a `BaseFutureSessionService`).

[ReflectiveTools](-reflective-tools/index.html)

Link copied to clipboard

jvm

object [ReflectiveTools](-reflective-tools/index.html)

Builds a [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html) from a [Tool](../com.google.adk.kt.annotations/-tool/index.html)-annotated Java method, the reflective counterpart of the engine's KSP `@Tool` path (which needs the Kotlin compiler and so is closed to a javac-only build). It reads the same [Tool](../com.google.adk.kt.annotations/-tool/index.html)/[Param](../com.google.adk.kt.annotations/-param/index.html) annotations, relying on [Param.name](../com.google.adk.kt.annotations/-param/name.html)/[Param.required](../com.google.adk.kt.annotations/-param/required.html) because Java retains neither parameter names nor nullability. JVM-only and intended for javac-only modules; prefer the KSP `@Tool` path whenever the code is built with the Kotlin compiler, which processes `.java` sources too.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
