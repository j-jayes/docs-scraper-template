JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/CredentialsHelper.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.applicationintegrationtoolset](package-summary.html)
  2. [CredentialsHelper](CredentialsHelper.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getGoogleCredentials(String)
     2. populateHeaders(HttpRequest.Builder, Credentials)

Hide sidebar  Show sidebar

# Interface CredentialsHelper

All Known Implementing Classes:
    `[GoogleCredentialsHelper](GoogleCredentialsHelper.html "class in com.google.adk.tools.applicationintegrationtoolset")`

* * *

public interface CredentialsHelper

This interface provides a method to convert a service account JSON string to a Google Credentials object. 

Additionally, contains helper methods that aid with transfering the credentials' data to the HttpRequest.Builder object

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`com.google.auth.Credentials`

`getGoogleCredentials(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") serviceAccountJson)`

Converts a service account JSON string to a Google Credentials object.

`static [HttpRequest.Builder](https://docs.oracle.com/en/java/javase/17/docs/api/java.net.http/java/net/http/HttpRequest.Builder.html "interface in java.net.http")`

`populateHeaders([HttpRequest.Builder](https://docs.oracle.com/en/java/javase/17/docs/api/java.net.http/java/net/http/HttpRequest.Builder.html "interface in java.net.http") builder, com.google.auth.Credentials credentials)`

Populates the headers (such as Authorization or x-goog-project) in the HttpRequest.Builder with the metadata from the credentials.




  * ## Method Details

    * ### getGoogleCredentials

com.google.auth.Credentials getGoogleCredentials(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") serviceAccountJson) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Converts a service account JSON string to a Google Credentials object.

Parameters:
    `serviceAccountJson` \- The service account JSON string.
Returns:
    A Google Credentials object.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- when an error occurs during the conversion.

    * ### populateHeaders

static [HttpRequest.Builder](https://docs.oracle.com/en/java/javase/17/docs/api/java.net.http/java/net/http/HttpRequest.Builder.html "interface in java.net.http") populateHeaders([HttpRequest.Builder](https://docs.oracle.com/en/java/javase/17/docs/api/java.net.http/java/net/http/HttpRequest.Builder.html "interface in java.net.http") builder, com.google.auth.Credentials credentials) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Populates the headers (such as Authorization or x-goog-project) in the HttpRequest.Builder with the metadata from the credentials.

Parameters:
    `builder` \- HttpRequest.Builder object to populate the headers
    `credentials` \- Credentials object containing the metadata
Returns:
    HttpRequest.Builder object with the headers populated
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- if an error occurs when getting the metadata from the credentials




* * *

Copyright (C) 1980\. All rights reserved.
