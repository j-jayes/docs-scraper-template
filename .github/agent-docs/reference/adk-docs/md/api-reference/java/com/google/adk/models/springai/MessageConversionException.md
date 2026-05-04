JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/MessageConversionException.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai](package-summary.html)
  2. [MessageConversionException](MessageConversionException.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. MessageConversionException(String)
     2. MessageConversionException(String, Throwable)
     3. MessageConversionException(Throwable)
  5. Method Details
     1. jsonParsingFailed(String, Throwable)
     2. invalidMessageStructure(String)
     3. unsupportedContentType(String)

Hide sidebar  Show sidebar

# Class MessageConversionException

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang")

[java.lang.Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang")

[java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang")

com.google.adk.models.springai.MessageConversionException

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io")`

* * *

public class MessageConversionException extends [RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang")

Exception thrown when message conversion between ADK and Spring AI formats fails. 

This exception is thrown when there are issues converting between ADK's Content/Part format and Spring AI's Message/ChatResponse format, such as JSON parsing errors, invalid message structures, or unsupported content types.

See Also:
    

  * [Serialized Form](../../../../../serialized-form.html#com.google.adk.models.springai.MessageConversionException)



  * ## Constructor Summary

Constructors

Constructor

Description

`MessageConversionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message)`

Constructs a new MessageConversionException with the specified detail message.

`MessageConversionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)`

Constructs a new MessageConversionException with the specified detail message and cause.

`MessageConversionException([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)`

Constructs a new MessageConversionException with the specified cause.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai")`

`invalidMessageStructure([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message)`

Creates a MessageConversionException for invalid message structure.

`static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai")`

`jsonParsingFailed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") context, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)`

Creates a MessageConversionException for JSON parsing failures.

`static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai")`

`unsupportedContentType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") contentType)`

Creates a MessageConversionException for unsupported content type.

### Methods inherited from class [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#method-summary "class in java.lang")

`[addSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed\(java.lang.Throwable\) "addSuppressed\(Throwable\)"), [fillInStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace\(\) "fillInStackTrace\(\)"), [getCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause\(\) "getCause\(\)"), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage\(\) "getLocalizedMessage\(\)"), [getMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage\(\) "getMessage\(\)"), [getStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace\(\) "getStackTrace\(\)"), [getSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed\(\) "getSuppressed\(\)"), [initCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause\(java.lang.Throwable\) "initCause\(Throwable\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(\) "printStackTrace\(\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintStream\) "printStackTrace\(PrintStream\)"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintWriter\) "printStackTrace\(PrintWriter\)"), [setStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace\(java.lang.StackTraceElement%5B%5D\) "setStackTrace\(StackTraceElement\[\]\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString\(\) "toString\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### MessageConversionException

public MessageConversionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message)

Constructs a new MessageConversionException with the specified detail message.

Parameters:
    `message` \- the detail message

    * ### MessageConversionException

public MessageConversionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)

Constructs a new MessageConversionException with the specified detail message and cause.

Parameters:
    `message` \- the detail message
    `cause` \- the cause of the exception

    * ### MessageConversionException

public MessageConversionException([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)

Constructs a new MessageConversionException with the specified cause.

Parameters:
    `cause` \- the cause of the exception

  * ## Method Details

    * ### jsonParsingFailed

public static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai") jsonParsingFailed([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") context, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") cause)

Creates a MessageConversionException for JSON parsing failures.

Parameters:
    `context` \- the context where the parsing failed (e.g., "tool call arguments")
    `cause` \- the underlying JSON processing exception
Returns:
    a new MessageConversionException with appropriate message

    * ### invalidMessageStructure

public static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai") invalidMessageStructure([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") message)

Creates a MessageConversionException for invalid message structure.

Parameters:
    `message` \- description of the invalid structure
Returns:
    a new MessageConversionException

    * ### unsupportedContentType

public static [MessageConversionException](MessageConversionException.html "class in com.google.adk.models.springai") unsupportedContentType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") contentType)

Creates a MessageConversionException for unsupported content type.

Parameters:
    `contentType` \- the unsupported content type
Returns:
    a new MessageConversionException




* * *

Copyright (C) 1980\. All rights reserved.
