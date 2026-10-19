JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Route.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Route](Route.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Field Details
     1. DEFAULT_ROUTE_SENTINEL

Hide sidebar  Show sidebar

# Interface Route

All Known Implementing Classes:
    `[Route.Default](Route.Default.html "enum class in com.google.adk.workflow"), [Route.Flag](Route.Flag.html "class in com.google.adk.workflow"), [Route.Num](Route.Num.html "class in com.google.adk.workflow"), [Route.Tag](Route.Tag.html "class in com.google.adk.workflow")`

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public sealed interface Route permits [Route.Tag](Route.Tag.html "class in com.google.adk.workflow"), [Route.Num](Route.Num.html "class in com.google.adk.workflow"), [Route.Flag](Route.Flag.html "class in com.google.adk.workflow"), [Route.Default](Route.Default.html "enum class in com.google.adk.workflow")

A value on a workflow edge, and the value a node emits to select which of its outgoing edges are followed. An edge fires when the value it carries matches one the node emitted. 

On the wire a route is a bare scalar (a string, integer or boolean), and [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") is the `DEFAULT_ROUTE_SENTINEL` string.

  * ## Nested Class Summary

Nested Classes

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

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`DEFAULT_ROUTE_SENTINEL`

The string that stands for [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") on the wire.




  * ## Field Details

    * ### DEFAULT_ROUTE_SENTINEL

static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") DEFAULT_ROUTE_SENTINEL

The string that stands for [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") on the wire.

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.workflow.Route.DEFAULT_ROUTE_SENTINEL)




* * *

Copyright (C) 1980\. All rights reserved.
