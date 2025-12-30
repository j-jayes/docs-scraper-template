JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.AgentController.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [AgentController](AdkWebServer.AgentController.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AgentController(BaseSessionService, BaseArtifactService, Map, AdkWebServer.ApiServerSpanExporter, AdkWebServer.RunnerService)
  5. Method Details
     1. listApps()
     2. getTraceDict(String)
     3. getSessionTrace(String)
     4. getSession(String, String, String)
     5. listSessions(String, String)
     6. createSessionWithId(String, String, String, Map)
     7. createSession(String, String, Map)
     8. deleteSession(String, String, String)
     9. loadArtifact(String, String, String, String, Integer)
     10. loadArtifactVersion(String, String, String, String, int)
     11. listArtifactNames(String, String, String)
     12. listArtifactVersions(String, String, String, String)
     13. deleteArtifact(String, String, String, String)
     14. agentRun(AdkWebServer.AgentRunRequest)
     15. agentRunSse(AdkWebServer.AgentRunRequest)
     16. getEventGraph(String, String, String, String)
     17. createEvalSet(String, String)
     18. listEvalSets(String)
     19. addSessionToEvalSet(String, String, AdkWebServer.AddSessionToEvalSetRequest)
     20. listEvalsInEvalSet(String, String)
     21. runEval(String, String, AdkWebServer.RunEvalRequest)
     22. getEvalResult(String, String)
     23. listEvalResults(String)



# Class AdkWebServer.AgentController

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AdkWebServer.AgentController

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

@RestController public static class AdkWebServer.AgentController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Spring Boot REST Controller handling agent-related API endpoints.

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentController([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter, [AdkWebServer.RunnerService](AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)`

Constructs the AgentController.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`addSessionToEvalSet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, [AdkWebServer.AddSessionToEvalSetRequest](AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web") req)`

Placeholder for adding a session to an evaluation set.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`agentRun([AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web") request)`

Executes a non-streaming agent run for a given session and message.

`org.springframework.web.servlet.mvc.method.annotation.SseEmitter`

`agentRunSse([AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web") request)`

Executes an agent run and streams the resulting events using Server-Sent Events (SSE).

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`createEvalSet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId)`

Placeholder for creating an evaluation set.

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

Creates a new session where the ID is generated by the service.

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`createSessionWithId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

Creates a new session with a specific ID provided by the client.

`org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class or interface in java.lang")>`

`deleteArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName)`

Deletes an artifact and all its versions.

`org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class or interface in java.lang")>`

`deleteSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Deletes a specific session.

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getEvalResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalResultId)`

Gets a specific evaluation result.

`org.springframework.http.ResponseEntity<[AdkWebServer.GraphResponse](AdkWebServer.GraphResponse.html "class in com.google.adk.web")>`

`getEventGraph([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)`

Endpoint to get a graph representation of an event (currently returns a placeholder).

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`getSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Retrieves a specific session by its ID.

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getSessionTrace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Retrieves trace spans for a given session ID.

`org.springframework.http.ResponseEntity<?>`

`getTraceDict([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)`

Endpoint for retrieving trace information stored by the ApiServerSpanExporter, based on event ID.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listApps()`

Lists available applications.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listArtifactNames([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists the names of all artifacts associated with a session.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

`listArtifactVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName)`

Lists the available versions for a specific artifact.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listEvalResults([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

Lists all evaluation results for an app.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listEvalSets([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

Placeholder for listing evaluation sets.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`listEvalsInEvalSet([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId)`

Placeholder for listing evaluations within an evaluation set.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Session](../sessions/Session.html "class in com.google.adk.sessions")>`

`listSessions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

Lists all non-evaluation sessions for a given app and user.

`com.google.genai.types.Part`

`loadArtifact([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") version)`

Loads the latest or a specific version of an artifact associated with a session.

`com.google.genai.types.Part`

`loadArtifactVersion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName, int versionId)`

Loads a specific version of an artifact.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[AdkWebServer.RunEvalResult](AdkWebServer.RunEvalResult.html "class in com.google.adk.web")>`

`runEval([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, [AdkWebServer.RunEvalRequest](AdkWebServer.RunEvalRequest.html "class in com.google.adk.web") req)`

Placeholder for running evaluations.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentController

@Autowired public AgentController([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, @Qualifier("loadedAgentRegistry") [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [AdkWebServer.ApiServerSpanExporter](AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter, [AdkWebServer.RunnerService](AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)

Constructs the AgentController.

Parameters:
    `sessionService` \- The service for managing sessions.
    `artifactService` \- The service for managing artifacts.
    `agentRegistry` \- The registry of loaded agents.
    `apiServerSpanExporter` \- The exporter holding all trace data.
    `runnerService` \- The service for obtaining Runner instances.

  * ## Method Details

    * ### listApps

@GetMapping("/list-apps") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listApps()

Lists available applications. Currently returns only the configured root agent's name.

Returns:
    A list containing the root agent's name.

    * ### getTraceDict

@GetMapping("/debug/trace/{eventId}") public org.springframework.http.ResponseEntity<?> getTraceDict(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)

Endpoint for retrieving trace information stored by the ApiServerSpanExporter, based on event ID.

Parameters:
    `eventId` \- The ID of the event to trace (expected to be gcp.vertex.agent.event_id).
Returns:
    A ResponseEntity containing the trace data or NOT_FOUND.

    * ### getSessionTrace

@GetMapping("/debug/trace/session/{sessionId}") public org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getSessionTrace(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Retrieves trace spans for a given session ID.

Parameters:
    `sessionId` \- The session ID.
Returns:
    A ResponseEntity containing a list of span data maps for the session, or an empty list.

    * ### getSession

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}") public [Session](../sessions/Session.html "class in com.google.adk.sessions") getSession(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Retrieves a specific session by its ID.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
Returns:
    The requested Session object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the session is not found.

    * ### listSessions

@GetMapping("/apps/{appName}/users/{userId}/sessions") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Session](../sessions/Session.html "class in com.google.adk.sessions")> listSessions(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)

Lists all non-evaluation sessions for a given app and user.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The ID of the user.
Returns:
    A list of sessions, excluding those used for evaluation.

    * ### createSessionWithId

@PostMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}") public [Session](../sessions/Session.html "class in com.google.adk.sessions") createSessionWithId(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @RequestBody(required=false) [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)

Creates a new session with a specific ID provided by the client.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The desired session ID.
    `state` \- Optional initial state for the session.
Returns:
    The newly created Session object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if a session with the given ID already exists (BAD_REQUEST) or if creation fails (INTERNAL_SERVER_ERROR).

    * ### createSession

@PostMapping("/apps/{appName}/users/{userId}/sessions") public [Session](../sessions/Session.html "class in com.google.adk.sessions") createSession(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @RequestBody(required=false) [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)

Creates a new session where the ID is generated by the service.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `state` \- Optional initial state for the session.
Returns:
    The newly created Session object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if creation fails (INTERNAL_SERVER_ERROR).

    * ### deleteSession

@DeleteMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}") public org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class or interface in java.lang")> deleteSession(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Deletes a specific session.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID to delete.
Returns:
    A ResponseEntity with status NO_CONTENT on success.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if deletion fails (INTERNAL_SERVER_ERROR).

    * ### loadArtifact

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}") public com.google.genai.types.Part loadArtifact(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName, @RequestParam(required=false) [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") version)

Loads the latest or a specific version of an artifact associated with a session.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
    `version` \- Optional specific version number. If null, loads the latest.
Returns:
    The artifact content as a Part object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the artifact is not found (NOT_FOUND).

    * ### loadArtifactVersion

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}/versions/{versionId}") public com.google.genai.types.Part loadArtifactVersion(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName, @PathVariable int versionId)

Loads a specific version of an artifact.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
    `versionId` \- The specific version number.
Returns:
    The artifact content as a Part object.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the artifact version is not found (NOT_FOUND).

    * ### listArtifactNames

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listArtifactNames(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Lists the names of all artifacts associated with a session.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
Returns:
    A list of artifact names.

    * ### listArtifactVersions

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}/versions") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> listArtifactVersions(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName)

Lists the available versions for a specific artifact.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact.
Returns:
    A list of version numbers (integers).

    * ### deleteArtifact

@DeleteMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/artifacts/{artifactName}") public org.springframework.http.ResponseEntity<[Void](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Void.html "class or interface in java.lang")> deleteArtifact(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") artifactName)

Deletes an artifact and all its versions.

Parameters:
    `appName` \- The application name.
    `userId` \- The user ID.
    `sessionId` \- The session ID.
    `artifactName` \- The name of the artifact to delete.
Returns:
    A ResponseEntity with status NO_CONTENT on success.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if deletion fails (INTERNAL_SERVER_ERROR).

    * ### agentRun

@PostMapping("/run") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> agentRun(@RequestBody [AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web") request)

Executes a non-streaming agent run for a given session and message.

Parameters:
    `request` \- The AgentRunRequest containing run details.
Returns:
    A list of events generated during the run.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the session is not found or the run fails.

    * ### agentRunSse

@PostMapping(value="/run_sse", produces="text/event-stream") public org.springframework.web.servlet.mvc.method.annotation.SseEmitter agentRunSse(@RequestBody [AdkWebServer.AgentRunRequest](AdkWebServer.AgentRunRequest.html "class in com.google.adk.web") request)

Executes an agent run and streams the resulting events using Server-Sent Events (SSE).

Parameters:
    `request` \- The AgentRunRequest containing run details.
Returns:
    A Flux that will stream events to the client.

    * ### getEventGraph

@GetMapping("/apps/{appName}/users/{userId}/sessions/{sessionId}/events/{eventId}/graph") public org.springframework.http.ResponseEntity<[AdkWebServer.GraphResponse](AdkWebServer.GraphResponse.html "class in com.google.adk.web")> getEventGraph(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)

Endpoint to get a graph representation of an event (currently returns a placeholder). Requires Graphviz or similar tooling for full implementation.

Parameters:
    `appName` \- Application name.
    `userId` \- User ID.
    `sessionId` \- Session ID.
    `eventId` \- Event ID.
Returns:
    ResponseEntity containing a GraphResponse with placeholder DOT source.
Throws:
    `org.springframework.web.server.ResponseStatusException` \- if the session or event is not found.

    * ### createEvalSet

@PostMapping("/apps/{appName}/eval_sets/{evalSetId}") public org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> createEvalSet(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId)

Placeholder for creating an evaluation set.

    * ### listEvalSets

@GetMapping("/apps/{appName}/eval_sets") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listEvalSets(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

Placeholder for listing evaluation sets.

    * ### addSessionToEvalSet

@PostMapping("/apps/{appName}/eval_sets/{evalSetId}/add-session") public org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> addSessionToEvalSet(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, @RequestBody [AdkWebServer.AddSessionToEvalSetRequest](AdkWebServer.AddSessionToEvalSetRequest.html "class in com.google.adk.web") req)

Placeholder for adding a session to an evaluation set.

    * ### listEvalsInEvalSet

@GetMapping("/apps/{appName}/eval_sets/{evalSetId}/evals") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listEvalsInEvalSet(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId)

Placeholder for listing evaluations within an evaluation set.

    * ### runEval

@PostMapping("/apps/{appName}/eval_sets/{evalSetId}/run-eval") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[AdkWebServer.RunEvalResult](AdkWebServer.RunEvalResult.html "class in com.google.adk.web")> runEval(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, @RequestBody [AdkWebServer.RunEvalRequest](AdkWebServer.RunEvalRequest.html "class in com.google.adk.web") req)

Placeholder for running evaluations.

    * ### getEvalResult

@GetMapping("/apps/{appName}/eval_results/{evalResultId}") public org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getEvalResult(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalResultId)

Gets a specific evaluation result. (STUB - Not Implemented)

Parameters:
    `appName` \- The application name.
    `evalResultId` \- The evaluation result ID.
Returns:
    A ResponseEntity indicating the endpoint is not implemented.

    * ### listEvalResults

@GetMapping("/apps/{appName}/eval_results") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> listEvalResults(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

Lists all evaluation results for an app. (STUB - Not Implemented)

Parameters:
    `appName` \- The application name.
Returns:
    An empty list, as this endpoint is not implemented.




* * *

Copyright (C) 2025\. All rights reserved.
