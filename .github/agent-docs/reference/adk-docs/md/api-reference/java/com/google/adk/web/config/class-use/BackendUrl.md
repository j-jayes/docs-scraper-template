JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../BackendUrl.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.config](../package-summary.html)
  2. [BackendUrl](../BackendUrl.html)



# Uses of Class  
com.google.adk.web.config.BackendUrl

Packages that use [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")

Package

Description

com.google.adk.web

 

com.google.adk.web.config

 

com.google.adk.web.controller

 

  * ## Uses of [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config") in [com.google.adk.web](../../package-summary.html)

Methods in [com.google.adk.web](../../package-summary.html) that return [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")

Modifier and Type

Method

Description

`[BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")`

AdkWebServer.`[backendUrl](../../AdkWebServer.html#backendUrl\(\))()`

One bean, so this and the runtime-config endpoint cannot read the property differently.

  * ## Uses of [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config") in [com.google.adk.web.config](../package-summary.html)

Methods in [com.google.adk.web.config](../package-summary.html) that return [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")

Modifier and Type

Method

Description

`static [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")`

BackendUrl.`[from](../BackendUrl.html#from\(java.lang.String\))(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configured)`

Parses `configured`.

  * ## Uses of [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config") in [com.google.adk.web.controller](../../controller/package-summary.html)

Constructors in [com.google.adk.web.controller](../../controller/package-summary.html) with parameters of type [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config")

Modifier

Constructor

Description

` `

`[RuntimeConfigController](../../controller/RuntimeConfigController.html#%3Cinit%3E\(org.springframework.core.io.ResourceLoader,com.fasterxml.jackson.databind.ObjectMapper,java.lang.String,com.google.adk.web.config.BackendUrl\))(org.springframework.core.io.ResourceLoader resourceLoader, com.fasterxml.jackson.databind.ObjectMapper objectMapper, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") webUiDir, [BackendUrl](../BackendUrl.html "class in com.google.adk.web.config") backendUrl)`

Reads the bundled config through `resourceLoader`, or from `webUiDir` if set.




* * *

Copyright (C) 1980\. All rights reserved.
