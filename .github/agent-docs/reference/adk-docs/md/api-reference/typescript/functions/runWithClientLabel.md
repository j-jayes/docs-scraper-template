[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [runWithClientLabel]()



# Function runWithClientLabel

  * runWithClientLabel<R>(clientLabel: string, callback: () => R): R

Runs the given callback within a context that has the specified client label. All LLM calls made within this callback will include the client label in their tracking headers.

#### Type Parameters

    * R

#### Parameters

    * clientLabel: string

The custom client label to apply.

    * callback: () => R

The callback function to execute.

#### Returns R

The result of the callback.

    * Defined in [core/src/utils/client_labels.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/client_labels.ts#L64)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


