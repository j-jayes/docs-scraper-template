[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [functionsExportedForTestingOnly]()



# Variable functionsExportedForTestingOnly`Const`

functionsExportedForTestingOnly: {  
generateAuthEvent: (  
invocationContext: [InvocationContext](../classes/InvocationContext.html),  
functionResponseEvent: [Event](../interfaces/Event.html),  
) => [Event](../interfaces/Event.html) | undefined;  
generateRequestConfirmationEvent: (  
__namedParameters: {  
functionCallEvent: [Event](../interfaces/Event.html);  
functionResponseEvent: [Event](../interfaces/Event.html);  
invocationContext: [InvocationContext](../classes/InvocationContext.html);  
},  
) => [Event](../interfaces/Event.html)  
| undefined;  
handleFunctionCallList: (  
__namedParameters: {  
afterToolCallbacks: [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[];  
beforeToolCallbacks: [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[];  
filters?: Set<string>;  
functionCalls: FunctionCall[];  
invocationContext: [InvocationContext](../classes/InvocationContext.html);  
toolConfirmationDict?: Record<string, [ToolConfirmation](../classes/ToolConfirmation.html)>;  
toolsDict: Record<string, [BaseTool](../classes/BaseTool.html)>;  
},  
) => Promise<[Event](../interfaces/Event.html) | null>;  
} = ...

#### Type Declaration

  * ##### generateAuthEvent: (  
invocationContext: [InvocationContext](../classes/InvocationContext.html),  
functionResponseEvent: [Event](../interfaces/Event.html),  
) => [Event](../interfaces/Event.html) | undefined

  * ##### generateRequestConfirmationEvent: (  
__namedParameters: {  
functionCallEvent: [Event](../interfaces/Event.html);  
functionResponseEvent: [Event](../interfaces/Event.html);  
invocationContext: [InvocationContext](../classes/InvocationContext.html);  
},  
) => [Event](../interfaces/Event.html)  
| undefined

  * ##### handleFunctionCallList: (  
__namedParameters: {  
afterToolCallbacks: [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[];  
beforeToolCallbacks: [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[];  
filters?: Set<string>;  
functionCalls: FunctionCall[];  
invocationContext: [InvocationContext](../classes/InvocationContext.html);  
toolConfirmationDict?: Record<string, [ToolConfirmation](../classes/ToolConfirmation.html)>;  
toolsDict: Record<string, [BaseTool](../classes/BaseTool.html)>;  
},  
) => Promise<[Event](../interfaces/Event.html) | null>




  * Defined in [core/src/agents/functions.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/functions.ts#L44)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


