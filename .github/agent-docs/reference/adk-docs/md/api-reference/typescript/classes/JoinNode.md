[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [JoinNode]()



# Class JoinNode

A fan-in barrier node: via requiresAllPredecessors the engine holds it until ALL of its predecessors complete, then runs it with their aggregated outputs as input.

This node emits that input unchanged — the engine supplies the predecessor-name → output map; the join just passes it through as its output. The barrier itself is enforced by the orchestrator (which reads `requiresAllPredecessors`) and lands in a later part.

Ported from `google/adk-python` `workflow/_join_node.py`.

#### Hierarchy ([View Summary](../hierarchy.html#JoinNode))

  * [BaseNode](BaseNode.html)
    * JoinNode



  * Defined in [core/src/workflow/nodes/join_node.ts:23](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/join_node.ts#L23)



## Constructors

### constructor

  * new JoinNode(config: [BaseNodeConfig](../interfaces/BaseNodeConfig.html)): [JoinNode]()

#### Parameters

    * config: [BaseNodeConfig](../interfaces/BaseNodeConfig.html)

#### Returns [JoinNode]()

Inherited from [BaseNode](BaseNode.html).[constructor](BaseNode.html#constructor)

    * Defined in [core/src/workflow/base_node.ts:107](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L107)




## Properties

### `Readonly`[BASE_NODE_SIGNATURE_SYMBOL]

"[BASE_NODE_SIGNATURE_SYMBOL]": true

Brand identifying this object as a [BaseNode](BaseNode.html) (see `isBaseNode`).

Inherited from [BaseNode](BaseNode.html).[[BASE_NODE_SIGNATURE_SYMBOL]](BaseNode.html#base_node_signature_symbol)

  * Defined in [core/src/workflow/base_node.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L88)



### `Readonly`description

description: string

Inherited from [BaseNode](BaseNode.html).[description](BaseNode.html#description)

  * Defined in [core/src/workflow/base_node.ts:91](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L91)



### `Optional` `Readonly`inputSchema

inputSchema?: [SchemaLike](../types/SchemaLike.html)

Inherited from [BaseNode](BaseNode.html).[inputSchema](BaseNode.html#inputschema)

  * Defined in [core/src/workflow/base_node.ts:102](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L102)



### `Optional` `Readonly`isolationScope

isolationScope?: string | true

Inherited from [BaseNode](BaseNode.html).[isolationScope](BaseNode.html#isolationscope)

  * Defined in [core/src/workflow/base_node.ts:105](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L105)



### `Readonly`name

name: string

Inherited from [BaseNode](BaseNode.html).[name](BaseNode.html#name)

  * Defined in [core/src/workflow/base_node.ts:90](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L90)



### `Optional` `Readonly`outputSchema

outputSchema?: [SchemaLike](../types/SchemaLike.html)

Inherited from [BaseNode](BaseNode.html).[outputSchema](BaseNode.html#outputschema)

  * Defined in [core/src/workflow/base_node.ts:103](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L103)



### `Optional` `Readonly`preparedRetryConfig

preparedRetryConfig?: [PreparedRetryConfig](../interfaces/PreparedRetryConfig.html)

The retry config with its exception filter normalized once, up front (see [prepareRetryConfig](../functions/prepareRetryConfig.html)). Used by the node runner so the retry hot path never re-normalizes or throws on a malformed config mid-retry.

Inherited from [BaseNode](BaseNode.html).[preparedRetryConfig](BaseNode.html#preparedretryconfig)

  * Defined in [core/src/workflow/base_node.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L100)



### `Readonly`rerunOnResume

rerunOnResume: boolean

Inherited from [BaseNode](BaseNode.html).[rerunOnResume](BaseNode.html#rerunonresume)

  * Defined in [core/src/workflow/base_node.ts:92](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L92)



### `Optional` `Readonly`retryConfig

retryConfig?: [RetryConfig](../interfaces/RetryConfig.html)

Inherited from [BaseNode](BaseNode.html).[retryConfig](BaseNode.html#retryconfig)

  * Defined in [core/src/workflow/base_node.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L94)



### `Optional` `Readonly`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Inherited from [BaseNode](BaseNode.html).[stateSchema](BaseNode.html#stateschema)

  * Defined in [core/src/workflow/base_node.ts:104](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L104)



### `Optional` `Readonly`timeout

timeout?: number

Inherited from [BaseNode](BaseNode.html).[timeout](BaseNode.html#timeout)

  * Defined in [core/src/workflow/base_node.ts:101](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L101)



### `Readonly`waitForOutput

waitForOutput: boolean

Inherited from [BaseNode](BaseNode.html).[waitForOutput](BaseNode.html#waitforoutput)

  * Defined in [core/src/workflow/base_node.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L93)



## Accessors

### requiresAllPredecessors

  * get requiresAllPredecessors(): boolean

Whether this node must wait for ALL of its predecessors to trigger before it runs (fan-in barrier). Overridden by `JoinNode`.

#### Returns boolean

Overrides BaseNode.requiresAllPredecessors

    * Defined in [core/src/workflow/nodes/join_node.ts:24](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/join_node.ts#L24)




## Methods

### run

  * run(ctx: [NodeContext](NodeContext.html), input: unknown): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the node, normalizing every yielded item into an [Event](../interfaces/Event.html). This is what the engine (and `ctx.runNode()`) consumes. Validates the input against `inputSchema` once, up front (skipping genai `Content`, which nodes coerce themselves).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: unknown

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Inherited from [BaseNode](BaseNode.html).[run](BaseNode.html#run)

    * Defined in [core/src/workflow/base_node.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L155)




### `Protected`runImpl

  * runImpl(ctx: [NodeContext](NodeContext.html), input: unknown): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core execution contract. Subclasses yield one of:

    * an [Event](../interfaces/Event.html) (emitted as-is),
    * a raw value (boxed into an event whose `output` is that value),
    * `null`/`undefined` (skipped).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: unknown

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseNode](BaseNode.html).[runImpl](BaseNode.html#runimpl)

    * Defined in [core/src/workflow/nodes/join_node.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/join_node.ts#L28)




### `Protected`toEvent

  * toEvent(ctx: [NodeContext](NodeContext.html), data: unknown): [Event](../interfaces/Event.html) | null

Normalizes a single yielded item into an [Event](../interfaces/Event.html) (or `null` to skip). Subclasses may override for richer coercion (e.g. `FunctionNode`).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * data: unknown

#### Returns [Event](../interfaces/Event.html) | null

Inherited from [BaseNode](BaseNode.html).[toEvent](BaseNode.html#toevent)

    * Defined in [core/src/workflow/base_node.ts:217](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L217)




### `Protected`validateInput

  * validateInput(input: unknown): unknown

Validates node input against `inputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * input: unknown

#### Returns unknown

Inherited from [BaseNode](BaseNode.html).[validateInput](BaseNode.html#validateinput)

    * Defined in [core/src/workflow/base_node.ts:178](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L178)




### `Protected`validateOutput

  * validateOutput(output: unknown): unknown

Validates node output against `outputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * output: unknown

#### Returns unknown

Inherited from [BaseNode](BaseNode.html).[validateOutput](BaseNode.html#validateoutput)

    * Defined in [core/src/workflow/base_node.ts:198](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L198)




Constructors

constructor

Properties

[BASE_NODE_SIGNATURE_SYMBOL]descriptioninputSchemaisolationScopenameoutputSchemapreparedRetryConfigrerunOnResumeretryConfigstateSchematimeoutwaitForOutput

Accessors

requiresAllPredecessors

Methods

runrunImpltoEventvalidateInputvalidateOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


