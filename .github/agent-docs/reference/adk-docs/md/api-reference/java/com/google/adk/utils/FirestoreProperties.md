JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FirestoreProperties.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [FirestoreProperties](FirestoreProperties.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getProperty(String)
     2. getFirebaseRootCollectionName()
     3. getStopWords()
     4. getGcsAdkBucketName()
     5. getInstance()
     6. resetForTest()

Hide sidebar  Show sidebar

# Class FirestoreProperties

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.FirestoreProperties

* * *

public class FirestoreProperties extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Placeholder class to test that the FirestoreProperties file is correctly included in the test resources.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getFirebaseRootCollectionName()`

Get the root collection name from the properties file, or return the default value if not found.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getGcsAdkBucketName()`

Get the GCS ADK bucket name from the properties file.

`static [FirestoreProperties](FirestoreProperties.html "class in com.google.adk.utils")`

`getInstance()`

Returns a singleton instance of FirestoreProperties.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") key)`

Functionality to read a property from the loaded properties file.

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getStopWords()`

Get the stop words for keyword extraction from the properties file, or return the default set if not found.

`static void`

`resetForTest()`

Resets the singleton instance.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### getProperty

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") key)

Functionality to read a property from the loaded properties file.

Parameters:
    `key` \- the property key
Returns:
    the property value, or null if not found

    * ### getFirebaseRootCollectionName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getFirebaseRootCollectionName()

Get the root collection name from the properties file, or return the default value if not found.

Returns:
    the root collection name

    * ### getStopWords

public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getStopWords()

Get the stop words for keyword extraction from the properties file, or return the default set if not found.

Returns:
    the set of stop words

    * ### getGcsAdkBucketName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getGcsAdkBucketName()

Get the GCS ADK bucket name from the properties file.

Returns:
    the GCS ADK bucket name

    * ### getInstance

public static [FirestoreProperties](FirestoreProperties.html "class in com.google.adk.utils") getInstance()

Returns a singleton instance of FirestoreProperties.

Returns:
    the FirestoreProperties instance

    * ### resetForTest

public static void resetForTest()

Resets the singleton instance. For testing purposes only.




* * *

Copyright (C) 1980\. All rights reserved.
