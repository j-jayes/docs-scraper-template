[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolCallPolicyContext]()



# Interface ToolCallPolicyContext

Context passed to a policy engine when evaluating a tool call.

interface ToolCallPolicyContext {  
tool: [BaseTool](../classes/BaseTool.html);  
toolArgs: Record<string, unknown>;  
}

  * Defined in [core/src/plugins/security_plugin.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L49)



## Properties

### tool

tool: [BaseTool](../classes/BaseTool.html)

The tool being invoked.

  * Defined in [core/src/plugins/security_plugin.ts:51](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L51)



### toolArgs

toolArgs: Record<string, unknown>

The arguments supplied to the tool call.

  * Defined in [core/src/plugins/security_plugin.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/security_plugin.ts#L53)



Properties

tooltoolArgs

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


