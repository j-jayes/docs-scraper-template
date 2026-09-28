[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolAuthHandler]()



# Class ToolAuthHandler

  * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts#L47)



## Constructors

### constructor

  * new ToolAuthHandler(  
context: [Context](Context.html),  
authScheme?: SecuritySchemeObject,  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html),  
credentialKey?: string,  
): [ToolAuthHandler]()

#### Parameters

    * context: [Context](Context.html)
    * `Optional`authScheme: SecuritySchemeObject
    * `Optional`authCredential: [AuthCredential](../interfaces/AuthCredential.html)
    * `Optional`credentialKey: string

#### Returns [ToolAuthHandler]()

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts#L48)




## Methods

### prepareAuthCredentials

  * prepareAuthCredentials(): Promise<[AuthPreparationResult](../interfaces/AuthPreparationResult.html)>

#### Returns Promise<[AuthPreparationResult](../interfaces/AuthPreparationResult.html)>

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts:71](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts#L71)




### `Static`fromToolContext

  * fromToolContext(  
context: [Context](Context.html),  
authScheme?: SecuritySchemeObject,  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html),  
options?: { credentialKey?: string },  
): [ToolAuthHandler]()

#### Parameters

    * context: [Context](Context.html)
    * `Optional`authScheme: SecuritySchemeObject
    * `Optional`authCredential: [AuthCredential](../interfaces/AuthCredential.html)
    * options: { credentialKey?: string } = {}

#### Returns [ToolAuthHandler]()

    * Defined in [core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_spec_parser/tool_auth_handler.ts#L56)




Constructors

constructor

Methods

prepareAuthCredentialsfromToolContext

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


