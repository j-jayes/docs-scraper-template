JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQueryLoggerConfig](BigQueryLoggerConfig.html)
  3. [Builder](BigQueryLoggerConfig.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. setEnabled(boolean)
     2. setEventAllowlist(List)
     3. setEventDenylist(List)
     4. setMaxContentLength(int)
     5. setProjectId(String)
     6. setDatasetId(String)
     7. setTableName(String)
     8. setClusteringFields(List)
     9. setLogMultiModalContent(boolean)
     10. setRetryConfig(BigQueryLoggerConfig.RetryConfig)
     11. setBatchSize(int)
     12. setBatchFlushInterval(Duration)
     13. setShutdownTimeout(Duration)
     14. setQueueMaxSize(int)
     15. setContentFormatter(BiFunction)
     16. setConnectionId(String)
     17. setLogSessionMetadata(boolean)
     18. setCustomTags(Map)
     19. setAutoSchemaUpgrade(boolean)
     20. setCredentials(Credentials)
     21. build()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder

Enclosing class:
    `[BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

* * *

public abstract static class BigQueryLoggerConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`BigQueryLoggerConfig`](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`abstract [BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

`build()`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setAutoSchemaUpgrade(boolean autoSchemaUpgrade)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setBatchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setBatchSize(int batchSize)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setClusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setConnectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setContentFormatter([BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setCredentials(com.google.auth.Credentials credentials)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setCustomTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setDatasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEnabled(boolean enabled)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEventAllowlist([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEventDenylist([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setLogMultiModalContent(boolean logMultiModalContent)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setLogSessionMetadata(boolean logSessionMetadata)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setMaxContentLength(int maxContentLength)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setProjectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setQueueMaxSize(int queueMaxSize)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setRetryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setShutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setTableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setEnabled

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEnabled(boolean enabled)

    * ### setEventAllowlist

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)

    * ### setEventDenylist

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)

    * ### setMaxContentLength

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setMaxContentLength(int maxContentLength)

    * ### setProjectId

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setProjectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)

    * ### setDatasetId

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setDatasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)

    * ### setTableName

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setTableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)

    * ### setClusteringFields

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setClusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)

    * ### setLogMultiModalContent

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setLogMultiModalContent(boolean logMultiModalContent)

    * ### setRetryConfig

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setRetryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)

    * ### setBatchSize

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setBatchSize(int batchSize)

    * ### setBatchFlushInterval

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setBatchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)

    * ### setShutdownTimeout

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setShutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)

    * ### setQueueMaxSize

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setQueueMaxSize(int queueMaxSize)

    * ### setContentFormatter

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setContentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)

    * ### setConnectionId

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setConnectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)

    * ### setLogSessionMetadata

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setLogSessionMetadata(boolean logSessionMetadata)

    * ### setCustomTags

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setCustomTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)

    * ### setAutoSchemaUpgrade

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setAutoSchemaUpgrade(boolean autoSchemaUpgrade)

    * ### setCredentials

public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setCredentials(com.google.auth.Credentials credentials)

    * ### build

public abstract [BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") build()




* * *

Copyright (C) 1980\. All rights reserved.
