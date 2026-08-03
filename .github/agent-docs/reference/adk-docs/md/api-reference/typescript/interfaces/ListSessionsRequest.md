[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ListSessionsRequest]()



# Interface ListSessionsRequest

The parameters for `listSessions`.

interface ListSessionsRequest {  
appName: string;  
limit?: number;  
offset?: number;  
order?: "asc" | "desc";  
page?: number;  
userId: string;  
}

  * Defined in [core/src/sessions/base_session_service.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L49)



## Properties

### appName

appName: string

The name of the application.

  * Defined in [core/src/sessions/base_session_service.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L51)



### `Optional`limit

limit?: number

Maximum number of sessions to return.

  * Defined in [core/src/sessions/base_session_service.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L55)



### `Optional`offset

offset?: number

Zero-based index of the first session to return. Ignored if `page` is set.

  * Defined in [core/src/sessions/base_session_service.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L57)



### `Optional`order

order?: "asc" | "desc"

Sort direction by last update time. No ordering is applied if omitted.

  * Defined in [core/src/sessions/base_session_service.ts:61](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L61)



### `Optional`page

page?: number

1-based page number. Requires `limit`. Takes precedence over `offset`.

  * Defined in [core/src/sessions/base_session_service.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L59)



### userId

userId: string

The ID of the user.

  * Defined in [core/src/sessions/base_session_service.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L53)



Properties

appNamelimitoffsetorderpageuserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


