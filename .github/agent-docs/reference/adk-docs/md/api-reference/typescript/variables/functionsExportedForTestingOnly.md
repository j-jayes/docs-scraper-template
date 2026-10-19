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
resumeInputsDict?: Record<string, [ResumeInputs](../types/ResumeInputs.html)>;  
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
resumeInputsDict?: Record<string, [ResumeInputs](../types/ResumeInputs.html)>;  
toolConfirmationDict?: Record<string, [ToolConfirmation](../classes/ToolConfirmation.html)>;  
toolsDict: Record<string, [BaseTool](../classes/BaseTool.html)>;  
},  
) => Promise<[Event](../interfaces/Event.html) | null>




  * Defined in [core/src/agents/functions.ts:69](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/functions.ts#L69)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


