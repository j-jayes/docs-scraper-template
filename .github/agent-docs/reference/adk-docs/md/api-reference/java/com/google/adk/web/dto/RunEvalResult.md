JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RunEvalResult.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.web.dto](package-summary.html)
  2. [RunEvalResult](RunEvalResult.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. appName
     2. evalSetId
     3. evalId
     4. finalEvalStatus
     5. evalMetricResults
     6. sessionId
  6. Constructor Details
     1. RunEvalResult(String, String, String, String, List, String)
     2. RunEvalResult()

Hide sidebar  Show sidebar

# Class RunEvalResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")

com.google.adk.web.dto.RunEvalResult

* * *

public class RunEvalResult extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval. Contains the results of an evaluation run.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`appName`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`evalId`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`evalMetricResults`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`evalSetId`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`finalEvalStatus`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`sessionId`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`RunEvalResult()`

 

`RunEvalResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalSetId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") finalEvalStatus, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> evalMetricResults, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Constructs a RunEvalResult.

  * ## Method Summary

### Methods inherited from class [JsonBaseModel](../../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName

    * ### evalSetId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalSetId

    * ### evalId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalId

    * ### finalEvalStatus

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") finalEvalStatus

    * ### evalMetricResults

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> evalMetricResults

    * ### sessionId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId

  * ## Constructor Details

    * ### RunEvalResult

public RunEvalResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalSetId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") evalId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") finalEvalStatus, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> evalMetricResults, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Constructs a RunEvalResult.

Parameters:
    `appName` \- The application name.
    `evalSetId` \- The evaluation set ID.
    `evalId` \- The evaluation ID.
    `finalEvalStatus` \- The final status of the evaluation.
    `evalMetricResults` \- The results for each metric.
    `sessionId` \- The session ID associated with the evaluation.

    * ### RunEvalResult

public RunEvalResult()




* * *

Copyright (C) 1980\. All rights reserved.
