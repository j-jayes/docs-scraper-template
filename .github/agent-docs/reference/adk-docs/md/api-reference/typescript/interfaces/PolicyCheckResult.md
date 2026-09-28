[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [PolicyCheckResult]()



# Interface PolicyCheckResult

The result returned by a policy engine after evaluating a tool call.

interface PolicyCheckResult {  
outcome: string;  
reason?: string;  
}

  * Defined in [core/src/plugins/security_plugin.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L40)



## Properties

### outcome

outcome: string

The policy decision: `ALLOW`, `DENY`, or `CONFIRM`.

  * Defined in [core/src/plugins/security_plugin.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L42)



### `Optional`reason

reason?: string

Optional human-readable explanation of the decision.

  * Defined in [core/src/plugins/security_plugin.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L44)



Properties

outcomereason

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


