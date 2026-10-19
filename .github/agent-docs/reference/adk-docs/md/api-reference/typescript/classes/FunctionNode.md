[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FunctionNode]()



# Class FunctionNode<TInput, TOutput>

A node that wraps a plain function, async function, or (sync/async) generator.

Ported (TS-idiomatic subset) from `google/adk-python` `_function_node.py`. Return-value handling:

  * `Event` → emitted as-is (output validated against `outputSchema`)
  * genai `Content` → emitted as the event content
  * `null`/`undefined` → skipped (unless there are pending state deltas)
  * anything else → emitted as `Event(output=value)` State written via `ctx.state` during execution is attached to emitted events.



#### Type Parameters

  * TInput = unknown
  * TOutput = unknown



#### Hierarchy ([View Summary](../hierarchy.html#FunctionNode))

  * [BaseNode](BaseNode.html)<TInput, TOutput>
    * FunctionNode



  * Defined in [core/src/workflow/nodes/function_node.ts:70](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L70)



## Constructors

### constructor

  * new FunctionNode<TInput = unknown, TOutput = unknown>(  
name: string,  
handler: [FunctionNodeHandler](../types/FunctionNodeHandler.html)<TInput, TOutput>,  
config?: [FunctionNodeConfig](../interfaces/FunctionNodeConfig.html),  
): [FunctionNode]()<TInput, TOutput>

#### Type Parameters

    * TInput = unknown
    * TOutput = unknown

#### Parameters

    * name: string
    * handler: [FunctionNodeHandler](../types/FunctionNodeHandler.html)<TInput, TOutput>
    * config: [FunctionNodeConfig](../interfaces/FunctionNodeConfig.html) = {}

#### Returns [FunctionNode]()<TInput, TOutput>

Overrides [BaseNode](BaseNode.html).[constructor](BaseNode.html#constructor)

    * Defined in [core/src/workflow/nodes/function_node.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L82)




## Properties

### `Readonly`[BASE_NODE_SIGNATURE_SYMBOL]

"[BASE_NODE_SIGNATURE_SYMBOL]": true

Brand identifying this object as a [BaseNode](BaseNode.html) (see `isBaseNode`).

Inherited from [BaseNode](BaseNode.html).[[BASE_NODE_SIGNATURE_SYMBOL]](BaseNode.html#base_node_signature_symbol)

  * Defined in [core/src/workflow/base_node.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L88)



### `Optional` `Readonly`authConfig

authConfig?: [AuthConfig](../interfaces/AuthConfig.html)

  * Defined in [core/src/workflow/nodes/function_node.ts:74](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L74)



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

Inherited from BaseNode.requiresAllPredecessors

    * Defined in [core/src/workflow/base_node.ts:134](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L134)




## Methods

### run

  * run(ctx: [NodeContext](NodeContext.html), input: TInput): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the node, normalizing every yielded item into an [Event](../interfaces/Event.html). This is what the engine (and `ctx.runNode()`) consumes. Validates the input against `inputSchema` once, up front (skipping genai `Content`, which nodes coerce themselves).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: TInput

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Inherited from [BaseNode](BaseNode.html).[run](BaseNode.html#run)

    * Defined in [core/src/workflow/base_node.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L155)




### `Protected`runImpl

  * runImpl(ctx: [NodeContext](NodeContext.html), input: TInput): AsyncGenerator<unknown, void, void>

Core execution contract. Subclasses yield one of:

    * an [Event](../interfaces/Event.html) (emitted as-is),
    * a raw value (boxed into an event whose `output` is that value),
    * `null`/`undefined` (skipped).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: TInput

#### Returns AsyncGenerator<unknown, void, void>

Overrides [BaseNode](BaseNode.html).[runImpl](BaseNode.html#runimpl)

    * Defined in [core/src/workflow/nodes/function_node.ts:97](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L97)




### `Protected`toEvent

  * toEvent(ctx: [NodeContext](NodeContext.html), data: unknown): [Event](../interfaces/Event.html) | null

Normalizes a single yielded item into an [Event](../interfaces/Event.html) (or `null` to skip). Subclasses may override for richer coercion (e.g. `FunctionNode`).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * data: unknown

#### Returns [Event](../interfaces/Event.html) | null

Overrides [BaseNode](BaseNode.html).[toEvent](BaseNode.html#toevent)

    * Defined in [core/src/workflow/nodes/function_node.ts:208](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L208)




### `Protected`validateInput

  * validateInput(input: TInput): TInput

Validates node input against `inputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * input: TInput

#### Returns TInput

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

[BASE_NODE_SIGNATURE_SYMBOL]authConfigdescriptioninputSchemaisolationScopenameoutputSchemapreparedRetryConfigrerunOnResumeretryConfigstateSchematimeoutwaitForOutput

Accessors

requiresAllPredecessors

Methods

runrunImpltoEventvalidateInputvalidateOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


