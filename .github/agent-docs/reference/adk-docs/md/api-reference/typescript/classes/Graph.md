[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Graph]()



# Class Graph

A compiled workflow graph. Nodes are inferred (deduped by identity) from the edges.

Mirrors `google/adk-python` `workflow/_graph.py::Graph`.

  * Defined in [core/src/workflow/graph.ts:124](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L124)



## Constructors

### constructor

  * new Graph(edges: [Edge](Edge.html)[]): [Graph]()

#### Parameters

    * edges: [Edge](Edge.html)[]

#### Returns [Graph]()

    * Defined in [core/src/workflow/graph.ts:129](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L129)




## Properties

### `Readonly`edges

edges: [Edge](Edge.html)[]

  * Defined in [core/src/workflow/graph.ts:126](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L126)



### `Readonly`nodes

nodes: [BaseNode](BaseNode.html)<unknown, unknown>[]

  * Defined in [core/src/workflow/graph.ts:125](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L125)



## Accessors

### terminalNodeNames

  * get terminalNodeNames(): ReadonlySet<string>

Terminal node names (no outgoing edges); populated by validate.

#### Returns ReadonlySet<string>

    * Defined in [core/src/workflow/graph.ts:145](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L145)




## Methods

### getNextPendingNodes

  * getNextPendingNodes(  
nodeName: string,  
routesToMatch: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[] | null | undefined,  
): string[]

Determines the next nodes to transition to PENDING based on the route(s) emitted by a completed node. Ported from Python `get_next_pending_nodes`.

Logs at debug when the node emitted a route, has conditional outgoing edges, and none of them (nor a `DEFAULT_ROUTE` edge) matched — the branch stops there, which is easy to mistake for a bug. Behaviour is unchanged.

#### Parameters

    * nodeName: string
    * routesToMatch: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[] | null | undefined

#### Returns string[]

    * Defined in [core/src/workflow/graph.ts:157](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L157)




### validate

  * validate(): void

Validates the graph and computes terminal node names.

#### Returns void

    * Defined in [core/src/workflow/graph.ts:254](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L254)




Constructors

constructor

Properties

edgesnodes

Accessors

terminalNodeNames

Methods

getNextPendingNodesvalidate

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


