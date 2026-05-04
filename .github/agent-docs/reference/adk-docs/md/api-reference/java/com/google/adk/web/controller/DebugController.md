JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/DebugController.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.web.controller.DebugController

* * *

@RestController public class DebugController extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`getSessionTrace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Retrieves trace spans for a given session ID.

`org.springframework.http.ResponseEntity<?>`

`getTraceDict([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)`

Endpoint for retrieving trace information stored by the ApiServerSpanExporter, based on event ID.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### DebugController

@Autowired public DebugController([ApiServerSpanExporter](../service/ApiServerSpanExporter.html "class in com.google.adk.web.service") apiServerSpanExporter)

  * ## Method Details

    * ### getTraceDict

@GetMapping("/debug/trace/{eventId}") public org.springframework.http.ResponseEntity<?> getTraceDict(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId)

Endpoint for retrieving trace information stored by the ApiServerSpanExporter, based on event ID.

Parameters:
    `eventId` \- The ID of the event to trace (expected to be gcp.vertex.agent.event_id).
Returns:
    A ResponseEntity containing the trace data or NOT_FOUND.

    * ### getSessionTrace

@GetMapping("/debug/trace/session/{sessionId}") public org.springframework.http.ResponseEntity<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> getSessionTrace(@PathVariable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Retrieves trace spans for a given session ID.

Parameters:
    `sessionId` \- The session ID.
Returns:
    A ResponseEntity containing a list of span data maps for the session, or an empty list.




* * *

Copyright (C) 1980\. All rights reserved.
