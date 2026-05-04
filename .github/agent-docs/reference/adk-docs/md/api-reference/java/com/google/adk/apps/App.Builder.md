JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/App.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     4. plugins(Plugin...)
     5. eventsCompactionConfig(EventsCompactionConfig)
     6. contextCacheConfig(ContextCacheConfig)
     7. build()

Hide sidebar  Show sidebar

# Class App.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.apps.App.Builder

Enclosing class:
    `[App](App.html "class in com.google.adk.apps")`

* * *

public static class App.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`plugins([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")... plugins)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[App.Builder](App.Builder.html "class in com.google.adk.apps")`

`rootAgent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") rootAgent)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### rootAgent

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") rootAgent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") rootAgent)

    * ### plugins

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### plugins

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") plugins([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")... plugins)

    * ### eventsCompactionConfig

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") eventsCompactionConfig([EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)

    * ### contextCacheConfig

@CanIgnoreReturnValue public [App.Builder](App.Builder.html "class in com.google.adk.apps") contextCacheConfig([ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)

    * ### build

public [App](App.html "class in com.google.adk.apps") build()




* * *

Copyright (C) 1980\. All rights reserved.
