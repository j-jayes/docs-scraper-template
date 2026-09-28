[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [createEventActions]()



# Function createEventActions

  * createEventActions(state?: Partial<[EventActions](../interfaces/EventActions.html)>): [EventActions](../interfaces/EventActions.html)

Creates an [EventActions](../interfaces/EventActions.html) object with default empty-dict values for all dictionary fields.

#### Parameters

    * state: Partial<[EventActions](../interfaces/EventActions.html)> = {}

Optional partial [EventActions](../interfaces/EventActions.html) whose properties override the defaults. Dictionary fields (`stateDelta`, `artifactDelta`, `requestedAuthConfigs`, `requestedToolConfirmations`) default to `{}`; scalar fields (`skipSummarization`, `transferToAgent`, `escalate`) default to `undefined`.

#### Returns [EventActions](../interfaces/EventActions.html)

A fully populated [EventActions](../interfaces/EventActions.html) object.

    * Defined in [core/src/events/event_actions.ts:72](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L72)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


