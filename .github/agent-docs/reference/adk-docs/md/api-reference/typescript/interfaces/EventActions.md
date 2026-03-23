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

  * Defined in [events/event_actions.ts:16](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L16)



## Properties

### artifactDelta

artifactDelta: { [key: string]: number }

Indicates that the event is updating an artifact. key is the filename, value is the version.

  * Defined in [events/event_actions.ts:32](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L32)



### `Optional`escalate

escalate?: boolean

The agent is escalating to a higher level agent.

  * Defined in [events/event_actions.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L42)



### requestedAuthConfigs

requestedAuthConfigs: { [key: string]: any }

Authentication configurations requested by tool responses.

This field will only be set by a tool response event indicating tool request auth credential.

  * Keys: The function call id. Since one function response event could contain multiple function responses that correspond to multiple function calls. Each function call could request different auth configs. This id is used to identify the function call.
  * Values: The requested auth config.



  * Defined in [events/event_actions.ts:55](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L55)



### requestedToolConfirmations

requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) }

A dict of tool confirmation requested by this event, keyed by the function call id.

  * Defined in [events/event_actions.ts:61](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L61)



### `Optional`skipSummarization

skipSummarization?: boolean

If true, it won't call model to summarize function response. Only used for function_response event.

  * Defined in [events/event_actions.ts:21](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L21)



### stateDelta

stateDelta: { [key: string]: unknown }

Indicates that the event is updating the state with the given delta.

  * Defined in [events/event_actions.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L26)



### `Optional`transferToAgent

transferToAgent?: string

If set, the event transfers to the specified agent.

  * Defined in [events/event_actions.ts:37](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event_actions.ts#L37)



Properties

artifactDeltaescalaterequestedAuthConfigsrequestedToolConfirmationsskipSummarizationstateDeltatransferToAgent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


