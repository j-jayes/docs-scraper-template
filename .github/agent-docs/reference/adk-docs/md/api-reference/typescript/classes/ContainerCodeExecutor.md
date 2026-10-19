[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ContainerCodeExecutor]()



# Class ContainerCodeExecutor

A code executor that runs model-generated code inside a hardened Docker container via the `dockerode` client.

Security note: this executor runs model-generated code, which may be influenced by untrusted input (e.g. via prompt injection). By default the container is started with networking disabled and all Linux capabilities dropped so the executed code cannot reach the network (including the cloud metadata endpoint at `169.254.169.254`) or escalate privileges. Networking can be re-enabled via `networkEnabled: true` when the executed code is trusted.

Limitations: this executor runs a code string only. `inputFiles` and `args` on the request are not copied into the container, and output files are not collected (`outputFiles` is always empty), so tools that stage resource files or read artifacts back (e.g. `RunSkillScriptTool`) are not yet supported. Sending files in and out via `putArchive`/`getArchive` is future work.

#### Hierarchy ([View Summary](../hierarchy.html#ContainerCodeExecutor))

  * [BaseCodeExecutor](BaseCodeExecutor.html)
    * ContainerCodeExecutor



  * Defined in [core/src/code_executors/container_code_executor.ts:114](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L114)



## Constructors

### constructor

  * new ContainerCodeExecutor(  
options?: [ContainerCodeExecutorOptions](../interfaces/ContainerCodeExecutorOptions.html),  
): [ContainerCodeExecutor]()

#### Parameters

    * options: [ContainerCodeExecutorOptions](../interfaces/ContainerCodeExecutorOptions.html) = {}

#### Returns [ContainerCodeExecutor]()

Overrides [BaseCodeExecutor](BaseCodeExecutor.html).[constructor](BaseCodeExecutor.html#constructor)

    * Defined in [core/src/code_executors/container_code_executor.ts:121](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L121)




## Properties

### `Readonly`[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]

"[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]": true

A unique symbol to identify BaseCodeExecutor class.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]](BaseCodeExecutor.html#base_code_executor_signature_symbol)

  * Defined in [core/src/code_executors/base_code_executor.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L52)



### codeBlockDelimiters

codeBlockDelimiters: [string, string][] = ...

The list of the enclosing delimiters to identify the code blocks. For example, the delimiter('`javascript\\n', '\\n`') can be used to identify code blocks with the following format:
    
    
     console.log("hello")
    Copy

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[codeBlockDelimiters](BaseCodeExecutor.html#codeblockdelimiters)

  * Defined in [core/src/code_executors/base_code_executor.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L82)



### errorRetryAttempts

errorRetryAttempts: number = 2

The number of attempts to retry on consecutive code execution errors. Default to 2.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[errorRetryAttempts](BaseCodeExecutor.html#errorretryattempts)

  * Defined in [core/src/code_executors/base_code_executor.ts:71](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L71)



### executionResultDelimiters

executionResultDelimiters: [string, string] = ...

The delimiters to format the code execution result.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[executionResultDelimiters](BaseCodeExecutor.html#executionresultdelimiters)

  * Defined in [core/src/code_executors/base_code_executor.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L94)



### optimizeDataFile

optimizeDataFile: boolean = false

If true, extract and process data files from the model request and attach them to the code executor.

Supported data file MimeTypes are [text/csv]. Default to false.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[optimizeDataFile](BaseCodeExecutor.html#optimizedatafile)

  * Defined in [core/src/code_executors/base_code_executor.ts:60](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L60)



### stateful

stateful: boolean = false

Whether the code executor is stateful. Default to false.

Inherited from [BaseCodeExecutor](BaseCodeExecutor.html).[stateful](BaseCodeExecutor.html#stateful)

  * Defined in [core/src/code_executors/base_code_executor.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/base_code_executor.ts#L65)



## Methods

### close

  * close(): Promise<void>

Stops and removes the container. Safe to call when no container has been started; provided for deterministic teardown in tests and app shutdown.

#### Returns Promise<void>

    * Defined in [core/src/code_executors/container_code_executor.ts:200](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L200)




### executeCode

  * executeCode(params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)): Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

Executes code and return the code execution result.

#### Parameters

    * params: [ExecuteCodeParams](../interfaces/ExecuteCodeParams.html)

The parameters for executing code.

#### Returns Promise<[CodeExecutionResult](../interfaces/CodeExecutionResult.html)>

The result of the code execution.

Overrides [BaseCodeExecutor](BaseCodeExecutor.html).[executeCode](BaseCodeExecutor.html#executecode)

    * Defined in [core/src/code_executors/container_code_executor.ts:149](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L149)




Constructors

constructor

Properties

[BASE_CODE_EXECUTOR_SIGNATURE_SYMBOL]codeBlockDelimiterserrorRetryAttemptsexecutionResultDelimitersoptimizeDataFilestateful

Methods

closeexecuteCode

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


