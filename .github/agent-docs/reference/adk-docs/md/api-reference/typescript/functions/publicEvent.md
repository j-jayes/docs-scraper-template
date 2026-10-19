[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [publicEvent]()



# Function publicEvent

  * publicEvent<T extends [Event](../interfaces/Event.html)>(event: T): T

Returns the event as callers see it, without internal metadata.

#### Type Parameters

    * T extends [Event](../interfaces/Event.html)

#### Parameters

    * event: T

A stored event. It is not modified.

#### Returns T

The same event if it has no internal keys. Otherwise a copy whose `customMetadata` drops them, or is `undefined` if nothing else is left.

    * Defined in [core/src/events/internal_metadata.ts:131](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/internal_metadata.ts#L131)




[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


