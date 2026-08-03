[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [EventActions]()



# Interface EventActions

Represents the actions attached to an event.

interface EventActions {  
artifactDelta: { [key: string]: number };  
escalate?: boolean;  
requestedAuthConfigs: { [key: string]: [AuthConfig](AuthConfig.html) };  
requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) };  
skipSummarization?: boolean;  
stateDelta: { [key: string]: unknown };  
transferToAgent?: string;  
}

  * Defined in [core/src/events/event_actions.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L13)



## Properties

### artifactDelta

artifactDelta: { [key: string]: number }

Indicates that the event is updating an artifact. key is the filename, value is the version.

  * Defined in [core/src/events/event_actions.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L29)



### `Optional`escalate

escalate?: boolean

The agent is escalating to a higher level agent.

  * Defined in [core/src/events/event_actions.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L39)



### requestedAuthConfigs

requestedAuthConfigs: { [key: string]: [AuthConfig](AuthConfig.html) }

Authentication configurations requested by tool responses.

This field will only be set by a tool response event indicating tool request auth credential.

  * Keys: The function call id. Since one function response event could contain multiple function responses that correspond to multiple function calls. Each function call could request different auth configs. This id is used to identify the function call.
  * Values: The requested auth config.



  * Defined in [core/src/events/event_actions.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L52)



### requestedToolConfirmations

requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) }

A dict of tool confirmation requested by this event, keyed by the function call id.

  * Defined in [core/src/events/event_actions.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L58)



### `Optional`skipSummarization

skipSummarization?: boolean

If true, it won't call model to summarize function response. Only used for function_response event.

  * Defined in [core/src/events/event_actions.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L18)



### stateDelta

stateDelta: { [key: string]: unknown }

Indicates that the event is updating the state with the given delta.

  * Defined in [core/src/events/event_actions.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L23)



### `Optional`transferToAgent

transferToAgent?: string

If set, the event transfers to the specified agent.

  * Defined in [core/src/events/event_actions.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event_actions.ts#L34)



Properties

artifactDeltaescalaterequestedAuthConfigsrequestedToolConfirmationsskipSummarizationstateDeltatransferToAgent

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


