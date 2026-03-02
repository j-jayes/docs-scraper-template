JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/WebMojo.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.maven](package-summary.html)
  2. [WebMojo](WebMojo.html)



Contents 

  1. Description
     1. Basic Usage
     2. Configuration Parameters
     3. AgentLoader Implementation
     4. Web Interface
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. WebMojo()
  6. Method Details
     1. execute()

Hide sidebar  Show sidebar

# Class WebMojo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

org.apache.maven.plugin.AbstractMojo 

com.google.adk.maven.WebMojo

All Implemented Interfaces:
    `org.apache.maven.plugin.ContextEnabled, org.apache.maven.plugin.Mojo`

* * *

@Mojo(name="web", requiresDependencyResolution=RUNTIME) @Execute(phase=COMPILE) public class WebMojo extends org.apache.maven.plugin.AbstractMojo

Maven plugin goal that starts the Google ADK Web Server with user-provided agents. 

This Mojo provides a convenient way for developers to test and interact with their agents through ADK Web UI. The plugin dynamically loads user-defined agents and makes them available through a browser interface. 

## Basic Usage
    
    
    mvn google-adk:web -Dagents=com.example.MyAgentLoader
    

## Configuration Parameters

  * **agents** (required) - Full class path to AgentLoader implementation 
  * **port** (optional, default: 8000) - Server port 
  * **host** (optional, default: localhost) - Server host address 
  * **hotReloading** (optional, default: true) - Enable hot reloading for config-based agents 
  * **registry** (optional) - Full class path to custom ComponentRegistry subclass for injecting customized tools and agents 


## AgentLoader Implementation

The agents parameter should point to a class that implements [`AgentLoader`](../web/AgentLoader.html "interface in com.google.adk.web"). It can reference either: 

  * A static field: `com.example.MyProvider.INSTANCE`
  * A class with default constructor: `com.example.MyProvider` 


## Web Interface

Once started, ADK Web UI is available at `http://host:port` where users can interact with available agents.

Author:
    Google ADK Team

  * ## Field Summary

### Fields inherited from interface org.apache.maven.plugin.Mojo

`ROLE`

  * ## Constructor Summary

Constructors

Constructor

Description

`WebMojo()`

 

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

    * ### WebMojo

public WebMojo()

  * ## Method Details

    * ### execute

public void execute() throws org.apache.maven.plugin.MojoExecutionException, org.apache.maven.plugin.MojoFailureException

Throws:
    `org.apache.maven.plugin.MojoExecutionException`
    `org.apache.maven.plugin.MojoFailureException`




* * *

Copyright (C) 1980\. All rights reserved.
