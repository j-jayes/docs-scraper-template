JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Recording.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.recordings](package-summary.html)
  2. [Recording](Recording.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Recording()
  6. Method Details
     1. userMessageIndex()
     2. agentName()
     3. llmRecording()
     4. toolRecording()
     5. builder()

Hide sidebar  Show sidebar

# Class Recording

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.recordings.Recording

* * *

public abstract class Recording extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Single interaction recording, ordered by request timestamp.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[Recording.Builder](Recording.Builder.html "class in com.google.adk.plugins.recordings")`

Builder for Recording.

  * ## Constructor Summary

Constructors

Constructor

Description

`Recording()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`agentName()`

Name of the agent.

`static [Recording.Builder](Recording.Builder.html "class in com.google.adk.plugins.recordings")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmRecording](LlmRecording.html "class in com.google.adk.plugins.recordings")>`

`llmRecording()`

LLM request-response pair.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolRecording](ToolRecording.html "class in com.google.adk.plugins.recordings")>`

`toolRecording()`

Tool call-response pair.

`abstract int`

`userMessageIndex()`

Index of the user message this recording belongs to (0-based).

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Recording

public Recording()

  * ## Method Details

    * ### userMessageIndex

public abstract int userMessageIndex()

Index of the user message this recording belongs to (0-based).

    * ### agentName

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName()

Name of the agent.

    * ### llmRecording

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmRecording](LlmRecording.html "class in com.google.adk.plugins.recordings")> llmRecording()

LLM request-response pair.

    * ### toolRecording

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ToolRecording](ToolRecording.html "class in com.google.adk.plugins.recordings")> toolRecording()

Tool call-response pair.

    * ### builder

public static [Recording.Builder](Recording.Builder.html "class in com.google.adk.plugins.recordings") builder()




* * *

Copyright (C) 1980\. All rights reserved.
