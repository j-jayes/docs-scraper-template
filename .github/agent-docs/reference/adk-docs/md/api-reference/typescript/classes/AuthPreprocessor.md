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



  * Defined in [core/src/auth/auth_preprocessor.ts:122](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_preprocessor.ts#L122)



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

    * Defined in [core/src/auth/auth_preprocessor.ts:123](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_preprocessor.ts#L123)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


