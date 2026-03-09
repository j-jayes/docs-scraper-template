JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/A2AClient.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.a2a](package-summary.html)
  2. [A2AClient](A2AClient.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. A2AClient(AgentCard)
     2. A2AClient(AgentCard, A2AHttpClient, Map)
  5. Method Details
     1. getAgentCard()
     2. getUrl()
     3. sendMessage(SendMessageRequest)
     4. extractHostAndPort(String)

Hide sidebar  Show sidebar

# Class A2AClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.A2AClient

* * *

public final class A2AClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

A thin HTTP client for interacting with an A2A-compliant agent endpoint. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Constructor Summary

Constructors

Constructor

Description

`A2AClient(io.a2a.spec.AgentCard agentCard)`

 

`A2AClient(io.a2a.spec.AgentCard agentCard, io.a2a.client.http.A2AHttpClient httpClient, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> defaultHeaders)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`extractHostAndPort([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") urlString)`

 

`io.a2a.spec.AgentCard`

`getAgentCard()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getUrl()`

 

`io.reactivex.rxjava3.core.Flowable<io.a2a.spec.SendMessageResponse>`

`sendMessage(io.a2a.spec.SendMessageRequest request)`

Sends a JSON-RPC message to the remote A2A agent and converts the response into the canonical `SendMessageResponse` model.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### A2AClient

public A2AClient(io.a2a.spec.AgentCard agentCard)

    * ### A2AClient

public A2AClient(io.a2a.spec.AgentCard agentCard, io.a2a.client.http.A2AHttpClient httpClient, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> defaultHeaders)

  * ## Method Details

    * ### getAgentCard

public io.a2a.spec.AgentCard getAgentCard()

    * ### getUrl

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getUrl()

    * ### sendMessage

public io.reactivex.rxjava3.core.Flowable<io.a2a.spec.SendMessageResponse> sendMessage(io.a2a.spec.SendMessageRequest request)

Sends a JSON-RPC message to the remote A2A agent and converts the response into the canonical `SendMessageResponse` model.

    * ### extractHostAndPort

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") extractHostAndPort([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") urlString)




* * *

Copyright (C) 1980\. All rights reserved.
