JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/NamedToolPredicate.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [NamedToolPredicate](NamedToolPredicate.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. NamedToolPredicate(List)
     2. NamedToolPredicate(String...)
  5. Method Details
     1. test(BaseTool, Optional)

Hide sidebar  Show sidebar

# Class NamedToolPredicate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.NamedToolPredicate

All Implemented Interfaces:
    `[ToolPredicate](ToolPredicate.html "interface in com.google.adk.tools")`

* * *

public class NamedToolPredicate extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [ToolPredicate](ToolPredicate.html "interface in com.google.adk.tools")

  * ## Constructor Summary

Constructors

Constructor

Description

`NamedToolPredicate([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")... toolNames)`

 

`NamedToolPredicate([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`boolean`

`test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Decides if the given tool is selected.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [ToolPredicate](ToolPredicate.html#method-summary "interface in com.google.adk.tools")

`[test](ToolPredicate.html#test\(com.google.adk.tools.BaseTool,com.google.adk.agents.ReadonlyContext\) "test\(BaseTool, ReadonlyContext\)")`

Modifier and Type

Method

Description

`default boolean`

`[test](ToolPredicate.html#test\(com.google.adk.tools.BaseTool,com.google.adk.agents.ReadonlyContext\))([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, @Nullable [ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Decides if the given tool is selected.




  * ## Constructor Details

    * ### NamedToolPredicate

public NamedToolPredicate([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

    * ### NamedToolPredicate

public NamedToolPredicate([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")... toolNames)

  * ## Method Details

    * ### test

public boolean test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)

Description copied from interface: `[ToolPredicate](ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))`

Decides if the given tool is selected.

Specified by:
    `[test](ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))` in interface `[ToolPredicate](ToolPredicate.html "interface in com.google.adk.tools")`
Parameters:
    `tool` \- The tool to check.
    `readonlyContext` \- The current context.
Returns:
    true if the tool should be selected, false otherwise.




* * *

Copyright (C) 1980\. All rights reserved.
