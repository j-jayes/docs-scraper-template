JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemoryMemoryService.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [InMemoryMemoryService](InMemoryMemoryService.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. InMemoryMemoryService()
  5. Method Details
     1. addSessionToMemory(Session)
     2. searchMemory(String, String, String)



# Class InMemoryMemoryService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.memory.InMemoryMemoryService

All Implemented Interfaces:
    `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`

* * *

public final class InMemoryMemoryService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")

An in-memory memory service for prototyping purposes only. 

Uses keyword matching instead of semantic search.

  * ## Constructor Summary

Constructors

Constructor

Description

`InMemoryMemoryService()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)`

Adds a session to the memory service.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")>`

`searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)`

Searches for sessions that match the query asynchronously.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### InMemoryMemoryService

public InMemoryMemoryService()

  * ## Method Details

    * ### addSessionToMemory

public io.reactivex.rxjava3.core.Completable addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)

Description copied from interface: `[BaseMemoryService](BaseMemoryService.html#addSessionToMemory\(com.google.adk.sessions.Session\))`

Adds a session to the memory service. 

A session may be added multiple times during its lifetime.

Specified by:
    `[addSessionToMemory](BaseMemoryService.html#addSessionToMemory\(com.google.adk.sessions.Session\))` in interface `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`
Parameters:
    `session` \- The session to add.

    * ### searchMemory

public io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")> searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)

Description copied from interface: `[BaseMemoryService](BaseMemoryService.html#searchMemory\(java.lang.String,java.lang.String,java.lang.String\))`

Searches for sessions that match the query asynchronously.

Specified by:
    `[searchMemory](BaseMemoryService.html#searchMemory\(java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseMemoryService](BaseMemoryService.html "interface in com.google.adk.memory")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The id of the user.
    `query` \- The query to search for.
Returns:
    A [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory") containing the matching memories.




* * *

Copyright (C) 2025\. All rights reserved.
