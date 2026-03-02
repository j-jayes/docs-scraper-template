JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/GoogleCredentialsHelper.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.applicationintegrationtoolset.GoogleCredentialsHelper

All Implemented Interfaces:
    `[CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")`

* * *

public final class GoogleCredentialsHelper extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")

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

`getGoogleCredentials([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") serviceAccountJson)`

Converts a service account JSON string to a Google Credentials object.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### GoogleCredentialsHelper

public GoogleCredentialsHelper()

  * ## Method Details

    * ### getGoogleCredentials

public com.google.auth.oauth2.GoogleCredentials getGoogleCredentials(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") serviceAccountJson) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")

Description copied from interface: `[CredentialsHelper](CredentialsHelper.html#getGoogleCredentials\(java.lang.String\))`

Converts a service account JSON string to a Google Credentials object.

Specified by:
    `[getGoogleCredentials](CredentialsHelper.html#getGoogleCredentials\(java.lang.String\))` in interface `[CredentialsHelper](CredentialsHelper.html "interface in com.google.adk.tools.applicationintegrationtoolset")`
Parameters:
    `serviceAccountJson` \- The service account JSON string.
Returns:
    A Google Credentials object.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- when an error occurs during the conversion.




* * *

Copyright (C) 1980\. All rights reserved.
