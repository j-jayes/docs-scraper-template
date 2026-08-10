toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/[InMemoryRunner](index.html)/InMemoryRunner

# InMemoryRunner

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService())

Creates an [InMemoryRunner](index.html) from a root [agent](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html) and default in-memory services.

* * *

constructor(app: [App](../../com.google.adk.kt.apps/-app/index.html), sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), skipClosingPlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Creates an [InMemoryRunner](index.html) from an [App](../../com.google.adk.kt.apps/-app/index.html), deriving its [App.appName](../../com.google.adk.kt.apps/-app/app-name.html), [App.rootAgent](../../com.google.adk.kt.apps/-app/root-agent.html), [App.plugins](../../com.google.adk.kt.apps/-app/plugins.html), and [App.resumabilityConfig](../../com.google.adk.kt.apps/-app/resumability-config.html).

This is the recommended way to configure plugins and resumability.

#### Parameters

 _skip ClosingPlugins_

See [PluginManager.skipClosingPlugins](../../com.google.adk.kt.plugins/-plugin-manager/skip-closing-plugins.html). Set to `true` when the [App.plugins](../../com.google.adk.kt.apps/-app/plugins.html) are shared with another (parent) runner whose lifecycle owns them.

* * *

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html))

### Deprecated

Configure plugins via App.plugins instead, e.g. InMemoryRunner(App(appName, agent, plugins = listOf(...))). Passing a PluginManager directly to the runner is deprecated.

#### Replace with
    
    
    InMemoryRunner(App(appName, agent, plugins = pluginManager.plugins))

Content copied to clipboard

Creates an [InMemoryRunner](index.html) with an explicit [pluginManager](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

* * *

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html))

### Deprecated

Configure resumability via App.resumabilityConfig instead, e.g. InMemoryRunner(App(appName, agent, resumabilityConfig = ...)). Passing a ResumabilityConfig directly to the runner is deprecated.

#### Replace with
    
    
    InMemoryRunner(App(appName, agent, resumabilityConfig = resumabilityConfig))

Content copied to clipboard

Creates an [InMemoryRunner](index.html) with an explicit [resumabilityConfig](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

* * *

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html))

### Deprecated

Configure plugins and resumability via App instead, e.g. InMemoryRunner(App(appName, agent, plugins = listOf(...), resumabilityConfig = ...)). Passing them directly to the runner is deprecated.

#### Replace with
    
    
    InMemoryRunner(App(appName, agent, plugins = pluginManager.plugins, resumabilityConfig = resumabilityConfig))

Content copied to clipboard

Creates an [InMemoryRunner](index.html) with both an explicit [pluginManager](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html) and [resumabilityConfig](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
