[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.apps](../index.html)/App

# App

common

data class [App](index.html)(val appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val rootAgent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), val plugins: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)> = emptyList(), val resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)? = null, val eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, val contextCacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null, val rootNode: [Node](../../com.google.adk.kt.workflow/-node/index.html)? = null)

Represents an LLM-backed agentic application.

An [App](index.html) is the top-level container for an agentic system powered by LLMs. It bundles an application name together with the [rootAgent](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) that serves as the root of the agent tree, enabling coordination and communication across all agents in the hierarchy. It also carries application-wide configuration, such as [plugins](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) and [resumabilityConfig](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html), that the runner applies to every session it runs.

[appName](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) must start with a letter and may contain only letters, digits, underscores, and hyphens, and must not be the reserved value `"user"`, which is reserved for end-user input. Construction throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) if [appName](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) does not meet these requirements.

Members

## Constructors

[App](-app.html)

Link copied to clipboard

common

constructor(appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), rootAgent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), plugins: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)> = emptyList(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)? = null, eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, contextCacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null, rootNode: [Node](../../com.google.adk.kt.workflow/-node/index.html)? = null)

constructor(appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), rootAgent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), plugins: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)> = emptyList(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)? = null, eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, contextCacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null)

The 1.1.0 constructor, which had no [rootNode](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html). Stays visible because javac skips hidden constructors, so Java code written against 1.1.0 would otherwise bind to the node-rooted one.

constructor(appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), rootNode: [Node](../../com.google.adk.kt.workflow/-node/index.html), plugins: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)> = emptyList(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)? = null, eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, contextCacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null)

Creates an app rooted on a node graph rather than an agent tree. Wraps [rootNode](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) in a NodeViewAgent so the future-deprecated [rootAgent](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) stays non-null during the deprecation window.

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [App](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[appName](app-name.html)

Link copied to clipboard

common

val [appName](app-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The application name.

[contextCacheConfig](context-cache-config.html)

Link copied to clipboard

common

val [contextCacheConfig](context-cache-config.html): [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)?

Optional context cache configuration that applies to all LLM agents in the app. When `null`, context caching is disabled.

[eventsCompactionConfig](events-compaction-config.html)

Link copied to clipboard

common

val [eventsCompactionConfig](events-compaction-config.html): [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)?

Optional configuration controlling context-compaction strategies for sessions of this application. When `null`, no compaction runs.

[plugins](plugins.html)

Link copied to clipboard

common

val [plugins](plugins.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)>

Application-wide [Plugin](../../com.google.adk.kt.plugins/-plugin/index.html)s providing shared callbacks and services to the entire system. Defaults to an empty list.

[resumabilityConfig](resumability-config.html)

Link copied to clipboard

common

val [resumabilityConfig](resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)?

Optional resumability configuration applied to the application's sessions. When `null`, resumability is disabled.

[rootAgent](root-agent.html)

Link copied to clipboard

common

val [rootAgent](root-agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

The root agent of the application's agent tree.

[rootNode](root-node.html)

Link copied to clipboard

common

val [rootNode](root-node.html): [Node](../../com.google.adk.kt.workflow/-node/index.html)?

The application's entry point, set for a graph app. The go-forward field; once [rootAgent](../../../google-adk-kotlin-core/com.google.adk.kt.apps/-app/--root--.html) is removed it holds the running unit for every app.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [App.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
