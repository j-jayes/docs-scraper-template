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

  * Defined in [core/src/plugins/security_plugin.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L41)



## Properties

### outcome

outcome: string

The policy decision: `ALLOW`, `DENY`, or `CONFIRM`.

  * Defined in [core/src/plugins/security_plugin.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L43)



### `Optional`reason

reason?: string

Optional human-readable explanation of the decision.

  * Defined in [core/src/plugins/security_plugin.ts:45](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L45)



Properties

outcomereason

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


