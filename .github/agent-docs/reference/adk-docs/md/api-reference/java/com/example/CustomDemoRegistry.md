JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../index.html)
  * Class
  * [Use](class-use/CustomDemoRegistry.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../deprecated-list.html)
  * [Index](../../index-all.html)
  * [Search](../../search.html)



  1. [com.example](package-summary.html)
  2. [CustomDemoRegistry](CustomDemoRegistry.html)



Contents 

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. INSTANCE
  6. Constructor Details
     1. CustomDemoRegistry()

Hide sidebar  Show sidebar

# Class CustomDemoRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.utils.ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils")

com.example.CustomDemoRegistry

* * *

public class CustomDemoRegistry extends [ComponentRegistry](../google/adk/utils/ComponentRegistry.html "class in com.google.adk.utils")

Custom ComponentRegistry for the user-defined config agent demo. 

This registry is used to add custom tools and agents to the ADK Web Server.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [CustomDemoRegistry](CustomDemoRegistry.html "class in com.example")`

`INSTANCE`

Singleton instance for easy access

  * ## Constructor Summary

Constructors

Constructor

Description

`CustomDemoRegistry()`

Private constructor to initialize custom components

  * ## Method Summary

### Methods inherited from class [ComponentRegistry](../google/adk/utils/ComponentRegistry.html#method-summary "class in com.google.adk.utils")

`[get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String\) "get\(String\)"), [get](../google/adk/utils/ComponentRegistry.html#get\(java.lang.String,java.lang.Class\) "get\(String, Class\)"), [getInstance](../google/adk/utils/ComponentRegistry.html#getInstance\(\) "getInstance\(\)"), [getToolNamesWithPrefix](../google/adk/utils/ComponentRegistry.html#getToolNamesWithPrefix\(java.lang.String\) "getToolNamesWithPrefix\(String\)"), [register](../google/adk/utils/ComponentRegistry.html#register\(java.lang.String,java.lang.Object\) "register\(String, Object\)"), [resolveAfterAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterAgentCallback\(java.lang.String\) "resolveAfterAgentCallback\(String\)"), [resolveAfterModelCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterModelCallback\(java.lang.String\) "resolveAfterModelCallback\(String\)"), [resolveAfterToolCallback](../google/adk/utils/ComponentRegistry.html#resolveAfterToolCallback\(java.lang.String\) "resolveAfterToolCallback\(String\)"), [resolveAgentClass](../google/adk/utils/ComponentRegistry.html#resolveAgentClass\(java.lang.String\) "resolveAgentClass\(String\)"), [resolveAgentInstance](../google/adk/utils/ComponentRegistry.html#resolveAgentInstance\(java.lang.String\) "resolveAgentInstance\(String\)"), [resolveBeforeAgentCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeAgentCallback\(java.lang.String\) "resolveBeforeAgentCallback\(String\)"), [resolveBeforeModelCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeModelCallback\(java.lang.String\) "resolveBeforeModelCallback\(String\)"), [resolveBeforeToolCallback](../google/adk/utils/ComponentRegistry.html#resolveBeforeToolCallback\(java.lang.String\) "resolveBeforeToolCallback\(String\)"), [resolveToolClass](../google/adk/utils/ComponentRegistry.html#resolveToolClass\(java.lang.String\) "resolveToolClass\(String\)"), [resolveToolInstance](../google/adk/utils/ComponentRegistry.html#resolveToolInstance\(java.lang.String\) "resolveToolInstance\(String\)"), [resolveToolsetClass](../google/adk/utils/ComponentRegistry.html#resolveToolsetClass\(java.lang.String\) "resolveToolsetClass\(String\)"), [resolveToolsetInstance](../google/adk/utils/ComponentRegistry.html#resolveToolsetInstance\(java.lang.String\) "resolveToolsetInstance\(String\)"), [setInstance](../google/adk/utils/ComponentRegistry.html#setInstance\(com.google.adk.utils.ComponentRegistry\) "setInstance\(ComponentRegistry\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### INSTANCE

public static final [CustomDemoRegistry](CustomDemoRegistry.html "class in com.example") INSTANCE

Singleton instance for easy access

  * ## Constructor Details

    * ### CustomDemoRegistry

public CustomDemoRegistry()

Private constructor to initialize custom components




* * *

Copyright (C) 1980\. All rights reserved.
