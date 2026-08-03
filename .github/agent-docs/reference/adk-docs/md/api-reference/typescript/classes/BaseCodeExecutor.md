[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseCodeExecutor]()



# Class BaseCodeExecutor`Abstract`

The code executor allows the agent to execute code blocks from model responses and incorporate the execution results into the final response.

#### Hierarchy ([View Summary](../hierarchy.html#BaseCodeExecutor))

  * BaseCodeExecutor
    * [AgentEngineSandboxCodeExecutor](AgentEngineSandboxCodeExecutor.html)
    * [UnsafeLocalCodeExecutor](UnsafeLocalCodeExecutor.html)
    * [BuiltInCodeExecutor](BuiltInCodeExecutor.html)



  * Defined in [core/src/code_executors/base_code_executor.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L50)



## Constructors

### constructor

  * new BaseCodeExecutor(): [BaseCodeExecutor]()

#### Returns [BaseCodeExecutor]()




## Properties

### `Readonly`[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]

"[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]": true

A unique symbol to identify BaseCodeExecutor class.

  * Defined in [core/src/code_executors/base_code_executor.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L52)



### codeBlockDelimiters

codeBlockDelimiters: [string, string][] = ...

The list of the enclosing delimiters to identify the code blocks. For example, the delimiter('`javascript\\n', '\\n`') can be used to identify code blocks with the following format:
    
    
     console.log("hello")
    Copy

  * Defined in [core/src/code_executors/base_code_executor.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L82)



### errorRetryAttempts

errorRetryAttempts: number = 2

The number of attempts to retry on consecutive code execution errors. Default to 2.

  * Defined in [core/src/code_executors/base_code_executor.ts:71](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L71)



### executionResultDelimiters

executionResultDelimiters: [string, string] = ...

The delimiters to format the code execution result.

  * Defined in [core/src/code_executors/base_code_executor.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L94)



### optimizeDataFile

optimizeDataFile: boolean = false

If true, extract and process data files from the model request and attach them to the code executor.

Supported data file MimeTypes are [text/csv]. Default to false.

  * Defined in [core/src/code_executors/base_code_executor.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L60)



### stateful

stateful: boolean = false

Whether the code executor is stateful. Default to false.

  * Defined in [core/src/code_executors/base_code_executor.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L65)



## Methods

### `Abstract`executeCode

  * executeCode(params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)): Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

Executes code and return the code execution result.

#### Parameters

    * params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)

The parameters for executing code.

#### Returns Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

The result of the code execution.

    * Defined in [core/src/code_executors/base_code_executor.ts:102](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/base_code_executor.ts#L102)




Constructors

constructor

Properties

[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]codeBlockDelimiterserrorRetryAttemptsexecutionResultDelimitersoptimizeDataFilestateful

Methods

executeCode

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


