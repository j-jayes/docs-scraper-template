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
     3. A2A_DATA_PART_METADATA_IS_PARTIAL_KEY
     4. LANGUAGE_KEY
     5. OUTCOME_KEY
     6. CODE_KEY
     7. OUTPUT_KEY
     8. NAME_KEY
     9. ARGS_KEY
     10. RESPONSE_KEY
     11. ID_KEY
     12. WILL_CONTINUE_KEY
     13. PARTIAL_ARGS_KEY
     14. SCHEDULING_KEY
     15. PARTS_KEY
  5. Method Details
     1. toTextPart(Part)
     2. toGenaiPart(Part)
     3. toGenaiParts(List)
     4. messageToContent(Message)
     5. fromGenaiPart(Part, boolean)
     6. remoteCallAsUserPart(String, Part)

Hide sidebar  Show sidebar

# Class PartConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.converters.PartConverter

* * *

public final class PartConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for converting between Google GenAI Parts and A2A DataParts.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_IS_LONG_RUNNING_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_IS_PARTIAL_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`A2A_DATA_PART_METADATA_TYPE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`ARGS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`CODE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`ID_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`LANGUAGE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`NAME_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`OUTCOME_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`OUTPUT_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`PARTIAL_ARGS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`PARTS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`RESPONSE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`SCHEDULING_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`WILL_CONTINUE_KEY`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static io.a2a.spec.Part<?>`

`fromGenaiPart(com.google.genai.types.Part part, boolean isPartial)`

Convert a GenAI part into the A2A JSON representation.

`static com.google.genai.types.Content`

`messageToContent(io.a2a.spec.Message message)`

Converts an A2A Message to a Google GenAI Content object.

`static com.google.genai.types.Part`

`remoteCallAsUserPart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author, com.google.genai.types.Part part)`

Converts a remote call part to a user part.

`static com.google.genai.types.Part`

`toGenaiPart(io.a2a.spec.Part<?> a2aPart)`

Convert an A2A JSON part into a Google GenAI part representation.

`static com.google.common.collect.ImmutableList<com.google.genai.types.Part>`

`toGenaiParts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<io.a2a.spec.Part<?>> a2aParts)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.TextPart>`

`toTextPart(io.a2a.spec.Part<?> part)`

 

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

    * ### A2A_DATA_PART_METADATA_IS_PARTIAL_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") A2A_DATA_PART_METADATA_IS_PARTIAL_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_METADATA_IS_PARTIAL_KEY)

    * ### LANGUAGE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") LANGUAGE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.LANGUAGE_KEY)

    * ### OUTCOME_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") OUTCOME_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.OUTCOME_KEY)

    * ### CODE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") CODE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.CODE_KEY)

    * ### OUTPUT_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") OUTPUT_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.OUTPUT_KEY)

    * ### NAME_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") NAME_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.NAME_KEY)

    * ### ARGS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") ARGS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.ARGS_KEY)

    * ### RESPONSE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") RESPONSE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.RESPONSE_KEY)

    * ### ID_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") ID_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.ID_KEY)

    * ### WILL_CONTINUE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") WILL_CONTINUE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.WILL_CONTINUE_KEY)

    * ### PARTIAL_ARGS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") PARTIAL_ARGS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.PARTIAL_ARGS_KEY)

    * ### SCHEDULING_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") SCHEDULING_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.SCHEDULING_KEY)

    * ### PARTS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") PARTS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.PARTS_KEY)

  * ## Method Details

    * ### toTextPart

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<io.a2a.spec.TextPart> toTextPart(io.a2a.spec.Part<?> part)

    * ### toGenaiPart

public static com.google.genai.types.Part toGenaiPart(io.a2a.spec.Part<?> a2aPart)

Convert an A2A JSON part into a Google GenAI part representation.

    * ### toGenaiParts

public static com.google.common.collect.ImmutableList<com.google.genai.types.Part> toGenaiParts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<io.a2a.spec.Part<?>> a2aParts)

    * ### messageToContent

public static com.google.genai.types.Content messageToContent(io.a2a.spec.Message message)

Converts an A2A Message to a Google GenAI Content object.

Parameters:
    `message` \- The A2A Message to convert.
Returns:
    The converted Google GenAI Content object.

    * ### fromGenaiPart

public static io.a2a.spec.Part<?> fromGenaiPart(com.google.genai.types.Part part, boolean isPartial)

Convert a GenAI part into the A2A JSON representation.

    * ### remoteCallAsUserPart

public static com.google.genai.types.Part remoteCallAsUserPart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") author, com.google.genai.types.Part part)

Converts a remote call part to a user part. 

Events are rephrased as if a user was telling what happened in the session up to the point. E.g. 
          
          For context:
          User said: Now help me with Z
          Agent A said: Agent B can help you with it!
          Agent B said: Agent C might know better.*
          

Parameters:
    `author` \- The author of the part.
    `part` \- The part to convert.
Returns:
    The converted part.




* * *

Copyright (C) 1980\. All rights reserved.
