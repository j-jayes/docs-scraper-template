[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OperationParser]()



# Class OperationParser

Parses an OpenAPI OperationObject and extracts its parameters, request body, and return value.

It maps OpenAPI parameters and request bodies into a flat list of `ApiParameter` objects that are compatible with Gemini's tool function declarations.

  * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L35)



## Constructors

### constructor

  * new OperationParser(  
operation: string | Record<string, unknown> | {},  
options?: { preservePropertyNames?: boolean; shouldParse?: boolean },  
): [OperationParser]()

#### Parameters

    * operation: string | Record<string, unknown> | {}

The operation to parse. A string is parsed as JSON, and a plain object is used as given.

    * options: { preservePropertyNames?: boolean; shouldParse?: boolean } = {}
      * ##### `Optional`preservePropertyNames?: boolean

Keeps the original parameter and function names instead of converting them to snake_case.

      * ##### `Optional`shouldParse?: boolean

Whether to parse the operation during construction. Defaults to `true`.

#### Returns [OperationParser]()

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L49)




## Methods

### getAuthSchemeName

  * getAuthSchemeName(): string

Gets the name of the security scheme this operation declares.

Only operation-level security is considered. Document-level security is not visible from here, so a caller that needs the fallback uses `OpenApiSpecParser` instead.

#### Returns string

The first declared scheme name, or `''` when the operation declares none.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:308](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L308)




### getDescription

  * getDescription(): string

Gets the description of the tool, derived from the operation's description or summary.

#### Returns string

A string representing the description.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:293](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L293)




### getFunctionName

  * getFunctionName(): string

Gets a valid tool function name derived from the operation's operationId.

#### Returns string

A string representing the function name.

#### Throws

If the operation does not have an operationId.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:279](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L279)




### getJsonSchema

  * getJsonSchema(): Record<string, unknown>

Generates a JSON schema representing the arguments of the tool function call.

#### Returns Record<string, unknown>

A JSON Schema object.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:253](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L253)




### getParameters

  * getParameters(): [ApiParameter](../interfaces/ApiParameter.html)[]

Gets the list of parsed parameters extracted from the OpenAPI operation.

#### Returns [ApiParameter](../interfaces/ApiParameter.html)[]

An array of parsed parameters.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:243](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L243)




### getPydocString

  * getPydocString(): string

Generates a Python-style docstring describing the operation, every parameter and the return value.

The type names inside it are Python's, because the artifact is a docstring in adk-python's format and the same text reaches the model in both SDKs.

#### Returns string

The generated docstring.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:345](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L345)




### getReturnTypeHint

  * getReturnTypeHint(): string

Gets the Python-style type hint of the return value.

#### Returns string

A type name such as `str`, or `Any` when the operation declares no typed 2xx response.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:331](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L331)




### getReturnValue

  * getReturnValue(): [ApiParameter](../interfaces/ApiParameter.html) | undefined

Gets the parsed return value of the operation.

#### Returns [ApiParameter](../interfaces/ApiParameter.html) | undefined

The return value, or `undefined` when the parser was constructed with `shouldParse: false` and nothing was loaded.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:320](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L320)




### `Static`load

  * load(  
operation: string | Record<string, unknown> | {},  
params: [ApiParameter](../interfaces/ApiParameter.html)[],  
returnValue?: [ApiParameter](../interfaces/ApiParameter.html),  
): [OperationParser]()

Builds a parser from parameters that were already parsed, without walking the operation again.

#### Parameters

    * operation: string | Record<string, unknown> | {}

The operation the parameters came from.

    * params: [ApiParameter](../interfaces/ApiParameter.html)[]

The parsed parameters.

    * `Optional`returnValue: [ApiParameter](../interfaces/ApiParameter.html)

The parsed return value, if any.

#### Returns [OperationParser]()

A parser holding the given parameters.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts:77](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/openapi_spec_parser/operation_parser.ts#L77)




Constructors

constructor

Methods

getAuthSchemeNamegetDescriptiongetFunctionNamegetJsonSchemagetParametersgetPydocStringgetReturnTypeHintgetReturnValueload

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


