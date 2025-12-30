JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AdkWebCorsConfig.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.config](package-summary.html)
  2. [AdkWebCorsConfig](AdkWebCorsConfig.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AdkWebCorsConfig()
  5. Method Details
     1. corsConfigurationSource(AdkWebCorsProperties)
     2. corsFilter(CorsConfigurationSource)



# Class AdkWebCorsConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.config.AdkWebCorsConfig

* * *

@Configuration public class AdkWebCorsConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AdkWebCorsConfig

public AdkWebCorsConfig()

  * ## Method Details

    * ### corsConfigurationSource

@Bean public org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource([AdkWebCorsProperties](AdkWebCorsProperties.html "class in com.google.adk.web.config") corsProperties)

    * ### corsFilter

@Bean public org.springframework.web.filter.CorsFilter corsFilter(org.springframework.web.cors.CorsConfigurationSource corsConfigurationSource)




* * *

Copyright (C) 2025\. All rights reserved.
