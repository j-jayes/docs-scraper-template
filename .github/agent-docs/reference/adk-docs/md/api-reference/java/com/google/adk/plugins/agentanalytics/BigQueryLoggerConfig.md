JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQueryLoggerConfig](BigQueryLoggerConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. BigQueryLoggerConfig()
  6. Method Details
     1. enabled()
     2. eventAllowlist()
     3. eventDenylist()
     4. maxContentLength()
     5. location()
     6. projectId()
     7. datasetId()
     8. tableName()
     9. clusteringFields()
     10. logMultiModalContent()
     11. retryConfig()
     12. batchSize()
     13. batchFlushInterval()
     14. shutdownTimeout()
     15. queueMaxSize()
     16. contentFormatter()
     17. gcsBucketName()
     18. connectionId()
     19. logSessionMetadata()
     20. customTags()
     21. autoSchemaUpgrade()
     22. createViews()
     23. viewPrefix()
     24. credentials()
     25. toBuilder()
     26. builder()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig

* * *

public abstract class BigQueryLoggerConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration for the BigQueryAgentAnalyticsPlugin.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

Builder for [`BigQueryLoggerConfig`](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics").

`static class `

`[BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics")`

Retry configuration for BigQuery writes.

  * ## Constructor Summary

Constructors

Constructor

Description

`BigQueryLoggerConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract boolean`

`autoSchemaUpgrade()`

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`batchFlushInterval()`

 

`abstract int`

`batchSize()`

 

`static [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`builder()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`clusteringFields()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`connectionId()`

 

`abstract @Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`contentFormatter()`

Optional custom formatter for content.

`abstract boolean`

`createViews()`

 

`abstract @Nullable com.google.auth.Credentials`

`credentials()`

 

`abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`customTags()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`datasetId()`

 

`abstract boolean`

`enabled()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`eventAllowlist()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`eventDenylist()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`gcsBucketName()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`location()`

 

`abstract boolean`

`logMultiModalContent()`

 

`abstract boolean`

`logSessionMetadata()`

 

`abstract int`

`maxContentLength()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`projectId()`

 

`abstract int`

`queueMaxSize()`

 

`abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics")`

`retryConfig()`

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`shutdownTimeout()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`tableName()`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`toBuilder()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`viewPrefix()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### BigQueryLoggerConfig

public BigQueryLoggerConfig()

  * ## Method Details

    * ### enabled

public abstract boolean enabled()

    * ### eventAllowlist

public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventAllowlist()

    * ### eventDenylist

public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventDenylist()

    * ### maxContentLength

public abstract int maxContentLength()

    * ### location

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") location()

    * ### projectId

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") projectId()

    * ### datasetId

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") datasetId()

    * ### tableName

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") tableName()

    * ### clusteringFields

public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> clusteringFields()

    * ### logMultiModalContent

public abstract boolean logMultiModalContent()

    * ### retryConfig

public abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig()

    * ### batchSize

public abstract int batchSize()

    * ### batchFlushInterval

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") batchFlushInterval()

    * ### shutdownTimeout

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") shutdownTimeout()

    * ### queueMaxSize

public abstract int queueMaxSize()

    * ### contentFormatter

public abstract @Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> contentFormatter()

Optional custom formatter for content. 

Allow plugins to modify the content before logging. This is useful for masking sensitive data, formatting content, etc. 

The contentFormatter must be **thread-safe** as it may be called concurrently across different agent invocations and **fast/non-blocking** to avoid adding latency to the agent's event processing pipeline. 

**Important:** To avoid corruption of the logs, the incoming content object should **not** be mutated. Modifying code should return a **new copy** of the object with desired changes.

    * ### gcsBucketName

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") gcsBucketName()

    * ### connectionId

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> connectionId()

    * ### logSessionMetadata

public abstract boolean logSessionMetadata()

    * ### customTags

public abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> customTags()

    * ### autoSchemaUpgrade

public abstract boolean autoSchemaUpgrade()

    * ### createViews

public abstract boolean createViews()

    * ### viewPrefix

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") viewPrefix()

    * ### credentials

public abstract @Nullable com.google.auth.Credentials credentials()

    * ### toBuilder

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") toBuilder()

    * ### builder

public static [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") builder()




* * *

Copyright (C) 1980\. All rights reserved.
