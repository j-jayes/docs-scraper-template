[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleBeforeToolCallback]()



# Type Alias SingleBeforeToolCallback

SingleBeforeToolCallback: (  
params: {  
args: Record<string, unknown>;  
context: [Context](../classes/Context.html);  
tool: [BaseTool](../classes/BaseTool.html);  
},  
) => | Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>

A callback that runs before a tool is called.

#### Type Declaration

  *     * (  
params: {  
args: Record<string, unknown>;  
context: [Context](../classes/Context.html);  
tool: [BaseTool](../classes/BaseTool.html);  
},  
): | Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>
    * #### Parameters

      * params: { args: Record<string, unknown>; context: [Context](../classes/Context.html); tool: [BaseTool](../classes/BaseTool.html) }
        * ##### args: Record<string, unknown>

The arguments to the tool.

        * ##### context: [Context](../classes/Context.html)

Context for the tool call.

        * ##### tool: [BaseTool](../classes/BaseTool.html)

The tool to be called.

#### Returns   
| Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>

The tool response. When present, the returned tool response will be used and the framework will skip calling the actual tool.




  * Defined in [core/src/agents/llm_agent.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L143)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


