[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LLMRegistry]()



# Class LLMRegistry

Registry for LLMs.

  * Defined in [core/src/models/registry.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/registry.ts#L57)



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

    * Defined in [core/src/models/registry.ts:70](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/registry.ts#L70)




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

    * Defined in [core/src/models/registry.ts:88](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/registry.ts#L88)




### `Static`resolve

  * resolve(model: string): BaseLlmType

Resolves the model to a BaseLlm subclass.

#### Parameters

    * model: string

The model name.

#### Returns BaseLlmType

The BaseLlm subclass.

#### Throws

If the model is not found.

    * Defined in [core/src/models/registry.ts:103](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/registry.ts#L103)




Constructors

constructor

Methods

newLlmregisterresolve

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


