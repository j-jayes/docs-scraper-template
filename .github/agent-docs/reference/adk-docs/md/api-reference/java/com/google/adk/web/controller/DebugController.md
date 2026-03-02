JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/DebugController.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.controller](package-summary.html)
  2. [DebugController](DebugController.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. DebugController(ApiServerSpanExporter)
  5. Method Details
     1. getTraceDict(String)
     2. getSessionTrace(String)

Hide sidebar  Show sidebar

# Class DebugController

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.controller.DebugController

* * *

@RestController public class DebugController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Controller handling debug and tracing endpoints.

  * ## Constructor Summary

Constructors

Constructor

Description

`DebugController([ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getSessionTrace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Retrieves trace spans for a given session ID.

`org.springframework.http.ResponseEntity<?>`

`getTraceDict([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId)`

Endpoint for retrieving trace information stored by the ApiServerSpanExporter, based on event ID.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### DebugController

@Autowired public DebugController([ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter)

  * ## Method Details

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




* * *

Copyright (C) 1980\. All rights reserved.
