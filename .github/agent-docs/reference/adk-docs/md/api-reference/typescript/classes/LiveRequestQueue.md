[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LiveRequestQueue]()



# Class LiveRequestQueue

Queue used to send LiveRequest in a live (bidirectional streaming) way.

  * Defined in [core/src/agents/live_request_queue.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L31)



## Constructors

### constructor

  * new LiveRequestQueue(): [LiveRequestQueue]()

#### Returns [LiveRequestQueue]()




## Methods

### [asyncIterator]

  * "[asyncIterator]"(): AsyncGenerator<[LiveRequest](../interfaces/LiveRequest.html), void, undefined>

Implements the async iterator protocol.

#### Returns AsyncGenerator<[LiveRequest](../interfaces/LiveRequest.html), void, undefined>

    * Defined in [core/src/agents/live_request_queue.ts:132](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L132)




### close

  * close(): void

Sends a close signal to the queue.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:75](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L75)




### get

  * get(): Promise<[LiveRequest](../interfaces/LiveRequest.html)>

Retrieves a request from the queue. If the queue is empty, it will wait until a request is available.

#### Returns Promise<[LiveRequest](../interfaces/LiveRequest.html)>

A promise that resolves with the next available request.

    * Defined in [core/src/agents/live_request_queue.ts:60](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L60)




### send

  * send(req: [LiveRequest](../interfaces/LiveRequest.html)): void

Adds a request to the queue. If there is a pending `get()` call, it will be resolved with the given request.

#### Parameters

    * req: [LiveRequest](../interfaces/LiveRequest.html)

The request to send.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L43)




### sendActivityEnd

  * sendActivityEnd(): void

Sends an activity end signal to mark the end of user input.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:124](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L124)




### sendActivityStart

  * sendActivityStart(): void

Sends an activity start signal to mark the beginning of user input.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:117](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L117)




### sendContent

  * sendContent(content: Content): void

Sends a content object to the queue.

#### Parameters

    * content: Content

The content to send.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:102](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L102)




### sendRealtime

  * sendRealtime(blob: Blob_2): void

Sends a blob to the model in realtime mode.

#### Parameters

    * blob: Blob_2

The blob to send.

#### Returns void

    * Defined in [core/src/agents/live_request_queue.ts:110](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/live_request_queue.ts#L110)




Constructors

constructor

Methods

[asyncIterator]closegetsendsendActivityEndsendActivityStartsendContentsendRealtime

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


