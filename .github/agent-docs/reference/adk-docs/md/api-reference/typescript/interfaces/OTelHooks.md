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

  * Defined in [core/src/telemetry/setup.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/telemetry/setup.ts#L30)



## Properties

### `Optional`logRecordProcessors

logRecordProcessors?: LogRecordProcessor[]

  * Defined in [core/src/telemetry/setup.ts:33](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/telemetry/setup.ts#L33)



### `Optional`metricReaders

metricReaders?: MetricReader[]

  * Defined in [core/src/telemetry/setup.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/telemetry/setup.ts#L32)



### `Optional`spanProcessors

spanProcessors?: SpanProcessor[]

  * Defined in [core/src/telemetry/setup.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/telemetry/setup.ts#L31)



Properties

logRecordProcessorsmetricReadersspanProcessors

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


