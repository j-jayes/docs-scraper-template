JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AdkWebCorsProperties.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.web.config](package-summary.html)
  2. [AdkWebCorsProperties](AdkWebCorsProperties.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AdkWebCorsProperties(String, List, List, List, boolean, long)
  5. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)
     4. mapping()
     5. origins()
     6. methods()
     7. headers()
     8. allowCredentials()
     9. maxAge()



# Record Class AdkWebCorsProperties

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

com.google.adk.web.config.AdkWebCorsProperties

* * *

@ConfigurationProperties(prefix="adk.web.cors") public record AdkWebCorsProperties([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") mapping, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> origins, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> methods, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> headers, boolean allowCredentials, long maxAge) extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

Properties for configuring CORS in ADK Web. This class is used to load CORS settings from application properties.

  * ## Constructor Summary

Constructors

Constructor

Description

`AdkWebCorsProperties([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") mapping, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> origins, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> methods, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> headers, boolean allowCredentials, long maxAge)`

Creates an instance of a `AdkWebCorsProperties` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`boolean`

`allowCredentials()`

Returns the value of the `allowCredentials` record component.

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`final int`

`hashCode()`

Returns a hash code value for this object.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`headers()`

Returns the value of the `headers` record component.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`mapping()`

Returns the value of the `mapping` record component.

`long`

`maxAge()`

Returns the value of the `maxAge` record component.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`methods()`

Returns the value of the `methods` record component.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`origins()`

Returns the value of the `origins` record component.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AdkWebCorsProperties

public AdkWebCorsProperties([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") mapping, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> origins, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> methods, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> headers, boolean allowCredentials, long maxAge)

Creates an instance of a `AdkWebCorsProperties` record class.

Parameters:
    `mapping` \- the value for the `mapping` record component
    `origins` \- the value for the `origins` record component
    `methods` \- the value for the `methods` record component
    `headers` \- the value for the `headers` record component
    `allowCredentials` \- the value for the `allowCredentials` record component
    `maxAge` \- the value for the `maxAge` record component

  * ## Method Details

    * ### toString

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. Reference components are compared with [`Objects::equals(Object,Object)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html#equals\(java.lang.Object,java.lang.Object\) "class or interface in java.util"); primitive components are compared with the `compare` method from their corresponding wrapper classes.

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.

    * ### mapping

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") mapping()

Returns the value of the `mapping` record component.

Returns:
    the value of the `mapping` record component

    * ### origins

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> origins()

Returns the value of the `origins` record component.

Returns:
    the value of the `origins` record component

    * ### methods

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> methods()

Returns the value of the `methods` record component.

Returns:
    the value of the `methods` record component

    * ### headers

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> headers()

Returns the value of the `headers` record component.

Returns:
    the value of the `headers` record component

    * ### allowCredentials

public boolean allowCredentials()

Returns the value of the `allowCredentials` record component.

Returns:
    the value of the `allowCredentials` record component

    * ### maxAge

public long maxAge()

Returns the value of the `maxAge` record component.

Returns:
    the value of the `maxAge` record component




* * *

Copyright (C) 2025\. All rights reserved.
