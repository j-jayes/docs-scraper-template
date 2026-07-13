JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instrumentation.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Instrumentation](Instrumentation.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. recordAgentInvocation(InvocationContext, BaseAgent)
     2. recordAgentInvocation(InvocationContext, BaseAgent, Context)
     3. recordToolExecution(BaseTool, BaseAgent, Map)
     4. recordToolExecution(BaseTool, BaseAgent, Map, Context)

Hide sidebar  Show sidebar

# Class Instrumentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Instrumentation

* * *

public final class Instrumentation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Unified context manager utility class for agent and tool execution telemetry in ADK.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry")`

AutoCloseable telemetry tracking scope for agent invocations.

`static class `

`[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`

Base class for AutoCloseable telemetry tracking scopes.

`static final class `

`[Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

Stores all telemetry related state.

`static final class `

`[Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

AutoCloseable telemetry tracking scope for tool executions.

  * ## Method Summary

All MethodsStatic MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`static [Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry")`

`recordAgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

Deprecated.

Use the version with explicit parent context instead.

`static [Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry")`

`recordAgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, io.opentelemetry.context.Context parentContext)`

Creates an [`Instrumentation.AgentInvocation`](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry") context to record agent invocation telemetry with an explicit parent context.

`static [Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

`recordToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs)`

Creates a ToolExecution context to record tool execution telemetry.

`static [Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

`recordToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs, io.opentelemetry.context.Context parentContext)`

Creates a [`Instrumentation.ToolExecution`](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") context to record tool execution telemetry with an explicit parent context.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### recordAgentInvocation

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public static [Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry") recordAgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

Deprecated.

Use the version with explicit parent context instead. This method will be removed once all callers are updated.

Creates an AgentInvocation context to record agent invocation telemetry.

    * ### recordAgentInvocation

public static [Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry") recordAgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, io.opentelemetry.context.Context parentContext)

Creates an [`Instrumentation.AgentInvocation`](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry") context to record agent invocation telemetry with an explicit parent context.

Parameters:
    `ctx` \- The invocation context of the agent execution.
    `agent` \- The agent being invoked.
    `parentContext` \- The OpenTelemetry parent context.
Returns:
    A new [`Instrumentation.AgentInvocation`](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry") scope.

    * ### recordToolExecution

public static [Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") recordToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs)

Creates a ToolExecution context to record tool execution telemetry.

    * ### recordToolExecution

public static [Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") recordToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs, io.opentelemetry.context.Context parentContext)

Creates a [`Instrumentation.ToolExecution`](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") context to record tool execution telemetry with an explicit parent context.

Parameters:
    `tool` \- The tool being executed.
    `agent` \- The agent invoking the tool.
    `functionArgs` \- The arguments passed to the tool.
    `parentContext` \- The OpenTelemetry parent context.
Returns:
    A new [`Instrumentation.ToolExecution`](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry") scope.




* * *

Copyright (C) 1980\. All rights reserved.
