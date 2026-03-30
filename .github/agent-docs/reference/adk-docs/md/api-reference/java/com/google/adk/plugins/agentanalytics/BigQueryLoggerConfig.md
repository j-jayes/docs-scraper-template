JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



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
     5. projectId()
     6. datasetId()
     7. tableName()
     8. clusteringFields()
     9. logMultiModalContent()
     10. retryConfig()
     11. batchSize()
     12. batchFlushInterval()
     13. shutdownTimeout()
     14. queueMaxSize()
     15. contentFormatter()
     16. connectionId()
     17. logSessionMetadata()
     18. customTags()
     19. autoSchemaUpgrade()
     20. credentials()
     21. builder()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig

* * *

public abstract class BigQueryLoggerConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`batchFlushInterval()`

 

`abstract int`

`batchSize()`

 

`static [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`builder()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`clusteringFields()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`connectionId()`

 

`abstract [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`contentFormatter()`

 

`abstract com.google.auth.Credentials`

`credentials()`

 

`abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`customTags()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`datasetId()`

 

`abstract boolean`

`enabled()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`eventAllowlist()`

 

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`eventDenylist()`

 

`abstract boolean`

`logMultiModalContent()`

 

`abstract boolean`

`logSessionMetadata()`

 

`abstract int`

`maxContentLength()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`projectId()`

 

`abstract int`

`queueMaxSize()`

 

`abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics")`

`retryConfig()`

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`shutdownTimeout()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`tableName()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BigQueryLoggerConfig

public BigQueryLoggerConfig()

  * ## Method Details

    * ### enabled

public abstract boolean enabled()

    * ### eventAllowlist

@Nullable public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist()

    * ### eventDenylist

@Nullable public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist()

    * ### maxContentLength

public abstract int maxContentLength()

    * ### projectId

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId()

    * ### datasetId

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId()

    * ### tableName

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName()

    * ### clusteringFields

public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields()

    * ### logMultiModalContent

public abstract boolean logMultiModalContent()

    * ### retryConfig

public abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig()

    * ### batchSize

public abstract int batchSize()

    * ### batchFlushInterval

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval()

    * ### shutdownTimeout

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout()

    * ### queueMaxSize

public abstract int queueMaxSize()

    * ### contentFormatter

@Nullable public abstract [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter()

    * ### connectionId

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> connectionId()

    * ### logSessionMetadata

public abstract boolean logSessionMetadata()

    * ### customTags

public abstract com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags()

    * ### autoSchemaUpgrade

public abstract boolean autoSchemaUpgrade()

    * ### credentials

@Nullable public abstract com.google.auth.Credentials credentials()

    * ### builder

public static [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") builder()




* * *

Copyright (C) 1980\. All rights reserved.
