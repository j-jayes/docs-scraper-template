[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryPolicyEngine]()



# Class InMemoryPolicyEngine

In-memory policy engine that permits all tool calls. Intended for prototyping.

#### Implements

  * [BasePolicyEngine](../interfaces/BasePolicyEngine.html)



  * Defined in [core/src/plugins/security_plugin.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L67)



## Constructors

### constructor

  * new InMemoryPolicyEngine(): [InMemoryPolicyEngine]()

#### Returns [InMemoryPolicyEngine]()




## Methods

### evaluate

  * evaluate(): Promise<[PolicyCheckResult](../interfaces/PolicyCheckResult.html)>

Always returns [PolicyOutcome.ALLOW](../enums/PolicyOutcome.html#allow) for every tool call.

#### Returns Promise<[PolicyCheckResult](../interfaces/PolicyCheckResult.html)>

A promise resolving to an ALLOW result.

Implementation of [BasePolicyEngine](../interfaces/BasePolicyEngine.html).[evaluate](../interfaces/BasePolicyEngine.html#evaluate)

    * Defined in [core/src/plugins/security_plugin.ts:73](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L73)




Constructors

constructor

Methods

evaluate

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


