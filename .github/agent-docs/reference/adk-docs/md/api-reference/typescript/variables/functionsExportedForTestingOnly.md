[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [functionsExportedForTestingOnly]()



# Variable functionsExportedForTestingOnly`Const`

functionsExportedForTestingOnly: {  
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




  * Defined in [core/src/agents/functions.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/functions.ts#L27)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


