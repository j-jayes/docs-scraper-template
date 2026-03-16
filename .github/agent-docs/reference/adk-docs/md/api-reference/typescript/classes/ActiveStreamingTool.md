[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ActiveStreamingTool]()



# Class ActiveStreamingTool

Manages streaming tool related resources during invocation.

  * Defined in [agents/active_streaming_tool.ts:20](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/active_streaming_tool.ts#L20)



## Constructors

### constructor

  * new ActiveStreamingTool(params?: [ActiveStreamingToolParams](../interfaces/ActiveStreamingToolParams.html)): [ActiveStreamingTool]()

#### Parameters

    * params: [ActiveStreamingToolParams](../interfaces/ActiveStreamingToolParams.html) = {}

#### Returns [ActiveStreamingTool]()

    * Defined in [agents/active_streaming_tool.ts:33](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/active_streaming_tool.ts#L33)




## Properties

### `Optional`stream

stream?: [LiveRequestQueue](LiveRequestQueue.html)

The active (input) streams of this streaming tool.

  * Defined in [agents/active_streaming_tool.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/active_streaming_tool.ts#L31)



### `Optional`task

task?: Promise<void>

The active task of this streaming tool. TODO: Replace 'Promise' with a proper Task type if available in this env.

  * Defined in [agents/active_streaming_tool.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/active_streaming_tool.ts#L26)



Constructors

constructor

Properties

streamtask

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


