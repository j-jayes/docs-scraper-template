JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/App.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.apps](package-summary.html)
  2. [App](App.html)
  3. [Builder](App.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. name(String)
     2. rootAgent(BaseAgent)
     3. plugins(List)
     4. eventsCompactionConfig(EventsCompactionConfig)
     5. contextCacheConfig(ContextCacheConfig)
     6. build()

Hide sidebar  Show sidebar

# Class App.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.apps.App.Builder

Enclosing class:
    `[App](App.html "class in com.google.adk.apps")`

* * *

public static class App.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`App`](App.html "class in com.google.adk.apps").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[App](App.html "class in com.google.adk.apps")`

`build()`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`contextCacheConfig([ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`eventsCompactionConfig([EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`rootAgent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") rootAgent)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

    * ### rootAgent

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") rootAgent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") rootAgent)

    * ### plugins

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### eventsCompactionConfig

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") eventsCompactionConfig([EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)

    * ### contextCacheConfig

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") contextCacheConfig([ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)

    * ### build

public [App](App.html "class in com.google.adk.apps") build()




* * *

Copyright (C) 1980\. All rights reserved.
