JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQuerySchema.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQuerySchema](BigQuerySchema.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getEventsSchema()
     2. getArrowSchema()
     3. getSerializedArrowSchema()
     4. getDefaultClusteringFields()
     5. getEventsTableSchema()

Hide sidebar  Show sidebar

# Class BigQuerySchema

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.plugins.agentanalytics.BigQuerySchema

* * *

public final class BigQuerySchema extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility for defining the BigQuery events table schema.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static org.apache.arrow.vector.types.pojo.Schema`

`getArrowSchema()`

Returns the Arrow schema for the events table.

`static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getDefaultClusteringFields()`

Returns names of fields to cluster by default.

`static com.google.cloud.bigquery.Schema`

`getEventsSchema()`

Returns the BigQuery schema for the events table.

`static com.google.cloud.bigquery.storage.v1.TableSchema`

`getEventsTableSchema()`

Returns the BigQuery TableSchema for the events table (Storage Write API).

`static com.google.protobuf.ByteString`

`getSerializedArrowSchema()`

Returns the serialized Arrow schema for the events table.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### getEventsSchema

public static com.google.cloud.bigquery.Schema getEventsSchema()

Returns the BigQuery schema for the events table.

    * ### getArrowSchema

public static org.apache.arrow.vector.types.pojo.Schema getArrowSchema()

Returns the Arrow schema for the events table.

    * ### getSerializedArrowSchema

public static com.google.protobuf.ByteString getSerializedArrowSchema()

Returns the serialized Arrow schema for the events table.

    * ### getDefaultClusteringFields

public static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getDefaultClusteringFields()

Returns names of fields to cluster by default.

    * ### getEventsTableSchema

public static com.google.cloud.bigquery.storage.v1.TableSchema getEventsTableSchema()

Returns the BigQuery TableSchema for the events table (Storage Write API).




* * *

Copyright (C) 1980\. All rights reserved.
