JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ApplicationIntegrationToolset.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.applicationintegrationtoolset](package-summary.html)
  2. [ApplicationIntegrationToolset](ApplicationIntegrationToolset.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. OBJECT_MAPPER
  6. Constructor Details
     1. ApplicationIntegrationToolset(String, String, String, List, String, Map, List, String, String, String)
  7. Method Details
     1. getTools(ReadonlyContext)
     2. close()



# Class ApplicationIntegrationToolset

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.applicationintegrationtoolset.ApplicationIntegrationToolset

All Implemented Interfaces:
    `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

* * *

public class ApplicationIntegrationToolset extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Application Integration Toolset

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final com.fasterxml.jackson.databind.ObjectMapper`

`OBJECT_MAPPER`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`ApplicationIntegrationToolset([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") project, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") location, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") integration, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> triggers, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connection, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> entityOperations, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> actions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") serviceAccountJson, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolNamePrefix, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

ApplicationIntegrationToolset generates tools from a given Application Integration resource.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Performs cleanup and releases resources held by the toolset.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

`getTools(@Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface com.google.adk.tools.[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.util.Optional,java.util.Optional\))`




  * ## Field Details

    * ### OBJECT_MAPPER

public static final com.fasterxml.jackson.databind.ObjectMapper OBJECT_MAPPER

  * ## Constructor Details

    * ### ApplicationIntegrationToolset

public ApplicationIntegrationToolset([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") project, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") location, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") integration, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> triggers, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connection, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> entityOperations, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> actions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") serviceAccountJson, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolNamePrefix, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

ApplicationIntegrationToolset generates tools from a given Application Integration resource. 

Example Usage: 

integrationTool = new ApplicationIntegrationToolset( project="test-project", location="us-central1", integration="test-integration", triggers=ImmutableList.of("api_trigger/test_trigger", "api_trigger/test_trigger_2", serviceAccountJson="{....}"),connection=null,enitityOperations=null,actions=null,toolNamePrefix="test-integration-tool",toolInstructions="This tool is used to get response from test-integration."); 

connectionTool = new ApplicationIntegrationToolset( project="test-project", location="us-central1", integration=null, triggers=null, connection="test-connection", entityOperations=ImmutableMap.of("Entity1", ImmutableList.of("LIST", "GET", "UPDATE")), "Entity2", ImmutableList.of()), actions=ImmutableList.of("ExecuteCustomQuery"), serviceAccountJson="{....}", toolNamePrefix="test-tool", toolInstructions="This tool is used to list, get and update issues in Jira.");

Parameters:
    `project` \- The GCP project ID.
    `location` \- The GCP location of integration.
    `integration` \- The integration name.
    `triggers` \- (Optional) The list of trigger ids in the integration.
    `connection` \- (Optional) The connection name.
    `entityOperations` \- (Optional) The entity operations.
    `actions` \- (Optional) The actions.
    `serviceAccountJson` \- (Optional) The service account configuration as a dictionary. Required if not using default service credential. Used for fetching the Application Integration or Integration Connector resource.
    `toolNamePrefix` \- (Optional) The tool name prefix.
    `toolInstructions` \- (Optional) The tool instructions.

  * ## Method Details

    * ### getTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")> getTools(@Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)

Description copied from interface: `[BaseToolset](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))`

Return all tools in the toolset based on the provided context.

Specified by:
    `[getTools](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`
Parameters:
    `readonlyContext` \- Context used to filter tools available to the agent.
Returns:
    A Single emitting a list of tools available under the specified context.

    * ### close

public void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Description copied from interface: `[BaseToolset](../BaseToolset.html#close\(\))`

Performs cleanup and releases resources held by the toolset. 

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Specified by:
    `[close](../BaseToolset.html#close\(\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`




* * *

Copyright (C) 2025\. All rights reserved.
