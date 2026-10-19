[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FunctionNodeHandler]()



# Type Alias FunctionNodeHandler<TInput, TOutput>

FunctionNodeHandler: (  
ctx: [NodeContext](../classes/NodeContext.html),  
input: TInput,  
) =>  
| [FunctionNodeResult](FunctionNodeResult.html)<TOutput>  
| Promise<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>>  
| Generator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>  
| AsyncGenerator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>

The handler wrapped by a [FunctionNode](../classes/FunctionNode.html).

Unlike Python's `FunctionNode` (which binds named parameters from `ctx.state` or `node_input` via runtime signature introspection), the TypeScript form uses the idiomatic explicit `(ctx, input)` signature. Read `ctx.state` directly for state-bound values. It may return a value/`Event`, a Promise, or a (sync/async) generator of those.

#### Type Parameters

  * TInput = unknown
  * TOutput = unknown



#### Type Declaration

  *     * (  
ctx: [NodeContext](../classes/NodeContext.html),  
input: TInput,  
):  
| [FunctionNodeResult](FunctionNodeResult.html)<TOutput>  
| Promise<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>>  
| Generator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>  
| AsyncGenerator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>
    * #### Parameters

      * ctx: [NodeContext](../classes/NodeContext.html)
      * input: TInput

#### Returns   
| [FunctionNodeResult](FunctionNodeResult.html)<TOutput>  
| Promise<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>>  
| Generator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>  
| AsyncGenerator<[FunctionNodeResult](FunctionNodeResult.html)<TOutput>, void, unknown>




  * Defined in [core/src/workflow/nodes/function_node.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/function_node.ts#L37)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


