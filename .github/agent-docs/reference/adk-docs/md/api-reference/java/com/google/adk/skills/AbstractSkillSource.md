JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AbstractSkillSource.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [AbstractSkillSource](AbstractSkillSource.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AbstractSkillSource()
  6. Method Details
     1. listFrontmatters()
     2. loadFrontmatter(String)
     3. loadInstructions(String)
     4. loadResource(String, String)
     5. listSkills()
     6. findSkillMdPath(String)
     7. findResourcePath(String, String)
     8. openChannel(PathT)

Hide sidebar  Show sidebar

# Class AbstractSkillSource<PathT>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.skills.AbstractSkillSource<PathT>

Type Parameters:
    `PathT` \- the type of path object

All Implemented Interfaces:
    `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`

Direct Known Subclasses:
    `[ClassPathSkillSource](ClassPathSkillSource.html "class in com.google.adk.skills"), [LocalSkillSource](LocalSkillSource.html "class in com.google.adk.skills")`

* * *

public abstract class AbstractSkillSource<PathT> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [SkillSource](SkillSource.html "interface in com.google.adk.skills")

Abstract base class for SkillSource implementations that load skills from path like object.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<[PathT](AbstractSkillSource.SkillMdPath.html#type-param-PathT "type parameter in AbstractSkillSource.SkillMdPath")>`

A container class that holds a skill's name and the path to its SKILL.md file.

  * ## Constructor Summary

Constructors

Constructor

Description

`AbstractSkillSource()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`protected abstract io.reactivex.rxjava3.core.Single<PathT>`

`findResourcePath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)`

Returns the path to the resource for the given skill.

`protected abstract io.reactivex.rxjava3.core.Single<PathT>`

`findSkillMdPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Returns the path to the SKILL.md file for the given skill.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>>`

`listFrontmatters()`

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills.

`protected abstract io.reactivex.rxjava3.core.Flowable<[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<PathT>>`

`listSkills()`

Returns a `Flowable` of skills as a pair of skill name and the path to the SKILL.md file.

`io.reactivex.rxjava3.core.Single<[Frontmatter](Frontmatter.html "class in com.google.adk.skills")>`

`loadFrontmatter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for a specific skill.

`io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`loadInstructions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the instructions (body of SKILL.md) for a specific skill.

`io.reactivex.rxjava3.core.Single<com.google.common.io.ByteSource>`

`loadResource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)`

Loads a specific resource file content.

`protected abstract [ReadableByteChannel](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/channels/ReadableByteChannel.html "interface in java.nio.channels")`

`openChannel(PathT path)`

Opens a [`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") for reading the content of the given path.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [SkillSource](SkillSource.html#method-summary "interface in com.google.adk.skills")

`[listResources](SkillSource.html#listResources\(java.lang.String,java.lang.String\) "listResources\(String, String\)")`

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`[listResources](SkillSource.html#listResources\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)`

Lists all resource files for a specific skill within a given directory.




  * ## Constructor Details

    * ### AbstractSkillSource

public AbstractSkillSource()

  * ## Method Details

    * ### listFrontmatters

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>> listFrontmatters()

Description copied from interface: `[SkillSource](SkillSource.html#listFrontmatters\(\))`

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills. 

If the source is misconfigured, such as directory doesn't exist, or having malformed skill, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills") with the reason in the message.

Specified by:
    `[listFrontmatters](SkillSource.html#listFrontmatters\(\))` in interface `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`
Returns:
    a `Single` emitting a map where keys are skill names and values are their [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")

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

    * ### listSkills

protected abstract io.reactivex.rxjava3.core.Flowable<[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<PathT>> listSkills()

Returns a `Flowable` of skills as a pair of skill name and the path to the SKILL.md file.

    * ### findSkillMdPath

protected abstract io.reactivex.rxjava3.core.Single<PathT> findSkillMdPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Returns the path to the SKILL.md file for the given skill.

    * ### findResourcePath

protected abstract io.reactivex.rxjava3.core.Single<PathT> findResourcePath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)

Returns the path to the resource for the given skill.

    * ### openChannel

protected abstract [ReadableByteChannel](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/channels/ReadableByteChannel.html "interface in java.nio.channels") openChannel(PathT path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Opens a [`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") for reading the content of the given path.

Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")`




* * *

Copyright (C) 1980\. All rights reserved.
