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
     2. enabled(boolean)
     3. setEventAllowlist(List)
     4. eventAllowlist(List)
     5. setEventDenylist(List)
     6. eventDenylist(List)
     7. setMaxContentLength(int)
     8. maxContentLength(int)
     9. setProjectId(String)
     10. projectId(String)
     11. setDatasetId(String)
     12. datasetId(String)
     13. setTableName(String)
     14. tableName(String)
     15. setClusteringFields(List)
     16. clusteringFields(List)
     17. setLogMultiModalContent(boolean)
     18. logMultiModalContent(boolean)
     19. setRetryConfig(BigQueryLoggerConfig.RetryConfig)
     20. retryConfig(BigQueryLoggerConfig.RetryConfig)
     21. setBatchSize(int)
     22. batchSize(int)
     23. setBatchFlushInterval(Duration)
     24. batchFlushInterval(Duration)
     25. setShutdownTimeout(Duration)
     26. shutdownTimeout(Duration)
     27. setQueueMaxSize(int)
     28. queueMaxSize(int)
     29. setContentFormatter(BiFunction)
     30. contentFormatter(BiFunction)
     31. setConnectionId(String)
     32. connectionId(String)
     33. setLogSessionMetadata(boolean)
     34. logSessionMetadata(boolean)
     35. setCustomTags(Map)
     36. customTags(Map)
     37. setAutoSchemaUpgrade(boolean)
     38. autoSchemaUpgrade(boolean)
     39. setCredentials(Credentials)
     40. credentials(Credentials)
     41. build()

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

All MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`autoSchemaUpgrade(boolean autoSchemaUpgrade)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`batchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`batchSize(int batchSize)`

 

`abstract [BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

`build()`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`clusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`connectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`contentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`credentials(com.google.auth.Credentials credentials)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`customTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`datasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`enabled(boolean enabled)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`eventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`eventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`logMultiModalContent(boolean logMultiModalContent)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`logSessionMetadata(boolean logSessionMetadata)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`maxContentLength(int maxContentLength)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`projectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`queueMaxSize(int queueMaxSize)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`retryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)`

 

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setAutoSchemaUpgrade(boolean autoSchemaUpgrade)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setBatchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setBatchSize(int batchSize)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setClusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setConnectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setContentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setCredentials(com.google.auth.Credentials credentials)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setCustomTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setDatasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEnabled(boolean enabled)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setEventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setLogMultiModalContent(boolean logMultiModalContent)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setLogSessionMetadata(boolean logSessionMetadata)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setMaxContentLength(int maxContentLength)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setProjectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setQueueMaxSize(int queueMaxSize)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setRetryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setShutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)`

Deprecated.

`final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setTableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)`

Deprecated.

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`shutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`tableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setEnabled

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEnabled(boolean enabled)

Deprecated.

    * ### enabled

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") enabled(boolean enabled)

    * ### setEventAllowlist

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)

Deprecated.

    * ### eventAllowlist

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") eventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventAllowlist)

    * ### setEventDenylist

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setEventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)

Deprecated.

    * ### eventDenylist

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") eventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> eventDenylist)

    * ### setMaxContentLength

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setMaxContentLength(int maxContentLength)

Deprecated.

    * ### maxContentLength

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") maxContentLength(int maxContentLength)

    * ### setProjectId

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setProjectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)

Deprecated.

    * ### projectId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") projectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") projectId)

    * ### setDatasetId

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setDatasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)

Deprecated.

    * ### datasetId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") datasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") datasetId)

    * ### setTableName

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setTableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)

Deprecated.

    * ### tableName

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") tableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") tableName)

    * ### setClusteringFields

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setClusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)

Deprecated.

    * ### clusteringFields

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") clusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> clusteringFields)

    * ### setLogMultiModalContent

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setLogMultiModalContent(boolean logMultiModalContent)

Deprecated.

    * ### logMultiModalContent

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") logMultiModalContent(boolean logMultiModalContent)

    * ### setRetryConfig

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setRetryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)

Deprecated.

    * ### retryConfig

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") retryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)

    * ### setBatchSize

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setBatchSize(int batchSize)

Deprecated.

    * ### batchSize

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") batchSize(int batchSize)

    * ### setBatchFlushInterval

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setBatchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)

Deprecated.

    * ### batchFlushInterval

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") batchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") batchFlushInterval)

    * ### setShutdownTimeout

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setShutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)

Deprecated.

    * ### shutdownTimeout

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") shutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") shutdownTimeout)

    * ### setQueueMaxSize

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setQueueMaxSize(int queueMaxSize)

Deprecated.

    * ### queueMaxSize

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") queueMaxSize(int queueMaxSize)

    * ### setContentFormatter

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setContentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)

Deprecated.

    * ### contentFormatter

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") contentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "class or interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> contentFormatter)

    * ### setConnectionId

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setConnectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)

Deprecated.

    * ### connectionId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") connectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connectionId)

    * ### setLogSessionMetadata

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setLogSessionMetadata(boolean logSessionMetadata)

Deprecated.

    * ### logSessionMetadata

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") logSessionMetadata(boolean logSessionMetadata)

    * ### setCustomTags

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setCustomTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)

Deprecated.

    * ### customTags

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") customTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> customTags)

    * ### setAutoSchemaUpgrade

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setAutoSchemaUpgrade(boolean autoSchemaUpgrade)

Deprecated.

    * ### autoSchemaUpgrade

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") autoSchemaUpgrade(boolean autoSchemaUpgrade)

    * ### setCredentials

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") @CanIgnoreReturnValue public final [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setCredentials(com.google.auth.Credentials credentials)

Deprecated.

    * ### credentials

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") credentials(com.google.auth.Credentials credentials)

    * ### build

public abstract [BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") build()




* * *

Copyright (C) 1980\. All rights reserved.
