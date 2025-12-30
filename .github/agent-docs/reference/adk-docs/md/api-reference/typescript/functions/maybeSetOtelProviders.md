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

    * Defined in [core/src/telemetry/setup.ts:58](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/telemetry/setup.ts#L58)




[ADK for TypeScript: API Reference](../index.html)

  * Loading...


