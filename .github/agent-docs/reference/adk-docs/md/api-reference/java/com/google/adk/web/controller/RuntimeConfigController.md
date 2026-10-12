JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RuntimeConfigController.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.controller](package-summary.html)
  2. [RuntimeConfigController](RuntimeConfigController.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. RuntimeConfigController(ResourceLoader, ObjectMapper, String, BackendUrl)
  5. Method Details
     1. runtimeConfig()

Hide sidebar  Show sidebar

# Class RuntimeConfigController

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.controller.RuntimeConfigController

* * *

@RestController public class RuntimeConfigController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Serves the dev UI's runtime configuration, shadowing the copy bundled in the static assets so `adk.web.backend-url` can point the UI at the address browsers reach this server on. The bundled document is merged rather than replaced, so keys the UI gains in a later bundle survive.

  * ## Constructor Summary

Constructors

Constructor

Description

`RuntimeConfigController(org.springframework.core.io.ResourceLoader resourceLoader, com.fasterxml.jackson.databind.ObjectMapper objectMapper, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") webUiDir, [BackendUrl](../config/BackendUrl.html "class in com.google.adk.web.config") backendUrl)`

Reads the bundled config through `resourceLoader`, or from `webUiDir` if set.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.http.ResponseEntity<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`runtimeConfig()`

Serves the bundled config with `backendUrl` taken from configuration when set.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### RuntimeConfigController

@Autowired public RuntimeConfigController(org.springframework.core.io.ResourceLoader resourceLoader, com.fasterxml.jackson.databind.ObjectMapper objectMapper, @Value("${adk.web.ui.dir:#{null}}") @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") webUiDir, [BackendUrl](../config/BackendUrl.html "class in com.google.adk.web.config") backendUrl)

Reads the bundled config through `resourceLoader`, or from `webUiDir` if set.

  * ## Method Details

    * ### runtimeConfig

@GetMapping(value="/dev-ui/assets/config/runtime-config.json", produces="application/json") public org.springframework.http.ResponseEntity<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> runtimeConfig()

Serves the bundled config with `backendUrl` taken from configuration when set.




* * *

Copyright (C) 1980\. All rights reserved.
