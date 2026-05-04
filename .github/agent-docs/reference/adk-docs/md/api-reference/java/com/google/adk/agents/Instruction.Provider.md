JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instruction.Provider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Instruction](Instruction.html)
  3. [Provider](Instruction.Provider.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Provider(Function)
  6. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. getInstruction()

Hide sidebar  Show sidebar

# Record Class Instruction.Provider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.agents.Instruction.Provider

All Implemented Interfaces:
    `[Instruction](Instruction.html "interface in com.google.adk.agents")`

Enclosing interface:
    `[Instruction](Instruction.html "interface in com.google.adk.agents")`

* * *

public static record Instruction.Provider([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "interface in java.util.function")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> getInstruction) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang") implements [Instruction](Instruction.html "interface in com.google.adk.agents")

Returns an instruction dynamically constructed from the given context.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [Instruction](Instruction.html#nested-class-summary "interface in com.google.adk.agents")

`[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents"), [Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")`

Modifier and Type

Interface

Description

`static final record `

`[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")`

Returns an instruction dynamically constructed from the given context.

`static final record `

`[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")`

Plain instruction directly provided to the agent.

  * ## Constructor Summary

Constructors

Constructor

Description

`Provider([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "interface in java.util.function")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> getInstruction)`

Creates an instance of a `Provider` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`[Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "interface in java.util.function")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`getInstruction()`

Returns the value of the `getInstruction` record component.

`final int`

`hashCode()`

Returns a hash code value for this object.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Provider

public Provider([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "interface in java.util.function")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> getInstruction)

Creates an instance of a `Provider` record class.

Parameters:
    `getInstruction` \- the value for the `getInstruction` record component

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

    * ### getInstruction

public [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html "interface in java.util.function")<[ReadonlyContext](ReadonlyContext.html "class in com.google.adk.agents"), io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> getInstruction()

Returns the value of the `getInstruction` record component.

Returns:
    the value of the `getInstruction` record component




* * *

Copyright (C) 1980\. All rights reserved.
