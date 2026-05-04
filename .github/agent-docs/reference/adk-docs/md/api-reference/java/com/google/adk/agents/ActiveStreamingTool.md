JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ActiveStreamingTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [ActiveStreamingTool](ActiveStreamingTool.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ActiveStreamingTool(Disposable)
     2. ActiveStreamingTool(LiveRequestQueue)
     3. ActiveStreamingTool(Disposable, LiveRequestQueue)
     4. ActiveStreamingTool()
  5. Method Details
     1. task()
     2. task(Disposable)
     3. stream()
     4. stream(LiveRequestQueue)

Hide sidebar  Show sidebar

# Class ActiveStreamingTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.ActiveStreamingTool

* * *

public class ActiveStreamingTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Manages streaming tool related resources during invocation.

  * ## Constructor Summary

Constructors

Constructor

Description

`ActiveStreamingTool()`

 

`ActiveStreamingTool([LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)`

 

`ActiveStreamingTool(io.reactivex.rxjava3.disposables.Disposable task)`

 

`ActiveStreamingTool(io.reactivex.rxjava3.disposables.Disposable task, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`@Nullable [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")`

`stream()`

Returns the active stream of this streaming tool.

`void`

`stream(@Nullable [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)`

Sets the active stream of this streaming tool.

`@Nullable io.reactivex.rxjava3.disposables.Disposable`

`task()`

Returns the active task of this streaming tool.

`void`

`task(@Nullable io.reactivex.rxjava3.disposables.Disposable task)`

Sets the active task of this streaming tool.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ActiveStreamingTool

public ActiveStreamingTool(io.reactivex.rxjava3.disposables.Disposable task)

    * ### ActiveStreamingTool

public ActiveStreamingTool([LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)

    * ### ActiveStreamingTool

public ActiveStreamingTool(io.reactivex.rxjava3.disposables.Disposable task, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)

    * ### ActiveStreamingTool

public ActiveStreamingTool()

  * ## Method Details

    * ### task

public @Nullable io.reactivex.rxjava3.disposables.Disposable task()

Returns the active task of this streaming tool.

    * ### task

public void task(@Nullable io.reactivex.rxjava3.disposables.Disposable task)

Sets the active task of this streaming tool.

    * ### stream

public @Nullable [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream()

Returns the active stream of this streaming tool.

    * ### stream

public void stream(@Nullable [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") stream)

Sets the active stream of this streaming tool.




* * *

Copyright (C) 1980\. All rights reserved.
