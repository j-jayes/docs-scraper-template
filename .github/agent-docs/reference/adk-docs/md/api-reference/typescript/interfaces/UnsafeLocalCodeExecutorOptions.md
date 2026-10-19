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

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/unsafe_local_code_executor.ts#L52)



## Properties

### `Optional`commandPath

commandPath?: string

The command to run JavaScript code. Default is `process.execPath` (Node.js).

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:60](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/unsafe_local_code_executor.ts#L60)



### `Optional`pythonCommandPath

pythonCommandPath?: string

The command to run Python code. Default is `python3`.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:64](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/unsafe_local_code_executor.ts#L64)



### `Optional`shellCommandPath

shellCommandPath?: string

The command to run Shell code. Default is `bash`.

When it names `powershell` or `pwsh` (with or without `.exe`) the script is written as `.ps1` and run through PowerShell rather than as a bare shell script.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:72](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/unsafe_local_code_executor.ts#L72)



### `Optional`timeoutSeconds

timeoutSeconds?: number

Timeout for code execution in seconds. Default is 30.

  * Defined in [core/src/code_executors/unsafe_local_code_executor.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/unsafe_local_code_executor.ts#L56)



Properties

commandPathpythonCommandPathshellCommandPathtimeoutSeconds

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


