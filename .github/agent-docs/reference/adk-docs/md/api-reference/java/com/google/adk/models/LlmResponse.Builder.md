JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmResponse.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [LlmResponse](LlmResponse.html)
  3. [Builder](LlmResponse.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. content(Content)
     2. interrupted(Boolean)
     3. interrupted(Optional)
     4. groundingMetadata(GroundingMetadata)
     5. groundingMetadata(Optional)
     6. partial(Boolean)
     7. partial(Optional)
     8. turnComplete(Boolean)
     9. turnComplete(Optional)
     10. errorCode(FinishReason)
     11. errorCode(Optional)
     12. errorMessage(String)
     13. errorMessage(Optional)
     14. usageMetadata(GenerateContentResponseUsageMetadata)
     15. usageMetadata(Optional)
     16. response(GenerateContentResponse)
     17. build()



# Class LlmResponse.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.LlmResponse.Builder

Enclosing class:
    `[LlmResponse](LlmResponse.html "class in com.google.adk.models")`

* * *

public abstract static class LlmResponse.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for constructing [`LlmResponse`](LlmResponse.html "class in com.google.adk.models") instances.

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`[LlmResponse](LlmResponse.html "class in com.google.adk.models")`

`build()`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`content(com.google.genai.types.Content content)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorCode(com.google.genai.types.FinishReason errorCode)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorMessage)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`errorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`groundingMetadata(com.google.genai.types.GroundingMetadata groundingMetadata)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`groundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`interrupted([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") interrupted)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`interrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`partial([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") partial)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`partial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial)`

 

`final [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`response(com.google.genai.types.GenerateContentResponse response)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`turnComplete([Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") turnComplete)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`turnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`usageMetadata(com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)`

 

`abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models")`

`usageMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata> usageMetadata)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### content

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") content(com.google.genai.types.Content content)

    * ### interrupted

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") interrupted(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") interrupted)

    * ### interrupted

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") interrupted([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> interrupted)

    * ### groundingMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") groundingMetadata(@Nullable com.google.genai.types.GroundingMetadata groundingMetadata)

    * ### groundingMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") groundingMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GroundingMetadata> groundingMetadata)

    * ### partial

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") partial(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") partial)

    * ### partial

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") partial([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> partial)

    * ### turnComplete

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") turnComplete(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang") turnComplete)

    * ### turnComplete

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") turnComplete([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class or interface in java.lang")> turnComplete)

    * ### errorCode

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorCode(@Nullable com.google.genai.types.FinishReason errorCode)

    * ### errorCode

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorCode([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FinishReason> errorCode)

    * ### errorMessage

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorMessage(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorMessage)

    * ### errorMessage

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") errorMessage([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorMessage)

    * ### usageMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") usageMetadata(@Nullable com.google.genai.types.GenerateContentResponseUsageMetadata usageMetadata)

    * ### usageMetadata

public abstract [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") usageMetadata([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentResponseUsageMetadata> usageMetadata)

    * ### response

@CanIgnoreReturnValue public final [LlmResponse.Builder](LlmResponse.Builder.html "class in com.google.adk.models") response(com.google.genai.types.GenerateContentResponse response)

    * ### build

public [LlmResponse](LlmResponse.html "class in com.google.adk.models") build()




* * *

Copyright (C) 2025\. All rights reserved.
