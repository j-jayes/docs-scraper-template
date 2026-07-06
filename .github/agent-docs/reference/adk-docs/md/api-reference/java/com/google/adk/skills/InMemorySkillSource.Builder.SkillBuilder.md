JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemorySkillSource.Builder.SkillBuilder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [InMemorySkillSource](InMemorySkillSource.html)
  3. [Builder](InMemorySkillSource.Builder.html)
  4. [SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. frontmatter(Frontmatter)
     2. instructions(String)
     3. addResource(String, ByteSource)
     4. addResource(String, byte[])
     5. addResource(String, String)
     6. skill(String)
     7. build()

Hide sidebar  Show sidebar

# Class InMemorySkillSource.Builder.SkillBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.skills.InMemorySkillSource.Builder.SkillBuilder

Enclosing class:
    `[InMemorySkillSource.Builder](InMemorySkillSource.Builder.html "class in com.google.adk.skills")`

* * *

public final class InMemorySkillSource.Builder.SkillBuilder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for a specific skill.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, byte[] content)`

 

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, com.google.common.io.ByteSource content)`

 

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") content)`

 

`[InMemorySkillSource](InMemorySkillSource.html "class in com.google.adk.skills")`

`build()`

Builds the [`InMemorySkillSource`](InMemorySkillSource.html "class in com.google.adk.skills") containing all configured skills.

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`frontmatter([Frontmatter](Frontmatter.html "class in com.google.adk.skills") frontmatter)`

 

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`instructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instructions)`

 

`[InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills")`

`skill([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Switches context to configure another skill, creating it if it doesn't exist.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### frontmatter

@CanIgnoreReturnValue public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") frontmatter([Frontmatter](Frontmatter.html "class in com.google.adk.skills") frontmatter)

    * ### instructions

@CanIgnoreReturnValue public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") instructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") instructions)

    * ### addResource

@CanIgnoreReturnValue public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, com.google.common.io.ByteSource content)

    * ### addResource

@CanIgnoreReturnValue public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, byte[] content)

    * ### addResource

@CanIgnoreReturnValue public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") addResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") content)

    * ### skill

public [InMemorySkillSource.Builder.SkillBuilder](InMemorySkillSource.Builder.SkillBuilder.html "class in com.google.adk.skills") skill([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Switches context to configure another skill, creating it if it doesn't exist.

    * ### build

public [InMemorySkillSource](InMemorySkillSource.html "class in com.google.adk.skills") build()

Builds the [`InMemorySkillSource`](InMemorySkillSource.html "class in com.google.adk.skills") containing all configured skills.




* * *

Copyright (C) 1980\. All rights reserved.
