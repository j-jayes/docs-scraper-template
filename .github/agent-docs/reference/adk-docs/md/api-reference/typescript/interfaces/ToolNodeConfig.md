[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolNodeConfig]()



# Interface ToolNodeConfig

Options for a [ToolNode](../classes/ToolNode.html).

interface ToolNodeConfig {  
description?: string;  
inputSchema?: [SchemaLike](../types/SchemaLike.html);  
isolationScope?: string | true;  
name?: string;  
outputSchema?: [SchemaLike](../types/SchemaLike.html);  
rerunOnResume?: boolean;  
retryConfig?: [RetryConfig](RetryConfig.html);  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
timeout?: number;  
waitForOutput?: boolean;  
}

#### Hierarchy

  * Partial<Omit<[BaseNodeConfig](BaseNodeConfig.html), "name">>
    * ToolNodeConfig



  * Defined in [core/src/workflow/nodes/tool_node.ts:15](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/tool_node.ts#L15)



## Properties

### `Optional`description

description?: string

Human-readable description (used when a node is exposed as a tool).

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[description](BaseNodeConfig.html#description)

  * Defined in [core/src/workflow/base_node.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L41)



### `Optional`inputSchema

inputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node input (Zod v3/v4 or genai `Schema`).

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[inputSchema](BaseNodeConfig.html#inputschema)

  * Defined in [core/src/workflow/base_node.ts:62](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L62)



### `Optional`isolationScope

isolationScope?: string | true

Runs this node's subtree in an isolated conversation scope: an agent inside it sees only session events carrying the same scope, plus untagged ones. `true` derives a scope per node run; a string is an explicit shared tag.

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[isolationScope](BaseNodeConfig.html#isolationscope)

  * Defined in [core/src/workflow/base_node.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L75)



### `Optional`name

name?: string

Optional name override; defaults to the tool's name.

  * Defined in [core/src/workflow/nodes/tool_node.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/tool_node.ts#L17)



### `Optional`outputSchema

outputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node output (Zod v3/v4 or genai `Schema`).

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[outputSchema](BaseNodeConfig.html#outputschema)

  * Defined in [core/src/workflow/base_node.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L65)



### `Optional`rerunOnResume

rerunOnResume?: boolean

If true, the node re-executes when a workflow resumes even if it already completed in a prior turn. Default false.

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[rerunOnResume](BaseNodeConfig.html#rerunonresume)

  * Defined in [core/src/workflow/base_node.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L47)



### `Optional`retryConfig

retryConfig?: [RetryConfig](RetryConfig.html)

Optional retry configuration for transient failures.

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[retryConfig](BaseNodeConfig.html#retryconfig)

  * Defined in [core/src/workflow/base_node.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L56)



### `Optional`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating relevant session state (Zod v3/v4 or genai `Schema`).

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[stateSchema](BaseNodeConfig.html#stateschema)

  * Defined in [core/src/workflow/base_node.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L68)



### `Optional`timeout

timeout?: number

Maximum time, in seconds, for this node to complete.

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[timeout](BaseNodeConfig.html#timeout)

  * Defined in [core/src/workflow/base_node.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L59)



### `Optional`waitForOutput

waitForOutput?: boolean

If true, the node only produces its output once all of its predecessors have triggered it (fan-in / join semantics). Default false.

Inherited from [BaseNodeConfig](BaseNodeConfig.html).[waitForOutput](BaseNodeConfig.html#waitforoutput)

  * Defined in [core/src/workflow/base_node.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L53)



Properties

descriptioninputSchemaisolationScopenameoutputSchemarerunOnResumeretryConfigstateSchematimeoutwaitForOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


