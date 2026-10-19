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

  * Defined in [core/src/code_executors/code_execution_utils.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L59)



## Properties

### `Optional`args

args?: string[] | Record<string, string | number | boolean>

Optional arguments to pass to the executed code/script.

  * Defined in [core/src/code_executors/code_execution_utils.ts:83](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L83)



### code

code: string

The code to execute.

  * Defined in [core/src/code_executors/code_execution_utils.ts:63](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L63)



### `Optional`executionId

executionId?: string

The execution ID for the stateful code execution.

  * Defined in [core/src/code_executors/code_execution_utils.ts:78](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L78)



### inputFiles

inputFiles: [File](File.html)[]

The input files available to the code.

  * Defined in [core/src/code_executors/code_execution_utils.ts:73](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L73)



### language

language: [CodeExecutionLanguage](../enums/CodeExecutionLanguage.html)

The language of the code to execute.

  * Defined in [core/src/code_executors/code_execution_utils.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/code_execution_utils.ts#L68)



Properties

argscodeexecutionIdinputFileslanguage

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


