JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SkillToolset.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.skills](package-summary.html)
  2. [SkillToolset](SkillToolset.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SkillToolset(SkillSource)
     2. SkillToolset(SkillSource, String)
  5. Method Details
     1. getTools(ReadonlyContext)
     2. processLlmRequest(LlmRequest.Builder, ToolContext)
     3. close()

Hide sidebar  Show sidebar

# Class SkillToolset

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.skills.SkillToolset

All Implemented Interfaces:
    `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

* * *

public class SkillToolset extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

A toolset for managing and interacting with agent skills. Provides tools to list, load, and run skills.

  * ## Constructor Summary

Constructors

Constructor

Description

`SkillToolset([SkillSource](../../skills/SkillSource.html "interface in com.google.adk.skills") skillSource)`

Initializes the SkillToolset with a SkillSource and default execution settings.

`SkillToolset([SkillSource](../../skills/SkillSource.html "interface in com.google.adk.skills") skillSource, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") systemInstruction)`

Initializes the SkillToolset with a SkillSource.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Performs cleanup and releases resources held by the toolset.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

`getTools([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [BaseToolset](../BaseToolset.html#method-summary "interface in com.google.adk.tools")

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\) "isToolSelected\(BaseTool, Object, ReadonlyContext\)")`

Modifier and Type

Method

Description

`default boolean`

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") toolFilter, @Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Checks if a tool should be selected based on a filter.




  * ## Constructor Details

    * ### SkillToolset

public SkillToolset([SkillSource](../../skills/SkillSource.html "interface in com.google.adk.skills") skillSource)

Initializes the SkillToolset with a SkillSource and default execution settings.

    * ### SkillToolset

public SkillToolset([SkillSource](../../skills/SkillSource.html "interface in com.google.adk.skills") skillSource, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") systemInstruction)

Initializes the SkillToolset with a SkillSource.

  * ## Method Details

    * ### getTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")> getTools([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)

Description copied from interface: `[BaseToolset](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))`

Return all tools in the toolset based on the provided context.

Specified by:
    `[getTools](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`
Parameters:
    `readonlyContext` \- Context used to filter tools available to the agent.
Returns:
    A Flowable emitting tools available under the specified context.

    * ### processLlmRequest

public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from interface: `[BaseToolset](../BaseToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

Specified by:
    `[processLlmRequest](../BaseToolset.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`

    * ### close

public void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")

Description copied from interface: `[BaseToolset](../BaseToolset.html#close\(\))`

Performs cleanup and releases resources held by the toolset. 

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\))` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`
Specified by:
    `[close](../BaseToolset.html#close\(\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
