JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ReadonlyContext.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [ReadonlyContext](ReadonlyContext.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. invocationContext
  6. Constructor Details
     1. ReadonlyContext(InvocationContext)
  7. Method Details
     1. userContent()
     2. invocationId()
     3. branch()
     4. agentName()
     5. sessionId()
     6. events()
     7. state()



# Class ReadonlyContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.ReadonlyContext

Direct Known Subclasses:
    `[CallbackContext](CallbackContext.html "class in com.google.adk.agents")`

* * *

public class ReadonlyContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Provides read-only access to the context of an agent run.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected final [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`invocationContext`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`ReadonlyContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`agentName()`

Returns the name of the agent currently running.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`branch()`

Returns the branch of the current invocation, if present.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`events()`

Returns an unmodifiable view of the events of the session.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`invocationId()`

Returns the ID of the current invocation.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`sessionId()`

Returns the session ID.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`state()`

Returns an unmodifiable view of the state of the session.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`userContent()`

Returns the user content that initiated this invocation.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### invocationContext

protected final [InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext

  * ## Constructor Details

    * ### ReadonlyContext

public ReadonlyContext([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

  * ## Method Details

    * ### userContent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent()

Returns the user content that initiated this invocation.

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId()

Returns the ID of the current invocation.

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch()

Returns the branch of the current invocation, if present.

    * ### agentName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName()

Returns the name of the agent currently running.

    * ### sessionId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId()

Returns the session ID.

    * ### events

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events()

Returns an unmodifiable view of the events of the session. 

**Warning:** This is a live view, not a snapshot.

    * ### state

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state()

Returns an unmodifiable view of the state of the session. 

**Warning:** This is a live view, not a snapshot.




* * *

Copyright (C) 2025\. All rights reserved.
