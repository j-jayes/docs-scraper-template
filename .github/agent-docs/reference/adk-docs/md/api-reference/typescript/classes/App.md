[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [App]()



# Class App

Represents an LLM-backed agentic application.

An `App` is the top-level container for an agentic system powered by LLMs. It manages a root agent (`rootAgent`), which serves as the entry point for execution.

Exactly one `rootAgent` must be provided.

The `plugins` are application-wide components that provide shared capabilities and services to the entire system.

  * Defined in [core/src/apps/app.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L68)



## Constructors

### constructor

  * new App(options: [AppOptions](../interfaces/AppOptions.html)): [App]()

#### Parameters

    * options: [AppOptions](../interfaces/AppOptions.html)

#### Returns [App]()

    * Defined in [core/src/apps/app.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L77)




## Properties

### `Readonly`[APP_SIGNATURE_SYMBOL]

"[APP_SIGNATURE_SYMBOL]": true

  * Defined in [core/src/apps/app.ts:69](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L69)



### `Readonly`name

name: string

  * Defined in [core/src/apps/app.ts:71](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L71)



### `Readonly`plugins

plugins: [BasePlugin](BasePlugin.html)[]

  * Defined in [core/src/apps/app.ts:74](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L74)



### `Optional` `Readonly`resumabilityConfig

resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html)

  * Defined in [core/src/apps/app.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L75)



### `Readonly`rootAgent

rootAgent: any

  * Defined in [core/src/apps/app.ts:73](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/apps/app.ts#L73)



Constructors

constructor

Properties

[APP_SIGNATURE_SYMBOL]namepluginsresumabilityConfigrootAgent

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


