JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/A2ARemoteService.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.webservice](package-summary.html)
  2. [A2ARemoteService](A2ARemoteService.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. A2ARemoteService(A2ASendMessageExecutor)
  5. Method Details
     1. handle(SendMessageRequest)

Hide sidebar  Show sidebar

# Class A2ARemoteService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.webservice.A2ARemoteService

* * *

@Service public class A2ARemoteService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Core service that bridges the A2A JSON-RPC sendMessage API to a local ADK runner. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Constructor Summary

Constructors

Constructor

Description

`A2ARemoteService([A2ASendMessageExecutor](../a2a/A2ASendMessageExecutor.html "class in com.google.adk.a2a") executor)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.a2a.spec.SendMessageResponse`

`handle(io.a2a.spec.SendMessageRequest request)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### A2ARemoteService

public A2ARemoteService([A2ASendMessageExecutor](../a2a/A2ASendMessageExecutor.html "class in com.google.adk.a2a") executor)

  * ## Method Details

    * ### handle

public io.a2a.spec.SendMessageResponse handle(io.a2a.spec.SendMessageRequest request)




* * *

Copyright (C) 1980\. All rights reserved.
