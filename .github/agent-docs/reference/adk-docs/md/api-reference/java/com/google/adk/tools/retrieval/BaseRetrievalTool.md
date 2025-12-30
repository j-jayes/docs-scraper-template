JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BaseRetrievalTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.retrieval](package-summary.html)
  2. [BaseRetrievalTool](BaseRetrievalTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseRetrievalTool(String, String)
     2. BaseRetrievalTool(String, String, boolean)
  5. Method Details
     1. declaration()



# Class BaseRetrievalTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.retrieval.BaseRetrievalTool

Direct Known Subclasses:
    `[VertexAiRagRetrieval](VertexAiRagRetrieval.html "class in com.google.adk.tools.retrieval")`

* * *

public abstract class BaseRetrievalTool extends [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Base class for retrieval tools.

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseRetrievalTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`BaseRetrievalTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

### Methods inherited from class com.google.adk.tools.[BaseTool](../BaseTool.html "class in com.google.adk.tools")

`[description](../BaseTool.html#description\(\)), [longRunning](../BaseTool.html#longRunning\(\)), [name](../BaseTool.html#name\(\)), [processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\)), [runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseRetrievalTool

public BaseRetrievalTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### BaseRetrievalTool

public BaseRetrievalTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)

  * ## Method Details

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Description copied from class: `[BaseTool](../BaseTool.html#declaration\(\))`

Gets the `FunctionDeclaration` representation of this tool.

Overrides:
    `[declaration](../BaseTool.html#declaration\(\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 2025\. All rights reserved.
