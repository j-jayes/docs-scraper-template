JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ConfigMapper.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models.springai](package-summary.html)
  2. [ConfigMapper](ConfigMapper.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ConfigMapper()
  5. Method Details
     1. toSpringAiChatOptions(Optional)
     2. createDefaultChatOptions()
     3. isConfigurationValid(Optional)

Hide sidebar  Show sidebar

# Class ConfigMapper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.ConfigMapper

* * *

public class ConfigMapper extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Maps ADK GenerateContentConfig to Spring AI ChatOptions. 

This mapper handles the translation between ADK's GenerateContentConfig and Spring AI's ChatOptions, enabling configuration parameters like temperature, max tokens, and stop sequences to be passed through to Spring AI models.

  * ## Constructor Summary

Constructors

Constructor

Description

`ConfigMapper()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`org.springframework.ai.chat.prompt.ChatOptions`

`createDefaultChatOptions()`

Creates default ChatOptions for cases where no ADK config is provided.

`boolean`

`isConfigurationValid([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config)`

Validates that the configuration is compatible with Spring AI.

`org.springframework.ai.chat.prompt.ChatOptions`

`toSpringAiChatOptions([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config)`

Converts ADK GenerateContentConfig to Spring AI ChatOptions.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ConfigMapper

public ConfigMapper()

  * ## Method Details

    * ### toSpringAiChatOptions

public org.springframework.ai.chat.prompt.ChatOptions toSpringAiChatOptions([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config)

Converts ADK GenerateContentConfig to Spring AI ChatOptions.

Parameters:
    `config` \- The ADK configuration to convert
Returns:
    Spring AI ChatOptions or null if no config provided

    * ### createDefaultChatOptions

public org.springframework.ai.chat.prompt.ChatOptions createDefaultChatOptions()

Creates default ChatOptions for cases where no ADK config is provided.

Returns:
    Basic ChatOptions with reasonable defaults

    * ### isConfigurationValid

public boolean isConfigurationValid([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.GenerateContentConfig> config)

Validates that the configuration is compatible with Spring AI.

Parameters:
    `config` \- The ADK configuration to validate
Returns:
    true if configuration is valid and supported




* * *

Copyright (C) 1980\. All rights reserved.
