[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LiveRequest]()



# Interface LiveRequest

Request sent to live agents.

interface LiveRequest {  
activityEnd?: ActivityEnd;  
activityStart?: ActivityStart;  
blob?: Blob_2;  
close?: boolean;  
content?: Content;  
}

  * Defined in [core/src/agents/live_request_queue.ts:12](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L12)



## Properties

### `Optional`activityEnd

activityEnd?: ActivityEnd

If set, signal the end of user activity to the model.

  * Defined in [core/src/agents/live_request_queue.ts:20](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L20)



### `Optional`activityStart

activityStart?: ActivityStart

If set, signal the start of user activity to the model.

  * Defined in [core/src/agents/live_request_queue.ts:18](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L18)



### `Optional`blob

blob?: Blob_2

If set, send the blob to the model in realtime mode.

  * Defined in [core/src/agents/live_request_queue.ts:16](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L16)



### `Optional`close

close?: boolean

If set, close the queue.

  * Defined in [core/src/agents/live_request_queue.ts:22](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L22)



### `Optional`content

content?: Content

If set, send the content to the model in turn-by-turn mode.

  * Defined in [core/src/agents/live_request_queue.ts:14](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L14)



Properties

activityEndactivityStartblobclosecontent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


