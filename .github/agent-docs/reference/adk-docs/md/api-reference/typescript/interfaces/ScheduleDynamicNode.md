[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ScheduleDynamicNode]()



# Interface ScheduleDynamicNode

Protocol for scheduling a dynamically-invoked node (via `ctx.runNode()`).

Implementations handle fresh execution, deduplication of concurrent calls, and (Phase 5) resumption from session events. Ported from `google/adk-python` `workflow/_schedule_dynamic_node.py`.

interface ScheduleDynamicNode {  
schedule(  
ctx: [NodeContext](../classes/NodeContext.html),  
node: [BaseNode](../classes/BaseNode.html),  
input: unknown,  
options: [ScheduleDynamicNodeOptions](ScheduleDynamicNodeOptions.html),  
): Promise<[NodeContext](../classes/NodeContext.html) | [NodeResult](NodeResult.html)>;  
}

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L36)



## Methods

### schedule

  * schedule(  
ctx: [NodeContext](../classes/NodeContext.html),  
node: [BaseNode](../classes/BaseNode.html),  
input: unknown,  
options: [ScheduleDynamicNodeOptions](ScheduleDynamicNodeOptions.html),  
): Promise<[NodeContext](../classes/NodeContext.html) | [NodeResult](NodeResult.html)>

#### Parameters

    * ctx: [NodeContext](../classes/NodeContext.html)
    * node: [BaseNode](../classes/BaseNode.html)
    * input: unknown
    * options: [ScheduleDynamicNodeOptions](ScheduleDynamicNodeOptions.html)

#### Returns Promise<[NodeContext](../classes/NodeContext.html) | [NodeResult](NodeResult.html)>

    * Defined in [core/src/workflow/schedule_dynamic_node.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L37)




Methods

schedule

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


