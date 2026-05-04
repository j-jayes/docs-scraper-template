JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ReplanPolicy.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [ReplanPolicy](ReplanPolicy.html)



Contents  

  1. Description
  2. Nested Class Summary

Hide sidebar  Show sidebar

# Interface ReplanPolicy

All Known Implementing Classes:
    `[ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")`

* * *

public sealed interface ReplanPolicy permits [ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap")

Policy governing how the planner reacts to missing expected outputs after an agent group executes.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

`static final record `

`[ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap")`

Stop immediately on failure with an error message.

`static final record `

`[ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap")`

Ignore failures and proceed with the remaining plan as-is.

`static final record `

`[ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")`

Attempt to recompute the remaining plan from current world state.




* * *

Copyright (C) 1980\. All rights reserved.
