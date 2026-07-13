JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SkillSource.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [SkillSource](SkillSource.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. listFrontmatters()
     2. listResources(String, String)
     3. loadFrontmatter(String)
     4. loadInstructions(String)
     5. loadResource(String, String)

Hide sidebar  Show sidebar

# Interface SkillSource

All Known Implementing Classes:
    `[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills"), [ClassPathSkillSource](ClassPathSkillSource.html "class in com.google.adk.skills"), [InMemorySkillSource](InMemorySkillSource.html "class in com.google.adk.skills"), [LocalSkillSource](LocalSkillSource.html "class in com.google.adk.skills")`

* * *

public interface SkillSource

Interface for getting access to available skills. 

All operations are asynchronous and communicate failures reactively through the returned `Single` error channel (terminating with `onError`), rather than throwing exceptions synchronously. Implementation must use the [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") for propagating error message back to the LLM.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

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




  * ## Method Details

    * ### listFrontmatters

io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>> listFrontmatters()

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills. 

If the source is misconfigured, such as directory doesn't exist, or having malformed skill, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") with the reason in the message.

Returns:
    a `Single` emitting a map where keys are skill names and values are their [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")

    * ### listResources

io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> listResources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)

Lists all resource files for a specific skill within a given directory. 

If the skill or the resource directory does not exist, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Parameters:
    `skillName` \- the name of the skill
    `resourceDirectory` \- the relative directory within the skill to list (e.g., "assets", "scripts")
Returns:
    a `Single` emitting a list of resource paths relative to the skill directory

    * ### loadFrontmatter

io.reactivex.rxjava3.core.Single<[Frontmatter](Frontmatter.html "class in com.google.adk.skills")> loadFrontmatter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Loads the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for a specific skill. 

If the skill is not found or its frontmatter is malformed, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") or parsing error.

Parameters:
    `skillName` \- the name of the skill
Returns:
    a `Single` emitting the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for the skill

    * ### loadInstructions

io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> loadInstructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Loads the instructions (body of SKILL.md) for a specific skill. 

If the skill is not found or its file structure is invalid (e.g., unclosed frontmatter blocks), the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Parameters:
    `skillName` \- the name of the skill
Returns:
    a `Single` emitting the instructions as a String

    * ### loadResource

io.reactivex.rxjava3.core.Single<com.google.common.io.ByteSource> loadResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)

Loads a specific resource file content. 

If the skill or the specific resource path cannot be found, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Parameters:
    `skillName` \- the name of the skill
    `resourcePath` \- the path to the resource file relative to the skill directory
Returns:
    a `Single` emitting the `ByteSource` for the resource content




* * *

Copyright (C) 1980\. All rights reserved.
