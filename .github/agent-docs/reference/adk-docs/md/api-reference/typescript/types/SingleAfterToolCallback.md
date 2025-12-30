[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleAfterToolCallback]()



# Type Alias SingleAfterToolCallback

SingleAfterToolCallback: (  
params: {  
args: Dict;  
context: [ToolContext](../classes/ToolContext.html);  
response: Dict;  
tool: [BaseTool](../classes/BaseTool.html);  
},  
) => Dict  
| undefined  
| Promise<Dict | undefined>

A callback that runs after a tool is called.

#### Type Declaration

  *     * (  
params: {  
args: Dict;  
context: [ToolContext](../classes/ToolContext.html);  
response: Dict;  
tool: [BaseTool](../classes/BaseTool.html);  
},  
): Dict  
| undefined  
| Promise<Dict | undefined>
    * #### Parameters

      * params: { args: Dict; context: [ToolContext](../classes/ToolContext.html); response: Dict; tool: [BaseTool](../classes/BaseTool.html) }

#### Returns Dict | undefined | Promise<Dict | undefined>

When present, the returned dict will be used as tool result.




  * Defined in [core/src/agents/llm_agent.ts:118](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L118)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


