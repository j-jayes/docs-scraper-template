JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.workflow

* * *

package com.google.adk.workflow

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesEnum ClassesRecord Classes

Class

Description

[BaseNode](BaseNode.html "class in com.google.adk.workflow")

Base class for nodes in a workflow graph.

[Edge](Edge.html "class in com.google.adk.workflow")

A connection between two nodes in a workflow graph.

[JoinNode](JoinNode.html "class in com.google.adk.workflow")

A node that waits for every predecessor to complete, then outputs their outputs keyed by predecessor name.

[JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow")

Builder for [`JoinNode`](JoinNode.html "class in com.google.adk.workflow").

[Node](Node.html "interface in com.google.adk.workflow")

A unit of work in a workflow graph.

[NodeConfig](NodeConfig.html "class in com.google.adk.workflow")

A node's retry policy and execution timeout.

[NodeConfig.Builder](NodeConfig.Builder.html "class in com.google.adk.workflow")

Builder for [`NodeConfig`](NodeConfig.html "class in com.google.adk.workflow").

[NodeInfo](NodeInfo.html "class in com.google.adk.workflow")

The identity of the workflow-node activation that emitted an [`Event`](../events/Event.html "class in com.google.adk.events").

[NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow")

Builder for [`NodeInfo`](NodeInfo.html "class in com.google.adk.workflow").

[RetryConfig](RetryConfig.html "class in com.google.adk.workflow")

How a node is retried when it fails.

[RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")

Builder for [`RetryConfig`](RetryConfig.html "class in com.google.adk.workflow").

[Route](Route.html "interface in com.google.adk.workflow")

A value on a workflow edge, and the value a node emits to select which of its outgoing edges are followed.

[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route.

[Route.Flag](Route.Flag.html "class in com.google.adk.workflow")

A route identified by a boolean, for a two-way branch.

[Route.Num](Route.Num.html "class in com.google.adk.workflow")

A route identified by an integer.

[Route.Tag](Route.Tag.html "class in com.google.adk.workflow")

A route identified by a string, which is the common case.

[Start](Start.html "class in com.google.adk.workflow")

The node that marks where a workflow graph starts.

[Workflow](Workflow.html "class in com.google.adk.workflow")

A graph of nodes that is itself a node, so a workflow can go wherever a node can, including in another workflow.

[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")

Builder for [`Workflow`](Workflow.html "class in com.google.adk.workflow").




* * *

Copyright (C) 1980\. All rights reserved.
