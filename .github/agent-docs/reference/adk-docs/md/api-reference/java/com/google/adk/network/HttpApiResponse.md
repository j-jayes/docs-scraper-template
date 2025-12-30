JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/HttpApiResponse.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.network](package-summary.html)
  2. [HttpApiResponse](HttpApiResponse.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. HttpApiResponse(Response)
  5. Method Details
     1. getEntity()
     2. close()



# Class HttpApiResponse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.network.ApiResponse](ApiResponse.html "class in com.google.adk.network")

com.google.adk.network.HttpApiResponse

All Implemented Interfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

* * *

public final class HttpApiResponse extends [ApiResponse](ApiResponse.html "class in com.google.adk.network")

Wraps a real HTTP response to expose the methods needed by the GenAI SDK.

  * ## Constructor Summary

Constructors

Constructor

Description

`HttpApiResponse(okhttp3.Response response)`

Constructs a HttpApiResponse instance with the response.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Closes the Http response.

`okhttp3.ResponseBody`

`getEntity()`

Returns the ResponseBody from the response.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### HttpApiResponse

public HttpApiResponse(okhttp3.Response response)

Constructs a HttpApiResponse instance with the response.

  * ## Method Details

    * ### getEntity

public okhttp3.ResponseBody getEntity()

Returns the ResponseBody from the response.

Specified by:
    `[getEntity](ApiResponse.html#getEntity\(\))` in class `[ApiResponse](ApiResponse.html "class in com.google.adk.network")`

    * ### close

public void close()

Closes the Http response.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Specified by:
    `[close](ApiResponse.html#close\(\))` in class `[ApiResponse](ApiResponse.html "class in com.google.adk.network")`




* * *

Copyright (C) 2025\. All rights reserved.
