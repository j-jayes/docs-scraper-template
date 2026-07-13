JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/App.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.apps](package-summary.html)
  2. [App](App.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. name()
     2. rootAgent()
     3. plugins()
     4. eventsCompactionConfig()
     5. contextCacheConfig()
     6. resumabilityConfig()
     7. builder()

Hide sidebar  Show sidebar

# Class App

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.apps.App

* * *

public class App extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Represents an LLM-backed agentic application. 

An `App` is the top-level container for an agentic system powered by LLMs. It manages a root agent (`rootAgent`), which serves as the root of an agent tree, enabling coordination and communication across all agents in the hierarchy. The `plugins` are application-wide components that provide shared capabilities and services to the entire system.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

Builder for [`App`](App.html "class in com.google.adk.apps").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [App.Builder](App.Builder.html "class in com.google.adk.apps")`

`builder()`

 

`@Nullable [ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents")`

`contextCacheConfig()`

 

`@Nullable [EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer")`

`eventsCompactionConfig()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")>`

`plugins()`

 

`@Nullable [ResumabilityConfig](ResumabilityConfig.html "class in com.google.adk.apps")`

`resumabilityConfig()`

 

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`rootAgent()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### name

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

    * ### rootAgent

public [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") rootAgent()

    * ### plugins

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins()

    * ### eventsCompactionConfig

public @Nullable [EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig()

    * ### contextCacheConfig

public @Nullable [ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig()

    * ### resumabilityConfig

public @Nullable [ResumabilityConfig](ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig()

    * ### builder

public static [App.Builder](App.Builder.html "class in com.google.adk.apps") builder()




* * *

Copyright (C) 1980\. All rights reserved.
