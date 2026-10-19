[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseNodeConfig]()



# Interface BaseNodeConfig

Configuration shared by all workflow nodes.

Mirrors the fields of `google/adk-python` `workflow/_base_node.py::BaseNode`.

interface BaseNodeConfig {  
description?: string;  
inputSchema?: [SchemaLike](../types/SchemaLike.html);  
isolationScope?: string | true;  
name: string;  
outputSchema?: [SchemaLike](../types/SchemaLike.html);  
rerunOnResume?: boolean;  
retryConfig?: [RetryConfig](RetryConfig.html);  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
timeout?: number;  
waitForOutput?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#BaseNodeConfig))

  * BaseNodeConfig
    * [BaseAgentConfig](BaseAgentConfig.html)



  * Defined in [core/src/workflow/base_node.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L36)



## Properties

### `Optional`description

description?: string

Human-readable description (used when a node is exposed as a tool).

  * Defined in [core/src/workflow/base_node.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L41)



### `Optional`inputSchema

inputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node input (Zod v3/v4 or genai `Schema`).

  * Defined in [core/src/workflow/base_node.ts:62](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L62)



### `Optional`isolationScope

isolationScope?: string | true

Runs this node's subtree in an isolated conversation scope: an agent inside it sees only session events carrying the same scope, plus untagged ones. `true` derives a scope per node run; a string is an explicit shared tag.

  * Defined in [core/src/workflow/base_node.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L75)



### name

name: string

Canonical, unique-within-a-graph node name.

  * Defined in [core/src/workflow/base_node.ts:38](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L38)



### `Optional`outputSchema

outputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node output (Zod v3/v4 or genai `Schema`).

  * Defined in [core/src/workflow/base_node.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L65)



### `Optional`rerunOnResume

rerunOnResume?: boolean

If true, the node re-executes when a workflow resumes even if it already completed in a prior turn. Default false.

  * Defined in [core/src/workflow/base_node.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L47)



### `Optional`retryConfig

retryConfig?: [RetryConfig](RetryConfig.html)

Optional retry configuration for transient failures.

  * Defined in [core/src/workflow/base_node.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L56)



### `Optional`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating relevant session state (Zod v3/v4 or genai `Schema`).

  * Defined in [core/src/workflow/base_node.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L68)



### `Optional`timeout

timeout?: number

Maximum time, in seconds, for this node to complete.

  * Defined in [core/src/workflow/base_node.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L59)



### `Optional`waitForOutput

waitForOutput?: boolean

If true, the node only produces its output once all of its predecessors have triggered it (fan-in / join semantics). Default false.

  * Defined in [core/src/workflow/base_node.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L53)



Properties

descriptioninputSchemaisolationScopenameoutputSchemarerunOnResumeretryConfigstateSchematimeoutwaitForOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


