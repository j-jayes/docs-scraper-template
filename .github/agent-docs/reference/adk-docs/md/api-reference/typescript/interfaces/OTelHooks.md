[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OTelHooks]()



# Interface OTelHooks

Configuration hooks for OpenTelemetry setup.

This interface defines the structure for configuring OpenTelemetry components including span processors, metric readers, and log record processors.

interface OTelHooks {  
logRecordProcessors?: LogRecordProcessor[];  
metricReaders?: MetricReader[];  
spanProcessors?: SpanProcessor[];  
}

  * Defined in [core/src/telemetry/setup.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/telemetry/setup.ts#L38)



## Properties

### `Optional`logRecordProcessors

logRecordProcessors?: LogRecordProcessor[]

  * Defined in [core/src/telemetry/setup.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/telemetry/setup.ts#L41)



### `Optional`metricReaders

metricReaders?: MetricReader[]

  * Defined in [core/src/telemetry/setup.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/telemetry/setup.ts#L40)



### `Optional`spanProcessors

spanProcessors?: SpanProcessor[]

  * Defined in [core/src/telemetry/setup.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/telemetry/setup.ts#L39)



Properties

logRecordProcessorsmetricReadersspanProcessors

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


