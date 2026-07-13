JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ClassPathSkillSource.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [ClassPathSkillSource](ClassPathSkillSource.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ClassPathSkillSource(String)
     2. ClassPathSkillSource(String, ClassLoader)
  6. Method Details
     1. listResources(String, String)
     2. listSkills()
     3. findSkillMdPath(String)
     4. findResourcePath(String, String)
     5. openChannel(ClassPath.ResourceInfo)

Hide sidebar  Show sidebar

# Class ClassPathSkillSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.skills.AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>

com.google.adk.skills.ClassPathSkillSource

All Implemented Interfaces:
    `[SkillSource](SkillSource.html "interface in com.google.adk.skills")`

* * *

public final class ClassPathSkillSource extends [AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>

Loads skills from the classpath.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [AbstractSkillSource](AbstractSkillSource.html#nested-class-summary "class in com.google.adk.skills")

`[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<PathT>`

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

`ClassPathSkillSource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseResourcePath)`

Creates a new [`ClassPathSkillSource`](ClassPathSkillSource.html "class in com.google.adk.skills") that loads skills from the given base resource path using the current thread's context class loader.

`ClassPathSkillSource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseResourcePath, [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class in java.lang") classLoader)`

Creates a new [`ClassPathSkillSource`](ClassPathSkillSource.html "class in com.google.adk.skills") that loads skills from the given base resource path using the specified [`ClassLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class in java.lang").

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Single<com.google.common.reflect.ClassPath.ResourceInfo>`

`findResourcePath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)`

Returns the path to the resource for the given skill.

`protected io.reactivex.rxjava3.core.Single<com.google.common.reflect.ClassPath.ResourceInfo>`

`findSkillMdPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Returns the path to the SKILL.md file for the given skill.

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`listResources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)`

Lists all resource files for a specific skill within a given directory.

`protected io.reactivex.rxjava3.core.Flowable<[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>>`

`listSkills()`

Returns a `Flowable` of skills as a pair of skill name and the path to the SKILL.md file.

`protected [ReadableByteChannel](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/channels/ReadableByteChannel.html "interface in java.nio.channels")`

`openChannel(com.google.common.reflect.ClassPath.ResourceInfo path)`

Opens a [`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") for reading the content of the given path.

### Methods inherited from class [AbstractSkillSource](AbstractSkillSource.html#method-summary "class in com.google.adk.skills")

`[listFrontmatters](AbstractSkillSource.html#listFrontmatters\(\) "listFrontmatters\(\)"), [loadFrontmatter](AbstractSkillSource.html#loadFrontmatter\(java.lang.String\) "loadFrontmatter\(String\)"), [loadInstructions](AbstractSkillSource.html#loadInstructions\(java.lang.String\) "loadInstructions\(String\)"), [loadResource](AbstractSkillSource.html#loadResource\(java.lang.String,java.lang.String\) "loadResource\(String, String\)")`

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [Frontmatter](Frontmatter.html "class in com.google.adk.skills")>>`

`[listFrontmatters](AbstractSkillSource.html#listFrontmatters\(\))()`

Lists all available [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills")s for discovered skills.

`io.reactivex.rxjava3.core.Single<[Frontmatter](Frontmatter.html "class in com.google.adk.skills")>`

`[loadFrontmatter](AbstractSkillSource.html#loadFrontmatter\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the [`Frontmatter`](Frontmatter.html "class in com.google.adk.skills") for a specific skill.

`io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[loadInstructions](AbstractSkillSource.html#loadInstructions\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)`

Loads the instructions (body of SKILL.md) for a specific skill.

`io.reactivex.rxjava3.core.Single<com.google.common.io.ByteSource>`

`[loadResource](AbstractSkillSource.html#loadResource\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)`

Loads a specific resource file content.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ClassPathSkillSource

public ClassPathSkillSource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseResourcePath)

Creates a new [`ClassPathSkillSource`](ClassPathSkillSource.html "class in com.google.adk.skills") that loads skills from the given base resource path using the current thread's context class loader.

Parameters:
    `baseResourcePath` \- the base classpath path to scan for skills (e.g., "skills/")

    * ### ClassPathSkillSource

public ClassPathSkillSource([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseResourcePath, [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class in java.lang") classLoader)

Creates a new [`ClassPathSkillSource`](ClassPathSkillSource.html "class in com.google.adk.skills") that loads skills from the given base resource path using the specified [`ClassLoader`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html "class in java.lang").

Parameters:
    `baseResourcePath` \- the base classpath path to scan for skills
    `classLoader` \- the class loader to use for scanning resources

  * ## Method Details

    * ### listResources

public io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> listResources([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourceDirectory)

Description copied from interface: `[SkillSource](SkillSource.html#listResources\(java.lang.String,java.lang.String\))`

Lists all resource files for a specific skill within a given directory. 

If the skill or the resource directory does not exist, the returned `Single` will terminate with a [`SkillSourceException`](SkillSourceException.html "class in com.google.adk.skills").

Parameters:
    `skillName` \- the name of the skill
    `resourceDirectory` \- the relative directory within the skill to list (e.g., "assets", "scripts")
Returns:
    a `Single` emitting a list of resource paths relative to the skill directory

    * ### listSkills

protected io.reactivex.rxjava3.core.Flowable<[AbstractSkillSource.SkillMdPath](AbstractSkillSource.SkillMdPath.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>> listSkills()

Description copied from class: `[AbstractSkillSource](AbstractSkillSource.html#listSkills\(\))`

Returns a `Flowable` of skills as a pair of skill name and the path to the SKILL.md file.

Specified by:
    `[listSkills](AbstractSkillSource.html#listSkills\(\))` in class `[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>`

    * ### findSkillMdPath

protected io.reactivex.rxjava3.core.Single<com.google.common.reflect.ClassPath.ResourceInfo> findSkillMdPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName)

Description copied from class: `[AbstractSkillSource](AbstractSkillSource.html#findSkillMdPath\(java.lang.String\))`

Returns the path to the SKILL.md file for the given skill.

Specified by:
    `[findSkillMdPath](AbstractSkillSource.html#findSkillMdPath\(java.lang.String\))` in class `[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>`

    * ### findResourcePath

protected io.reactivex.rxjava3.core.Single<com.google.common.reflect.ClassPath.ResourceInfo> findResourcePath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") skillName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resourcePath)

Description copied from class: `[AbstractSkillSource](AbstractSkillSource.html#findResourcePath\(java.lang.String,java.lang.String\))`

Returns the path to the resource for the given skill.

Specified by:
    `[findResourcePath](AbstractSkillSource.html#findResourcePath\(java.lang.String,java.lang.String\))` in class `[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>`

    * ### openChannel

protected [ReadableByteChannel](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/channels/ReadableByteChannel.html "interface in java.nio.channels") openChannel(com.google.common.reflect.ClassPath.ResourceInfo path) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Description copied from class: `[AbstractSkillSource](AbstractSkillSource.html#openChannel\(PathT\))`

Opens a [`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class in java.io") for reading the content of the given path.

Specified by:
    `[openChannel](AbstractSkillSource.html#openChannel\(PathT\))` in class `[AbstractSkillSource](AbstractSkillSource.html "class in com.google.adk.skills")<com.google.common.reflect.ClassPath.ResourceInfo>`
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")`




* * *

Copyright (C) 1980\. All rights reserved.
