[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RestApiTool]()



# Class RestApiTool

The base class for all tools.

#### Hierarchy ([View Summary](../hierarchy.html#RestApiTool))

  * [BaseTool](BaseTool.html)
    * RestApiTool



  * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L24)



## Constructors

### constructor

  * new RestApiTool(  
name: string,  
description: string,  
endpoint: [OperationEndpoint](../interfaces/OperationEndpoint.html),  
operation: {},  
authScheme?: SecuritySchemeObject,  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html),  
options?: {  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
preservePropertyNames?: boolean;  
},  
): [RestApiTool]()

#### Parameters

    * name: string
    * description: string
    * endpoint: [OperationEndpoint](../interfaces/OperationEndpoint.html)
    * operation: {}
    * `Optional`authScheme: SecuritySchemeObject
    * `Optional`authCredential: [AuthCredential](../interfaces/AuthCredential.html)
    * options: {  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
preservePropertyNames?: boolean;  
} = {}

#### Returns [RestApiTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L30)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:66](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from BaseTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:151](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L151)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Gets the OpenAPI specification of this tool in the form of a FunctionDeclaration.

NOTE

    * Required if subclass uses the default implementation of `processLlmRequest` to add function declaration to LLM request.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns FunctionDeclaration

The FunctionDeclaration of this tool, or undefined if it doesn't need to be added to LlmRequest.config.

Overrides [BaseTool](BaseTool.html).[_getDeclaration](BaseTool.html#_getdeclaration)

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L67)




### configureAuthCredential

  * configureAuthCredential(authCredential: [AuthCredential](../interfaces/AuthCredential.html)): void

#### Parameters

    * authCredential: [AuthCredential](../interfaces/AuthCredential.html)

#### Returns void

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L57)




### configureAuthScheme

  * configureAuthScheme(authScheme: SecuritySchemeObject): void

#### Parameters

    * authScheme: SecuritySchemeObject

#### Returns void

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L52)




### configureCredentialKey

  * configureCredentialKey(credentialKey: string): void

#### Parameters

    * credentialKey: string

#### Returns void

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L62)




### processLlmRequest

  * processLlmRequest(request: [ToolProcessLlmRequest](../interfaces/ToolProcessLlmRequest.html)): Promise<void>

Processes the outgoing LLM request for this tool.

Use cases:

    * Most common use case is adding this tool to the LLM request.
    * Some tools may just preprocess the LLM request before it's sent out.

#### Parameters

    * request: [ToolProcessLlmRequest](../interfaces/ToolProcessLlmRequest.html)

The request to process the LLM request.

#### Returns Promise<void>

Inherited from [BaseTool](BaseTool.html).[processLlmRequest](BaseTool.html#processllmrequest)

    * Defined in [core/src/tools/base_tool.ts:120](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L120)




### runAsync

  * runAsync(request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Runs the tool with the given arguments and context.

NOTE

    * Required if this tool needs to run at the client side.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Parameters

    * request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

The request to run the tool.

#### Returns Promise<unknown>

A promise that resolves to the tool response.

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L77)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationconfigureAuthCredentialconfigureAuthSchemeconfigureCredentialKeyprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


