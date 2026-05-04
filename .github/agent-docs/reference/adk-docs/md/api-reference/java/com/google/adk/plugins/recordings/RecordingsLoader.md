JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RecordingsLoader.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.recordings](package-summary.html)
  2. [RecordingsLoader](RecordingsLoader.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. load(Path)
     2. load(InputStream)
     3. load(String)

Hide sidebar  Show sidebar

# Class RecordingsLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.recordings.RecordingsLoader

* * *

public final class RecordingsLoader extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for loading recordings from YAML files.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings")`

`load([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") inputStream)`

Loads recordings from a YAML input stream.

`static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings")`

`load([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") yamlContent)`

Loads recordings from a YAML string.

`static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings")`

`load([Path](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/Path.html "interface in java.nio.file") path)`

Loads recordings from a YAML file.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### load

public static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings") load([Path](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/Path.html "interface in java.nio.file") path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Loads recordings from a YAML file.

Parameters:
    `path` \- the path to the YAML file
Returns:
    the parsed Recordings object
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- if an I/O error occurs

    * ### load

public static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings") load([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") inputStream) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Loads recordings from a YAML input stream.

Parameters:
    `inputStream` \- the YAML input stream
Returns:
    the parsed Recordings object
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- if an I/O error occurs

    * ### load

public static [Recordings](Recordings.html "class in com.google.adk.plugins.recordings") load([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") yamlContent) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Loads recordings from a YAML string.

Parameters:
    `yamlContent` \- the YAML content as a string
Returns:
    the parsed Recordings object
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")` \- if an I/O error occurs




* * *

Copyright (C) 1980\. All rights reserved.
