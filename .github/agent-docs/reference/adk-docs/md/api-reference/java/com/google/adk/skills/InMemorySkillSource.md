JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemorySkillSource.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [InMemorySkillSource](InMemorySkillSource.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. listFrontmatters()
     3. listResources(String, String)
     4. loadFrontmatter(String)
     5. loadInstructions(String)
     6. loadResource(String, String)

Hide sidebar  Show sidebar

# Class InMemorySkillSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.skills.InMemorySkillSource

All Implemented Interfaces:
    `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`

* * *

public final class InMemorySkillSource extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [SkillSource](SkillSource.html "interface in com.google.adk.skills")

An in-memory implementation of [`SkillSource`](SkillSource.html "interface in com.google.adk.skills"). 

Everything is provided upfront using a builder pattern.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[InMemorySkillSource.Builder](InMemorySkillSource.Builder.html "class in com.google.adk.skills")`

Builder for [`InMemorySkillSource`](InMemorySkillSource.html "class in com.google.adk.skills").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [InMemorySkillSource.Builder](InMemorySkillSource.Builder.html "class in com.google.adk.skills")`

`builder()`

 

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>>`

`listFrontmatters()`

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`listResources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)`

Lists all resource files for a specific skill within a given directory.

`io.reactivex.rxjava3.core.Single<[Frontmatter](Frontmatter.html "class in com.google.adk.skills")>`

`loadFrontmatter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for a specific skill.

`io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`loadInstructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the instructions (body of SKILL.md) for a specific skill.

`io.reactivex.rxjava3.core.Single<com.google.common.io.ByteSource>`

`loadResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)`

Loads a specific resource file content.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### builder

public static [InMemorySkillSource.Builder](InMemorySkillSource.Builder.html "class in com.google.adk.skills") builder()

    * ### listFrontmatters

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>> listFrontmatters()

Description copied from interface: `[SkillSource](SkillSource.html#listFrontmatters\(\))`

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills. 

If the source is misconfigured, such as directory doesn't exist, or having malformed skill, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") with the reason in the message.

Specified by:
    `[listFrontmatters](SkillSource.html#listFrontmatters\(\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Returns:
    a `Single` emitting a map where keys are skill names and values are their [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")

    * ### listResources

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> listResources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)

Description copied from interface: `[SkillSource](SkillSource.html#listResources\(java.lang.String,java.lang.String\))`

Lists all resource files for a specific skill within a given directory. 

If the skill or the resource directory does not exist, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Specified by:
    `[listResources](SkillSource.html#listResources\(java.lang.String,java.lang.String\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Parameters:
    `skillName` \- the name of the skill
    `resourceDirectory` \- the relative directory within the skill to list (e.g., "assets", "scripts")
Returns:
    a `Single` emitting a list of resource paths relative to the skill directory

    * ### loadFrontmatter

public io.reactivex.rxjava3.core.Single<[Frontmatter](Frontmatter.html "class in com.google.adk.skills")> loadFrontmatter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Description copied from interface: `[SkillSource](SkillSource.html#loadFrontmatter\(java.lang.String\))`

Loads the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for a specific skill. 

If the skill is not found or its frontmatter is malformed, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") or parsing error.

Specified by:
    `[loadFrontmatter](SkillSource.html#loadFrontmatter\(java.lang.String\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Parameters:
    `skillName` \- the name of the skill
Returns:
    a `Single` emitting the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for the skill

    * ### loadInstructions

public io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> loadInstructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Description copied from interface: `[SkillSource](SkillSource.html#loadInstructions\(java.lang.String\))`

Loads the instructions (body of SKILL.md) for a specific skill. 

If the skill is not found or its file structure is invalid (e.g., unclosed frontmatter blocks), the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Specified by:
    `[loadInstructions](SkillSource.html#loadInstructions\(java.lang.String\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Parameters:
    `skillName` \- the name of the skill
Returns:
    a `Single` emitting the instructions as a String

    * ### loadResource

public io.reactivex.rxjava3.core.Single<com.google.common.io.ByteSource> loadResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)

Description copied from interface: `[SkillSource](SkillSource.html#loadResource\(java.lang.String,java.lang.String\))`

Loads a specific resource file content. 

If the skill or the specific resource path cannot be found, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Specified by:
    `[loadResource](SkillSource.html#loadResource\(java.lang.String,java.lang.String\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Parameters:
    `skillName` \- the name of the skill
    `resourcePath` \- the path to the resource file relative to the skill directory
Returns:
    a `Single` emitting the `ByteSource` for the resource content




* * *

Copyright (C) 1980\. All rights reserved.
