JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ReplanPolicy.Ignore.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [ReplanPolicy](ReplanPolicy.html)
  3. [Ignore](ReplanPolicy.Ignore.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Ignore()
  6. Method Details
     1. toString()
     2. hashCode()
     3. equals(Object)

Hide sidebar  Show sidebar

# Record Class ReplanPolicy.Ignore

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")

com.google.adk.planner.goap.ReplanPolicy.Ignore

All Implemented Interfaces:
    `[ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap")`

Enclosing interface:
    `[ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap")`

* * *

public static record ReplanPolicy.Ignore() extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang") implements [ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap")

Ignore failures and proceed with the remaining plan as-is.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [ReplanPolicy](ReplanPolicy.html#nested-class-summary "interface in com.google.adk.planner.goap")

`[ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap"), [ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")`

Modifier and Type

Interface

Description

`static final record `

`[ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap")`

Stop immediately on failure with an error message.

`static final record `

`[ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap")`

Ignore failures and proceed with the remaining plan as-is.

`static final record `

`[ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")`

Attempt to recompute the remaining plan from current world state.

  * ## Constructor Summary

Constructors

Constructor

Description

`Ignore()`

Creates an instance of a `Ignore` record class.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`final boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)`

Indicates whether some other object is "equal to" this one.

`final int`

`hashCode()`

Returns a hash code value for this object.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

Returns a string representation of this record class.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Ignore

public Ignore()

Creates an instance of a `Ignore` record class.

  * ## Method Details

    * ### toString

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#toString\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a string representation of this object

    * ### hashCode

public final int hashCode()

Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#hashCode\(\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Returns:
    a hash code value for this object

    * ### equals

public final boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") o)

Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. 

Specified by:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#equals\(java.lang.Object\))` in class `[Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class in java.lang")`
Parameters:
    `o` \- the object with which to compare
Returns:
    `true` if this object is the same as the `o` argument; `false` otherwise.




* * *

Copyright (C) 1980\. All rights reserved.
