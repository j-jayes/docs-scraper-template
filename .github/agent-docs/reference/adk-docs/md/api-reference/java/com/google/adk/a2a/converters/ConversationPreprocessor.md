JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ConversationPreprocessor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [ConversationPreprocessor](ConversationPreprocessor.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. extractHistoryAndUserContent(List)

Hide sidebar  Show sidebar

# Class ConversationPreprocessor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.ConversationPreprocessor

* * *

public final class ConversationPreprocessor extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Preprocesses a batch of ADK events prior to invoking a remote A2A agent. 

The class splits the conversation into two logical buckets: 

  * The historical session events that should be preserved as-is when relayed over the wire. 
  * The most recent user-authored text event, surfaced separately so it can be supplied as the pending user input on the [`InvocationContext`](../../agents/InvocationContext.html "class in com.google.adk.agents"). 


This mirrors the Python A2A implementation where the in-flight user message is maintained separately from the persisted transcript. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[ConversationPreprocessor.PreparedInput](ConversationPreprocessor.PreparedInput.html "class in com.google.adk.a2a.converters")`

Immutable value that surfaces the results of preprocessing.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ConversationPreprocessor.PreparedInput](ConversationPreprocessor.PreparedInput.html "class in com.google.adk.a2a.converters")`

`extractHistoryAndUserContent([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> inputEvents)`

Splits the provided event list into history and the latest user-authored text message.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### extractHistoryAndUserContent

public static [ConversationPreprocessor.PreparedInput](ConversationPreprocessor.PreparedInput.html "class in com.google.adk.a2a.converters") extractHistoryAndUserContent([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> inputEvents)

Splits the provided event list into history and the latest user-authored text message.

Parameters:
    `inputEvents` \- ordered session events, oldest to newest; may be `null`
Returns:
    container encapsulating the derived history, optional user content, and the original user event when present




* * *

Copyright (C) 1980\. All rights reserved.
