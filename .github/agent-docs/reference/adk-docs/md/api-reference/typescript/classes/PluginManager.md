[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [PluginManager]()



# Class PluginManager

Manages the registration and execution of plugins.

The PluginManager is an internal class that orchestrates the invocation of plugin callbacks at key points in the SDK's execution lifecycle. It maintains a list of registered plugins and ensures they are called in the order they were registered.

The core execution logic implements an "early exit" strategy: if any plugin callback returns a non-`undefined` value, the execution of subsequent plugins for that specific event is halted, and the returned value is propagated up the call stack. This allows plugins to short-circuit operations like agent runs, tool calls, or model requests.

  * Defined in [core/src/plugins/plugin_manager.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L34)



## Constructors

### constructor

  * new PluginManager(plugins?: [BasePlugin](BasePlugin.html)[]): [PluginManager]()

Initializes the plugin service.

#### Parameters

    * `Optional`plugins: [BasePlugin](BasePlugin.html)[]

An optional list of plugins to register upon initialization.

#### Returns [PluginManager]()

    * Defined in [core/src/plugins/plugin_manager.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L42)




## Methods

### getPlugin

  * getPlugin(pluginName: string): [BasePlugin](BasePlugin.html) | undefined

Retrieves a registered plugin by its name.

#### Parameters

    * pluginName: string

The name of the plugin to retrieve.

#### Returns [BasePlugin](BasePlugin.html) | undefined

The plugin instance if found, otherwise `undefined`.

    * Defined in [core/src/plugins/plugin_manager.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L77)




### registerPlugin

  * registerPlugin(plugin: [BasePlugin](BasePlugin.html)): void

Registers a new plugin.

#### Parameters

    * plugin: [BasePlugin](BasePlugin.html)

The plugin instance to register.

#### Returns void

#### Throws

If the same exact plugin or a plugin with the same name is already registered.

    * Defined in [core/src/plugins/plugin_manager.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L57)




### runAfterAgentCallback

  * runAfterAgentCallback(  
__namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Runs the `afterAgentCallback` for all plugins.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:204](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L204)




### runAfterContextCompaction

  * runAfterContextCompaction(  
__namedParameters: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Runs the `afterContextCompaction` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }

#### Returns Promise<void>

    * Defined in [core/src/plugins/plugin_manager.ts:258](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L258)




### runAfterModelCallback

  * runAfterModelCallback(  
__namedParameters: {  
callbackContext: [Context](Context.html);  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `afterModelCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:356](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L356)




### runAfterRunCallback

  * runAfterRunCallback(  
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Runs the `afterRunCallback` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<void>

    * Defined in [core/src/plugins/plugin_manager.ts:153](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L153)




### runAfterToolCallback

  * runAfterToolCallback(  
__namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `afterToolCallback` for all plugins.

#### Parameters

    * __namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:296](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L296)




### runBeforeAgentCallback

  * runBeforeAgentCallback(  
__namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Runs the `beforeAgentCallback` for all plugins.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:186](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L186)




### runBeforeContextCompaction

  * runBeforeContextCompaction(  
__namedParameters: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Runs the `beforeContextCompaction` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }

#### Returns Promise<void>

    * Defined in [core/src/plugins/plugin_manager.ts:240](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L240)




### runBeforeModelCallback

  * runBeforeModelCallback(  
__namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `beforeModelCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:338](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L338)




### runBeforeRunCallback

  * runBeforeRunCallback(  
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Runs the `beforeRunCallback` for all plugins.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<Content | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:138](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L138)




### runBeforeToolCallback

  * runBeforeToolCallback(  
__namedParameters: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `beforeToolCallback` for all plugins.

#### Parameters

    * __namedParameters: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [Context](Context.html) }

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:276](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L276)




### runBeforeToolSelection

  * runBeforeToolSelection(  
__namedParameters: {  
callbackContext: [Context](Context.html);  
tools: Readonly<Record<string, [BaseTool](BaseTool.html)>>;  
},  
): Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

Runs the `beforeToolSelection` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); tools: Readonly<Record<string, [BaseTool](BaseTool.html)>> }

#### Returns Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:222](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L222)




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

    * Defined in [core/src/plugins/plugin_manager.ts:168](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L168)




### runOnModelErrorCallback

  * runOnModelErrorCallback(  
__namedParameters: {  
callbackContext: [Context](Context.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Runs the `onModelErrorCallback` for all plugins.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:318](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L318)




### runOnToolErrorCallback

  * runOnToolErrorCallback(  
__namedParameters: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Runs the `onToolErrorCallback` for all plugins.

#### Parameters

    * __namedParameters: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

    * Defined in [core/src/plugins/plugin_manager.ts:374](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L374)




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

    * Defined in [core/src/plugins/plugin_manager.ts:120](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/plugin_manager.ts#L120)




Constructors

constructor

Methods

getPluginregisterPluginrunAfterAgentCallbackrunAfterContextCompactionrunAfterModelCallbackrunAfterRunCallbackrunAfterToolCallbackrunBeforeAgentCallbackrunBeforeContextCompactionrunBeforeModelCallbackrunBeforeRunCallbackrunBeforeToolCallbackrunBeforeToolSelectionrunOnEventCallbackrunOnModelErrorCallbackrunOnToolErrorCallbackrunOnUserMessageCallback

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


