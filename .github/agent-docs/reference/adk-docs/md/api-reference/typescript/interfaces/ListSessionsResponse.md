[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ListSessionsResponse]()



# Interface ListSessionsResponse

The response of listing sessions.

The events and states are not set within each Session object. When no pagination params were requested, `page` is 1, `limit` equals `totalItems`, and `totalPages` is 1 (or 0 when there are no sessions).

interface ListSessionsResponse {  
limit: number;  
page: number;  
sessions: [Session](Session.html)[];  
totalItems: number;  
totalPages: number;  
}

  * Defined in [core/src/sessions/base_session_service.ts:86](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L86)



## Properties

### limit

limit: number

Page size used. Equals `totalItems` when no limit was requested.

  * Defined in [core/src/sessions/base_session_service.ts:92](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L92)



### page

page: number

Current page number (1-based).

  * Defined in [core/src/sessions/base_session_service.ts:90](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L90)



### sessions

sessions: [Session](Session.html)[]

A list of sessions.

  * Defined in [core/src/sessions/base_session_service.ts:88](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L88)



### totalItems

totalItems: number

Total number of sessions matching the request.

  * Defined in [core/src/sessions/base_session_service.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L94)



### totalPages

totalPages: number

Total number of pages.

  * Defined in [core/src/sessions/base_session_service.ts:96](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L96)



Properties

limitpagesessionstotalItemstotalPages

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


