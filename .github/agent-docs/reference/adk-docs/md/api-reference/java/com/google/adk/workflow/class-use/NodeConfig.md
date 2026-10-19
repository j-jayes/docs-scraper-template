JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../NodeConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](../package-summary.html)
  2. [NodeConfig](../NodeConfig.html)



# Uses of Class  
com.google.adk.workflow.NodeConfig

Packages that use [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")

Package

Description

com.google.adk.workflow

 

  * ## Uses of [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow") in [com.google.adk.workflow](../package-summary.html)

Methods in [com.google.adk.workflow](../package-summary.html) that return [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")

Modifier and Type

Method

Description

`final [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")`

NodeConfig.Builder.`[build](../NodeConfig.Builder.html#build\(\))()`

 

`[NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")`

BaseNode.`[config](../BaseNode.html#config\(\))()`

 

`default [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")`

Node.`[config](../Node.html#config\(\))()`

Returns the node's retry policy and execution timeout.

Methods in [com.google.adk.workflow](../package-summary.html) with parameters of type [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")

Modifier and Type

Method

Description

`[Workflow.Builder](../Workflow.Builder.html "class in com.google.adk.workflow")`

Workflow.Builder.`[config](../Workflow.Builder.html#config\(com.google.adk.workflow.NodeConfig\))([NodeConfig](../NodeConfig.html "class in com.google.adk.workflow") config)`

 

Constructors in [com.google.adk.workflow](../package-summary.html) with parameters of type [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow")

Modifier

Constructor

Description

`protected `

`[BaseNode](../BaseNode.html#%3Cinit%3E\(java.lang.String,java.lang.String,boolean,boolean,com.google.adk.workflow.NodeConfig,com.google.genai.types.Schema,com.google.genai.types.Schema,com.google.genai.types.Schema\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, boolean rerunOnResume, boolean waitForOutput, [NodeConfig](../NodeConfig.html "class in com.google.adk.workflow") config, @Nullable com.google.genai.types.Schema inputSchema, @Nullable com.google.genai.types.Schema outputSchema, @Nullable com.google.genai.types.Schema stateSchema)`

Creates a node; each parameter sets the [`Node`](../Node.html "interface in com.google.adk.workflow") property of the same name.




* * *

Copyright (C) 1980\. All rights reserved.
