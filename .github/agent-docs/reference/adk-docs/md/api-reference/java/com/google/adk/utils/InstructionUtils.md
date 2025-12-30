JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InstructionUtils.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.utils](package-summary.html)
  2. [InstructionUtils](InstructionUtils.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. injectSessionState(InvocationContext, String)



# Class InstructionUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.utils.InstructionUtils

* * *

public final class InstructionUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility methods for handling instruction templates.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`injectSessionState([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") template)`

Populates placeholders in an instruction template string with values from the session state or loaded artifacts.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### injectSessionState

public static io.reactivex.rxjava3.core.Single<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> injectSessionState([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") context, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") template)

Populates placeholders in an instruction template string with values from the session state or loaded artifacts. 

**Placeholder Syntax:**

Placeholders are enclosed by one or more curly braces at the start and end, e.g., ` {key}` or `{{key}}`. The core `key` is extracted from whatever is between the innermost pair of braces after trimming whitespace and possibly removing the `?` which denotes optionality (e.g. `{key?}`). The `key` itself must not contain curly braces. For typical usage, a single pair of braces like `{my_variable}` is standard. 

The extracted `key` determines the source and name of the value: 
      * **Session State Variables:** The `key` (e.g., `"variable_name"` or ` "prefix:variable_name"`) refers to a variable in session state. 
        * Simple name: `{variable_name}`. The `variable_name` part must be a valid identifier as per `isValidStateName(String)`. Invalid names will result in the placeholder being returned as is. 
        * Prefixed name: `{prefix:variable_name}`. Valid prefixes are: ["app:"](../sessions/State.html#APP_PREFIX), ["user:"](../sessions/State.html#USER_PREFIX), and ["temp:"](../sessions/State.html#TEMP_PREFIX) The part of the name following the prefix must also be a valid identifier. Invalid prefixes will result in the placeholder being returned as is. 
      * **Artifacts:** The `key` starts with "`artifact.`" (e.g., ` "artifact.file_name"`). 
      * **Optional Placeholders:** A `key` can be marked as optional by appending a question mark `?` at its very end, inside the braces. 
        * Example: `{optional_variable?}`, `{{artifact.optional_file.txt?}}`
        * If an optional placeholder cannot be resolved (e.g., variable not found, artifact not found), it is replaced with an empty string.  **Example Usage:**
              
              InvocationContext context = ...; // Assume this is initialized with session and artifact service
               Session session = context.session();
              
               session.state().put("user:name", "Alice");
              
               context.artifactService().saveArtifact(
                   session.appName(), session.userId(), session.id(), "knowledge.txt", Part.fromText("Origins of the universe: At first, there was-"));
              
               String template = "You are {user:name}'s assistant. Answer questions based on your knowledge. Your knowledge: {artifact.knowledge.txt}." +
                                 " Your extra knowledge: {artifact.missing_artifact.txt?}";
              
               Single<String> populatedStringSingle = InstructionUtils.injectSessionState(context, template);
               populatedStringSingle.subscribe(
                   result -> System.out.println(result),
                   // Expected: "You are Alice's assistant. Answer questions based on your knowledge. Your knowledge: Origins of the universe: At first, there was-. Your extra knowledge: "
                   error -> System.err.println("Error populating template: " + error.getMessage())
               );
               

Parameters:
    `context` \- The invocation context providing access to session state and artifact services.
    `template` \- The instruction template string containing placeholders to be populated.
Returns:
    A `Single` that will emit the populated instruction string upon successful resolution of all non-optional placeholders. Emits the original template if it is empty or contains no placeholders that are processed.
Throws:
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if the template or context is null.
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if a non-optional variable or artifact is not found.




* * *

Copyright (C) 2025\. All rights reserved.
