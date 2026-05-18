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




  * Defined in [agents/functions.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/functions.ts#L35)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


