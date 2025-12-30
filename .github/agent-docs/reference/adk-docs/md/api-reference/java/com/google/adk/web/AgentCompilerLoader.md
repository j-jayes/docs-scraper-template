JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AgentCompilerLoader.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AgentCompilerLoader](AgentCompilerLoader.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AgentCompilerLoader(AgentLoadingProperties)
  5. Method Details
     1. loadAgents()



# Class AgentCompilerLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.web.AgentCompilerLoader

* * *

@Service public class AgentCompilerLoader extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Dynamically compiles and loads ADK [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") implementations from source files. It orchestrates the discovery of the ADK core JAR, compilation of agent sources using the Eclipse JDT (ECJ) compiler, and loading of compiled agents into isolated classloaders. Agents are identified by a public static field named `ROOT_AGENT`. Supports agent organization in subdirectories or as individual `.java` files.

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentCompilerLoader([AgentLoadingProperties](config/AgentLoadingProperties.html "class in com.google.adk.web.config") properties)`

Initializes the loader with agent configuration and proactively attempts to locate the ADK core JAR.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>`

`loadAgents()`

Discovers, compiles, and loads agents from the configured source directory.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentCompilerLoader

public AgentCompilerLoader([AgentLoadingProperties](config/AgentLoadingProperties.html "class in com.google.adk.web.config") properties)

Initializes the loader with agent configuration and proactively attempts to locate the ADK core JAR. This JAR, containing [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") and other core ADK types, is crucial for agent compilation. The location strategy (see `locateAndPrepareAdkCoreJar()`) includes handling directly available JARs and extracting nested JARs (e.g., in Spring Boot fat JARs) to ensure it's available for the compilation classpath.

Parameters:
    `properties` \- Configuration detailing agent source locations and compilation settings.

  * ## Method Details

    * ### loadAgents

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> loadAgents() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")

Discovers, compiles, and loads agents from the configured source directory. 

The process for each potential "agent unit" (a subdirectory or a root `.java` file): 
      1. Collects `.java` source files. 
      2. Compiles these sources using ECJ (see `compileSourcesWithECJ(List, Path)`) into a temporary, unit-specific output directory. This directory is cleaned up on JVM exit. 
      3. Creates a dedicated [`URLClassLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URLClassLoader.html "class or interface in java.net") for the compiled unit, isolating its classes. 
      4. Scans compiled classes for a public static field `ROOT_AGENT` assignable to [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents"). This field serves as the designated entry point for an agent. 
      5. Instantiates and stores the [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") if found, keyed by its name.  This approach allows for dynamic addition of agents without pre-compilation and supports independent classpaths per agent unit if needed (though current implementation uses a shared parent classloader).

Returns:
    A map of successfully loaded agent names to their [`BaseAgent`](../agents/BaseAgent.html "class in com.google.adk.agents") instances. Returns an empty map if the source directory isn't configured or no agents are found.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- If an I/O error occurs (e.g., creating temp directories, reading sources).




* * *

Copyright (C) 2025\. All rights reserved.
