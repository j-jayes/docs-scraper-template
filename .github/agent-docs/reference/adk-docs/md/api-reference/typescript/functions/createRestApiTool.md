[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [createRestApiTool]()



# Function createRestApiTool

  * createRestApiTool(  
parsed: {  
authScheme?: SecuritySchemeObject;  
description: string;  
endpoint: [OperationEndpoint](../interfaces/OperationEndpoint.html);  
name: string;  
operation: {};  
},  
options?: {  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](../classes/ReadonlyContext.html)) => Record<string, string>;  
preservePropertyNames?: boolean;  
},  
): [RestApiTool](../classes/RestApiTool.html)

#### Parameters

    * parsed: {  
authScheme?: SecuritySchemeObject;  
description: string;  
endpoint: [OperationEndpoint](../interfaces/OperationEndpoint.html);  
name: string;  
operation: {};  
}
    * options: {  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](../classes/ReadonlyContext.html)) => Record<string, string>;  
preservePropertyNames?: boolean;  
} = {}

#### Returns [RestApiTool](../classes/RestApiTool.html)

    * Defined in [core/src/tools/openapi_tool/rest_api_tool.ts:279](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/rest_api_tool.ts#L279)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


