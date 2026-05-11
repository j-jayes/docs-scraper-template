[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseExampleProvider]()



# Class BaseExampleProvider`Abstract`

Base class for example providers.

This class defines the interface for providing examples for a given query.

  * Defined in [examples/base_example_provider.ts:38](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/examples/base_example_provider.ts#L38)



## Constructors

### constructor

  * new BaseExampleProvider(): [BaseExampleProvider]()

#### Returns [BaseExampleProvider]()




## Properties

### `Readonly`[BASE_EXAMPLE_PROVIDER_SIGNATURE_SYMBOL]

"[BASE_EXAMPLE_PROVIDER_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK example provider classes.

  * Defined in [examples/base_example_provider.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/examples/base_example_provider.ts#L42)



## Methods

### `Abstract`getExamples

  * getExamples(query: string): [Example](../interfaces/Example.html)[]

Returns a list of examples for a given query.

#### Parameters

    * query: string

The query to get examples for.

#### Returns [Example](../interfaces/Example.html)[]

A list of Example objects.

    * Defined in [examples/base_example_provider.ts:50](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/examples/base_example_provider.ts#L50)




Constructors

constructor

Properties

[BASE_EXAMPLE_PROVIDER_SIGNATURE_SYMBOL]

Methods

getExamples

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


