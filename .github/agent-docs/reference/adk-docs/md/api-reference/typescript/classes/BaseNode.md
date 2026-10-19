[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseNode]()



# Class BaseNode<TInput, TOutput>`Abstract`

Abstract base class for all nodes in an ADK workflow.

A node is a discrete unit of execution. Subclasses implement runImpl, which may yield [Event](../interfaces/Event.html)s, raw values (boxed into an event), or `null`/`undefined` (skipped). run normalizes those into a stream of [Event](../interfaces/Event.html)s consumed by the engine.

#### Type Parameters

  * TInput = unknown
  * TOutput = unknown



#### Hierarchy ([View Summary](../hierarchy.html#BaseNode))

  * BaseNode
    * [BaseAgent](BaseAgent.html)
    * [FunctionNode](FunctionNode.html)
    * [JoinNode](JoinNode.html)
    * [ParallelWorker](ParallelWorker.html)
    * [ToolNode](ToolNode.html)
    * [Workflow](Workflow.html)
    * [WorkflowNode](WorkflowNode.html)



  * Defined in [core/src/workflow/base_node.ts:86](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L86)



## Constructors

### constructor

  * new BaseNode<TInput = unknown, TOutput = unknown>(  
config: [BaseNodeConfig](../interfaces/BaseNodeConfig.html),  
): [BaseNode]()<TInput, TOutput>

#### Type Parameters

    * TInput = unknown
    * TOutput = unknown

#### Parameters

    * config: [BaseNodeConfig](../interfaces/BaseNodeConfig.html)

#### Returns [BaseNode]()<TInput, TOutput>

    * Defined in [core/src/workflow/base_node.ts:107](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L107)




## Properties

### `Readonly`[BASE_NODE_SIGNATURE_SYMBOL]

"[BASE_NODE_SIGNATURE_SYMBOL]": true

Brand identifying this object as a BaseNode (see `isBaseNode`).

  * Defined in [core/src/workflow/base_node.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L88)



### `Readonly`description

description: string

  * Defined in [core/src/workflow/base_node.ts:91](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L91)



### `Optional` `Readonly`inputSchema

inputSchema?: [SchemaLike](../types/SchemaLike.html)

  * Defined in [core/src/workflow/base_node.ts:102](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L102)



### `Optional` `Readonly`isolationScope

isolationScope?: string | true

  * Defined in [core/src/workflow/base_node.ts:105](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L105)



### `Readonly`name

name: string

  * Defined in [core/src/workflow/base_node.ts:90](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L90)



### `Optional` `Readonly`outputSchema

outputSchema?: [SchemaLike](../types/SchemaLike.html)

  * Defined in [core/src/workflow/base_node.ts:103](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L103)



### `Optional` `Readonly`preparedRetryConfig

preparedRetryConfig?: [PreparedRetryConfig](../interfaces/PreparedRetryConfig.html)

The retry config with its exception filter normalized once, up front (see [prepareRetryConfig](../functions/prepareRetryConfig.html)). Used by the node runner so the retry hot path never re-normalizes or throws on a malformed config mid-retry.

  * Defined in [core/src/workflow/base_node.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L100)



### `Readonly`rerunOnResume

rerunOnResume: boolean

  * Defined in [core/src/workflow/base_node.ts:92](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L92)



### `Optional` `Readonly`retryConfig

retryConfig?: [RetryConfig](../interfaces/RetryConfig.html)

  * Defined in [core/src/workflow/base_node.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L94)



### `Optional` `Readonly`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

  * Defined in [core/src/workflow/base_node.ts:104](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L104)



### `Optional` `Readonly`timeout

timeout?: number

  * Defined in [core/src/workflow/base_node.ts:101](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L101)



### `Readonly`waitForOutput

waitForOutput: boolean

  * Defined in [core/src/workflow/base_node.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L93)



## Accessors

### requiresAllPredecessors

  * get requiresAllPredecessors(): boolean

Whether this node must wait for ALL of its predecessors to trigger before it runs (fan-in barrier). Overridden by `JoinNode`.

#### Returns boolean

    * Defined in [core/src/workflow/base_node.ts:134](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L134)




## Methods

### run

  * run(ctx: [NodeContext](NodeContext.html), input: TInput): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the node, normalizing every yielded item into an [Event](../interfaces/Event.html). This is what the engine (and `ctx.runNode()`) consumes. Validates the input against `inputSchema` once, up front (skipping genai `Content`, which nodes coerce themselves).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: TInput

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

    * Defined in [core/src/workflow/base_node.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L155)




### `Protected` `Abstract`runImpl

  * runImpl(ctx: [NodeContext](NodeContext.html), input: TInput): AsyncGenerator<unknown, void, void>

Core execution contract. Subclasses yield one of:

    * an [Event](../interfaces/Event.html) (emitted as-is),
    * a raw value (boxed into an event whose `output` is that value),
    * `null`/`undefined` (skipped).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: TInput

#### Returns AsyncGenerator<unknown, void, void>

    * Defined in [core/src/workflow/base_node.ts:144](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L144)




### `Protected`toEvent

  * toEvent(ctx: [NodeContext](NodeContext.html), data: unknown): [Event](../interfaces/Event.html) | null

Normalizes a single yielded item into an [Event](../interfaces/Event.html) (or `null` to skip). Subclasses may override for richer coercion (e.g. `FunctionNode`).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * data: unknown

#### Returns [Event](../interfaces/Event.html) | null

    * Defined in [core/src/workflow/base_node.ts:217](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L217)




### `Protected`validateInput

  * validateInput(input: TInput): TInput

Validates node input against `inputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * input: TInput

#### Returns TInput

    * Defined in [core/src/workflow/base_node.ts:178](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L178)




### `Protected`validateOutput

  * validateOutput(output: unknown): unknown

Validates node output against `outputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * output: unknown

#### Returns unknown

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


