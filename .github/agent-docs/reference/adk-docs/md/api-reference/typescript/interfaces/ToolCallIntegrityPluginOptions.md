[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolCallIntegrityPluginOptions]()



# Interface ToolCallIntegrityPluginOptions

Options for [ToolCallIntegrityPlugin](../classes/ToolCallIntegrityPlugin.html).

interface ToolCallIntegrityPluginOptions {  
allowUnstampedCalls?: boolean;  
name?: string;  
secretKey:  
| Uint8Array<ArrayBufferLike>  
| readonly Uint8Array<ArrayBufferLike>[];  
}

  * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L43)



## Properties

### `Optional`allowUnstampedCalls

allowUnstampedCalls?: boolean

Log a warning instead of throwing for function calls that have no stamp, such as calls stored before the plugin was installed. Such calls also run, so this reports tampering that removes a stamp but does not prevent it. A stamp that is present but wrong is always rejected. Defaults to `false`.

  * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L56)



### `Optional`name

name?: string

The plugin name. Defaults to `'tool_call_integrity'`.

  * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L59)



### secretKey

secretKey: Uint8Array<ArrayBufferLike> | readonly Uint8Array<ArrayBufferLike>[]

The HMAC key, or a list of keys during rotation. The first key stamps new calls; every key is accepted when verifying.

  * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L48)



Properties

allowUnstampedCallsnamesecretKey

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


