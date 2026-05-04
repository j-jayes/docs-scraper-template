JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ComponentRegistry.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [ComponentRegistry](ComponentRegistry.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ComponentRegistry()
  5. Method Details
     1. register(String, Object)
     2. get(String, Class)
     3. get(String)
     4. getInstance()
     5. setInstance(ComponentRegistry)
     6. resolveAgentInstance(String)
     7. resolveAgentClass(String)
     8. resolveToolsetInstance(String)
     9. resolveToolInstance(String)
     10. resolveToolClass(String)
     11. resolveToolsetClass(String)
     12. getToolNamesWithPrefix(String)
     13. resolveBeforeAgentCallback(String)
     14. resolveAfterAgentCallback(String)
     15. resolveBeforeModelCallback(String)
     16. resolveAfterModelCallback(String)
     17. resolveBeforeToolCallback(String)
     18. resolveAfterToolCallback(String)

Hide sidebar  Show sidebar

# Class ComponentRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.ComponentRegistry

Direct Known Subclasses:
    `[CustomDemoRegistry](../../../example/CustomDemoRegistry.html "class in com.example")`

* * *

public class ComponentRegistry extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

A registry for storing and retrieving ADK instances by name. 

This class provides a base registry with common ADK components and is designed to be extended by users who want to add their own pre-wired entries. The registry is fully thread-safe and supports storing any type of object. 

**Thread Safety:**

  * All instance methods are thread-safe due to the underlying ConcurrentHashMap 
  * The singleton instance access is thread-safe using volatile semantics 
  * The setInstance() method is synchronized to ensure atomic singleton replacement 


Base pre-wired entries include: 

  * "google_search" - GoogleSearchTool instance 
  * "code_execution" - BuiltInCodeExecutionTool instance 
  * "exit_loop" - ExitLoopTool instance 
  * "url_context" - UrlContextTool instance 
  * "google_maps_grounding" - GoogleMapsTool instance 


Example usage: 
    
    
    // Use the singleton instance
    ComponentRegistry registry = ComponentRegistry.getInstance();
    Optional<GoogleSearchTool> searchTool = registry.get("google_search", GoogleSearchTool.class);
    
    // Extend ComponentRegistry to add custom pre-wired entries
    public class MyComponentRegistry extends ComponentRegistry {
      public MyComponentRegistry() {
        super(); // Initialize base pre-wired entries
        register("my_custom_tool", new MyCustomTool());
        register("my_agent", new MyCustomAgent());
      }
    }
    
    // Replace the singleton with custom registry when server starts
    ComponentRegistry.setInstance(new MyComponentRegistry());
    

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`ComponentRegistry()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Retrieves an object by name without type checking.

`<T> [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<T>`

`get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> type)`

Retrieves an object by name and attempts to cast it to the specified type.

`static [ComponentRegistry](ComponentRegistry.html "class in com.google.adk.utils")`

`getInstance()`

Returns the global singleton instance of ComponentRegistry.

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getToolNamesWithPrefix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") prefix)`

 

`void`

`register([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)`

Registers an object with the given name.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterAgentCallback](../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")>`

`resolveAfterAgentCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterModelCallback](../agents/Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")>`

`resolveAfterModelCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterToolCallback](../agents/Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")>`

`resolveAfterToolCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>`

`resolveAgentClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClassName)`

Resolves the agent class based on the agent class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>`

`resolveAgentInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Resolves an agent instance from the registry.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeAgentCallback](../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")>`

`resolveBeforeAgentCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeModelCallback](../agents/Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")>`

`resolveBeforeModelCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeToolCallback](../agents/Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")>`

`resolveBeforeToolCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>>`

`resolveToolClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolClassName)`

Resolves the tool class based on the tool class name from the configuration.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`resolveToolInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`resolveToolsetClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolsetClassName)`

Resolves a toolset class by name from the registry or by attempting to load it.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>`

`resolveToolsetInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Resolves a toolset instance by name from the registry.

`static void`

`setInstance([ComponentRegistry](ComponentRegistry.html "class in com.google.adk.utils") newInstance)`

Updates the global singleton instance with a new ComponentRegistry.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ComponentRegistry

protected ComponentRegistry()

  * ## Method Details

    * ### register

public void register([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)

Registers an object with the given name. This can override pre-wired entries. 

This method is thread-safe due to the underlying ConcurrentHashMap.

Parameters:
    `name` \- the name to associate with the object
    `value` \- the object to register (can be an instance, class, function, etc.)
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if name is null or empty, or if value is null

    * ### get

public <T> [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<T> get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> type)

Retrieves an object by name and attempts to cast it to the specified type.

Type Parameters:
    `T` \- the type parameter
Parameters:
    `name` \- the name of the object to retrieve
    `type` \- the expected type of the object
Returns:
    an Optional containing the object if found and castable to the specified type, or an empty Optional otherwise

    * ### get

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Retrieves an object by name without type checking.

Parameters:
    `name` \- the name of the object to retrieve
Returns:
    an Optional containing the object if found, or an empty Optional otherwise

    * ### getInstance

public static [ComponentRegistry](ComponentRegistry.html "class in com.google.adk.utils") getInstance()

Returns the global singleton instance of ComponentRegistry.

Returns:
    the singleton ComponentRegistry instance

    * ### setInstance

public static void setInstance([ComponentRegistry](ComponentRegistry.html "class in com.google.adk.utils") newInstance)

Updates the global singleton instance with a new ComponentRegistry. This is useful for replacing the default registry with a custom one when the server starts. 

This method is thread-safe and ensures that all threads see the updated instance atomically.

Parameters:
    `newInstance` \- the new ComponentRegistry instance to use as the singleton
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if newInstance is null

    * ### resolveAgentInstance

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> resolveAgentInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Resolves an agent instance from the registry. 

This method looks up an agent in the ComponentRegistry by the given key. The registry should have been pre-populated with all available agents during initialization. 

The key can be any string that was used to register the agent, such as: 
      * A class name: "com.example.LifeAgent" 
      * A static field reference: "com.example.LifeAgent.INSTANCE" 
      * A simple name: "life_agent" 
      * Any custom key: "sub_agents_config.life_agent.agent" 

Parameters:
    `name` \- the registry key to look up
Returns:
    an Optional containing the BaseAgent if found, or empty if not found

    * ### resolveAgentClass

public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")> resolveAgentClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentClassName)

Resolves the agent class based on the agent class name from the configuration.

Parameters:
    `agentClassName` \- the name of the agent class from the config
Returns:
    the corresponding agent class
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if the agent class is not supported

    * ### resolveToolsetInstance

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")> resolveToolsetInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Resolves a toolset instance by name from the registry.

Parameters:
    `name` \- The name of the toolset instance to resolve.
Returns:
    An Optional containing the toolset instance if found, empty otherwise.

    * ### resolveToolInstance

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> resolveToolInstance([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveToolClass

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>> resolveToolClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolClassName)

Resolves the tool class based on the tool class name from the configuration.

Parameters:
    `toolClassName` \- the name of the tool class from the config
Returns:
    an Optional containing the tool class if found, empty otherwise

    * ### resolveToolsetClass

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>> resolveToolsetClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolsetClassName)

Resolves a toolset class by name from the registry or by attempting to load it. 

This method follows the same pattern as `resolveToolClass` but for BaseToolset implementations. It first checks the registry, then attempts direct class loading if the name contains a dot (indicating a fully qualified class name).

Parameters:
    `toolsetClassName` \- the name of the toolset class from the config
Returns:
    an Optional containing the toolset class if found, empty otherwise

    * ### getToolNamesWithPrefix

public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getToolNamesWithPrefix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") prefix)

    * ### resolveBeforeAgentCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeAgentCallback](../agents/Callbacks.BeforeAgentCallback.html "interface in com.google.adk.agents")> resolveBeforeAgentCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveAfterAgentCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterAgentCallback](../agents/Callbacks.AfterAgentCallback.html "interface in com.google.adk.agents")> resolveAfterAgentCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveBeforeModelCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeModelCallback](../agents/Callbacks.BeforeModelCallback.html "interface in com.google.adk.agents")> resolveBeforeModelCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveAfterModelCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterModelCallback](../agents/Callbacks.AfterModelCallback.html "interface in com.google.adk.agents")> resolveAfterModelCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveBeforeToolCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.BeforeToolCallback](../agents/Callbacks.BeforeToolCallback.html "interface in com.google.adk.agents")> resolveBeforeToolCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### resolveAfterToolCallback

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Callbacks.AfterToolCallback](../agents/Callbacks.AfterToolCallback.html "interface in com.google.adk.agents")> resolveAfterToolCallback([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)




* * *

Copyright (C) 1980\. All rights reserved.
