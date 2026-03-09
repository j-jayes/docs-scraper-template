JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/A2ARemoteConfiguration.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.webservice](package-summary.html)
  2. [A2ARemoteConfiguration](A2ARemoteConfiguration.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. A2ARemoteConfiguration()
  5. Method Details
     1. a2aSendMessageExecutor(BaseAgent, String, long)

Hide sidebar  Show sidebar

# Class A2ARemoteConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.webservice.A2ARemoteConfiguration

* * *

@Configuration @ComponentScan(basePackages="com.google.adk.webservice") public class A2ARemoteConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Registers the transport-only A2A webservice stack. 

Importers must supply a [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") bean. The agent remains opaque to this module so the transport can be reused across applications. 

TODO: 

  * Expose discovery endpoints (agent card / extended card) so clients can fetch metadata directly. 
  * Add optional remote-proxy wiring for cases where no local agent bean is available. 


**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Constructor Summary

Constructors

Constructor

Description

`A2ARemoteConfiguration()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[A2ASendMessageExecutor](../a2a/A2ASendMessageExecutor.html "class in com.google.adk.a2a")`

`a2aSendMessageExecutor([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, long timeoutSeconds)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### A2ARemoteConfiguration

public A2ARemoteConfiguration()

  * ## Method Details

    * ### a2aSendMessageExecutor

@Bean public [A2ASendMessageExecutor](../a2a/A2ASendMessageExecutor.html "class in com.google.adk.a2a") a2aSendMessageExecutor([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, @Value("${a2a.remote.appName:a2a-remote-service}") [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, @Value("${a2a.remote.timeoutSeconds:15}") long timeoutSeconds)




* * *

Copyright (C) 1980\. All rights reserved.
