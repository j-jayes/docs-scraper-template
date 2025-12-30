JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Gemini.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [Gemini](Gemini.html)
  3. [Builder](Gemini.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. modelName(String)
     2. apiClient(Client)
     3. apiKey(String)
     4. vertexCredentials(VertexCredentials)
     5. build()



# Class Gemini.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.Gemini.Builder

Enclosing class:
    `[Gemini](Gemini.html "class in com.google.adk.models")`

* * *

public static class Gemini.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`Gemini`](Gemini.html "class in com.google.adk.models").

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

`apiClient(com.google.genai.Client apiClient)`

Sets the explicit `Client` instance for making API calls.

`[Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

`apiKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") apiKey)`

Sets the Google Gemini API key.

`[Gemini](Gemini.html "class in com.google.adk.models")`

`build()`

Builds the [`Gemini`](Gemini.html "class in com.google.adk.models") instance.

`[Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

`modelName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

Sets the name of the Gemini model to use.

`[Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

`vertexCredentials([VertexCredentials](VertexCredentials.html "class in com.google.adk.models") vertexCredentials)`

Sets the Vertex AI credentials.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### modelName

@CanIgnoreReturnValue public [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models") modelName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

Sets the name of the Gemini model to use.

Parameters:
    `modelName` \- The model name (e.g., "gemini-2.0-flash").
Returns:
    This builder.

    * ### apiClient

@CanIgnoreReturnValue public [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models") apiClient(com.google.genai.Client apiClient)

Sets the explicit `Client` instance for making API calls. If this is set, apiKey and vertexCredentials will be ignored.

Parameters:
    `apiClient` \- The client instance.
Returns:
    This builder.

    * ### apiKey

@CanIgnoreReturnValue public [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models") apiKey([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") apiKey)

Sets the Google Gemini API key. If `apiClient(Client)` is also set, the explicit client will take precedence. If `vertexCredentials(VertexCredentials)` is also set, this apiKey will take precedence.

Parameters:
    `apiKey` \- The API key.
Returns:
    This builder.

    * ### vertexCredentials

@CanIgnoreReturnValue public [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models") vertexCredentials([VertexCredentials](VertexCredentials.html "class in com.google.adk.models") vertexCredentials)

Sets the Vertex AI credentials. If `apiClient(Client)` or `apiKey(String)` are also set, they will take precedence over these credentials.

Parameters:
    `vertexCredentials` \- The Vertex AI credentials.
Returns:
    This builder.

    * ### build

public [Gemini](Gemini.html "class in com.google.adk.models") build()

Builds the [`Gemini`](Gemini.html "class in com.google.adk.models") instance.

Returns:
    A new [`Gemini`](Gemini.html "class in com.google.adk.models") instance.
Throws:
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if modelName is null.




* * *

Copyright (C) 2025\. All rights reserved.
