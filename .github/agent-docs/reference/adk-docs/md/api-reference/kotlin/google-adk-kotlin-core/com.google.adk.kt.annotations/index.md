[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.annotations

# Package-level declarations

Types

## Types

[AdkJavaInteropApi](-adk-java-interop-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "Java-interop API: prefer the Kotlin constructor and named arguments; opt in only if you need the Java-facing surface.", level = [RequiresOptIn.Level.WARNING](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-w-a-r-n-i-n-g/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html)])

annotation class [AdkJavaInteropApi](-adk-java-interop-api/index.html)

Marks an API that exists only to make ADK usable from Java, such as the fluent builders. Kotlin callers should use the primary constructor and named arguments instead; opting in acknowledges that you specifically need the Java-facing surface. Java callers are unaffected, since the opt-in requirement is enforced only by the Kotlin compiler.

[ExperimentalAppFunctionsFeature](-experimental-app-functions-feature/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html), message = "ADK AppFunctions support is an experimental feature whose API may change at any time. Opt in with @OptIn(ExperimentalAppFunctionsFeature::class) to acknowledge the risk.")

annotation class [ExperimentalAppFunctionsFeature](-experimental-app-functions-feature/index.html)

Marks ADK's **AppFunctions** APIs as experimental: their shape and semantics may change in future releases without prior notice, as the underlying AppFunctions SDK is itself pre-release.

[ExperimentalAuthApi](-experimental-auth-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "The ADK auth API is experimental and may change without notice.", level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html), [AnnotationTarget.TYPEALIAS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html)])

annotation class [ExperimentalAuthApi](-experimental-auth-api/index.html)

Marks the auth API (credentials, auth schemes and sign-in requests), which is experimental and expected to change without notice. Opt in with `@OptIn(ExperimentalAuthApi::class)`.

[ExperimentalContextCachingFeature](-experimental-context-caching-feature/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html), message = "ADK context caching is an experimental feature whose API may change at any time. Opt in with @OptIn(ExperimentalContextCachingFeature::class) to acknowledge the risk.")

annotation class [ExperimentalContextCachingFeature](-experimental-context-caching-feature/index.html)

Marks ADK's **context caching** APIs as experimental: their shape and semantics may change in future releases without prior notice.

[ExperimentalEnvironmentApi](-experimental-environment-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html), message = "ADK environment APIs are experimental and may change at any time. Opt in with @OptIn(ExperimentalEnvironmentApi::class) to acknowledge the risk.")

annotation class [ExperimentalEnvironmentApi](-experimental-environment-api/index.html)

Marks ADK's **environment** APIs as experimental: their shape and semantics may change in future releases without prior notice.

[ExperimentalLiveApi](-experimental-live-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "The ADK live API is experimental and may change without notice.", level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html), [AnnotationTarget.TYPEALIAS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html)])

annotation class [ExperimentalLiveApi](-experimental-live-api/index.html)

Marks the live (bidirectional streaming) API, which is experimental and expected to change without notice. Opt in with `@OptIn(ExperimentalLiveApi::class)`.

[ExperimentalWorkflowApi](-experimental-workflow-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "The ADK workflow API is experimental and may change without notice.", level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html), [AnnotationTarget.TYPEALIAS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html)])

annotation class [ExperimentalWorkflowApi](-experimental-workflow-api/index.html)

Marks the graph-workflow API, which is experimental and expected to change without notice. Opt in with `@OptIn(ExperimentalWorkflowApi::class)`.

[FrameworkInternalApi](-framework-internal-api/index.html)

Link copied to clipboard

common

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "This API is for ADK framework use only.", level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html)])

annotation class [FrameworkInternalApi](-framework-internal-api/index.html)

[Param](-param/index.html)

Link copied to clipboard

common

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.VALUE_PARAMETER](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.html)])

annotation class [Param](-param/index.html)(val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val required: [Requiredness](-requiredness/index.html) = Requiredness.AUTO)

Annotates a parameter of a function annotated with [Tool](-tool/index.html) to provide explicit metadata.

[Requiredness](-requiredness/index.html)

Link copied to clipboard

common

enum [Requiredness](-requiredness/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[Requiredness](-requiredness/index.html)>

Whether a [Param](-param/index.html) is required in the generated tool schema.

[SecretAccess](-secret-access/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](-experimental-auth-api/index.html)

@[RequiresOptIn](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html)(message = "Reveals a secret value.", level = [RequiresOptIn.Level.ERROR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/-level/-e-r-r-o-r/index.html))

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.CLASS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html), [AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.PROPERTY](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html), [AnnotationTarget.CONSTRUCTOR](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html), [AnnotationTarget.TYPEALIAS](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html)])

annotation class [SecretAccess](-secret-access/index.html)

Marks APIs that return a secret's raw value, such as [Secret.reveal](../com.google.adk.kt.auth/-secret/reveal.html). Opt in with `@OptIn(SecretAccess::class)`, which makes each place that handles a raw credential visible in review.

[Tool](-tool/index.html)

Link copied to clipboard

common

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html)])

annotation class [Tool](-tool/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val requireConfirmation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Annotates a function to be exposed as an executable tool by the Google ADK Kotlin. KSP will generate a corresponding [com.google.adk.kt.tools.FunctionTool](../com.google.adk.kt.tools/-function-tool/index.html) wrapper for annotated functions.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
