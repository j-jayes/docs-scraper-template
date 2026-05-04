JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AdkWebCorsConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.config](package-summary.html)
  2. [AdkWebCorsConfig](AdkWebCorsConfig.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AdkWebCorsConfig()
  5. Method Details
     1. corsConfigurationSource(AdkWebCorsProperties)
     2. corsFilter(CorsConfigurationSource)

Hide sidebar  Show sidebar

# Class AdkWebCorsConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.config.AdkWebCorsConfig

* * *

@Configuration public class AdkWebCorsConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration class for setting up Cross-Origin Resource Sharing (CORS) in the ADK Web application. This class defines beans for configuring CORS settings based on properties defined in [`AdkWebCorsProperties`](AdkWebCorsProperties.html "class in com.google.adk.web.config"). 

CORS allows the application to handle requests from different origins, enabling secure communication between the frontend and backend services. 

Beans provided: 

  * `CorsConfigurationSource`: Configures CORS settings such as allowed origins, methods, headers, credentials, and max age. 
  * `CorsFilter`: Applies the CORS configuration to incoming requests. 


  * ## Constructor Summary

Constructors

Constructor

Description

`AdkWebCorsConfig()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.web.cors.CorsConfigurationSource`

`corsConfigurationSource([AdkWebCorsProperties](AdkWebCorsProperties.html "class in com.google.adk.web.config") corsProperties)`

 

`org.springframework.web.filter.CorsFilter`

`corsFilter(org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### AdkWebCorsConfig

public AdkWebCorsConfig()

  * ## Method Details

    * ### corsConfigurationSource

@Bean public org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource([AdkWebCorsProperties](AdkWebCorsProperties.html "class in com.google.adk.web.config") corsProperties)

    * ### corsFilter

@Bean public org.springframework.web.filter.CorsFilter corsFilter(org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource)




* * *

Copyright (C) 1980\. All rights reserved.
