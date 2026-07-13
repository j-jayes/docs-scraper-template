JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Instrumentation.ToolExecution.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](../package-summary.html)
  2. [Instrumentation](../Instrumentation.html)
  3. [ToolExecution](../Instrumentation.ToolExecution.html)



# Uses of Class  
com.google.adk.telemetry.Instrumentation.ToolExecution

Packages that use [Instrumentation.ToolExecution](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")

Package

Description

com.google.adk.telemetry

 

  * ## Uses of [Instrumentation.ToolExecution](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") in [com.google.adk.telemetry](../package-summary.html)

Methods in [com.google.adk.telemetry](../package-summary.html) that return [Instrumentation.ToolExecution](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")

Modifier and Type

Method

Description

`static [Instrumentation.ToolExecution](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

Instrumentation.`[recordToolExecution](../Instrumentation.html#recordToolExecution\(com.google.adk.tools.BaseTool,com.google.adk.agents.BaseAgent,java.util.Map\))([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs)`

Creates a ToolExecution context to record tool execution telemetry.

`static [Instrumentation.ToolExecution](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

Instrumentation.`[recordToolExecution](../Instrumentation.html#recordToolExecution\(com.google.adk.tools.BaseTool,com.google.adk.agents.BaseAgent,java.util.Map,io.opentelemetry.context.Context\))([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs, io.opentelemetry.context.Context parentContext)`

Creates a [`Instrumentation.ToolExecution`](../Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") context to record tool execution telemetry with an explicit parent context.




* * *

Copyright (C) 1980\. All rights reserved.
