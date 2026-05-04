JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
     1. Methods inherited from class Object
     2. Methods inherited from interface org.springframework.web.servlet.config.annotation.WebMvcConfigurer
  4. Constructor Details
     1. AdkWebServer()
  5. Method Details
     1. sessionService()
     2. artifactService()
     3. memoryService()
     4. objectMapper()
     5. mappingJackson2HttpMessageConverter(ObjectMapper)
     6. addResourceHandlers(ResourceHandlerRegistry)
     7. addViewControllers(ViewControllerRegistry)
     8. main(String[])
     9. start(BaseAgent...)

Hide sidebar  Show sidebar

# Class AdkWebServer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.AdkWebServer

All Implemented Interfaces:
    `org.springframework.web.servlet.config.annotation.WebMvcConfigurer`

* * *

@SpringBootApplication @ConfigurationPropertiesScan public class AdkWebServer extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements org.springframework.web.servlet.config.annotation.WebMvcConfigurer

Spring Boot application for the Agent Server.

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

`static void`

`main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args)`

Main entry point for the Spring Boot application.

`org.springframework.http.converter.json.MappingJackson2HttpMessageConverter`

`mappingJackson2HttpMessageConverter(com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Configures the message converter to use the custom ADK ObjectMapper.

`[BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory")`

`memoryService()`

Provides the singleton instance of the MemoryService (InMemory).

`com.fasterxml.jackson.databind.ObjectMapper`

`objectMapper()`

Configures the Jackson ObjectMapper for JSON serialization.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

 

`static void`

`start([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")... agents)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface org.springframework.web.servlet.config.annotation.WebMvcConfigurer

`addArgumentResolvers, addCorsMappings, addErrorResponseInterceptors, addFormatters, addInterceptors, addReturnValueHandlers, configureApiVersioning, configureAsyncSupport, configureContentNegotiation, configureDefaultServletHandling, configureHandlerExceptionResolvers, configureMessageConverters, configureMessageConverters, configurePathMatch, configureViewResolvers, extendHandlerExceptionResolvers, extendMessageConverters, getMessageCodesResolver, getValidator`




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

    * ### memoryService

@Bean public [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService()

Provides the singleton instance of the MemoryService (InMemory). Will be made configurable once we have the Vertex MemoryService.

Returns:
    An instance of BaseMemoryService (currently InMemoryMemoryService).

    * ### objectMapper

@Bean @Primary public com.fasterxml.jackson.databind.ObjectMapper objectMapper()

Configures the Jackson ObjectMapper for JSON serialization. Uses the ADK standard mapper configuration.

Returns:
    Configured ObjectMapper instance

    * ### mappingJackson2HttpMessageConverter

@Bean public org.springframework.http.converter.json.MappingJackson2HttpMessageConverter mappingJackson2HttpMessageConverter(com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Configures the message converter to use the custom ADK ObjectMapper. This ensures that Spring Web uses the correct JSON serialization settings (like omitting absent optional fields) and prevents double-serialization issues, particularly for Server-Sent Events (SSE).

Parameters:
    `objectMapper` \- The primary ObjectMapper configured for the ADK.
Returns:
    A configured MappingJackson2HttpMessageConverter.

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

public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args)

Main entry point for the Spring Boot application.

Parameters:
    `args` \- Command line arguments.

    * ### start

public static void start([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")... agents)




* * *

Copyright (C) 1980\. All rights reserved.
