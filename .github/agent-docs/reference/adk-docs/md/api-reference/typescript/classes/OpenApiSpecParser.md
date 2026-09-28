[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OpenApiSpecParser]()



# Class OpenApiSpecParser

  * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts#L38)



## Constructors

### constructor

  * new OpenApiSpecParser(  
options?: { preservePropertyNames?: boolean },  
): [OpenApiSpecParser]()

#### Parameters

    * options: { preservePropertyNames?: boolean } = {}

#### Returns [OpenApiSpecParser]()

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts#L41)




## Methods

### parse

  * parse(openapiSpec: Document): [ParsedOperation](../interfaces/ParsedOperation.html)[]

Parses an OpenAPI specification document and extracts a list of operations.

#### Parameters

    * openapiSpec: Document

The OpenAPI V3 document to parse.

#### Returns [ParsedOperation](../interfaces/ParsedOperation.html)[]

An array of parsed operations.

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts:52](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/openapi_spec_parser.ts#L52)




Constructors

constructor

Methods

parse

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


