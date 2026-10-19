[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeTimeoutError]()



# Class NodeTimeoutError

Raised when a node exceeds its configured timeout.

This is a regular `Error` (retryable) so a timed-out node can be retried via `retryConfig`.

#### Hierarchy

  * Error
    * NodeTimeoutError



  * Defined in [core/src/workflow/errors.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/errors.ts#L48)



## Constructors

### constructor

  * new NodeTimeoutError(  
options: { nodeName: string; timeout: number },  
): [NodeTimeoutError]()

#### Parameters

    * options: { nodeName: string; timeout: number }
      * ##### nodeName: string

The name of the node that timed out.

      * ##### timeout: number

The timeout, in seconds, that was exceeded.

#### Returns [NodeTimeoutError]()

Overrides Error.constructor

    * Defined in [core/src/workflow/errors.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/errors.ts#L56)




## Properties

### `Readonly`nodeName

nodeName: string

  * Defined in [core/src/workflow/errors.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/errors.ts#L49)



### `Readonly`timeout

timeout: number

  * Defined in [core/src/workflow/errors.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/errors.ts#L50)



Constructors

constructor

Properties

nodeNametimeout

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


