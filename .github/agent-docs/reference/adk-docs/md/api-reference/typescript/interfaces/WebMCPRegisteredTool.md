[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WebMCPRegisteredTool]()



# Interface WebMCPRegisteredTool

A tool as reported by `document.modelContext.getTools()`.

interface WebMCPRegisteredTool {  
annotations?: [WebMCPToolAnnotations](WebMCPToolAnnotations.html);  
description?: string;  
inputSchema?: string | object;  
name: string;  
origin?: string;  
title?: string;  
}

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L28)



## Properties

### `Optional`annotations

annotations?: [WebMCPToolAnnotations](WebMCPToolAnnotations.html)

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:40](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L40)



### `Optional`description

description?: string

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L31)



### `Optional`inputSchema

inputSchema?: string | object

JSON Schema for the tool's arguments.

Typed loosely on purpose: the specification says object, but browsers have been observed handing back a JSON string, and a schema that is silently misread leaves the model unable to pass any arguments at all.

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:39](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L39)



### name

name: string

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:29](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L29)



### `Optional`origin

origin?: string

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L41)



### `Optional`title

title?: string

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:30](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L30)



Properties

annotationsdescriptioninputSchemanameorigintitle

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


