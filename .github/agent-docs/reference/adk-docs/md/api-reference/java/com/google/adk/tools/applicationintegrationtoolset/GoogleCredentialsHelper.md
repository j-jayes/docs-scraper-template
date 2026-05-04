JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/GoogleCredentialsHelper.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.applicationintegrationtoolset](package-summary.html)
  2. [GoogleCredentialsHelper](GoogleCredentialsHelper.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. GoogleCredentialsHelper()
  5. Method Details
     1. getGoogleCredentials(String)

Hide sidebar  Show sidebar

# Class GoogleCredentialsHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.applicationintegrationtoolset.GoogleCredentialsHelper

All Implemented Interfaces:
    `[CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")`

* * *

public final class GoogleCredentialsHelper extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")

  * ## Constructor Summary

Constructors

Constructor

Description

`GoogleCredentialsHelper()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.auth.oauth2.GoogleCredentials`

`getGoogleCredentials(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") serviceAccountJson)`

Converts a service account JSON string to a Google Credentials object.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### GoogleCredentialsHelper

public GoogleCredentialsHelper()

  * ## Method Details

    * ### getGoogleCredentials

public com.google.auth.oauth2.GoogleCredentials getGoogleCredentials(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") serviceAccountJson) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Description copied from interface: `[CredentialsHelper](CredentialsHelper.html#getGoogleCredentials\(java.lang.String\))`

Converts a service account JSON string to a Google Credentials object.

Specified by:
    `[getGoogleCredentials](CredentialsHelper.html#getGoogleCredentials\(java.lang.String\))` in interface `[CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")`
Parameters:
    `serviceAccountJson` \- The service account JSON string.
Returns:
    A Google Credentials object.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- when an error occurs during the conversion.




* * *

Copyright (C) 1980\. All rights reserved.
