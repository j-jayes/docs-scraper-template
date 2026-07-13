JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../SkillSource.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](../package-summary.html)
  2. [SkillSource](../SkillSource.html)



# Uses of Interface  
com.google.adk.skills.SkillSource

Packages that use [SkillSource](../SkillSource.html "interface in com.google.adk.skills")

Package

Description

com.google.adk.skills

 

com.google.adk.tools.skills

 

  * ## Uses of [SkillSource](../SkillSource.html "interface in com.google.adk.skills") in [com.google.adk.skills](../package-summary.html)

Classes in [com.google.adk.skills](../package-summary.html) that implement [SkillSource](../SkillSource.html "interface in com.google.adk.skills")

Modifier and Type

Class

Description

`class `

`[AbstractSkillSource](../AbstractSkillSource.html "class in com.google.adk.skills")<PathT>`

Abstract base class for SkillSource implementations that load skills from path like object.

`final class `

`[ClassPathSkillSource](../ClassPathSkillSource.html "class in com.google.adk.skills")`

Loads skills from the classpath.

`final class `

`[InMemorySkillSource](../InMemorySkillSource.html "class in com.google.adk.skills")`

An in-memory implementation of [`SkillSource`](../SkillSource.html "interface in com.google.adk.skills").

`final class `

`[LocalSkillSource](../LocalSkillSource.html "class in com.google.adk.skills")`

Loads skills from the local file system.

  * ## Uses of [SkillSource](../SkillSource.html "interface in com.google.adk.skills") in [com.google.adk.tools.skills](../../tools/skills/package-summary.html)

Constructors in [com.google.adk.tools.skills](../../tools/skills/package-summary.html) with parameters of type [SkillSource](../SkillSource.html "interface in com.google.adk.skills")

Modifier

Constructor

Description

` `

`[SkillToolset](../../tools/skills/SkillToolset.html#%3Cinit%3E\(com.google.adk.skills.SkillSource\))([SkillSource](../SkillSource.html "interface in com.google.adk.skills") skillSource)`

Initializes the SkillToolset with a SkillSource and default execution settings.

` `

`[SkillToolset](../../tools/skills/SkillToolset.html#%3Cinit%3E\(com.google.adk.skills.SkillSource,java.lang.String\))([SkillSource](../SkillSource.html "interface in com.google.adk.skills") skillSource, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") systemInstruction)`

Initializes the SkillToolset with a SkillSource.




* * *

Copyright (C) 1980\. All rights reserved.
