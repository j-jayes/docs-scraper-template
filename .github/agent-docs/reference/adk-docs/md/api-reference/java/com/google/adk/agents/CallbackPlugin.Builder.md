JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CallbackPlugin.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [CallbackPlugin](CallbackPlugin.html)
  3. [Builder](CallbackPlugin.Builder.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. addBeforeAgentCallback(Callbacks.BeforeAgentCallback)
     2. addBeforeAgentCallbackSync(Callbacks.BeforeAgentCallbackSync)
     3. addAfterAgentCallback(Callbacks.AfterAgentCallback)
     4. addAfterAgentCallbackSync(Callbacks.AfterAgentCallbackSync)
     5. addBeforeModelCallback(Callbacks.BeforeModelCallback)
     6. addBeforeModelCallbackSync(Callbacks.BeforeModelCallbackSync)
     7. addAfterModelCallback(Callbacks.AfterModelCallback)
     8. addAfterModelCallbackSync(Callbacks.AfterModelCallbackSync)
     9. addBeforeToolCallback(Callbacks.BeforeToolCallback)
     10. addBeforeToolCallbackSync(Callbacks.BeforeToolCallbackSync)
     11. addAfterToolCallback(Callbacks.AfterToolCallback)
     12. addAfterToolCallbackSync(Callbacks.AfterToolCallbackSync)
     13. addCallback(Callbacks.BeforeAgentCallbackBase)
     14. addCallback(Callbacks.AfterAgentCallbackBase)
     15. addCallback(Callbacks.BeforeModelCallbackBase)
     16. addCallback(Callbacks.AfterModelCallbackBase)
     17. addCallback(Callbacks.BeforeToolCallbackBase)
     18. addCallback(Callbacks.AfterToolCallbackBase)
     19. build()

Hide sidebar  Show sidebar

# Class CallbackPlugin.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.CallbackPlugin.Builder

Enclosing class:
    `[CallbackPlugin](CallbackPlugin.html "class in com.google.adk.agents")`

* * *

public static class CallbackPlugin.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`CallbackPlugin`](CallbackPlugin.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addAfterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addBeforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.AfterAgentCallbackBase callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.AfterModelCallbackBase callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.AfterToolCallbackBase callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.BeforeAgentCallbackBase callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.BeforeModelCallbackBase callback)`

 

`[CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents")`

`addCallback(com.google.adk.agents.Callbacks.BeforeToolCallbackBase callback)`

 

`[CallbackPlugin](CallbackPlugin.html "class in com.google.adk.agents")`

`build()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### addBeforeAgentCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeAgentCallback([Callbacks.BeforeAgentCallback](Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents") callback)

    * ### addBeforeAgentCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeAgentCallbackSync([Callbacks.BeforeAgentCallbackSync](Callbacks.BeforeAgentCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addAfterAgentCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterAgentCallback([Callbacks.AfterAgentCallback](Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents") callback)

    * ### addAfterAgentCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterAgentCallbackSync([Callbacks.AfterAgentCallbackSync](Callbacks.AfterAgentCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addBeforeModelCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeModelCallback([Callbacks.BeforeModelCallback](Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents") callback)

    * ### addBeforeModelCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeModelCallbackSync([Callbacks.BeforeModelCallbackSync](Callbacks.BeforeModelCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addAfterModelCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterModelCallback([Callbacks.AfterModelCallback](Callbacks.AfterModelCallback.html "interface in com.google.adk.agents") callback)

    * ### addAfterModelCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterModelCallbackSync([Callbacks.AfterModelCallbackSync](Callbacks.AfterModelCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addBeforeToolCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeToolCallback([Callbacks.BeforeToolCallback](Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents") callback)

    * ### addBeforeToolCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addBeforeToolCallbackSync([Callbacks.BeforeToolCallbackSync](Callbacks.BeforeToolCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addAfterToolCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterToolCallback([Callbacks.AfterToolCallback](Callbacks.AfterToolCallback.html "interface in com.google.adk.agents") callback)

    * ### addAfterToolCallbackSync

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addAfterToolCallbackSync([Callbacks.AfterToolCallbackSync](Callbacks.AfterToolCallbackSync.html "interface in com.google.adk.agents") callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.BeforeAgentCallbackBase callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.AfterAgentCallbackBase callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.BeforeModelCallbackBase callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.AfterModelCallbackBase callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.BeforeToolCallbackBase callback)

    * ### addCallback

@CanIgnoreReturnValue public [CallbackPlugin.Builder](CallbackPlugin.Builder.html "class in com.google.adk.agents") addCallback(com.google.adk.agents.Callbacks.AfterToolCallbackBase callback)

    * ### build

public [CallbackPlugin](CallbackPlugin.html "class in com.google.adk.agents") build()




* * *

Copyright (C) 1980\. All rights reserved.
