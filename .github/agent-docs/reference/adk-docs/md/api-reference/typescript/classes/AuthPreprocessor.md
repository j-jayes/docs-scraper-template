[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthPreprocessor]()



# Class AuthPreprocessor

Base class for LLM request processors. Implementations mutate or augment the [LlmRequest](../interfaces/LlmRequest.html) before it is sent to the model.

#### Hierarchy ([View Summary](../hierarchy.html#AuthPreprocessor))

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)
    * AuthPreprocessor



  * Defined in [core/src/auth/auth_preprocessor.ts:97](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_preprocessor.ts#L97)



## Constructors

### constructor

  * new AuthPreprocessor(): [AuthPreprocessor]()

#### Returns [AuthPreprocessor]()

Inherited from [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[constructor](BaseLlmRequestProcessor.html#constructor)




## Methods

### runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the processor, optionally yielding intermediate [Event](../interfaces/Event.html)s.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[runAsync](BaseLlmRequestProcessor.html#runasync)

    * Defined in [core/src/auth/auth_preprocessor.ts:98](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_preprocessor.ts#L98)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


