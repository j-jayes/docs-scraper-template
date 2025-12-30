JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Class](../JsonBaseModel.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk](../package-summary.html)
  2. [JsonBaseModel](../JsonBaseModel.html)



# Uses of Class  
com.google.adk.JsonBaseModel

Packages that use [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.models

 

com.google.adk.sessions

 

com.google.adk.web

 

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk](../package-summary.html)

Methods in [com.google.adk](../package-summary.html) with type parameters of type [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

JsonBaseModel.`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

JsonBaseModel.`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.agents](../agents/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.agents](../agents/package-summary.html)

Modifier and Type

Class

Description

`class `

`[LiveRequest](../agents/LiveRequest.html "class in com.google.adk.agents")`

Represents a request to be sent to a live connection to the LLM model.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.events](../events/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.events](../events/package-summary.html)

Modifier and Type

Class

Description

`class `

`[Event](../events/Event.html "class in com.google.adk.events")`

Represents an event in a session.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.models](../models/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.models](../models/package-summary.html)

Modifier and Type

Class

Description

`class `

`[LlmRequest](../models/LlmRequest.html "class in com.google.adk.models")`

Represents a request to be sent to the LLM.

`class `

`[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")`

Represents a response received from the LLM.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.sessions](../sessions/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.sessions](../sessions/package-summary.html)

Modifier and Type

Class

Description

`final class `

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

A [`Session`](../sessions/Session.html "class in com.google.adk.sessions") object that encapsulates the [`State`](../sessions/State.html "class in com.google.adk.sessions") and [`Event`](../events/Event.html "class in com.google.adk.events")s of a session.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.web](../web/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.web](../web/package-summary.html)

Modifier and Type

Class

Description

`static class `

`[AdkWebServer.RunEvalResult](../web/AdkWebServer.RunEvalResult.html "class in com.google.adk.web")`

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval.




* * *

Copyright (C) 2025\. All rights reserved.
