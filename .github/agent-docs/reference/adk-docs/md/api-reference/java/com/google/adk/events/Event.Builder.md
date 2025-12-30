JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Event.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [Event](Event.html)
  3. [Builder](Event.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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
     5. content(Optional)
     6. actions(EventActions)
     7. longRunningToolIds(Set)
     8. longRunningToolIds(Optional)
     9. partial(Boolean)
     10. partial(Optional)
     11. turnComplete(Boolean)
     12. turnComplete(Optional)
     13. errorCode(FinishReason)
     14. errorCode(Optional)
     15. errorMessage(String)
     16. errorMessage(Optional)
     17. interrupted(Boolean)
     18. interrupted(Optional)
     19. timestamp(long)
     20. timestamp(Optional)
     21. branch(String)
     22. branch(Optional)
     23. groundingMetadata(GroundingMetadata)
     24. groundingMetadata(Optional)
     25. build()



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

`actions([EventActions](EventActions.html "class in com.google.adk.events") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`author([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`branch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`branch([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)`

 

`[Event](Event.html "class in com.google.adk.events")`

`build()`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`content(com.google.genai.types.Content value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`content([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorCode(com.google.genai.types.FinishReason value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`errorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`groundingMetadata(com.google.genai.types.GroundingMetadata value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`groundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`id([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`interrupted([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`interrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`invocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`longRunningToolIds([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`longRunningToolIds([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`partial([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`partial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`timestamp(long value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`timestamp([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html "class or interface in java.lang")> value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`turnComplete([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)`

 

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`turnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

    * ### content

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") content([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> value)

    * ### actions

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") actions([EventActions](EventActions.html "class in com.google.adk.events") value)

    * ### longRunningToolIds

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") longRunningToolIds(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)

    * ### longRunningToolIds

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") longRunningToolIds([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> value)

    * ### partial

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### partial

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") partial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)

    * ### turnComplete

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### turnComplete

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") turnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)

    * ### errorCode

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorCode(@Nullable com.google.genai.types.FinishReason value)

    * ### errorCode

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> value)

    * ### errorMessage

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### errorMessage

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") errorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)

    * ### interrupted

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") value)

    * ### interrupted

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") interrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> value)

    * ### timestamp

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") timestamp(long value)

    * ### timestamp

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") timestamp([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html "class or interface in java.lang")> value)

    * ### branch

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)

    * ### branch

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") branch([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)

    * ### groundingMetadata

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata value)

    * ### groundingMetadata

@CanIgnoreReturnValue public [Event.Builder](Event.Builder.html "class in com.google.adk.events") groundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> value)

    * ### build

public [Event](Event.html "class in com.google.adk.events") build()




* * *

Copyright (C) 2025\. All rights reserved.
