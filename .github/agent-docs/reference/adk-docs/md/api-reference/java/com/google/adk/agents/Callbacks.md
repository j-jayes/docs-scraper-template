JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary

Hide sidebar  Show sidebar

# Class Callbacks

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.Callbacks

* * *

public final class Callbacks extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Functional interfaces for agent lifecycle callbacks.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static interface `

`[Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")`

Async callback interface for actions to be performed after an agent has finished running.

`static interface `

`[Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync afterAgentCallback.

`static interface `

`[Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")`

 

`static interface `

`[Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync afterModelCallback.

`static interface `

`[Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")`

Async callback interface for actions to be performed after a tool has been invoked.

`static interface `

`[Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync afterToolCallback.

`static interface `

`[Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")`

Async callback interface for actions to be performed before an agent starts running.

`static interface `

`[Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync beforeAgentCallback.

`static interface `

`[Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")`

 

`static interface `

`[Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync beforeModelCallback.

`static interface `

`[Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")`

Async callback interface for actions to be performed before a tool is invoked.

`static interface `

`[Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync beforeToolCallback.

`static interface `

`[Callbacks.OnModelErrorCallback](Callbacks.OnModelErrorCallback.html "interface in com.google.adk.agents")`

Async callback interface for handling errors that occur during an LLM model call.

`static interface `

`[Callbacks.OnModelErrorCallbackSync](Callbacks.OnModelErrorCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync onModelErrorCallback.

`static interface `

`[Callbacks.OnToolErrorCallback](Callbacks.OnToolErrorCallback.html "interface in com.google.adk.agents")`

Async callback interface for handling errors that occur during a tool invocation.

`static interface `

`[Callbacks.OnToolErrorCallbackSync](Callbacks.OnToolErrorCallbackSync.html "interface in com.google.adk.agents")`

Helper interface to allow for sync onToolErrorCallback.

  * ## Method Summary

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




* * *

Copyright (C) 1980\. All rights reserved.
