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




  * Defined in [core/src/agents/routed_agent.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/routed_agent.ts#L36)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


