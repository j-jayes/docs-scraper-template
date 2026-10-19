[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RoutingMap]()



# Type Alias RoutingMap

RoutingMap: Record<string | number, [NodeLike](NodeLike.html) | readonly [NodeLike](NodeLike.html)[]>

A mapping from route values to destination node(s). A value may be a single node or an array of nodes (fan-out).

#### Example
    
    
    {question: answerNode, statement: commentNode}  
      {retry: [nodeA, nodeB]}   // fan-out: both triggered
    Copy

#### Remarks

JavaScript object keys are always strings, so a numeric key (`{2: node}`) and a boolean key (`{true: node}`) are reconstructed to their typed [RouteValue](RouteValue.html) (`2`, `true`) when parsed — mirroring Python dict keys. Because of this, routes are matched **by string value** ([Graph.getNextPendingNodes](../classes/Graph.html#getnextpendingnodes) compares `String(route)` on both sides), so a node emitting `2` and one emitting `'2'` both fire a `{2: node}` edge. The flip side is that a numeric/boolean-looking route and its string spelling cannot be distinguished in a routing map; use distinct, non-ambiguous route keys when that matters.

  * Defined in [core/src/workflow/graph.ts:67](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/graph.ts#L67)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


