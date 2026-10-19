[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeInfo]()



# Interface NodeInfo

Workflow-node provenance attached to an event.

Mirrors `google/adk-python` `Event.node_info`. Present only on events emitted from within a workflow node.

interface NodeInfo {  
messageAsOutput?: boolean;  
outputFor?: string[];  
path?: string;  
}

  * Defined in [core/src/events/event.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L43)



## Properties

### `Optional`messageAsOutput

messageAsOutput?: boolean

Whether the event's textual content should be promoted to the node's structured output.

  * Defined in [core/src/events/event.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L65)



### `Optional`outputFor

outputFor?: string[]

The node paths this event's output serves as the output for: the emitting node first, then any ancestor that delegated its own output to it.

A node that runs a child with `useAsOutput` takes the child's output as its own, so one event is the result for several nodes at once. Recording that on the event is what lets a resumed run tell which nodes already produced a result, instead of re-running an ancestor whose output only ever existed on a descendant's event.

Mirrors adk-python's `node_info.output_for`, which is likewise a list.

  * Defined in [core/src/events/event.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L59)



### `Optional`path

path?: string

The workflow node path that produced this event (e.g. `wf.child.0`).

  * Defined in [core/src/events/event.ts:45](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L45)



Properties

messageAsOutputoutputForpath

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


