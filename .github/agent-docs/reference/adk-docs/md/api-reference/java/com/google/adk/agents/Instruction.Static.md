JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instruction.Static.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [Instruction](Instruction.html)
  3. [Static](Instruction.Static.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Static(String)
  6. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. instruction()



# Record Class Instruction.Static

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

com.google.adk.agents.Instruction.Static

All Implemented Interfaces:
    `[Instruction](Instruction.html "interface in com.google.adk.agents")`

Enclosing interface:
    `[Instruction](Instruction.html "interface in com.google.adk.agents")`

* * *

public static record Instruction.Static([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang") implements [Instruction](Instruction.html "interface in com.google.adk.agents")

Plain instruction directly provided to the agent.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface com.google.adk.agents.[Instruction](Instruction.html "interface in com.google.adk.agents")

`[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents"), [Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")`

  * ## Constructor Summary

Constructors

Constructor

Description

`Static([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)`

Creates an instance of a `Static` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`final int`

`hashCode()`

Returns a hash code value for this object.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`instruction()`

Returns the value of the `instruction` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Static

public Static([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction)

Creates an instance of a `Static` record class.

Parameters:
    `instruction` \- the value for the `instruction` record component

  * ## Method Details

    * ### toString

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\) "class or interface in java.util").

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### instruction

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") instruction()

Returns the value of the `instruction` record component.

Returns:
    the value of the `instruction` record component




* * *

Copyright (C) 2025\. All rights reserved.
