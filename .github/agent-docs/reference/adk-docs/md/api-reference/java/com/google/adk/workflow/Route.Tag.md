JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Route.Tag.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Route](Route.html)
  3. [Tag](Route.Tag.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Constructor Details
     1. Tag(String)
  7. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. value()

Hide sidebar  Show sidebar

# Record Class Route.Tag

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.workflow.Route.Tag

All Implemented Interfaces:
    `[Route](Route.html "interface in com.google.adk.workflow")`

Enclosing interface:
    `[Route](Route.html "interface in com.google.adk.workflow")`

* * *

public static record Route.Tag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang") implements [Route](Route.html "interface in com.google.adk.workflow")

A route identified by a string, which is the common case. Its value cannot be [`Route.DEFAULT_ROUTE_SENTINEL`](Route.html#DEFAULT_ROUTE_SENTINEL); use [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") for the default route.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [Route](Route.html#nested-class-summary "interface in com.google.adk.workflow")

`[Route.Default](Route.Default.html "enum class in com.google.adk.workflow"), [Route.Flag](Route.Flag.html "class in com.google.adk.workflow"), [Route.Num](Route.Num.html "class in com.google.adk.workflow"), [Route.Tag](Route.Tag.html "class in com.google.adk.workflow")`

Modifier and Type

Interface

Description

`static enum `

`[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")`

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route.

`static final record `

`[Route.Flag](Route.Flag.html "class in com.google.adk.workflow")`

A route identified by a boolean, for a two-way branch.

`static final record `

`[Route.Num](Route.Num.html "class in com.google.adk.workflow")`

A route identified by an integer.

`static final record `

`[Route.Tag](Route.Tag.html "class in com.google.adk.workflow")`

A route identified by a string, which is the common case.

  * ## Field Summary

### Fields inherited from interface [Route](Route.html#field-summary "interface in com.google.adk.workflow")

`[DEFAULT_ROUTE_SENTINEL](Route.html#DEFAULT_ROUTE_SENTINEL)`

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[DEFAULT_ROUTE_SENTINEL](Route.html#DEFAULT_ROUTE_SENTINEL)`

The string that stands for [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") on the wire.

  * ## Constructor Summary

Constructors

Constructor

Description

`Tag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value)`

Creates an instance of a `Tag` record class.

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

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`value()`

Returns the value of the `value` record component.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Tag

public Tag([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value)

Creates an instance of a `Tag` record class.

Parameters:
    `value` \- the value for the `value` record component

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

    * ### value

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value()

Returns the value of the `value` record component.

Returns:
    the value of the `value` record component




* * *

Copyright (C) 1980\. All rights reserved.
