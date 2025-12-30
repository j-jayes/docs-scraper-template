[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [PluginManager]()



# Class PluginManager

Manages the registration and execution of plugins.

The PluginManager is an internal class that orchestrates the invocation of plugin callbacks at key points in the SDK's execution lifecycle. It maintains a list of registered plugins and ensures they are called in the order they were registered.

The core execution logic implements an "early exit" strategy: if any plugin callback returns a non-`undefined` value, the execution of subsequent plugins for that specific event is halted, and the returned value is propagated up the call stack. This allows plugins to short-circuit operations like agent runs, tool calls, or model requests.

  * Defined in [core/src/plugins/plugin_manager.ts:35](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L35)



## Constructors

### constructor

  * new PluginManager(plugins?: [BasePlugin](BasePlugin.html)[]): [PluginManager]()

Initializes the plugin service.

#### Parameters

    * `Optional`plugins: [BasePlugin](BasePlugin.html)[]

An optional list of plugins to register upon initialization.

#### Returns [PluginManager]()

    * Defined in [core/src/plugins/plugin_manager.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L43)




## Methods

### getPlugin

  * getPlugin(pluginName: string): [BasePlugin](BasePlugin.html) | undefined

Retrieves a registered plugin by its name.

#### Parameters

    * pluginName: string

The name of the plugin to retrieve.

#### Returns [BasePlugin](BasePlugin.html) | undefined

The plugin instance if found, otherwise `undefined`.

    * Defined in [core/src/plugins/plugin_manager.ts:78](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L78)




### registerPlugin

  * registerPlugin(plugin: [BasePlugin](BasePlugin.html)): void

Registers a new plugin.

#### Parameters

    * plugin: [BasePlugin](BasePlugin.html)

The plugin instance to register.

#### Returns void

#### Throws

If the same exact plugin or a plugin with the same name is already registered.

    * Defined in [core/src/plugins/plugin_manager.ts:58](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L58)




### runAfterAgentCallback

  * runAfterAgentCallback(  
__namedParameters: {  
agent: [BaseAgent](BaseAgent.html);  
callbackContext: [CallbackContext](CallbackContext.html);  
},  
): Promise<Content | undefined>

Runs the `afterAgentCallback` for all plugins.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:196](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L196)




### runAfterModelCallback

  * runAfterModelCallback(  
__namedParameters: {  
callbackContext: [CallbackContext](CallbackContext.html);  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `afterModelCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [CallbackContext](CallbackContext.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:272](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L272)




### runAfterRunCallback

  * runAfterRunCallback(  
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Runs the `afterRunCallback` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<void>

    * Defined in [core/src/plugins/plugin_manager.ts:153](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L153)




### runAfterToolCallback

  * runAfterToolCallback(  
__namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `afterToolCallback` for all plugins.

#### Parameters

    * __namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:226](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L226)




### runBeforeAgentCallback

  * runBeforeAgentCallback(  
__namedParameters: {  
agent: [BaseAgent](BaseAgent.html);  
callbackContext: [CallbackContext](CallbackContext.html);  
},  
): Promise<Content | undefined>

Runs the `beforeAgentCallback` for all plugins.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:181](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L181)




### runBeforeModelCallback

  * runBeforeModelCallback(  
__namedParameters: {  
callbackContext: [CallbackContext](CallbackContext.html);  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `beforeModelCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [CallbackContext](CallbackContext.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:257](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L257)




### runBeforeRunCallback

  * runBeforeRunCallback(  
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Runs the `beforeRunCallback` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:138](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L138)




### runBeforeToolCallback

  * runBeforeToolCallback(  
__namedParameters: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `beforeToolCallback` for all plugins.

#### Parameters

    * __namedParameters: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [ToolContext](ToolContext.html) }

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:211](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L211)




### runOnEventCallback

  * runOnEventCallback(  
__namedParameters: {  
event: [Event](../interfaces/Event.html);  
invocationContext: [InvocationContext](InvocationContext.html);  
},  
): Promise<[Event](../interfaces/Event.html) | undefined>

Runs the `onEventCallback` for all plugins.

#### Parameters

    * __namedParameters: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:166](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L166)




### runOnModelErrorCallback

  * runOnModelErrorCallback(  
__namedParameters: {  
callbackContext: [CallbackContext](CallbackContext.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `onModelErrorCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [CallbackContext](CallbackContext.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:242](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L242)




### runOnToolErrorCallback

  * runOnToolErrorCallback(  
__namedParameters: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `onToolErrorCallback` for all plugins.

#### Parameters

    * __namedParameters: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:287](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L287)




### runOnUserMessageCallback

  * runOnUserMessageCallback(  
__namedParameters: {  
invocationContext: [InvocationContext](InvocationContext.html);  
userMessage: Content;  
},  
): Promise<Content | undefined>

Runs the `onUserMessageCallback` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:122](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/plugin_manager.ts#L122)




Constructors

constructor

Methods

getPluginregisterPluginrunAfterAgentCallbackrunAfterModelCallbackrunAfterRunCallbackrunAfterToolCallbackrunBeforeAgentCallbackrunBeforeModelCallbackrunBeforeRunCallbackrunBeforeToolCallbackrunOnEventCallbackrunOnModelErrorCallbackrunOnToolErrorCallbackrunOnUserMessageCallback

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


