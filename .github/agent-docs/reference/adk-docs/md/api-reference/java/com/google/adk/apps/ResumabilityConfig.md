JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ResumabilityConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.apps](package-summary.html)
  2. [ResumabilityConfig](ResumabilityConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ResumabilityConfig()
  6. Method Details
     1. isResumable()
     2. isPlainTextContinuationAutoResume()
     3. builder()

Hide sidebar  Show sidebar

# Class ResumabilityConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.apps.ResumabilityConfig

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public abstract class ResumabilityConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Resumability config for every agent in an app: pause on a long-running call and resume from the last event. 

The two flags select different resumption flows and are mutually exclusive: `isResumable()` checkpoints agent state and resumes from it, `isPlainTextContinuationAutoResume()` selects the deprecated legacy flow, and with neither set the app never pauses. 

Experimental: resume is best-effort and at-least-once, so a resuming tool must be idempotent and in-memory state is lost on resumption.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps")`

Builder for [`ResumabilityConfig`](ResumabilityConfig.html "class in com.google.adk.apps").

  * ## Constructor Summary

Constructors

Constructor

Description

`ResumabilityConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`static [ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps")`

`builder()`

 

`abstract boolean`

`isPlainTextContinuationAutoResume()`

Deprecated.

Back-compat shim for callers that deliver a resume as a plain-text turn; migrate to `Runner.runAsync(userId, sessionId, invocationId, message, runConfig, stateDelta)` or answer the paused call with a function response, and set `isResumable()` instead; this flag will be removed.

`abstract boolean`

`isResumable()`

Whether the app supports agent resumption, checkpointing agent state as it runs.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ResumabilityConfig

public ResumabilityConfig()

  * ## Method Details

    * ### isResumable

public abstract boolean isResumable()

Whether the app supports agent resumption, checkpointing agent state as it runs.

    * ### isPlainTextContinuationAutoResume

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public abstract boolean isPlainTextContinuationAutoResume()

Deprecated.

Back-compat shim for callers that deliver a resume as a plain-text turn; migrate to `Runner.runAsync(userId, sessionId, invocationId, message, runConfig, stateDelta)` or answer the paused call with a function response, and set `isResumable()` instead; this flag will be removed.

Whether a plain-text `runAsync` continuation -- a user message that is not a function response -- resumes the last unfinished invocation instead of starting a new one; off by default. 

Selects the legacy resumption flow, which reconstructs the resume point from session events and never persists agent state; mutually exclusive with `isResumable()`.

    * ### builder

public static [ResumabilityConfig.Builder](ResumabilityConfig.Builder.html "class in com.google.adk.apps") builder()




* * *

Copyright (C) 1980\. All rights reserved.
