JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Class](../JsonBaseModel.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk](../package-summary.html)
  2. [JsonBaseModel](../JsonBaseModel.html)



# Uses of Class  
com.google.adk.JsonBaseModel

Packages that use [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.codeexecutors

 

com.google.adk.events

 

com.google.adk.examples

 

com.google.adk.models

 

com.google.adk.sessions

 

com.google.adk.tools

 

com.google.adk.tools.mcp

 

com.google.adk.web.dto

 

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk](../package-summary.html)

Methods in [com.google.adk](../package-summary.html) with type parameters of type [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

JsonBaseModel.`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

JsonBaseModel.`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.agents](../agents/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.agents](../agents/package-summary.html)

Modifier and Type

Class

Description

`class `

`[LiveRequest](../agents/LiveRequest.html "class in com.google.adk.agents")`

Represents a request to be sent to a live connection to the LLM model.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.codeexecutors](../codeexecutors/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.codeexecutors](../codeexecutors/package-summary.html)

Modifier and Type

Class

Description

`class `

`[BaseCodeExecutor](../codeexecutors/BaseCodeExecutor.html "class in com.google.adk.codeexecutors")`

Abstract base class for all code executors.

`class `

`[BuiltInCodeExecutor](../codeexecutors/BuiltInCodeExecutor.html "class in com.google.adk.codeexecutors")`

A code executor that uses the Model's built-in code executor.

`static class `

`[CodeExecutionUtils.CodeExecutionInput](../codeexecutors/CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors")`

A structure that contains the input of code execution.

`static class `

`[CodeExecutionUtils.CodeExecutionResult](../codeexecutors/CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

A structure that contains the result of code execution.

`static class `

`[CodeExecutionUtils.File](../codeexecutors/CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")`

A structure that contains a file name and its content.

`class `

`[ContainerCodeExecutor](../codeexecutors/ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

A code executor that uses a custom container to execute code.

`final class `

`[VertexAiCodeExecutor](../codeexecutors/VertexAiCodeExecutor.html "class in com.google.adk.codeexecutors")`

A code executor that uses Vertex Code Interpreter Extension to execute code.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.events](../events/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.events](../events/package-summary.html)

Modifier and Type

Class

Description

`class `

`[Event](../events/Event.html "class in com.google.adk.events")`

Represents an event in a session.

`class `

`[EventActions](../events/EventActions.html "class in com.google.adk.events")`

Represents the actions attached to an event.

`class `

`[ToolConfirmation](../events/ToolConfirmation.html "class in com.google.adk.events")`

Represents a tool confirmation configuration.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.examples](../examples/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.examples](../examples/package-summary.html)

Modifier and Type

Class

Description

`class `

`[Example](../examples/Example.html "class in com.google.adk.examples")`

Represents an few-shot example.

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

`final class `

`[SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions")`

Key for a session, composed of appName, userId and session id.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.tools](../tools/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.tools](../tools/package-summary.html)

Modifier and Type

Class

Description

`static class `

`[BaseTool.ToolArgsConfig](../tools/BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")`

Configuration class for tool arguments that allows arbitrary key-value pairs.

`static class `

`[BaseTool.ToolConfig](../tools/BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Configuration class for a tool definition in YAML/JSON.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.tools.mcp](../tools/mcp/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.tools.mcp](../tools/mcp/package-summary.html)

Modifier and Type

Class

Description

`static class `

`[McpToolset.McpToolsetConfig](../tools/mcp/McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp")`

Configuration class for MCPToolset.

  * ## Uses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.web.dto](../web/dto/package-summary.html)

Subclasses of [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk") in [com.google.adk.web.dto](../web/dto/package-summary.html)

Modifier and Type

Class

Description

`class `

`[RunEvalResult](../web/dto/RunEvalResult.html "class in com.google.adk.web.dto")`

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval.




* * *

Copyright (C) 1980\. All rights reserved.
