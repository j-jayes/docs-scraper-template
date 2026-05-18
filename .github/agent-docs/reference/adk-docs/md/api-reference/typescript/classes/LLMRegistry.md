[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LLMRegistry]()



# Class LLMRegistry

Registry for LLMs.

  * Defined in [models/registry.ts:58](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/registry.ts#L58)



## Constructors

### constructor

  * new LLMRegistry(): [LLMRegistry]()

#### Returns [LLMRegistry]()




## Methods

### `Static`newLlm

  * newLlm(model: string): [BaseLlm](BaseLlm.html)

Creates a new LLM instance.

#### Parameters

    * model: string

The model name.

#### Returns [BaseLlm](BaseLlm.html)

The LLM instance.

    * Defined in [models/registry.ts:71](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/registry.ts#L71)




### `Static`register

  * register<T extends [BaseLlm](BaseLlm.html)>(  
llmCls: new (params: { model: string }) => T & {  
supportedModels: (string | RegExp)[];  
},  
): void

Registers a new LLM class.

#### Type Parameters

    * T extends [BaseLlm](BaseLlm.html)

#### Parameters

    * llmCls: new (params: { model: string }) => T & { supportedModels: (string | RegExp)[] }

The class that implements the model.

#### Returns void

    * Defined in [models/registry.ts:91](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/registry.ts#L91)




### `Static`resolve

  * resolve(model: string): [BaseLlmType](../types/BaseLlmType.html)

Resolves the model to a BaseLlm subclass.

#### Parameters

    * model: string

The model name.

#### Returns [BaseLlmType](../types/BaseLlmType.html)

The BaseLlm subclass.

#### Throws

If the model is not found.

    * Defined in [models/registry.ts:107](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/registry.ts#L107)




Constructors

constructor

Methods

newLlmregisterresolve

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


