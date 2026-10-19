[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BasePolicyEngine]()



# Interface BasePolicyEngine

Interface for policy engines that gate tool call execution.

interface BasePolicyEngine {  
evaluate(context: [ToolCallPolicyContext](ToolCallPolicyContext.html)): Promise<[PolicyCheckResult](PolicyCheckResult.html)>;  
}

#### Implemented by

  * [InMemoryPolicyEngine](../classes/InMemoryPolicyEngine.html)



  * Defined in [core/src/plugins/security_plugin.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L57)



## Methods

### evaluate

  * evaluate(context: [ToolCallPolicyContext](ToolCallPolicyContext.html)): Promise<[PolicyCheckResult](PolicyCheckResult.html)>

Evaluates whether a tool call should be allowed, denied, or confirmed.

#### Parameters

    * context: [ToolCallPolicyContext](ToolCallPolicyContext.html)

The tool and its arguments to evaluate.

#### Returns Promise<[PolicyCheckResult](PolicyCheckResult.html)>

A promise resolving to the policy decision.

    * Defined in [core/src/plugins/security_plugin.ts:64](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L64)




Methods

evaluate

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


