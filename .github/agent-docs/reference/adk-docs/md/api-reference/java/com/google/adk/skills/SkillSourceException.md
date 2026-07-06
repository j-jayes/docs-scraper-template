JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SkillSourceException.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.skills](package-summary.html)
  2. [SkillSourceException](SkillSourceException.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. SKILL_LOAD_ERROR
     2. SKILL_NOT_FOUND
     3. SKILL_FORMAT_ERROR
     4. RESOURCE_LOAD_ERROR
     5. RESOURCE_NOT_FOUND
  6. Constructor Details
     1. SkillSourceException(String, String)
     2. SkillSourceException(String, String, Throwable)
  7. Method Details
     1. getErrorCode()

Hide sidebar  Show sidebar

# Class SkillSourceException

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang")

[java.lang.Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")

com.google.adk.skills.SkillSourceException

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io")`

* * *

public final class SkillSourceException extends [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")

Exception for [`SkillSource`](SkillSource.html "interface in com.google.adk.skills") implementations to signal recoverable errors that will have the message sending back to the LLM.

See Also:
    

  * [Serialized Form](../../../../serialized-form.html#com.google.adk.skills.SkillSourceException)



  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`RESOURCE_LOAD_ERROR`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`RESOURCE_NOT_FOUND`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`SKILL_FORMAT_ERROR`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`SKILL_LOAD_ERROR`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`SKILL_NOT_FOUND`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`SkillSourceException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorCode)`

Constructs a new exception with the specified detail message and error code.

`SkillSourceException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorCode, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)`

Constructs a new exception with the specified detail message, error code, and cause.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getErrorCode()`

Returns the error code categorizing the failure.

### Methods inherited from class [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#method-summary "class in java.lang")

`[addSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed\(java.lang.Throwable\) "addSuppressed\(Throwable\)"), [fillInStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace\(\) "fillInStackTrace\(\)"), [getCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause\(\) "getCause\(\)"), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage\(\) "getLocalizedMessage\(\)"), [getMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage\(\) "getMessage\(\)"), [getStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace\(\) "getStackTrace\(\)"), [getSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed\(\) "getSuppressed\(\)"), [initCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause\(java.lang.Throwable\) "initCause\(Throwable\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(\) "printStackTrace\(\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintStream\) "printStackTrace\(PrintStream\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintWriter\) "printStackTrace\(PrintWriter\)"), [setStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace\(java.lang.StackTraceElement%5B%5D\) "setStackTrace\(StackTraceElement\[\]\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString\(\) "toString\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### SKILL_LOAD_ERROR

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") SKILL_LOAD_ERROR

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.skills.SkillSourceException.SKILL_LOAD_ERROR)

    * ### SKILL_NOT_FOUND

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") SKILL_NOT_FOUND

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.skills.SkillSourceException.SKILL_NOT_FOUND)

    * ### SKILL_FORMAT_ERROR

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") SKILL_FORMAT_ERROR

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.skills.SkillSourceException.SKILL_FORMAT_ERROR)

    * ### RESOURCE_LOAD_ERROR

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") RESOURCE_LOAD_ERROR

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.skills.SkillSourceException.RESOURCE_LOAD_ERROR)

    * ### RESOURCE_NOT_FOUND

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") RESOURCE_NOT_FOUND

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.skills.SkillSourceException.RESOURCE_NOT_FOUND)

  * ## Constructor Details

    * ### SkillSourceException

public SkillSourceException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorCode)

Constructs a new exception with the specified detail message and error code.

Parameters:
    `message` \- The detail message.
    `errorCode` \- The specific error code categorizing the failure.

    * ### SkillSourceException

public SkillSourceException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") errorCode, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)

Constructs a new exception with the specified detail message, error code, and cause.

Parameters:
    `message` \- The detail message.
    `errorCode` \- The specific error code categorizing the failure.
    `cause` \- The cause.

  * ## Method Details

    * ### getErrorCode

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getErrorCode()

Returns the error code categorizing the failure.

Returns:
    The error code string.




* * *

Copyright (C) 1980\. All rights reserved.
