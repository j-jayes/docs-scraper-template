JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FirestoreMemoryService.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [FirestoreMemoryService](FirestoreMemoryService.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. FirestoreMemoryService(Firestore)
  5. Method Details
     1. addSessionToMemory(Session)
     2. searchMemory(String, String, String)

Hide sidebar  Show sidebar

# Class FirestoreMemoryService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.memory.FirestoreMemoryService

All Implemented Interfaces:
    `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`

* * *

public class FirestoreMemoryService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")

FirestoreMemoryService is an implementation of BaseMemoryService that uses Firestore to store and retrieve session memory entries.

  * ## Constructor Summary

Constructors

Constructor

Description

`FirestoreMemoryService(com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreMemoryService

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)`

Adds a session to memory.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")>`

`searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)`

Searches memory entries for the given appName and userId that match the query keywords.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### FirestoreMemoryService

public FirestoreMemoryService(com.google.cloud.firestore.Firestore firestore)

Constructor for FirestoreMemoryService

  * ## Method Details

    * ### addSessionToMemory

public io.reactivex.rxjava3.core.Completable addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)

Adds a session to memory. This is a no-op for FirestoreMemoryService since keywords are indexed when events are appended in FirestoreSessionService.

Specified by:
    `[addSessionToMemory](BaseMemoryService.html#addSessionToMemory\(com.google.adk.sessions.Session\))` in interface `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`
Parameters:
    `session` \- The session to add.

    * ### searchMemory

public io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")> searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)

Searches memory entries for the given appName and userId that match the query keywords.

Specified by:
    `[searchMemory](BaseMemoryService.html#searchMemory\(java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The id of the user.
    `query` \- The query to search for.
Returns:
    A [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory") containing the matching memories.




* * *

Copyright (C) 1980\. All rights reserved.
