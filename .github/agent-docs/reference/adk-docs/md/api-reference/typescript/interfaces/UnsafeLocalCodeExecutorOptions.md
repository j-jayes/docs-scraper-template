[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [UnsafeLocalCodeExecutorOptions]()



# Interface UnsafeLocalCodeExecutorOptions

Options for UnsafeLocalCodeExecutor.

interface UnsafeLocalCodeExecutorOptions {  
commandPath?: string;  
pythonCommandPath?: string;  
shellCommandPath?: string;  
timeoutSeconds?: number;  
}

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/unsafe_local_code_executor.ts#L26)



## Properties

### `Optional`commandPath

commandPath?: string

The command to run JavaScript code. Default is `process.execPath` (Node.js).

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/unsafe_local_code_executor.ts#L34)



### `Optional`pythonCommandPath

pythonCommandPath?: string

The command to run Python code. Default is `python3`.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/unsafe_local_code_executor.ts#L38)



### `Optional`shellCommandPath

shellCommandPath?: string

The command to run Shell code. Default is `bash`.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/unsafe_local_code_executor.ts#L42)



### `Optional`timeoutSeconds

timeoutSeconds?: number

Timeout for code execution in seconds. Default is 30.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/unsafe_local_code_executor.ts#L30)



Properties

commandPathpythonCommandPathshellCommandPathtimeoutSeconds

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


