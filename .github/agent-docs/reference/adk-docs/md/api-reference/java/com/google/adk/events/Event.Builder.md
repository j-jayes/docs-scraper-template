JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Event.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [Event](Event.html)
  3. [Builder](Event.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. id(String)
     2. invocationId(String)
     3. author(String)
     4. content(Content)
     5. actions(EventActions)
     6. longRunningToolIds(Set)
     7. partial(Boolean)
     8. turnComplete(Boolean)
     9. errorCode(FinishReason)
     10. errorMessage(String)
     11. finishReason(FinishReason)
     12. usageMetadata(GenerateContentResponseUsageMetadata)
     13. avgLogprobs(Double)
     14. interrupted(Boolean)
     15. timestamp(long)
     16. branch(String)
     17. groundingMetadata(GroundingMetadata)
     18. customMetadata(List)
     19. modelVersion(String)
     20. build()

Hide sidebar  Show sidebar

# Class Event.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.events.Event.Builder

Enclosing class:
    `[Event](Event.html "class in com.google.adk.events")`

* * *

public static class Event.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`Event`](Event.html "class in com.google.adk.events").

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

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`actions(@Nullable [EventActions](EventActions.html "class in com.google.adk.events") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`author([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`avgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event](Event.html "class in com.google.adk.events")`

`build()`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`content(@Nullable com.google.genai.types.Content value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`customMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.CustomMetadata> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorCode(@Nullable com.google.genai.types.FinishReason value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`finishReason(@Nullable com.google.genai.types.FinishReason value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`invocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`longRunningToolIds(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`modelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`timestamp(long value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`usageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata value)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### id

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### invocationId

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") invocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### author

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") author([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### content

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") content(@Nullable com.google.genai.types.Content value)

    * ### actions

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") actions(@Nullable [EventActions](EventActions.html "class in com.google.adk.events") value)

    * ### longRunningToolIds

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") longRunningToolIds(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)

    * ### partial

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### turnComplete

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### errorCode

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorCode(@Nullable com.google.genai.types.FinishReason value)

    * ### errorMessage

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### finishReason

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") finishReason(@Nullable com.google.genai.types.FinishReason value)

    * ### usageMetadata

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") usageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata value)

    * ### avgLogprobs

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") avgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") value)

    * ### interrupted

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### timestamp

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") timestamp(long value)

    * ### branch

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### groundingMetadata

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata value)

    * ### customMetadata

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") customMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.CustomMetadata> value)

    * ### modelVersion

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") modelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### build

public [Event](Event.html "class in com.google.adk.events") build()




* * *

Copyright (C) 1980\. All rights reserved.
