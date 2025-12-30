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
requestedAuthConfigs: { [key: string]: any };  
requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) };  
skipSummarization?: boolean;  
stateDelta: { [key: string]: unknown };  
transferToAgent?: string;  
}

  * Defined in [core/src/events/event_actions.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L15)



## Properties

### artifactDelta

artifactDelta: { [key: string]: number }

Indicates that the event is updating an artifact. key is the filename, value is the version.

  * Defined in [core/src/events/event_actions.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L31)



### `Optional`escalate

escalate?: boolean

The agent is escalating to a higher level agent.

  * Defined in [core/src/events/event_actions.ts:41](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L41)



### requestedAuthConfigs

requestedAuthConfigs: { [key: string]: any }

Authentication configurations requested by tool responses.

This field will only be set by a tool response event indicating tool request auth credential.

  * Keys: The function call id. Since one function response event could contain multiple function responses that correspond to multiple function calls. Each function call could request different auth configs. This id is used to identify the function call.
  * Values: The requested auth config.



  * Defined in [core/src/events/event_actions.ts:54](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L54)



### requestedToolConfirmations

requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) }

A dict of tool confirmation requested by this event, keyed by the function call id.

  * Defined in [core/src/events/event_actions.ts:60](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L60)



### `Optional`skipSummarization

skipSummarization?: boolean

If true, it won't call model to summarize function response. Only used for function_response event.

  * Defined in [core/src/events/event_actions.ts:20](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L20)



### stateDelta

stateDelta: { [key: string]: unknown }

Indicates that the event is updating the state with the given delta.

  * Defined in [core/src/events/event_actions.ts:25](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L25)



### `Optional`transferToAgent

transferToAgent?: string

If set, the event transfers to the specified agent.

  * Defined in [core/src/events/event_actions.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event_actions.ts#L36)



Properties

artifactDeltaescalaterequestedAuthConfigsrequestedToolConfirmationsskipSummarizationstateDeltatransferToAgent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


