JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/PartConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [PartConverter](PartConverter.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. LANGUAGE_KEY
     2. OUTCOME_KEY
     3. CODE_KEY
     4. OUTPUT_KEY
     5. NAME_KEY
     6. ARGS_KEY
     7. RESPONSE_KEY
     8. ID_KEY
     9. WILL_CONTINUE_KEY
     10. PARTIAL_ARGS_KEY
     11. SCHEDULING_KEY
     12. PARTS_KEY
     13. A2A_DATA_PART_START_TAG
     14. A2A_DATA_PART_END_TAG
     15. A2A_DATA_PART_TEXT_MIME_TYPE
  5. Method Details
     1. toTextPart(Part)
     2. toGenaiPart(Part)
     3. toGenaiParts(List)
     4. messageToContent(Message)
     5. fromGenaiPart(Part, boolean)
     6. remoteCallAsUserPart(String, Part)

Hide sidebar  Show sidebar

# Class PartConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.a2a.converters.PartConverter

* * *

public final class PartConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for converting between Google GenAI Parts and A2A DataParts.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`A2A_DATA_PART_END_TAG`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`A2A_DATA_PART_START_TAG`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`A2A_DATA_PART_TEXT_MIME_TYPE`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`ARGS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`CODE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`ID_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`LANGUAGE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`NAME_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`OUTCOME_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`OUTPUT_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`PARTIAL_ARGS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`PARTS_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`RESPONSE_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`SCHEDULING_KEY`

 

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

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

`remoteCallAsUserPart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") author, com.google.genai.types.Part part)`

Converts a remote call part to a user part.

`static com.google.genai.types.Part`

`toGenaiPart(io.a2a.spec.Part<?> a2aPart)`

Convert an A2A JSON part into a Google GenAI part representation.

`static com.google.common.collect.ImmutableList<com.google.genai.types.Part>`

`toGenaiParts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<io.a2a.spec.Part<?>> a2aParts)`

 

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<io.a2a.spec.TextPart>`

`toTextPart(io.a2a.spec.Part<?> part)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### LANGUAGE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") LANGUAGE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.LANGUAGE_KEY)

    * ### OUTCOME_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") OUTCOME_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.OUTCOME_KEY)

    * ### CODE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") CODE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.CODE_KEY)

    * ### OUTPUT_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") OUTPUT_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.OUTPUT_KEY)

    * ### NAME_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") NAME_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.NAME_KEY)

    * ### ARGS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") ARGS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.ARGS_KEY)

    * ### RESPONSE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") RESPONSE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.RESPONSE_KEY)

    * ### ID_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") ID_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.ID_KEY)

    * ### WILL_CONTINUE_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") WILL_CONTINUE_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.WILL_CONTINUE_KEY)

    * ### PARTIAL_ARGS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") PARTIAL_ARGS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.PARTIAL_ARGS_KEY)

    * ### SCHEDULING_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") SCHEDULING_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.SCHEDULING_KEY)

    * ### PARTS_KEY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") PARTS_KEY

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.PARTS_KEY)

    * ### A2A_DATA_PART_START_TAG

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") A2A_DATA_PART_START_TAG

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_START_TAG)

    * ### A2A_DATA_PART_END_TAG

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") A2A_DATA_PART_END_TAG

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_END_TAG)

    * ### A2A_DATA_PART_TEXT_MIME_TYPE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") A2A_DATA_PART_TEXT_MIME_TYPE

See Also:
    
      * [Constant Field Values](../../../../../constant-values.html#com.google.adk.a2a.converters.PartConverter.A2A_DATA_PART_TEXT_MIME_TYPE)

  * ## Method Details

    * ### toTextPart

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<io.a2a.spec.TextPart> toTextPart(io.a2a.spec.Part<?> part)

    * ### toGenaiPart

public static com.google.genai.types.Part toGenaiPart(io.a2a.spec.Part<?> a2aPart)

Convert an A2A JSON part into a Google GenAI part representation.

    * ### toGenaiParts

public static com.google.common.collect.ImmutableList<com.google.genai.types.Part> toGenaiParts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<io.a2a.spec.Part<?>> a2aParts)

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

public static com.google.genai.types.Part remoteCallAsUserPart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") author, com.google.genai.types.Part part)

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
