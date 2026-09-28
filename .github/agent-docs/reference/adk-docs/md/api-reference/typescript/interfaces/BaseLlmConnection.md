[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseLlmConnection]()



# Interface BaseLlmConnection

The base class for a live model connection.

interface BaseLlmConnection {  
close(): Promise<void>;  
receive(): AsyncGenerator<[LlmResponse](LlmResponse.html), void, void>;  
sendActivityEnd?(): Promise<void>;  
sendActivityStart?(): Promise<void>;  
sendContent(content: Content): Promise<void>;  
sendHistory(history: Content[]): Promise<void>;  
sendRealtime(blob: Blob_2): Promise<void>;  
}

  * Defined in [core/src/models/base_llm_connection.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L14)



## Methods

### close

  * close(): Promise<void>

Closes the llm server connection.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:69](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L69)




### receive

  * receive(): AsyncGenerator<[LlmResponse](LlmResponse.html), void, void>

Receives the model response using the llm server connection.

#### Returns AsyncGenerator<[LlmResponse](LlmResponse.html), void, void>

A generator of LlmResponse.

    * Defined in [core/src/models/base_llm_connection.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L64)




### `Optional`sendActivityEnd

  * sendActivityEnd?(): Promise<void>

Optionally signals the end of user activity (e.g. user finishes speaking) for models that support manual activity boundaries.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L57)




### `Optional`sendActivityStart

  * sendActivityStart?(): Promise<void>

Optionally signals the start of user activity (e.g. user begins speaking) for models that support manual activity boundaries.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L51)




### sendContent

  * sendContent(content: Content): Promise<void>

Sends the content to the model.

The model will respond immediately upon receiving the content. If you send function responses, all parts in the content should be function responses.

#### Parameters

    * content: Content

The content to send to the model.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L35)




### sendHistory

  * sendHistory(history: Content[]): Promise<void>

Sends the conversation history to the model.

You call this method right after setting up the model connection. The model will respond if the last content is from user, otherwise it will wait for new user input before responding.

#### Parameters

    * history: Content[]

The conversation history to send to the model.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L24)




### sendRealtime

  * sendRealtime(blob: Blob_2): Promise<void>

Sends a chunk of audio or a frame of video to the model in realtime.

The model may not respond immediately upon receiving the blob. It will do voice activity detection and decide when to respond.

#### Parameters

    * blob: Blob_2

The blob to send to the model.

#### Returns Promise<void>

    * Defined in [core/src/models/base_llm_connection.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm_connection.ts#L45)




Methods

closereceivesendActivityEndsendActivityStartsendContentsendHistorysendRealtime

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


