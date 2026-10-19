[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleAfterToolCallback]()



# Type Alias SingleAfterToolCallback

SingleAfterToolCallback: (  
params: {  
args: Record<string, unknown>;  
context: [Context](../classes/Context.html);  
response: Record<string, unknown>;  
tool: [BaseTool](../classes/BaseTool.html);  
},  
) => | Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>

A callback that runs after a tool is called.

#### Type Declaration

  *     * (  
params: {  
args: Record<string, unknown>;  
context: [Context](../classes/Context.html);  
response: Record<string, unknown>;  
tool: [BaseTool](../classes/BaseTool.html);  
},  
): | Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>
    * #### Parameters

      * params: {  
args: Record<string, unknown>;  
context: [Context](../classes/Context.html);  
response: Record<string, unknown>;  
tool: [BaseTool](../classes/BaseTool.html);  
}
        * ##### args: Record<string, unknown>

The arguments to the tool.

        * ##### context: [Context](../classes/Context.html)

Context for the tool call.

        * ##### response: Record<string, unknown>

The response from the tool.

        * ##### tool: [BaseTool](../classes/BaseTool.html)

The tool to be called.

#### Returns   
| Record<string, unknown>  
| undefined  
| Promise<Record<string, unknown> | undefined>

When present, the returned record will be used as tool result.




  * Defined in [core/src/agents/llm_agent.ts:266](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L266)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


