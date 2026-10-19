[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Edge]()



# Class Edge

A directed edge in the workflow graph.

Mirrors `google/adk-python` `workflow/_graph.py::Edge`.

  * Defined in [core/src/workflow/graph.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L87)



## Constructors

### constructor

  * new Edge(  
fromNode: [BaseNode](BaseNode.html),  
toNode: [BaseNode](BaseNode.html),  
route?: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[] | null,  
): [Edge]()

#### Parameters

    * fromNode: [BaseNode](BaseNode.html)
    * toNode: [BaseNode](BaseNode.html)
    * route: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[] | null = null

The route(s) this edge is associated with. `null` means unconditional (always triggered). A single value or a list; the edge fires when the emitted route matches any listed value.

#### Returns [Edge]()

    * Defined in [core/src/workflow/graph.ts:91](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L91)




## Properties

### `Readonly`[EDGE_SIGNATURE_SYMBOL]

"[EDGE_SIGNATURE_SYMBOL]": true

Brand identifying this object as an Edge (see `isEdge`).

  * Defined in [core/src/workflow/graph.ts:89](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L89)



### `Readonly`fromNode

fromNode: [BaseNode](BaseNode.html)

  * Defined in [core/src/workflow/graph.ts:92](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L92)



### `Readonly`route

route: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[] | null = null

The route(s) this edge is associated with. `null` means unconditional (always triggered). A single value or a list; the edge fires when the emitted route matches any listed value.

  * Defined in [core/src/workflow/graph.ts:99](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L99)



### `Readonly`toNode

toNode: [BaseNode](BaseNode.html)

  * Defined in [core/src/workflow/graph.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L93)



Constructors

constructor

Properties

[EDGE_SIGNATURE_SYMBOL]fromNoderoutetoNode

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


