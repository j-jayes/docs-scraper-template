JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/HttpApiClient.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [HttpApiClient](HttpApiClient.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. MEDIA_TYPE_APPLICATION_JSON
  5. Method Details
     1. request(String, String, String)
     2. vertexAI()
     3. project()
     4. location()
     5. apiKey()



# Class HttpApiClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.sessions.HttpApiClient

* * *

public class HttpApiClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Base client for the HTTP APIs.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final okhttp3.MediaType`

`MEDIA_TYPE_APPLICATION_JSON`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`apiKey()`

Returns the API key for Google AI APIs.

`@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`location()`

Returns the location for Vertex AI APIs.

`@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`project()`

Returns the project ID for Vertex AI APIs.

`[ApiResponse](ApiResponse.html "class in com.google.adk.sessions")`

`request([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") httpMethod, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") requestJson)`

Sends a Http request given the http method, path, and request json string.

`boolean`

`vertexAI()`

Returns whether the client is using Vertex AI APIs.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### MEDIA_TYPE_APPLICATION_JSON

public static final okhttp3.MediaType MEDIA_TYPE_APPLICATION_JSON

  * ## Method Details

    * ### request

public [ApiResponse](ApiResponse.html "class in com.google.adk.sessions") request([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") httpMethod, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") requestJson)

Sends a Http request given the http method, path, and request json string.

    * ### vertexAI

public boolean vertexAI()

Returns whether the client is using Vertex AI APIs.

    * ### project

public @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") project()

Returns the project ID for Vertex AI APIs.

    * ### location

public @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") location()

Returns the location for Vertex AI APIs.

    * ### apiKey

public @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") apiKey()

Returns the API key for Google AI APIs.




* * *

Copyright (C) 2025\. All rights reserved.
