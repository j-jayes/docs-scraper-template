[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentRouter]()



# Type Alias AgentRouter

AgentRouter: (  
agents: Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)>>,  
context: [InvocationContext](../classes/InvocationContext.html),  
errorContext?: { failedKeys: ReadonlySet<string>; lastError: unknown },  
) => Promise<string | undefined> | string | undefined

Type definition for a function that selects an agent based on the invocation context.

#### Type Declaration

  *     * (  
agents: Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)>>,  
context: [InvocationContext](../classes/InvocationContext.html),  
errorContext?: { failedKeys: ReadonlySet<string>; lastError: unknown },  
): Promise<string | undefined> | string | undefined
    * #### Parameters

      * agents: Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)>>
      * context: [InvocationContext](../classes/InvocationContext.html)
      * `Optional`errorContext: { failedKeys: ReadonlySet<string>; lastError: unknown }

#### Returns Promise<string | undefined> | string | undefined




  * Defined in [core/src/agents/routed_agent.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L37)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


