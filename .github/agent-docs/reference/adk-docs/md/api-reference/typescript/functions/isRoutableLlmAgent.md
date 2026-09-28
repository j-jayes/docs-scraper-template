[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [isRoutableLlmAgent]()



# Function isRoutableLlmAgent

  * isRoutableLlmAgent(agentToRun: [BaseAgent](../classes/BaseAgent.html)): boolean

Whether the agent to run can transfer to any other agent in the agent tree.

An agent is transferable if:

    * It is an instance of `LlmAgent`.
    * All its ancestors are also transferable (i.e., they have `disallowTransferToParent` set to false).

#### Parameters

    * agentToRun: [BaseAgent](../classes/BaseAgent.html)

The agent to check for transferability.

#### Returns boolean

True if the agent can transfer, False otherwise.

    * Defined in [core/src/runner/runner.ts:642](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L642)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


