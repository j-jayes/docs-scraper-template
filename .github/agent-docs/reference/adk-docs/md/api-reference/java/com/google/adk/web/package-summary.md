JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)



Contents

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Related Packages
  3. Classes and Interfaces



# Package com.google.adk.web

* * *

package com.google.adk.web

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

[com.google.adk.web.config](config/package-summary.html)

 

  * Classes

Class

Description

[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")

Single-file Spring Boot application for the Agent Server.

[AdkWebServer.AddSessionToEvalSetRequest](AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web")

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/add-session requests.

[AdkWebServer.AgentController](AdkWebServer.AgentController.html "class in com.google.adk.web")

Spring Boot REST Controller handling agent-related API endpoints.

[AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web")

Data Transfer Object (DTO) for POST /run and POST /run-sse requests.

[AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web")

A custom SpanExporter that stores relevant span data.

[AdkWebServer.GraphResponse](AdkWebServer.GraphResponse.html "class in com.google.adk.web")

DTO for the response of GET /apps/{appName}/users/{userId}/sessions/{sessionId}/events/{eventId}/graph.

[AdkWebServer.LiveWebSocketHandler](AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web")

WebSocket Handler for the /run_live endpoint.

[AdkWebServer.OpenTelemetryConfig](AdkWebServer.OpenTelemetryConfig.html "class in com.google.adk.web")

Configuration class for OpenTelemetry, setting up the tracer provider and span exporter.

[AdkWebServer.RunEvalRequest](AdkWebServer.RunEvalRequest.html "class in com.google.adk.web")

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/run-eval requests.

[AdkWebServer.RunEvalResult](AdkWebServer.RunEvalResult.html "class in com.google.adk.web")

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval.

[AdkWebServer.RunnerService](AdkWebServer.RunnerService.html "class in com.google.adk.web")

Service for creating and caching Runner instances.

[AdkWebServer.WebSocketConfig](AdkWebServer.WebSocketConfig.html "class in com.google.adk.web")

Configuration class for WebSocket handling.

[AgentCompilerLoader](AgentCompilerLoader.html "class in com.google.adk.web")

Dynamically compiles and loads ADK [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") implementations from source files.

[AgentGraphGenerator](AgentGraphGenerator.html "class in com.google.adk.web")

Utility class to generate Graphviz DOT representations of Agent structures.




* * *

Copyright (C) 2025\. All rights reserved.
