[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [isFeatureEnabled]()



# Function isFeatureEnabled

  * isFeatureEnabled(featureName: [PROGRESSIVE_SSE_STREAMING](../enums/FeatureName.html#progressive_sse_streaming)): boolean

Check if a feature is enabled at runtime.

Priority order (highest to lowest):

    1. Programmatic overrides
    2. Environment variables (ADK_ENABLE_* / ADK_DISABLE_*)
    3. Registry defaults

#### Parameters

    * featureName: [PROGRESSIVE_SSE_STREAMING](../enums/FeatureName.html#progressive_sse_streaming)

The feature name.

#### Returns boolean

True if the feature is enabled, false otherwise.

    * Defined in [core/src/features/feature_registry.ts:105](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/features/feature_registry.ts#L105)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


