JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Edge.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Edge](Edge.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Edge(Node, Node, ImmutableList)
     2. Edge(Node, Node)
     3. Edge(Node, Node, Route)
  5. Method Details
     1. isUnconditional()
     2. toString()
     3. hashCode()
     4. equals(Object)
     5. from()
     6. to()
     7. routes()

Hide sidebar  Show sidebar

# Record Class Edge

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.workflow.Edge

Record Components:
    `from` \- The node whose completion fires this edge.
    `to` \- The node this edge triggers.
    `routes` \- The routes that select this edge. An empty list makes the edge unconditional.

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public record Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to, com.google.common.collect.ImmutableList<[Route](Route.html "interface in com.google.adk.workflow")> routes) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

A connection between two nodes in a workflow graph. An edge with no routes fires whenever its source completes; any other edge fires only when one of its routes is selected, as [`Route`](Route.html "interface in com.google.adk.workflow") describes.

  * ## Constructor Summary

Constructors

Constructor

Description

`Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to)`

Creates an unconditional edge.

`Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to, [Route](Route.html "interface in com.google.adk.workflow") route)`

Creates an edge selected by a single route.

`Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to, com.google.common.collect.ImmutableList<[Route](Route.html "interface in com.google.adk.workflow")> routes)`

Creates an instance of a `Edge` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`[Node](Node.html "interface in com.google.adk.workflow")`

`from()`

Returns the value of the `from` record component.

`final int`

`hashCode()`

Returns a hash code value for this object.

`boolean`

`isUnconditional()`

Returns `true` if this edge fires regardless of the routes its source emits.

`com.google.common.collect.ImmutableList<[Route](Route.html "interface in com.google.adk.workflow")>`

`routes()`

Returns the value of the `routes` record component.

`[Node](Node.html "interface in com.google.adk.workflow")`

`to()`

Returns the value of the `to` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Edge

public Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to, com.google.common.collect.ImmutableList<[Route](Route.html "interface in com.google.adk.workflow")> routes)

Creates an instance of a `Edge` record class.

Parameters:
    `from` \- the value for the `from` record component
    `to` \- the value for the `to` record component
    `routes` \- the value for the `routes` record component

    * ### Edge

public Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to)

Creates an unconditional edge.

    * ### Edge

public Edge([Node](Node.html "interface in com.google.adk.workflow") from, [Node](Node.html "interface in com.google.adk.workflow") to, [Route](Route.html "interface in com.google.adk.workflow") route)

Creates an edge selected by a single route.

  * ## Method Details

    * ### isUnconditional

public boolean isUnconditional()

Returns `true` if this edge fires regardless of the routes its source emits.

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

    * ### from

public [Node](Node.html "interface in com.google.adk.workflow") from()

Returns the value of the `from` record component.

Returns:
    the value of the `from` record component

    * ### to

public [Node](Node.html "interface in com.google.adk.workflow") to()

Returns the value of the `to` record component.

Returns:
    the value of the `to` record component

    * ### routes

public com.google.common.collect.ImmutableList<[Route](Route.html "interface in com.google.adk.workflow")> routes()

Returns the value of the `routes` record component.

Returns:
    the value of the `routes` record component




* * *

Copyright (C) 1980\. All rights reserved.
