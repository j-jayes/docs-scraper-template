JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Event.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.events](package-summary.html)
  2. [Event](Event.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
     1. Methods inherited from class JsonBaseModel
     2. Methods inherited from class Object
  4. Method Details
     1. generateEventId()
     2. id()
     3. setId(String)
     4. invocationId()
     5. setInvocationId(String)
     6. author()
     7. setAuthor(String)
     8. content()
     9. setContent(Content)
     10. actions()
     11. setActions(EventActions)
     12. longRunningToolIds()
     13. setLongRunningToolIds(Set)
     14. partial()
     15. setPartial(Boolean)
     16. turnComplete()
     17. setTurnComplete(Boolean)
     18. errorCode()
     19. finishReason()
     20. setErrorCode(FinishReason)
     21. setFinishReason(Optional)
     22. setFinishReason(FinishReason)
     23. errorMessage()
     24. setErrorMessage(String)
     25. usageMetadata()
     26. setUsageMetadata(GenerateContentResponseUsageMetadata)
     27. avgLogprobs()
     28. setAvgLogprobs(Double)
     29. interrupted()
     30. setInterrupted(Boolean)
     31. branch()
     32. branch(String)
     33. groundingMetadata()
     34. setGroundingMetadata(GroundingMetadata)
     35. customMetadata()
     36. setCustomMetadata(List)
     37. modelVersion()
     38. setModelVersion(String)
     39. inputTranscription()
     40. setInputTranscription(Transcription)
     41. outputTranscription()
     42. setOutputTranscription(Transcription)
     43. timestamp()
     44. setTimestamp(long)
     45. functionCalls()
     46. functionResponses()
     47. hasTrailingCodeExecutionResult()
     48. finalResponse()
     49. stringifyContent()
     50. builder()
     51. fromJson(String)
     52. toBuilder()
     53. equals(Object)
     54. toString()
     55. hashCode()

Hide sidebar  Show sidebar

# Class Event

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`[EventActions](EventActions.html "class in com.google.adk.events")`

`actions()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`author()`

The author of the event, it could be the name of the agent or "user" literal.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")>`

`avgLogprobs()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`branch()`

The branch of the event.

`void`

`branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") branch)`

Sets the branch for this event.

`static [Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`builder()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content>`

`content()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata>>`

`customMetadata()`

The custom metadata of the event.

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") obj)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason>`

`errorCode()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`errorMessage()`

 

`final boolean`

`finalResponse()`

Returns true if this is a final response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason>`

`finishReason()`

 

`static [Event](Event.html "class in com.google.adk.events")`

`fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)`

Parses an event from a JSON string.

`final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionCall>`

`functionCalls()`

Returns all function calls from this event.

`final com.google.common.collect.ImmutableList<com.google.genai.types.FunctionResponse>`

`functionResponses()`

Returns all function responses from this event.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`generateEventId()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GroundingMetadata>`

`groundingMetadata()`

The grounding metadata of the event.

`int`

`hashCode()`

 

`final boolean`

`hasTrailingCodeExecutionResult()`

Returns whether the event has a trailing code execution result.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`id()`

The event id.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Transcription>`

`inputTranscription()`

Input transcription.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`interrupted()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`invocationId()`

Id of the invocation that this event belongs to.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`longRunningToolIds()`

Set of ids of the long running function calls.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`modelVersion()`

The model version used to generate the response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Transcription>`

`outputTranscription()`

Output transcription.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`partial()`

partial is true for incomplete chunks from the LLM streaming response.

`void`

`setActions([EventActions](EventActions.html "class in com.google.adk.events") actions)`

 

`void`

`setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") author)`

 

`void`

`setAvgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") avgLogprobs)`

 

`void`

`setContent(@Nullable com.google.genai.types.Content content)`

 

`void`

`setCustomMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata> customMetadata)`

 

`void`

`setErrorCode(@Nullable com.google.genai.types.FinishReason errorCode)`

 

`void`

`setErrorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorMessage)`

 

`void`

`setFinishReason(@Nullable com.google.genai.types.FinishReason finishReason)`

 

`void`

`setFinishReason([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason> finishReason)`

Deprecated.

`void`

`setGroundingMetadata(@Nullable com.google.genai.types.GroundingMetadata groundingMetadata)`

 

`void`

`setId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)`

 

`void`

`setInputTranscription(@Nullable com.google.genai.types.Transcription inputTranscription)`

 

`void`

`setInterrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") interrupted)`

 

`void`

`setInvocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)`

 

`void`

`setLongRunningToolIds(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> longRunningToolIds)`

 

`void`

`setModelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelVersion)`

 

`void`

`setOutputTranscription(@Nullable com.google.genai.types.Transcription outputTranscription)`

 

`void`

`setPartial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") partial)`

 

`void`

`setTimestamp(long timestamp)`

 

`void`

`setTurnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") turnComplete)`

 

`void`

`setUsageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)`

 

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`stringifyContent()`

Converts the event content into a readable string.

`long`

`timestamp()`

The timestamp of the event.

`[Event.Builder](Event.Builder.html "class in com.google.adk.events")`

`toBuilder()`

Creates a builder pre-filled with this event's values.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`turnComplete()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata>`

`usageMetadata()`

 

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### generateEventId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") generateEventId()

    * ### id

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id()

The event id.

    * ### setId

public void setId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId()

Id of the invocation that this event belongs to.

    * ### setInvocationId

public void setInvocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)

    * ### author

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") author()

The author of the event, it could be the name of the agent or "user" literal.

    * ### setAuthor

public void setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") author)

    * ### content

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Content> content()

    * ### setContent

public void setContent(@Nullable com.google.genai.types.Content content)

    * ### actions

public [EventActions](EventActions.html "class in com.google.adk.events") actions()

    * ### setActions

public void setActions([EventActions](EventActions.html "class in com.google.adk.events") actions)

    * ### longRunningToolIds

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> longRunningToolIds()

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running.

    * ### setLongRunningToolIds

public void setLongRunningToolIds(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> longRunningToolIds)

    * ### partial

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> partial()

partial is true for incomplete chunks from the LLM streaming response. The last chunk's partial is False.

    * ### setPartial

public void setPartial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") partial)

    * ### turnComplete

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> turnComplete()

    * ### setTurnComplete

public void setTurnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") turnComplete)

    * ### errorCode

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason> errorCode()

    * ### finishReason

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason> finishReason()

    * ### setErrorCode

public void setErrorCode(@Nullable com.google.genai.types.FinishReason errorCode)

    * ### setFinishReason

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public void setFinishReason([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FinishReason> finishReason)

Deprecated.

    * ### setFinishReason

public void setFinishReason(@Nullable com.google.genai.types.FinishReason finishReason)

    * ### errorMessage

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> errorMessage()

    * ### setErrorMessage

public void setErrorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorMessage)

    * ### usageMetadata

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata> usageMetadata()

    * ### setUsageMetadata

public void setUsageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)

    * ### avgLogprobs

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")> avgLogprobs()

    * ### setAvgLogprobs

public void setAvgLogprobs(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") avgLogprobs)

    * ### interrupted

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> interrupted()

    * ### setInterrupted

public void setInterrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") interrupted)

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> branch()

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3. Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

    * ### branch

public void branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") branch)

Sets the branch for this event. 

Format: agentA.agentB.agentC — shows hierarchy of nested agents.

Parameters:
    `branch` \- Branch identifier.

    * ### groundingMetadata

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata()

The grounding metadata of the event.

    * ### setGroundingMetadata

public void setGroundingMetadata(@Nullable com.google.genai.types.GroundingMetadata groundingMetadata)

    * ### customMetadata

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata>> customMetadata()

The custom metadata of the event.

    * ### setCustomMetadata

public void setCustomMetadata(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.CustomMetadata> customMetadata)

    * ### modelVersion

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> modelVersion()

The model version used to generate the response.

    * ### setModelVersion

public void setModelVersion(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelVersion)

    * ### inputTranscription

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Transcription> inputTranscription()

Input transcription. The transcription is independent to the model turn which means it doesn't imply any ordering between transcription and model turn.

    * ### setInputTranscription

public void setInputTranscription(@Nullable com.google.genai.types.Transcription inputTranscription)

    * ### outputTranscription

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Transcription> outputTranscription()

Output transcription. The transcription is independent to the model turn which means it doesn't imply any ordering between transcription and model turn.

    * ### setOutputTranscription

public void setOutputTranscription(@Nullable com.google.genai.types.Transcription outputTranscription)

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

    * ### hasTrailingCodeExecutionResult

public final boolean hasTrailingCodeExecutionResult()

Returns whether the event has a trailing code execution result.

    * ### finalResponse

public final boolean finalResponse()

Returns true if this is a final response.

    * ### stringifyContent

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") stringifyContent()

Converts the event content into a readable string. 

Includes text, function calls, and responses.

Returns:
    Stringified content.

    * ### builder

public static [Event.Builder](Event.Builder.html "class in com.google.adk.events") builder()

    * ### fromJson

public static [Event](Event.html "class in com.google.adk.events") fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)

Parses an event from a JSON string.

    * ### toBuilder

public [Event.Builder](Event.Builder.html "class in com.google.adk.events") toBuilder()

Creates a builder pre-filled with this event's values.

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") obj)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
