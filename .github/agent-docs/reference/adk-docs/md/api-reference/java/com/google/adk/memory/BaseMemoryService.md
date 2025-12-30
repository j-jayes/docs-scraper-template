JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseMemoryService.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.memory](package-summary.html)
  2. [BaseMemoryService](BaseMemoryService.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. addSessionToMemory(Session)
     2. searchMemory(String, String, String)



# Interface BaseMemoryService

All Known Implementing Classes:
    `[InMemoryMemoryService](InMemoryMemoryService.html "class in com.google.adk.memory")`

* * *

public interface BaseMemoryService

Base contract for memory services. 

The service provides functionalities to ingest sessions into memory so that the memory can be used for user queries.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)`

Adds a session to the memory service.

`io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")>`

`searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)`

Searches for sessions that match the query asynchronously.




  * ## Method Details

    * ### addSessionToMemory

io.reactivex.rxjava3.core.Completable addSessionToMemory([Session](../sessions/Session.html "class in com.google.adk.sessions") session)

Adds a session to the memory service. 

A session may be added multiple times during its lifetime.

Parameters:
    `session` \- The session to add.

    * ### searchMemory

io.reactivex.rxjava3.core.Single<[SearchMemoryResponse](SearchMemoryResponse.html "class in com.google.adk.memory")> searchMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query)

Searches for sessions that match the query asynchronously.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The id of the user.
    `query` \- The query to search for.
Returns:
    A [`SearchMemoryResponse`](SearchMemoryResponse.html "class in com.google.adk.memory") containing the matching memories.




* * *

Copyright (C) 2025\. All rights reserved.
