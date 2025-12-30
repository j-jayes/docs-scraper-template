JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Event.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [Event](Event.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. generateEventId()
     2. id()
     3. setId(String)
     4. invocationId()
     5. setInvocationId(String)
     6. author()
     7. setAuthor(String)
     8. content()
     9. setContent(Optional)
     10. actions()
     11. setActions(EventActions)
     12. longRunningToolIds()
     13. setLongRunningToolIds(Optional)
     14. partial()
     15. setPartial(Optional)
     16. turnComplete()
     17. setTurnComplete(Optional)
     18. errorCode()
     19. setErrorCode(Optional)
     20. errorMessage()
     21. setErrorMessage(Optional)
     22. interrupted()
     23. setInterrupted(Optional)
     24. branch()
     25. branch(String)
     26. branch(Optional)
     27. groundingMetadata()
     28. setGroundingMetadata(Optional)
     29. timestamp()
     30. setTimestamp(long)
     31. functionCalls()
     32. functionResponses()
     33. finalResponse()
     34. stringifyContent()
     35. builder()
     36. fromJson(String)
     37. toBuilder()
     38. equals(Object)
     39. toString()
     40. hashCode()



# Class Event

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.events.Event

* * *

public class Event extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Represents an event in a session.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

Builder for [`Event`](Event.html "class in com.google.adk.events").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[EventActions](EventActions.html "class in com.google.adk.events")`

`actions()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`author()`

The author of the event, it could be the name of the agent or "user" literal.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`branch()`

The branch of the event.

`void`

`branch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Sets the branch for this event.

`void`

`branch([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch)`

 

`static [Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`builder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`content()`

 

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") obj)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason>`

`errorCode()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`errorMessage()`

 

`final boolean`

`finalResponse()`

Returns true if this is a final response.

`static [Event](Event.html "class in com.google.adk.events")`

`fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)`

Parses an event from a JSON string.

`final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall>`

`functionCalls()`

Returns all function calls from this event.

`final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionResponse>`

`functionResponses()`

Returns all function responses from this event.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`generateEventId()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata>`

`groundingMetadata()`

The grounding metadata of the event.

`int`

`hashCode()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`id()`

The event id.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`interrupted()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`invocationId()`

Id of the invocation that this event belongs to.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`

`longRunningToolIds()`

Set of ids of the long running function calls.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`partial()`

partial is true for incomplete chunks from the LLM streaming response.

`void`

`setActions([EventActions](EventActions.html "class in com.google.adk.events") actions)`

 

`void`

`setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author)`

 

`void`

`setContent([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content)`

 

`void`

`setErrorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode)`

 

`void`

`setErrorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage)`

 

`void`

`setGroundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata)`

 

`void`

`setId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)`

 

`void`

`setInterrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted)`

 

`void`

`setInvocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

 

`void`

`setLongRunningToolIds([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> longRunningToolIds)`

 

`void`

`setPartial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial)`

 

`void`

`setTimestamp(long timestamp)`

 

`void`

`setTurnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete)`

 

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`stringifyContent()`

Converts the event content into a readable string.

`long`

`timestamp()`

The timestamp of the event.

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`toBuilder()`

Creates a builder pre-filled with this event's values.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")>`

`turnComplete()`

 

### Methods inherited from class com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\)), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\)), [getMapper](../JsonBaseModel.html#getMapper\(\)), [toJson](../JsonBaseModel.html#toJson\(\)), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\)), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### generateEventId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") generateEventId()

    * ### id

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id()

The event id.

    * ### setId

public void setId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") id)

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId()

Id of the invocation that this event belongs to.

    * ### setInvocationId

public void setInvocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)

    * ### author

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author()

The author of the event, it could be the name of the agent or "user" literal.

    * ### setAuthor

public void setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author)

    * ### content

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content()

    * ### setContent

public void setContent([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> content)

    * ### actions

public [EventActions](EventActions.html "class in com.google.adk.events") actions()

    * ### setActions

public void setActions([EventActions](EventActions.html "class in com.google.adk.events") actions)

    * ### longRunningToolIds

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> longRunningToolIds()

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running.

    * ### setLongRunningToolIds

public void setLongRunningToolIds([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> longRunningToolIds)

    * ### partial

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial()

partial is true for incomplete chunks from the LLM streaming response. The last chunk's partial is False.

    * ### setPartial

public void setPartial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial)

    * ### turnComplete

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete()

    * ### setTurnComplete

public void setTurnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete)

    * ### errorCode

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode()

    * ### setErrorCode

public void setErrorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode)

    * ### errorMessage

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage()

    * ### setErrorMessage

public void setErrorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage)

    * ### interrupted

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted()

    * ### setInterrupted

public void setInterrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted)

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch()

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3. Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

    * ### branch

public void branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)

Sets the branch for this event. 

Format: agentA.agentB.agentC — shows hierarchy of nested agents.

Parameters:
    `branch` \- Branch identifier.

    * ### branch

public void branch([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch)

    * ### groundingMetadata

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata()

The grounding metadata of the event.

    * ### setGroundingMetadata

public void setGroundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata)

    * ### timestamp

public long timestamp()

The timestamp of the event.

    * ### setTimestamp

public void setTimestamp(long timestamp)

    * ### functionCalls

public final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall> functionCalls()

Returns all function calls from this event.

    * ### functionResponses

public final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionResponse> functionResponses()

Returns all function responses from this event.

    * ### finalResponse

public final boolean finalResponse()

Returns true if this is a final response.

    * ### stringifyContent

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") stringifyContent()

Converts the event content into a readable string. 

Includes text, function calls, and responses.

Returns:
    Stringified content.

    * ### builder

public static [Event.Builder](Event.Builder.html "class in com.google.adk.events") builder()

    * ### fromJson

public static [Event](Event.html "class in com.google.adk.events") fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)

Parses an event from a JSON string.

    * ### toBuilder

public [Event.Builder](Event.Builder.html "class in com.google.adk.events") toBuilder()

Creates a builder pre-filled with this event's values.

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") obj)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 2025\. All rights reserved.
