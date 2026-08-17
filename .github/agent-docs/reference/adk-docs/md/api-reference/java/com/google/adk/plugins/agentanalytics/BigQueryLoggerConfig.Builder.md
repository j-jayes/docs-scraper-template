JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     1. enabled(boolean)
     2. eventAllowlist(List)
     3. eventDenylist(List)
     4. maxContentLength(int)
     5. location(String)
     6. projectId(String)
     7. datasetId(String)
     8. tableName(String)
     9. clusteringFields(List)
     10. logMultiModalContent(boolean)
     11. retryConfig(BigQueryLoggerConfig.RetryConfig)
     12. batchSize(int)
     13. batchFlushInterval(Duration)
     14. shutdownTimeout(Duration)
     15. queueMaxSize(int)
     16. contentFormatter(BiFunction)
     17. connectionId(String)
     18. logSessionMetadata(boolean)
     19. customTags(Map)
     20. autoSchemaUpgrade(boolean)
     21. createViews(boolean)
     22. viewPrefix(String)
     23. gcsBucketName(String)
     24. credentials(Credentials)
     25. build()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder

Enclosing class:
    `[BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

* * *

public abstract static class BigQueryLoggerConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`BigQueryLoggerConfig`](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics").

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

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`autoSchemaUpgrade(boolean autoSchemaUpgrade)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`batchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") batchFlushInterval)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`batchSize(int batchSize)`

 

`[BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

`build()`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`clusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> clusteringFields)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`connectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") connectionId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`contentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> contentFormatter)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`createViews(boolean createViews)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`credentials(com.google.auth.Credentials credentials)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`customTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> customTags)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`datasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") datasetId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`enabled(boolean enabled)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`eventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventAllowlist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`eventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventDenylist)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`gcsBucketName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") gcsBucketName)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`location([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") location)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`logMultiModalContent(boolean logMultiModalContent)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`logSessionMetadata(boolean logSessionMetadata)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`maxContentLength(int maxContentLength)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`projectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") projectId)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`queueMaxSize(int queueMaxSize)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`retryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`shutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") shutdownTimeout)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`tableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") tableName)`

 

`abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`viewPrefix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") viewPrefix)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### enabled

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") enabled(boolean enabled)

    * ### eventAllowlist

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") eventAllowlist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventAllowlist)

    * ### eventDenylist

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") eventDenylist(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> eventDenylist)

    * ### maxContentLength

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") maxContentLength(int maxContentLength)

    * ### location

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") location([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") location)

    * ### projectId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") projectId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") projectId)

    * ### datasetId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") datasetId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") datasetId)

    * ### tableName

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") tableName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") tableName)

    * ### clusteringFields

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") clusteringFields([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> clusteringFields)

    * ### logMultiModalContent

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") logMultiModalContent(boolean logMultiModalContent)

    * ### retryConfig

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") retryConfig([BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") retryConfig)

    * ### batchSize

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") batchSize(int batchSize)

    * ### batchFlushInterval

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") batchFlushInterval([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") batchFlushInterval)

    * ### shutdownTimeout

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") shutdownTimeout([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") shutdownTimeout)

    * ### queueMaxSize

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") queueMaxSize(int queueMaxSize)

    * ### contentFormatter

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") contentFormatter(@Nullable [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html "interface in java.util.function")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> contentFormatter)

    * ### connectionId

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") connectionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") connectionId)

    * ### logSessionMetadata

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") logSessionMetadata(boolean logSessionMetadata)

    * ### customTags

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") customTags([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> customTags)

    * ### autoSchemaUpgrade

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") autoSchemaUpgrade(boolean autoSchemaUpgrade)

    * ### createViews

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") createViews(boolean createViews)

    * ### viewPrefix

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") viewPrefix([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") viewPrefix)

    * ### gcsBucketName

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") gcsBucketName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") gcsBucketName)

    * ### credentials

@CanIgnoreReturnValue public abstract [BigQueryLoggerConfig.Builder](BigQueryLoggerConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") credentials(com.google.auth.Credentials credentials)

    * ### build

public [BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") build()




* * *

Copyright (C) 1980\. All rights reserved.
