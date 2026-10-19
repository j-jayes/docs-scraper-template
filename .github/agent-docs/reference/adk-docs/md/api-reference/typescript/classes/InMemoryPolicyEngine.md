[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryPolicyEngine]()



# Class InMemoryPolicyEngine

In-memory policy engine that permits all tool calls. Intended for prototyping.

#### Implements

  * [BasePolicyEngine](../interfaces/BasePolicyEngine.html)



  * Defined in [core/src/plugins/security_plugin.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L68)



## Constructors

### constructor

  * new InMemoryPolicyEngine(): [InMemoryPolicyEngine]()

#### Returns [InMemoryPolicyEngine]()




## Methods

### evaluate

  * evaluate(_context: [ToolCallPolicyContext](../interfaces/ToolCallPolicyContext.html)): Promise<[PolicyCheckResult](../interfaces/PolicyCheckResult.html)>

Always returns [PolicyOutcome.ALLOW](../enums/PolicyOutcome.html#allow) for every tool call.

#### Parameters

    * _context: [ToolCallPolicyContext](../interfaces/ToolCallPolicyContext.html)

The tool and its arguments; ignored.

#### Returns Promise<[PolicyCheckResult](../interfaces/PolicyCheckResult.html)>

A promise resolving to an ALLOW result.

Implementation of [BasePolicyEngine](../interfaces/BasePolicyEngine.html).[evaluate](../interfaces/BasePolicyEngine.html#evaluate)

    * Defined in [core/src/plugins/security_plugin.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L75)




Constructors

constructor

Methods

evaluate

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


