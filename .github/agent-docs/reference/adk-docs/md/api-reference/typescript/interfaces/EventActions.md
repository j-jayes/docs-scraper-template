[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [EventActions]()



# Interface EventActions

Represents the actions attached to an event.

interface EventActions {  
agentState?: Record<string, unknown>;  
artifactDelta: { [key: string]: number };  
endOfAgent?: boolean;  
escalate?: boolean;  
requestedAuthConfigs: { [key: string]: [AuthConfig](AuthConfig.html) };  
requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) };  
skipSummarization?: boolean;  
stateDelta: { [key: string]: unknown };  
transferToAgent?: string;  
}

  * Defined in [core/src/events/event_actions.ts:16](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L16)



## Properties

### `Optional`agentState

agentState?: Record<string, unknown>

Workflow: a serialized node/agent state snapshot used for resumable checkpointing. Mirrors Python `EventActions.agent_state`.

  * Defined in [core/src/events/event_actions.ts:67](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L67)



### artifactDelta

artifactDelta: { [key: string]: number }

Indicates that the event is updating an artifact. key is the filename, value is the version.

  * Defined in [core/src/events/event_actions.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L32)



### `Optional`endOfAgent

endOfAgent?: boolean

Workflow: marks that the emitting agent/workflow has reached the end of its execution for this invocation. Mirrors Python `EventActions.end_of_agent`.

  * Defined in [core/src/events/event_actions.ts:73](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L73)



### `Optional`escalate

escalate?: boolean

The agent is escalating to a higher level agent.

  * Defined in [core/src/events/event_actions.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L42)



### requestedAuthConfigs

requestedAuthConfigs: { [key: string]: [AuthConfig](AuthConfig.html) }

Authentication configurations requested by tool responses.

This field will only be set by a tool response event indicating tool request auth credential.

  * Keys: The function call id. Since one function response event could contain multiple function responses that correspond to multiple function calls. Each function call could request different auth configs. This id is used to identify the function call.
  * Values: The requested auth config.



  * Defined in [core/src/events/event_actions.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L55)



### requestedToolConfirmations

requestedToolConfirmations: { [key: string]: [ToolConfirmation](../classes/ToolConfirmation.html) }

A dict of tool confirmation requested by this event, keyed by the function call id.

  * Defined in [core/src/events/event_actions.ts:61](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L61)



### `Optional`skipSummarization

skipSummarization?: boolean

If true, it won't call model to summarize function response. Only used for function_response event.

  * Defined in [core/src/events/event_actions.ts:21](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L21)



### stateDelta

stateDelta: { [key: string]: unknown }

Indicates that the event is updating the state with the given delta.

  * Defined in [core/src/events/event_actions.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L26)



### `Optional`transferToAgent

transferToAgent?: string

If set, the event transfers to the specified agent.

  * Defined in [core/src/events/event_actions.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event_actions.ts#L37)



Properties

agentStateartifactDeltaendOfAgentescalaterequestedAuthConfigsrequestedToolConfirmationsskipSummarizationstateDeltatransferToAgent

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


