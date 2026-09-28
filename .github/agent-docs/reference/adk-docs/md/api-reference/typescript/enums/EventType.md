[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [EventType]()



# Enumeration EventType

The types of events that can be parsed from a raw Event.

Each value corresponds to one category of structured output that [toStructuredEvents](../functions/toStructuredEvents.html) may produce from a raw [Event](../interfaces/Event.html).

  * Defined in [core/src/events/structured_events.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L22)



## Enumeration Members

### ACTIVITY

ACTIVITY: "activity"

A generic activity or status update.

  * Defined in [core/src/events/structured_events.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L38)



### CALL_CODE

CALL_CODE: "call_code"

A request from the model to execute code.

  * Defined in [core/src/events/structured_events.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L32)



### CODE_RESULT

CODE_RESULT: "code_result"

The result of a code execution.

  * Defined in [core/src/events/structured_events.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L34)



### CONTENT

CONTENT: "content"

A text delta intended for the end user.

  * Defined in [core/src/events/structured_events.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L26)



### ERROR

ERROR: "error"

A runtime error signalled via `event.errorCode`.

  * Defined in [core/src/events/structured_events.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L36)



### FINISHED

FINISHED: "finished"

The agent has produced its final response for this turn.

  * Defined in [core/src/events/structured_events.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L42)



### THOUGHT

THOUGHT: "thought"

A reasoning trace (thought) emitted by the model.

  * Defined in [core/src/events/structured_events.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L24)



### TOOL_CALL

TOOL_CALL: "tool_call"

A request from the model to execute a tool (function call).

  * Defined in [core/src/events/structured_events.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L28)



### TOOL_CONFIRMATION

TOOL_CONFIRMATION: "tool_confirmation"

A request for the user to confirm one or more tool calls.

  * Defined in [core/src/events/structured_events.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L40)



### TOOL_RESULT

TOOL_RESULT: "tool_result"

The result returned by a tool execution (function response).

  * Defined in [core/src/events/structured_events.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/structured_events.ts#L30)



Enumeration Members

ACTIVITYCALL_CODECODE_RESULTCONTENTERRORFINISHEDTHOUGHTTOOL_CALLTOOL_CONFIRMATIONTOOL_RESULT

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


