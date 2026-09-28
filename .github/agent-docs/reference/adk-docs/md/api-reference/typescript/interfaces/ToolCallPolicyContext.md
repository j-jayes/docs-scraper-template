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

  * Defined in [core/src/plugins/security_plugin.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L48)



## Properties

### tool

tool: [BaseTool](../classes/BaseTool.html)

The tool being invoked.

  * Defined in [core/src/plugins/security_plugin.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L50)



### toolArgs

toolArgs: Record<string, unknown>

The arguments supplied to the tool call.

  * Defined in [core/src/plugins/security_plugin.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/security_plugin.ts#L52)



Properties

tooltoolArgs

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


