[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CodeExecutionInput]()



# Interface CodeExecutionInput

A structure that contains the input of code execution.

interface CodeExecutionInput {  
args?: string[] | Record<string, string | number | boolean>;  
code: string;  
executionId?: string;  
inputFiles: [File](File.html)[];  
language: [CodeExecutionLanguage](../enums/CodeExecutionLanguage.html);  
}

  * Defined in [core/src/code_executors/code_execution_utils.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L60)



## Properties

### `Optional`args

args?: string[] | Record<string, string | number | boolean>

Optional arguments to pass to the executed code/script.

  * Defined in [core/src/code_executors/code_execution_utils.ts:84](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L84)



### code

code: string

The code to execute.

  * Defined in [core/src/code_executors/code_execution_utils.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L64)



### `Optional`executionId

executionId?: string

The execution ID for the stateful code execution.

  * Defined in [core/src/code_executors/code_execution_utils.ts:79](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L79)



### inputFiles

inputFiles: [File](File.html)[]

The input files available to the code.

  * Defined in [core/src/code_executors/code_execution_utils.ts:74](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L74)



### language

language: [CodeExecutionLanguage](../enums/CodeExecutionLanguage.html)

The language of the code to execute.

  * Defined in [core/src/code_executors/code_execution_utils.ts:69](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/code_execution_utils.ts#L69)



Properties

argscodeexecutionIdinputFileslanguage

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


