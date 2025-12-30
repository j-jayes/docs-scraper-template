JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SessionNotFoundException.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [SessionNotFoundException](SessionNotFoundException.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SessionNotFoundException(String)
     2. SessionNotFoundException(String, Throwable)



# Class SessionNotFoundException

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang")

[java.lang.Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

[java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang")

[com.google.adk.sessions.SessionException](SessionException.html "class in com.google.adk.sessions")

com.google.adk.sessions.SessionNotFoundException

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")`

* * *

public class SessionNotFoundException extends [SessionException](SessionException.html "class in com.google.adk.sessions")

Indicates that a requested session could not be found.

See Also:
    

  * [Serialized Form](../../../../serialized-form.html#com.google.adk.sessions.SessionNotFoundException)



  * ## Constructor Summary

Constructors

Constructor

Description

`SessionNotFoundException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)`

 

`SessionNotFoundException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") cause)`

 

  * ## Method Summary

### Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang")

`[addSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed\(java.lang.Throwable\) "class or interface in java.lang"), [fillInStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace\(\) "class or interface in java.lang"), [getCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause\(\) "class or interface in java.lang"), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage\(\) "class or interface in java.lang"), [getMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage\(\) "class or interface in java.lang"), [getStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace\(\) "class or interface in java.lang"), [getSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed\(\) "class or interface in java.lang"), [initCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause\(java.lang.Throwable\) "class or interface in java.lang"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(\) "class or interface in java.lang"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintStream\) "class or interface in java.lang"), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace\(java.io.PrintWriter\) "class or interface in java.lang"), [setStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace\(java.lang.StackTraceElement%5B%5D\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString\(\) "class or interface in java.lang")`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SessionNotFoundException

public SessionNotFoundException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)

    * ### SessionNotFoundException

public SessionNotFoundException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") cause)




* * *

Copyright (C) 2025\. All rights reserved.
