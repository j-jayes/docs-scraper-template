[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleBeforeToolCallback]()



# Type Alias SingleBeforeToolCallback

SingleBeforeToolCallback: (  
params: { args: Dict; context: [ToolContext](../classes/ToolContext.html); tool: [BaseTool](../classes/BaseTool.html) },  
) => Dict | undefined | Promise<Dict | undefined>

A callback that runs before a tool is called.

#### Type Declaration

  *     * (  
params: { args: Dict; context: [ToolContext](../classes/ToolContext.html); tool: [BaseTool](../classes/BaseTool.html) },  
): Dict | undefined | Promise<Dict | undefined>
    * #### Parameters

      * params: { args: Dict; context: [ToolContext](../classes/ToolContext.html); tool: [BaseTool](../classes/BaseTool.html) }

#### Returns Dict | undefined | Promise<Dict | undefined>

The tool response. When present, the returned tool response will be used and the framework will skip calling the actual tool.




  * Defined in [core/src/agents/llm_agent.ts:96](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L96)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


