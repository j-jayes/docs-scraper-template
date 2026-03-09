JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/PartConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [PartConverter](PartConverter.html)



Contents 

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. A2A_DATA_PART_METADATA_TYPE_KEY
     2. A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY
     3. A2A_DATA_PART_METADATA_TYPE_FUNCTION_CALL
     4. A2A_DATA_PART_METADATA_TYPE_FUNCTION_RESPONSE
     5. A2A_DATA_PART_METADATA_TYPE_CODE_EXECUTION_RESULT
     6. A2A_DATA_PART_METADATA_TYPE_EXECUTABLE_CODE
  5. Method Details
     1. toGenaiPart(Part)
     2. convertGenaiPartToA2aPart(Part)
     3. fromGenaiPart(Part)

Hide sidebar  Show sidebar

# Class PartConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.PartConverter

* * *

public final class PartConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for converting between Google GenAI Parts and A2A DataParts. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_CODE_EXECUTION_RESULT`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_EXECUTABLE_CODE`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_FUNCTION_CALL`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_FUNCTION_RESPONSE`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_KEY`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.DataPart>`

`convertGenaiPartToA2aPart(com.google.genai.types.Part part)`

Convert a Google GenAI Part to an A2A Part.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Part<?>>`

`fromGenaiPart(com.google.genai.types.Part part)`

Convert a GenAI part into the A2A JSON representation.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Part>`

`toGenaiPart(io.a2a.spec.Part<?> a2aPart)`

Convert an A2A JSON part into a Google GenAI part representation.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### A2A_DATA_PART_METADATA_TYPE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_TYPE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_TYPE_KEY)

    * ### A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY)

    * ### A2A_DATA_PART_METADATA_TYPE_FUNCTION_CALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_TYPE_FUNCTION_CALL

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_TYPE_FUNCTION_CALL)

    * ### A2A_DATA_PART_METADATA_TYPE_FUNCTION_RESPONSE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_TYPE_FUNCTION_RESPONSE

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_TYPE_FUNCTION_RESPONSE)

    * ### A2A_DATA_PART_METADATA_TYPE_CODE_EXECUTION_RESULT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_TYPE_CODE_EXECUTION_RESULT

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_TYPE_CODE_EXECUTION_RESULT)

    * ### A2A_DATA_PART_METADATA_TYPE_EXECUTABLE_CODE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_TYPE_EXECUTABLE_CODE

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_TYPE_EXECUTABLE_CODE)

  * ## Method Details

    * ### toGenaiPart

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Part> toGenaiPart(io.a2a.spec.Part<?> a2aPart)

Convert an A2A JSON part into a Google GenAI part representation.

    * ### convertGenaiPartToA2aPart

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.DataPart> convertGenaiPartToA2aPart(com.google.genai.types.Part part)

Convert a Google GenAI Part to an A2A Part.

Parameters:
    `part` \- The GenAI part to convert.
Returns:
    Optional containing the converted A2A Part, or empty if conversion fails.

    * ### fromGenaiPart

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.Part<?>> fromGenaiPart(com.google.genai.types.Part part)

Convert a GenAI part into the A2A JSON representation.




* * *

Copyright (C) 1980\. All rights reserved.
