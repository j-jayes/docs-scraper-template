[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OperationParser]()



# Class OperationParser

Parses an OpenAPI OperationObject and extracts its parameters, request body, and return value.

It maps OpenAPI parameters and request bodies into a flat list of `ApiParameter` objects that are compatible with Gemini's tool function declarations.

  * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L26)



## Constructors

### constructor

  * new OperationParser(  
operation: {},  
options?: { preservePropertyNames?: boolean },  
): [OperationParser]()

#### Parameters

    * operation: {}
    * options: { preservePropertyNames?: boolean } = {}

#### Returns [OperationParser]()

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:31](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L31)




## Methods

### getDescription

  * getDescription(): string

Gets the description of the tool, derived from the operation's description or summary.

#### Returns string

A string representing the description.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:237](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L237)




### getFunctionName

  * getFunctionName(): string

Gets a valid tool function name derived from the operation's operationId.

#### Returns string

A string representing the function name.

#### Throws

If the operation does not have an operationId.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:223](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L223)




### getJsonSchema

  * getJsonSchema(): Record<string, unknown>

Generates a JSON schema representing the arguments of the tool function call.

#### Returns Record<string, unknown>

A JSON Schema object.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:197](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L197)




### getParameters

  * getParameters(): [ApiParameter](../interfaces/ApiParameter.html)[]

Gets the list of parsed parameters extracted from the OpenAPI operation.

#### Returns [ApiParameter](../interfaces/ApiParameter.html)[]

An array of parsed parameters.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:187](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L187)




Constructors

constructor

Methods

getDescriptiongetFunctionNamegetJsonSchemagetParameters

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


