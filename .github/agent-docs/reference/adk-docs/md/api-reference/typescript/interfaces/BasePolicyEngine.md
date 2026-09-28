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



  * Defined in [core/src/plugins/security_plugin.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L56)



## Methods

### evaluate

  * evaluate(context: [ToolCallPolicyContext](ToolCallPolicyContext.html)): Promise<[PolicyCheckResult](PolicyCheckResult.html)>

Evaluates whether a tool call should be allowed, denied, or confirmed.

#### Parameters

    * context: [ToolCallPolicyContext](ToolCallPolicyContext.html)

The tool and its arguments to evaluate.

#### Returns Promise<[PolicyCheckResult](PolicyCheckResult.html)>

A promise resolving to the policy decision.

    * Defined in [core/src/plugins/security_plugin.ts:63](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L63)




Methods

evaluate

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


