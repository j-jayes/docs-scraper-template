JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Route.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](../package-summary.html)
  2. [Route](../Route.html)



# Uses of Interface  
com.google.adk.workflow.Route

Packages that use [Route](../Route.html "interface in com.google.adk.workflow")

Package

Description

com.google.adk.events

 

com.google.adk.workflow

 

  * ## Uses of [Route](../Route.html "interface in com.google.adk.workflow") in [com.google.adk.events](../../events/package-summary.html)

Methods in [com.google.adk.events](../../events/package-summary.html) that return types with arguments of type [Route](../Route.html "interface in com.google.adk.workflow")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.common.collect.ImmutableList<[Route](../Route.html "interface in com.google.adk.workflow")>>`

EventActions.`[route](../../events/EventActions.html#route\(\))()`

For a workflow node, returns the routes this event selects; an edge is followed when it has one of these routes.

Method parameters in [com.google.adk.events](../../events/package-summary.html) with type arguments of type [Route](../Route.html "interface in com.google.adk.workflow")

Modifier and Type

Method

Description

`[EventActions.Builder](../../events/EventActions.Builder.html "class in com.google.adk.events")`

EventActions.Builder.`[route](../../events/EventActions.Builder.html#route\(java.util.List\))(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Route](../Route.html "interface in com.google.adk.workflow")> value)`

 

`void`

EventActions.`[setRoute](../../events/EventActions.html#setRoute\(java.util.List\))(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Route](../Route.html "interface in com.google.adk.workflow")> route)`

 

  * ## Uses of [Route](../Route.html "interface in com.google.adk.workflow") in [com.google.adk.workflow](../package-summary.html)

Classes in [com.google.adk.workflow](../package-summary.html) that implement [Route](../Route.html "interface in com.google.adk.workflow")

Modifier and Type

Class

Description

`static enum `

`[Route.Default](../Route.Default.html "enum class in com.google.adk.workflow")`

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route.

`static final record `

`[Route.Flag](../Route.Flag.html "class in com.google.adk.workflow")`

A route identified by a boolean, for a two-way branch.

`static final record `

`[Route.Num](../Route.Num.html "class in com.google.adk.workflow")`

A route identified by an integer.

`static final record `

`[Route.Tag](../Route.Tag.html "class in com.google.adk.workflow")`

A route identified by a string, which is the common case.

Methods in [com.google.adk.workflow](../package-summary.html) that return types with arguments of type [Route](../Route.html "interface in com.google.adk.workflow")

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<[Route](../Route.html "interface in com.google.adk.workflow")>`

Edge.`[routes](../Edge.html#routes\(\))()`

Returns the value of the [`routes`](../../../../../com/google/adk/workflow/Edge.html#param-routes) record component.

Constructors in [com.google.adk.workflow](../package-summary.html) with parameters of type [Route](../Route.html "interface in com.google.adk.workflow")

Modifier

Constructor

Description

` `

`[Edge](../Edge.html#%3Cinit%3E\(com.google.adk.workflow.Node,com.google.adk.workflow.Node,com.google.adk.workflow.Route\))([Node](../Node.html "interface in com.google.adk.workflow") from, [Node](../Node.html "interface in com.google.adk.workflow") to, [Route](../Route.html "interface in com.google.adk.workflow") route)`

Creates an edge selected by a single route.

Constructor parameters in [com.google.adk.workflow](../package-summary.html) with type arguments of type [Route](../Route.html "interface in com.google.adk.workflow")

Modifier

Constructor

Description

` `

`[Edge](../Edge.html#%3Cinit%3E\(com.google.adk.workflow.Node,com.google.adk.workflow.Node,com.google.common.collect.ImmutableList\))([Node](../Node.html "interface in com.google.adk.workflow") from, [Node](../Node.html "interface in com.google.adk.workflow") to, com.google.common.collect.ImmutableList<[Route](../Route.html "interface in com.google.adk.workflow")> routes)`

Creates an instance of a `Edge` record class.




* * *

Copyright (C) 1980\. All rights reserved.
