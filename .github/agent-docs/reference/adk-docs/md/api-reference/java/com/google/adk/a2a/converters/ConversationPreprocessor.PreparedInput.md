JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ConversationPreprocessor.PreparedInput.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [ConversationPreprocessor](ConversationPreprocessor.html)
  3. [PreparedInput](ConversationPreprocessor.PreparedInput.html)



Contents 

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. historyEvents
     2. userContent
     3. userEvent
  6. Constructor Details
     1. PreparedInput(ImmutableList, Optional, Optional)

Hide sidebar  Show sidebar

# Class ConversationPreprocessor.PreparedInput

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.ConversationPreprocessor.PreparedInput

Enclosing class:
    `[ConversationPreprocessor](ConversationPreprocessor.html "class in com.google.adk.a2a.converters")`

* * *

public static final class ConversationPreprocessor.PreparedInput extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Immutable value that surfaces the results of preprocessing. 

All fields are deliberately exposed to avoid additional AutoValue dependencies in this internal module.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`final com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")>`

`historyEvents`

Historical events that should remain in the session transcript.

`final [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`userContent`

Extracted user message content, if a qualifying text event was found.

`final [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`userEvent`

The concrete event that supplied `userContent`, for callers needing metadata.

  * ## Constructor Summary

Constructors

Constructor

Description

`PreparedInput(com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")> historyEvents, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> userEvent)`

Creates a new instance.

  * ## Method Summary

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### historyEvents

public final com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")> historyEvents

Historical events that should remain in the session transcript.

    * ### userContent

public final [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent

Extracted user message content, if a qualifying text event was found.

    * ### userEvent

public final [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> userEvent

The concrete event that supplied `userContent`, for callers needing metadata.

  * ## Constructor Details

    * ### PreparedInput

public PreparedInput(com.google.common.collect.ImmutableList<[Event](../../events/Event.html "class in com.google.adk.events")> historyEvents, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Event](../../events/Event.html "class in com.google.adk.events")> userEvent)

Creates a new instance.

Parameters:
    `historyEvents` \- ordered historical events retained in the session stream
    `userContent` \- optional content to place on the pending user message
    `userEvent` \- optional original event that contained `userContent`




* * *

Copyright (C) 1980\. All rights reserved.
