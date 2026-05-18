[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [maybeSetOtelProviders]()



# Function maybeSetOtelProviders

  * maybeSetOtelProviders(  
otelHooksToSetup?: [OTelHooks](../interfaces/OTelHooks.html)[],  
otelResource?: Resource,  
): void

`Experimental`

Sets up OTel providers if hooks for a given telemetry type were passed.

Additionally adds generic OTLP exporters based on following env variables: OTEL_EXPORTER_OTLP_ENDPOINT OTEL_EXPORTER_OTLP_TRACES_ENDPOINT OTEL_EXPORTER_OTLP_METRICS_ENDPOINT OTEL_EXPORTER_OTLP_LOGS_ENDPOINT See <https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/> for how they are used.

If a provider for a specific telemetry type was already globally set - this function will not override it or register more exporters.

(Experimental, subject to change)

#### Parameters

    * otelHooksToSetup: [OTelHooks](../interfaces/OTelHooks.html)[] = []

per-telemetry-type processors and readers to be added to OTel providers. If no hooks for a specific telemetry type are passed - provider will not be set.

    * `Optional`otelResource: Resource

OTel resource to use in providers. If empty - default OTel resource detection will be used.

#### Returns void

    * Defined in [telemetry/setup.ts:66](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/telemetry/setup.ts#L66)




[ADK for TypeScript: API Reference](../index.html)

  * Loading...


