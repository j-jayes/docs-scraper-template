[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeContext]()



# Class NodeContext

The execution context for a workflow node — the TypeScript analogue of `google/adk-python` `agents/context.py::Context` (the workflow flavour).

It exposes `ctx.runNode(...)` for programmatic child execution, `ctx.state` for delta-aware session state, `ctx.emit(...)` to stream an event, and the mutable `output`/`route`/`interruptIds` a node sets while running.

  * Defined in [core/src/workflow/node_context.ts:76](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L76)



## Constructors

### constructor

  * new NodeContext(opts: [NodeContextOptions](../interfaces/NodeContextOptions.html)): [NodeContext]()

#### Parameters

    * opts: [NodeContextOptions](../interfaces/NodeContextOptions.html)

#### Returns [NodeContext]()

    * Defined in [core/src/workflow/node_context.ts:158](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L158)




## Properties

### `Optional`abortSignal

abortSignal?: AbortSignal

Abort signal for the current node run, set by the engine while the node is executing under a deadline or an external cancellation signal — i.e. when the node declares a `timeout`, when the invocation itself can be aborted, or when it runs inside a Workflow (whose signal fires if a sibling fails). Cooperative node bodies can observe `ctx.abortSignal` to wind down their own in-flight work (e.g. pass it to a model/tool call); the engine also stops consuming the node's events once it fires, so nothing is pushed past cancellation. A fired `timeout` surfaces as a `NodeTimeoutError`; an external abort stops the node without raising.

  * Defined in [core/src/workflow/node_context.ts:128](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L128)



### `Readonly`actions

actions: [EventActions](../interfaces/EventActions.html)

  * Defined in [core/src/workflow/node_context.ts:98](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L98)



### attemptCount

attemptCount: number = 1

The current attempt number (1-based) for the running node (see retry).

  * Defined in [core/src/workflow/node_context.ts:139](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L139)



### `Readonly`channel

channel: [AsyncQueue](AsyncQueue.html)<[Event](../interfaces/Event.html)>

  * Defined in [core/src/workflow/node_context.ts:78](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L78)



### interruptIds

interruptIds: string[] = []

Interrupt ids the node is currently blocked on (HITL).

  * Defined in [core/src/workflow/node_context.ts:109](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L109)



### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

  * Defined in [core/src/workflow/node_context.ts:77](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L77)



### `Optional`isolationScope

isolationScope?: string

  * Defined in [core/src/workflow/node_context.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L100)



### `Readonly`nodePath

nodePath: string

  * Defined in [core/src/workflow/node_context.ts:79](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L79)



### output

output: unknown = undefined

The structured output produced by the node during its run.

  * Defined in [core/src/workflow/node_context.ts:103](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L103)



### outputDelegated

outputDelegated: boolean = false

Whether this node handed its output to a child run with `useAsOutput`.

The child already emitted that value as its own result, so an event from this node repeating it would put the same text in the stream twice. The node still reports the output — only the duplicate event is suppressed.

  * Defined in [core/src/workflow/node_context.ts:97](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L97)



### outputForAncestors

outputForAncestors: readonly string[] = []

Node paths whose output this node's output also becomes: its parent's if the parent ran it with `useAsOutput`, plus whatever the parent was standing in for. Stamped onto every output event as `nodeInfo.outputFor`, so a resumed run can tell that an ancestor already has a result.

  * Defined in [core/src/workflow/node_context.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L88)



### `Optional`reportedError

reportedError?: { errorCode?: string; errorMessage?: string }

The failure a node reported by emitting an error event rather than by throwing. Read back at the end of the attempt; cleared per attempt.

  * Defined in [core/src/workflow/node_context.ts:115](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L115)



### resumeInputs

resumeInputs: Record<string, unknown>

  * Defined in [core/src/workflow/node_context.ts:99](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L99)



### `Optional`route

route?: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[]

The route key(s) emitted by the node, if any (array = multi-route).

  * Defined in [core/src/workflow/node_context.ts:106](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L106)



### `Readonly`runId

runId: string

  * Defined in [core/src/workflow/node_context.ts:80](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L80)



### `Optional`scheduler

scheduler?: [ScheduleDynamicNode](../interfaces/ScheduleDynamicNode.html)

The dynamic-node scheduler for this subtree. When set, `ctx.runNode()` routes through it (dedup/resume/fresh); otherwise it runs the child directly. Propagated to child contexts by the node runner; a nested Workflow overrides it with its own scheduler.

  * Defined in [core/src/workflow/node_context.ts:136](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L136)



### `Optional` `Readonly`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

The state schema in force for this node, inherited by its children unless they declare their own.

  * Defined in [core/src/workflow/node_context.ts:145](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L145)



## Accessors

### branch

  * get branch(): string | undefined

The branch of the owning invocation context.

#### Returns string | undefined

    * Defined in [core/src/workflow/node_context.ts:184](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L184)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

    * Defined in [core/src/workflow/node_context.ts:189](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L189)




### session

  * get session(): [Session](../interfaces/Session.html)

The current session.

#### Returns [Session](../interfaces/Session.html)

    * Defined in [core/src/workflow/node_context.ts:194](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L194)




### state

  * get state(): [State](State.html)

Delta-aware session state; writes accumulate in `actions.stateDelta`.

#### Returns [State](State.html)

    * Defined in [core/src/workflow/node_context.ts:179](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L179)




## Methods

### emit

  * emit(event: [Event](../interfaces/Event.html)): void

Streams a single event out through the workflow's event channel.

#### Parameters

    * event: [Event](../interfaces/Event.html)

#### Returns void

    * Defined in [core/src/workflow/node_context.ts:230](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L230)




### getInvocationContext

  * getInvocationContext(): [InvocationContext](InvocationContext.html)

The invocation context to run a nested agent against.

The single place where "what a node sees" is translated into "what an agent sees", so an agent run as a node (`BaseAgent.runImpl`) and one run directly go through the same seam.

It hands back the node's own invocation context unchanged, and that is the intended behaviour rather than a placeholder.

adk-python's counterpart (`agents/context.py` `get_invocation_context`) is documented as returning "a copy with the proxy session", which reads as though the agent is handed a different view of state. It is not: that `Context.session` returns `self._invocation_context.session`, so the copy substitutes the same object, and `Context._state` is built directly over `session.state`. A Python agent run as a node reads session state exactly as a TypeScript one does.

The other thing that copy carries — the isolation scope — is already applied by the time this runs: the node runner builds the child invocation context with the node's scope, so it is present on the object returned.

That leaves the node's own `state`, which is this node's pending delta over `session.state` — the same thing an agent reads, so the two cannot disagree. The agent-node cases in `core/test/workflow/state_consistency_test.ts` pin that.

#### Returns [InvocationContext](InvocationContext.html)

    * Defined in [core/src/workflow/node_context.ts:225](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L225)




### runNode

  * runNode(  
nodeLike: [RunnableNode](../types/RunnableNode.html),  
input?: unknown,  
options?: [RunNodeOptions](../interfaces/RunNodeOptions.html),  
): Promise<[NodeContext]() | [NodeResult](../interfaces/NodeResult.html)>

Runs a child node programmatically, streaming its events through the same channel and resolving to the child's result — a full NodeContext for a node that actually ran, or a bare [NodeResult](../interfaces/NodeResult.html) for one that was fast-forwarded from cached output on resume. Either way the caller can read `output`, `route`, `branch`, and `interruptIds`; only a `NodeContext` offers live behaviour (`emit`, `state`, nested `runNode`).

When a dynamic-node scheduler is set (inside a Workflow subtree), the call routes through it for dedup/resume; otherwise the child runs directly.

Takes anything an edge takes — an agent, a tool, a plain function, or an already-built node — and wraps it the same way the graph does, so `ctx.runNode(myAgent, input)` works without `node(myAgent)`. Wrap it yourself when you need the options `node()` carries, such as a schema or a name that differs from the value's own.

#### Parameters

    * nodeLike: [RunnableNode](../types/RunnableNode.html)
    * `Optional`input: unknown
    * `Optional`options: [RunNodeOptions](../interfaces/RunNodeOptions.html)

#### Returns Promise<[NodeContext]() | [NodeResult](../interfaces/NodeResult.html)>

    * Defined in [core/src/workflow/node_context.ts:252](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L252)




Constructors

constructor

Properties

abortSignalactionsattemptCountchannelinterruptIdsinvocationContextisolationScopenodePathoutputoutputDelegatedoutputForAncestorsreportedErrorresumeInputsrouterunIdschedulerstateSchema

Accessors

branchinvocationIdsessionstate

Methods

emitgetInvocationContextrunNode

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


