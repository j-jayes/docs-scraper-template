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

  1. [com.google.adk.plugins](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.plugins

* * *

package com.google.adk.plugins

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

[com.google.adk.plugins.agentanalytics](agentanalytics/package-summary.html)

 

[com.google.adk.plugins.recordings](recordings/package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesException Classes

Class

Description

[BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

Base class for creating plugins.

[ContextFilterPlugin](ContextFilterPlugin.html "class in com.google.adk.plugins")

A plugin that filters the LLM request `Content` list to reduce its size, for example to adhere to context window limits.

[ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")

Builder for [`ContextFilterPlugin`](ContextFilterPlugin.html "class in com.google.adk.plugins").

[GlobalInstructionPlugin](GlobalInstructionPlugin.html "class in com.google.adk.plugins")

Plugin that provides global instructions functionality at the App level.

[LoggingPlugin](LoggingPlugin.html "class in com.google.adk.plugins")

A plugin that logs important information at each callback point.

[Plugin](Plugin.html "interface in com.google.adk.plugins")

Interface for creating plugins.

[PluginManager](PluginManager.html "class in com.google.adk.plugins")

Manages the registration and execution of plugins.

[ReplayConfigError](ReplayConfigError.html "class in com.google.adk.plugins")

Exception raised when replay configuration is invalid or missing.

[ReplayPlugin](ReplayPlugin.html "class in com.google.adk.plugins")

Plugin for replaying ADK agent interactions from recordings.

[ReplayVerificationError](ReplayVerificationError.html "class in com.google.adk.plugins")

Exception raised when replay verification fails.




* * *

Copyright (C) 1980\. All rights reserved.
