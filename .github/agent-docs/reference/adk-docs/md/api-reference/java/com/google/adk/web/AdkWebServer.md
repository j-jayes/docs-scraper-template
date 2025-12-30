JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AdkWebServer()
  6. Method Details
     1. sessionService()
     2. artifactService()
     3. loadedAgentRegistry(AgentCompilerLoader, AgentLoadingProperties)
     4. objectMapper()
     5. addResourceHandlers(ResourceHandlerRegistry)
     6. addViewControllers(ViewControllerRegistry)
     7. main(String[])



# Class AdkWebServer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer

All Implemented Interfaces:
    `org.springframework.web.servlet.config.annotation.WebMvcConfigurer`

* * *

@SpringBootApplication @ConfigurationPropertiesScan @ComponentScan(basePackages={"com.google.adk.web","com.google.adk.web.config"}) public class AdkWebServer extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements org.springframework.web.servlet.config.annotation.WebMvcConfigurer

Single-file Spring Boot application for the Agent Server. Combines configuration, DTOs, and controller logic.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[AdkWebServer.AddSessionToEvalSetRequest](AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web")`

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/add-session requests.

`static class `

`[AdkWebServer.AgentController](AdkWebServer.AgentController.html "class in com.google.adk.web")`

Spring Boot REST Controller handling agent-related API endpoints.

`static class `

`[AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web")`

Data Transfer Object (DTO) for POST /run and POST /run-sse requests.

`static class `

`[AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web")`

A custom SpanExporter that stores relevant span data.

`static class `

`[AdkWebServer.GraphResponse](AdkWebServer.GraphResponse.html "class in com.google.adk.web")`

DTO for the response of GET /apps/{appName}/users/{userId}/sessions/{sessionId}/events/{eventId}/graph.

`static class `

`[AdkWebServer.LiveWebSocketHandler](AdkWebServer.LiveWebSocketHandler.html "class in com.google.adk.web")`

WebSocket Handler for the /run_live endpoint.

`static class `

`[AdkWebServer.OpenTelemetryConfig](AdkWebServer.OpenTelemetryConfig.html "class in com.google.adk.web")`

Configuration class for OpenTelemetry, setting up the tracer provider and span exporter.

`static class `

`[AdkWebServer.RunEvalRequest](AdkWebServer.RunEvalRequest.html "class in com.google.adk.web")`

DTO for POST /apps/{appName}/eval_sets/{evalSetId}/run-eval requests.

`static class `

`[AdkWebServer.RunEvalResult](AdkWebServer.RunEvalResult.html "class in com.google.adk.web")`

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval.

`static class `

`[AdkWebServer.RunnerService](AdkWebServer.RunnerService.html "class in com.google.adk.web")`

Service for creating and caching Runner instances.

`static class `

`[AdkWebServer.WebSocketConfig](AdkWebServer.WebSocketConfig.html "class in com.google.adk.web")`

Configuration class for WebSocket handling.

  * ## Constructor Summary

Constructors

Constructor

Description

`AdkWebServer()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`addResourceHandlers(org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry registry)`

Configures resource handlers for serving static content (like the Dev UI).

`void`

`addViewControllers(org.springframework.web.servlet.config.annotation.ViewControllerRegistry registry)`

Configures simple automated controllers: - Redirects the root path "/" to "/dev-ui".

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

Provides the singleton instance of the ArtifactService (InMemory).

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>`

`loadedAgentRegistry([AgentCompilerLoader](AgentCompilerLoader.html "class in com.google.adk.web") loader, [AgentLoadingProperties](config/AgentLoadingProperties.html "class in com.google.adk.web.config") props)`

 

`static void`

`main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] args)`

Main entry point for the Spring Boot application.

`com.fasterxml.jackson.databind.ObjectMapper`

`objectMapper()`

 

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface org.springframework.web.servlet.config.annotation.WebMvcConfigurer

`addArgumentResolvers, addCorsMappings, addErrorResponseInterceptors, addFormatters, addInterceptors, addReturnValueHandlers, configureAsyncSupport, configureContentNegotiation, configureDefaultServletHandling, configureHandlerExceptionResolvers, configureMessageConverters, configurePathMatch, configureViewResolvers, extendHandlerExceptionResolvers, extendMessageConverters, getMessageCodesResolver, getValidator`




  * ## Constructor Details

    * ### AdkWebServer

public AdkWebServer()

  * ## Method Details

    * ### sessionService

@Bean public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

    * ### artifactService

@Bean public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

Provides the singleton instance of the ArtifactService (InMemory). TODO: configure this based on config (e.g., DB URL)

Returns:
    An instance of BaseArtifactService (currently InMemoryArtifactService).

    * ### loadedAgentRegistry

@Bean("loadedAgentRegistry") public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> loadedAgentRegistry([AgentCompilerLoader](AgentCompilerLoader.html "class in com.google.adk.web") loader, [AgentLoadingProperties](config/AgentLoadingProperties.html "class in com.google.adk.web.config") props)

    * ### objectMapper

@Bean public com.fasterxml.jackson.databind.ObjectMapper objectMapper()

    * ### addResourceHandlers

public void addResourceHandlers(org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry registry)

Configures resource handlers for serving static content (like the Dev UI). Maps requests starting with "/dev-ui/" to the directory specified by the 'adk.web.ui.dir' system property.

Specified by:
    `addResourceHandlers` in interface `org.springframework.web.servlet.config.annotation.WebMvcConfigurer`

    * ### addViewControllers

public void addViewControllers(org.springframework.web.servlet.config.annotation.ViewControllerRegistry registry)

Configures simple automated controllers: - Redirects the root path "/" to "/dev-ui". - Forwards requests to "/dev-ui" to "/dev-ui/index.html" so the ResourceHandler serves it.

Specified by:
    `addViewControllers` in interface `org.springframework.web.servlet.config.annotation.WebMvcConfigurer`

    * ### main

public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")[] args)

Main entry point for the Spring Boot application.

Parameters:
    `args` \- Command line arguments.




* * *

Copyright (C) 2025\. All rights reserved.
