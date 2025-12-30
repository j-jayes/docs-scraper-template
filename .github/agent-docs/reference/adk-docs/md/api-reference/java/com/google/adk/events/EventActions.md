JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventActions.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [EventActions](EventActions.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. EventActions()
  6. Method Details
     1. skipSummarization()
     2. setSkipSummarization(Boolean)
     3. setSkipSummarization(Optional)
     4. setSkipSummarization(boolean)
     5. stateDelta()
     6. setStateDelta(ConcurrentMap)
     7. artifactDelta()
     8. setArtifactDelta(ConcurrentMap)
     9. transferToAgent()
     10. setTransferToAgent(Optional)
     11. setTransferToAgent(String)
     12. escalate()
     13. setEscalate(Optional)
     14. setEscalate(boolean)
     15. requestedAuthConfigs()
     16. setRequestedAuthConfigs(ConcurrentMap)
     17. endInvocation()
     18. setEndInvocation(Optional)
     19. setEndInvocation(boolean)
     20. builder()
     21. toBuilder()
     22. equals(Object)
     23. hashCode()



# Class EventActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.events.EventActions

* * *

public class EventActions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Represents the actions attached to an event.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

Builder for [`EventActions`](EventActions.html "class in com.google.adk.events").

  * ## Constructor Summary

Constructors

Constructor

Description

`EventActions()`

Default constructor for Jackson.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part>`

`artifactDelta()`

 

`static [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`builder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`endInvocation()`

 

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`escalate()`

 

`int`

`hashCode()`

 

`[ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`requestedAuthConfigs()`

 

`void`

`setArtifactDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part> artifactDelta)`

 

`void`

`setEndInvocation(boolean endInvocation)`

 

`void`

`setEndInvocation([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> endInvocation)`

 

`void`

`setEscalate(boolean escalate)`

 

`void`

`setEscalate([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> escalate)`

 

`void`

`setRequestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> requestedAuthConfigs)`

 

`void`

`setSkipSummarization(boolean skipSummarization)`

 

`void`

`setSkipSummarization([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") skipSummarization)`

 

`void`

`setSkipSummarization([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> skipSummarization)`

 

`void`

`setStateDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

 

`void`

`setTransferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") transferToAgent)`

 

`void`

`setTransferToAgent([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`skipSummarization()`

 

`[ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`stateDelta()`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`toBuilder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`transferToAgent()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### EventActions

public EventActions()

Default constructor for Jackson.

  * ## Method Details

    * ### skipSummarization

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> skipSummarization()

    * ### setSkipSummarization

public void setSkipSummarization(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") skipSummarization)

    * ### setSkipSummarization

public void setSkipSummarization([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> skipSummarization)

    * ### setSkipSummarization

public void setSkipSummarization(boolean skipSummarization)

    * ### stateDelta

public [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta()

    * ### setStateDelta

public void setStateDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)

    * ### artifactDelta

public [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part> artifactDelta()

    * ### setArtifactDelta

public void setArtifactDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part> artifactDelta)

    * ### transferToAgent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent()

    * ### setTransferToAgent

public void setTransferToAgent([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)

    * ### setTransferToAgent

public void setTransferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") transferToAgent)

    * ### escalate

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> escalate()

    * ### setEscalate

public void setEscalate([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> escalate)

    * ### setEscalate

public void setEscalate(boolean escalate)

    * ### requestedAuthConfigs

public [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> requestedAuthConfigs()

    * ### setRequestedAuthConfigs

public void setRequestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> requestedAuthConfigs)

    * ### endInvocation

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> endInvocation()

    * ### setEndInvocation

public void setEndInvocation([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> endInvocation)

    * ### setEndInvocation

public void setEndInvocation(boolean endInvocation)

    * ### builder

public static [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") builder()

    * ### toBuilder

public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") toBuilder()

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 2025\. All rights reserved.
