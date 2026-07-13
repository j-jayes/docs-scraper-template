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

  1. [com.google.adk.skills](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.skills

* * *

package com.google.adk.skills

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesException Classes

Class

Description

[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<PathT>

Abstract base class for SkillSource implementations that load skills from path like object.

[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<PathT>

A container class that holds a skill's name and the path to its SKILL.md file.

[ClassPathSkillSource](ClassPathSkillSource.html "class in com.google.adk.skills")

Loads skills from the classpath.

[Frontmatter](Frontmatter.html "class in com.google.adk.skills")

Frontmatter represents the YAML metadata at the top of a SKILL.md file.

[Frontmatter.Builder](Frontmatter.Builder.html "class in com.google.adk.skills")

 

[InMemorySkillSource](InMemorySkillSource.html "class in com.google.adk.skills")

An in-memory implementation of [`SkillSource`](SkillSource.html "interface in com.google.adk.skills").

[InMemorySkillSource.Builder](InMemorySkillSource.Builder.html "class in com.google.adk.skills")

Builder for [`InMemorySkillSource`](InMemorySkillSource.html "class in com.google.adk.skills").

[LocalSkillSource](LocalSkillSource.html "class in com.google.adk.skills")

Loads skills from the local file system.

[SkillSource](SkillSource.html "interface in com.google.adk.skills")

Interface for getting access to available skills.

[SkillSourceException](SkillSourceException.html "class in com.google.adk.skills")

Exception for [`SkillSource`](SkillSource.html "interface in com.google.adk.skills") implementations to signal recoverable errors that will have the message sending back to the LLM.




* * *

Copyright (C) 1980\. All rights reserved.
