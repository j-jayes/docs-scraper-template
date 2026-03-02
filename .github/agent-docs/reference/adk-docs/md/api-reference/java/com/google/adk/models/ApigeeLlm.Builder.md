JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ApigeeLlm.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [ApigeeLlm](ApigeeLlm.html)
  3. [Builder](ApigeeLlm.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. modelName(String)
     2. proxyUrl(String)
     3. customHeaders(Map)
     4. build()

Hide sidebar  Show sidebar

# Class ApigeeLlm.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.ApigeeLlm.Builder

Enclosing class:
    `[ApigeeLlm](ApigeeLlm.html "class in com.google.adk.models")`

* * *

public static class ApigeeLlm.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`ApigeeLlm`](ApigeeLlm.html "class in com.google.adk.models").

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[ApigeeLlm](ApigeeLlm.html "class in com.google.adk.models")`

`build()`

Builds the [`ApigeeLlm`](ApigeeLlm.html "class in com.google.adk.models") instance.

`[ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models")`

`customHeaders([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> customHeaders)`

Sets a dictionary of headers to be sent with the request.

`[ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models")`

`modelName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

Sets the model string.

`[ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models")`

`proxyUrl([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") proxyUrl)`

Sets the URL of the Apigee proxy.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

protected Builder()

  * ## Method Details

    * ### modelName

@CanIgnoreReturnValue public [ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models") modelName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

Sets the model string. The model string specifies the LLM provider (e.g., Vertex AI, Gemini), API version, and the model ID. 

**Format:** `apigee/[<provider>/][<version>/]<model_id>`

**Components:**
      * **`provider`** (optional): `vertex_ai` or `gemini`. If omitted, behavior depends on the `GOOGLE_GENAI_USE_VERTEXAI` environment variable. If that is not set to `TRUE` or `1`, it defaults to `gemini`. 
      * **`version`** (optional): The API version (e.g., `v1`, `v1beta`). If omitted, the default version for the provider is used. 
      * **`model_id`** (required): The model identifier (e.g., ` gemini-2.5-flash`). 

**Examples:**
      * `apigee/gemini-2.5-flash`
      * `apigee/v1/gemini-2.5-flash`
      * `apigee/vertex_ai/gemini-2.5-flash`
      * `apigee/gemini/v1/gemini-2.5-flash`
      * `apigee/vertex_ai/v1beta/gemini-2.5-flash`

Parameters:
    `modelName` \- the model string.
Returns:
    this builder.

    * ### proxyUrl

@CanIgnoreReturnValue public [ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models") proxyUrl([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") proxyUrl)

Sets the URL of the Apigee proxy. If not set, it will be read from the ` APIGEE_PROXY_URL` environment variable.

Parameters:
    `proxyUrl` \- the Apigee proxy URL.
Returns:
    this builder.

    * ### customHeaders

@CanIgnoreReturnValue public [ApigeeLlm.Builder](ApigeeLlm.Builder.html "class in com.google.adk.models") customHeaders([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> customHeaders)

Sets a dictionary of headers to be sent with the request.

Parameters:
    `customHeaders` \- the custom headers.
Returns:
    this builder.

    * ### build

public [ApigeeLlm](ApigeeLlm.html "class in com.google.adk.models") build()

Builds the [`ApigeeLlm`](ApigeeLlm.html "class in com.google.adk.models") instance.

Returns:
    a new [`ApigeeLlm`](ApigeeLlm.html "class in com.google.adk.models") instance.
Throws:
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if modelName is null.
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the model string is invalid.




* * *

Copyright (C) 1980\. All rights reserved.
