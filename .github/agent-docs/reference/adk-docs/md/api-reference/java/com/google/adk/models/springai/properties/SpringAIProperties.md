JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIProperties.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.models.springai.properties](package-summary.html)
  2. [SpringAIProperties](SpringAIProperties.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SpringAIProperties()
  6. Method Details
     1. getModel()
     2. setModel(String)
     3. getTemperature()
     4. setTemperature(Double)
     5. getMaxTokens()
     6. setMaxTokens(Integer)
     7. getTopP()
     8. setTopP(Double)
     9. getTopK()
     10. setTopK(Integer)
     11. getValidation()
     12. setValidation(SpringAIProperties.Validation)
     13. getObservability()
     14. setObservability(SpringAIProperties.Observability)

Hide sidebar  Show sidebar

# Class SpringAIProperties

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.properties.SpringAIProperties

* * *

@ConfigurationProperties(prefix="adk.spring-ai") @Validated public class SpringAIProperties extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Configuration properties for Spring AI integration with ADK. 

These properties provide validation and default values for Spring AI model configurations used with the ADK SpringAI wrapper. 

Example configuration: 
    
    
    adk.spring-ai.temperature=0.7
    adk.spring-ai.max-tokens=2048
    adk.spring-ai.top-p=0.9
    adk.spring-ai.validation.enabled=true
    

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SpringAIProperties.Observability](SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties")`

Observability configuration settings.

`static class `

`[SpringAIProperties.Validation](SpringAIProperties.Validation.html "class in com.google.adk.models.springai.properties")`

Configuration validation settings.

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAIProperties()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`getMaxTokens()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getModel()`

 

`[SpringAIProperties.Observability](SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties")`

`getObservability()`

 

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang")`

`getTemperature()`

 

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")`

`getTopK()`

 

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang")`

`getTopP()`

 

`[SpringAIProperties.Validation](SpringAIProperties.Validation.html "class in com.google.adk.models.springai.properties")`

`getValidation()`

 

`void`

`setMaxTokens([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") maxTokens)`

 

`void`

`setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

`void`

`setObservability([SpringAIProperties.Observability](SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observability)`

 

`void`

`setTemperature([Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") temperature)`

 

`void`

`setTopK([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") topK)`

 

`void`

`setTopP([Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") topP)`

 

`void`

`setValidation([SpringAIProperties.Validation](SpringAIProperties.Validation.html "class in com.google.adk.models.springai.properties") validation)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SpringAIProperties

public SpringAIProperties()

  * ## Method Details

    * ### getModel

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getModel()

    * ### setModel

public void setModel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)

    * ### getTemperature

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") getTemperature()

    * ### setTemperature

public void setTemperature([Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") temperature)

    * ### getMaxTokens

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") getMaxTokens()

    * ### setMaxTokens

public void setMaxTokens([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") maxTokens)

    * ### getTopP

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") getTopP()

    * ### setTopP

public void setTopP([Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class or interface in java.lang") topP)

    * ### getTopK

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") getTopK()

    * ### setTopK

public void setTopK([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang") topK)

    * ### getValidation

public [SpringAIProperties.Validation](SpringAIProperties.Validation.html "class in com.google.adk.models.springai.properties") getValidation()

    * ### setValidation

public void setValidation([SpringAIProperties.Validation](SpringAIProperties.Validation.html "class in com.google.adk.models.springai.properties") validation)

    * ### getObservability

public [SpringAIProperties.Observability](SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") getObservability()

    * ### setObservability

public void setObservability([SpringAIProperties.Observability](SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observability)




* * *

Copyright (C) 1980\. All rights reserved.
