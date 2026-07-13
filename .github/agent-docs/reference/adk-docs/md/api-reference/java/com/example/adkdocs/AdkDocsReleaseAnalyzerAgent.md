JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/AdkDocsReleaseAnalyzerAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkdocs](package-summary.html)
  2. [AdkDocsReleaseAnalyzerAgent](AdkDocsReleaseAnalyzerAgent.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. ROOT_AGENT

Hide sidebar  Show sidebar

# Class AdkDocsReleaseAnalyzerAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkdocs.AdkDocsReleaseAnalyzerAgent

* * *

public final class AdkDocsReleaseAnalyzerAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Analyzes the diff between two code releases, files a deduplicated GitHub issue listing the documentation updates needed, and opens a pull request per recommendation that applies the edit. Java port of the Python `adk_release_analyzer`/`adk_docs_updater` samples.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`ROOT_AGENT`

 

  * ## Method Summary

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### ROOT_AGENT

public static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") ROOT_AGENT




* * *

Copyright (C) 1980\. All rights reserved.
