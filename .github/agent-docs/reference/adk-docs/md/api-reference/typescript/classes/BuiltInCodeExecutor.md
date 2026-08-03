[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BuiltInCodeExecutor]()



# Class BuiltInCodeExecutor

A code executor that uses the Model's built-in code executor.

Currently only supports Gemini 2.0+ models, but will be expanded to other models.

#### Hierarchy ([View Summary](../hierarchy.html#BuiltInCodeExecutor))

  * [BaseCodeExecutor](BaseCodeExecutor.html)
    * BuiltInCodeExecutor



  * Defined in [core/src/code_executors/built_in_code_executor.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/built_in_code_executor.ts#L42)



## Constructors

### constructor

  * new BuiltInCodeExecutor(): [BuiltInCodeExecutor]()

#### Returns [BuiltInCodeExecutor]()

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[constructor](BaseCodeExecutor.html#constructor)




## Properties

### `Readonly`[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]

"[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]": true

A unique symbol to identify BaseCodeExecutor class.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]](BaseCodeExecutor.html#base_code_executor_signature_symbol)

  * Defined in [core/src/code_executors/base_code_executor.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L52)



### `Readonly`[BUILT_IN_CODE_EXECUTOR_SIGNATURE_SYMBOL]

"[BUILT_IN_CODE_EXECUTOR_SIGNATURE_SYMBOL]": true

A unique symbol to identify BuiltInCodeExecutor class.

  * Defined in [core/src/code_executors/built_in_code_executor.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/built_in_code_executor.ts#L44)



### codeBlockDelimiters

codeBlockDelimiters: [string, string][] = ...

The list of the enclosing delimiters to identify the code blocks. For example, the delimiter('`javascript\\n', '\\n`') can be used to identify code blocks with the following format:
    
    
     console.log("hello")
    Copy

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[codeBlockDelimiters](BaseCodeExecutor.html#codeblockdelimiters)

  * Defined in [core/src/code_executors/base_code_executor.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L82)



### errorRetryAttempts

errorRetryAttempts: number = 2

The number of attempts to retry on consecutive code execution errors. Default to 2.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[errorRetryAttempts](BaseCodeExecutor.html#errorretryattempts)

  * Defined in [core/src/code_executors/base_code_executor.ts:71](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L71)



### executionResultDelimiters

executionResultDelimiters: [string, string] = ...

The delimiters to format the code execution result.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[executionResultDelimiters](BaseCodeExecutor.html#executionresultdelimiters)

  * Defined in [core/src/code_executors/base_code_executor.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L94)



### optimizeDataFile

optimizeDataFile: boolean = false

If true, extract and process data files from the model request and attach them to the code executor.

Supported data file MimeTypes are [text/csv]. Default to false.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[optimizeDataFile](BaseCodeExecutor.html#optimizedatafile)

  * Defined in [core/src/code_executors/base_code_executor.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L60)



### stateful

stateful: boolean = false

Whether the code executor is stateful. Default to false.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[stateful](BaseCodeExecutor.html#stateful)

  * Defined in [core/src/code_executors/base_code_executor.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L65)



## Methods

### executeCode

  * executeCode(_params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)): Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

Executes code and return the code execution result.

#### Parameters

    * _params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)

#### Returns Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

The result of the code execution.

Overrides [BaseCodeExecutor](BaseCodeExecutor.html).[executeCode](BaseCodeExecutor.html#executecode)

    * Defined in [core/src/code_executors/built_in_code_executor.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/built_in_code_executor.ts#L46)




### processLlmRequest

  * processLlmRequest(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns void

    * Defined in [core/src/code_executors/built_in_code_executor.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/built_in_code_executor.ts#L54)




Constructors

constructor

Properties

[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL][BUILT_IN_CODE_EXECUTOR_SIGNATURE_SYMBOL]codeBlockDelimiterserrorRetryAttemptsexecutionResultDelimitersoptimizeDataFilestateful

Methods

executeCodeprocessLlmRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


