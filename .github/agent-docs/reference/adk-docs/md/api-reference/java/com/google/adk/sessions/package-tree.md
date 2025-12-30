JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Package](package-summary.html)
  * [Use](package-use.html)
  * Tree
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)



# Hierarchy For Package com.google.adk.sessions

Package Hierarchies:

  * [All Packages](../../../../overview-tree.html)



## Class Hierarchy

  * java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
    * com.google.adk.sessions.[ApiResponse](ApiResponse.html "class in com.google.adk.sessions") (implements java.lang.[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")) 
      * com.google.adk.sessions.[HttpApiResponse](HttpApiResponse.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[GetSessionConfig.Builder](GetSessionConfig.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[HttpApiClient](HttpApiClient.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[InMemorySessionService](InMemorySessionService.html "class in com.google.adk.sessions") (implements com.google.adk.sessions.[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions"))
    * com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")
      * com.google.adk.sessions.[Session](Session.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListEventsResponse.Builder](ListEventsResponse.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[ListSessionsResponse.Builder](ListSessionsResponse.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[SessionUtils](SessionUtils.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[State](State.html "class in com.google.adk.sessions") (implements java.util.concurrent.[ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<K,V>)
    * java.lang.[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") (implements java.io.[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")) 
      * java.lang.[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")
        * java.lang.[RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang")
          * com.google.adk.sessions.[SessionException](SessionException.html "class in com.google.adk.sessions")
            * com.google.adk.sessions.[SessionNotFoundException](SessionNotFoundException.html "class in com.google.adk.sessions")
    * com.google.adk.sessions.[VertexAiSessionService](VertexAiSessionService.html "class in com.google.adk.sessions") (implements com.google.adk.sessions.[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions"))



## Interface Hierarchy

  * com.google.adk.sessions.[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")



* * *

Copyright (C) 2025\. All rights reserved.
