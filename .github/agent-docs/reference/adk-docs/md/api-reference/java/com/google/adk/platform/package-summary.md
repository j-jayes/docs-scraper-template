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

  1. [com.google.adk.platform](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.platform

* * *

package com.google.adk.platform

Seams for the system operations behind ADK-generated timestamps and ids. 

An invocation reads the time from a [`InstantSource`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") and mints identifiers from a [`UuidProvider`](UuidProvider.html "interface in com.google.adk.platform"), both configured once on the runner and carried on every `InvocationContext` it creates rather than held in static state, so concurrent invocations may use independent providers. Either may be called from several RxJava worker threads at once.

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * Interfaces

Class

Description

[UuidProvider](UuidProvider.html "interface in com.google.adk.platform")

Supplies new unique identifiers for ADK-generated ids.




* * *

Copyright (C) 1980\. All rights reserved.
