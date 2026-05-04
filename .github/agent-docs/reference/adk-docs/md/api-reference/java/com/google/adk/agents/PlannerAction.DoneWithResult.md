JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PlannerAction.DoneWithResult.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [PlannerAction](PlannerAction.html)
  3. [DoneWithResult](PlannerAction.DoneWithResult.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. DoneWithResult(String)
  6. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. result()

Hide sidebar  Show sidebar

# Record Class PlannerAction.DoneWithResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.agents.PlannerAction.DoneWithResult

All Implemented Interfaces:
    `[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")`

Enclosing interface:
    `[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")`

* * *

public static record PlannerAction.DoneWithResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") result) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang") implements [PlannerAction](PlannerAction.html "interface in com.google.adk.agents")

Plan is complete with a final text result.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [PlannerAction](PlannerAction.html#nested-class-summary "interface in com.google.adk.agents")

`[PlannerAction.Done](PlannerAction.Done.html "class in com.google.adk.agents"), [PlannerAction.DoneWithResult](PlannerAction.DoneWithResult.html "class in com.google.adk.agents"), [PlannerAction.NoOp](PlannerAction.NoOp.html "class in com.google.adk.agents"), [PlannerAction.RunAgents](PlannerAction.RunAgents.html "class in com.google.adk.agents")`

Modifier and Type

Interface

Description

`static final record `

`[PlannerAction.Done](PlannerAction.Done.html "class in com.google.adk.agents")`

Plan is complete, no result to emit.

`static final record `

`[PlannerAction.DoneWithResult](PlannerAction.DoneWithResult.html "class in com.google.adk.agents")`

Plan is complete with a final text result.

`static final record `

`[PlannerAction.NoOp](PlannerAction.NoOp.html "class in com.google.adk.agents")`

Skip this iteration (no-op).

`static final record `

`[PlannerAction.RunAgents](PlannerAction.RunAgents.html "class in com.google.adk.agents")`

Run the specified sub-agent(s).

  * ## Constructor Summary

Constructors

Constructor

Description

`DoneWithResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") result)`

Creates an instance of a `DoneWithResult` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`final int`

`hashCode()`

Returns a hash code value for this object.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`result()`

Returns the value of the `result` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### DoneWithResult

public DoneWithResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") result)

Creates an instance of a `DoneWithResult` record class.

Parameters:
    `result` \- the value for the `result` record component

  * ## Method Details

    * ### toString

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\)).

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### result

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") result()

Returns the value of the `result` record component.

Returns:
    the value of the `result` record component




* * *

Copyright (C) 1980\. All rights reserved.
