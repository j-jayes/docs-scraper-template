[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolConfirmation]()



# Class ToolConfirmation`Experimental`

Represents a tool confirmation configuration. (Experimental, subject to change)

  * Defined in [core/src/tools/tool_confirmation.ts:11](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/tool_confirmation.ts#L11)



## Constructors

### constructor

  * new ToolConfirmation(  
__namedParameters: {  
confirmed: boolean;  
hint?: string;  
payload?: unknown;  
},  
): [ToolConfirmation]()

`Experimental`

#### Parameters

    * __namedParameters: { confirmed: boolean; hint?: string; payload?: unknown }

#### Returns [ToolConfirmation]()

    * Defined in [core/src/tools/tool_confirmation.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/tool_confirmation.ts#L24)




## Properties

### `Experimental`confirmed

confirmed: boolean

Whether the tool execution is confirmed.

  * Defined in [core/src/tools/tool_confirmation.ts:16](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/tool_confirmation.ts#L16)



### `Experimental`hint

hint: string

The hint text for why the input is needed.

  * Defined in [core/src/tools/tool_confirmation.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/tool_confirmation.ts#L13)



### `Optional` `Experimental`payload

payload?: unknown

The custom data payload needed from the user to continue the flow. It should be JSON serializable.

  * Defined in [core/src/tools/tool_confirmation.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/tool_confirmation.ts#L22)



Constructors

constructor

Properties

confirmedhintpayload

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


