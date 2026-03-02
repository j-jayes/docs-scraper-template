JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/HelpMojo.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.google_adk_maven_plugin](package-summary.html)
  2. [HelpMojo](HelpMojo.html)



Contents 

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. HelpMojo()
  6. Method Details
     1. execute()

Hide sidebar  Show sidebar

# Class HelpMojo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

org.apache.maven.plugin.AbstractMojo 

com.google.adk.google_adk_maven_plugin.HelpMojo

All Implemented Interfaces:
    `org.apache.maven.plugin.ContextEnabled, org.apache.maven.plugin.Mojo`

* * *

@Mojo(name="help", requiresProject=false, threadSafe=true) public class HelpMojo extends org.apache.maven.plugin.AbstractMojo

Display help information on google-adk-maven-plugin.  
Call `mvn google-adk:help -Ddetail=true -Dgoal=<goal-name>` to display parameter details.

Author:
    maven-plugin-tools

  * ## Field Summary

### Fields inherited from interface org.apache.maven.plugin.Mojo

`ROLE`

  * ## Constructor Summary

Constructors

Constructor

Description

`HelpMojo()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`execute()`

### Methods inherited from class org.apache.maven.plugin.AbstractMojo

`getLog, getPluginContext, setLog, setPluginContext`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### HelpMojo

public HelpMojo()

  * ## Method Details

    * ### execute

public void execute() throws org.apache.maven.plugin.MojoExecutionException

Throws:
    `org.apache.maven.plugin.MojoExecutionException`




* * *

Copyright (C) 1980\. All rights reserved.
