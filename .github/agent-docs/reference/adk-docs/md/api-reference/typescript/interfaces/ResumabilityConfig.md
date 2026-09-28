[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ResumabilityConfig]()



# Interface ResumabilityConfig

The configuration of resumability for an application or runner.

The "resumability" in ADK refers to the ability to:

  1. pause an invocation upon a long-running function call.
  2. resume an invocation from the last event, if it's paused or failed midway through.



interface ResumabilityConfig {  
isResumable: boolean;  
}

  * Defined in [core/src/apps/resumability_config.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/resumability_config.ts#L15)



## Properties

### isResumable

isResumable: boolean

Whether the app/runner supports agent resumption. If enabled, resumption routing based on matching function responses will be active.

  * Defined in [core/src/apps/resumability_config.ts:20](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/resumability_config.ts#L20)



Properties

isResumable

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


