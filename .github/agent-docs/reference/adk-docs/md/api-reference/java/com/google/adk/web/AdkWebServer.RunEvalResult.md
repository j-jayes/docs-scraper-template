JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkWebServer.RunEvalResult.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.web](package-summary.html)
  2. [AdkWebServer](AdkWebServer.html)
  3. [RunEvalResult](AdkWebServer.RunEvalResult.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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



# Class AdkWebServer.RunEvalResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.web.AdkWebServer.RunEvalResult

Enclosing class:
    `[AdkWebServer](AdkWebServer.html "class in com.google.adk.web")`

* * *

public static class AdkWebServer.RunEvalResult extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

DTO for the response of POST /apps/{appName}/eval_sets/{evalSetId}/run-eval. Contains the results of an evaluation run.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`appName`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`evalId`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`evalMetricResults`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`evalSetId`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`finalEvalStatus`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`sessionId`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`RunEvalResult()`

 

`RunEvalResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") finalEvalStatus, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> evalMetricResults, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Constructs a RunEvalResult.

  * ## Method Summary

### Methods inherited from class com.google.adk.[JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\)), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\)), [getMapper](../JsonBaseModel.html#getMapper\(\)), [toJson](../JsonBaseModel.html#toJson\(\)), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\)), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName

    * ### evalSetId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId

    * ### evalId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalId

    * ### finalEvalStatus

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") finalEvalStatus

    * ### evalMetricResults

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> evalMetricResults

    * ### sessionId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId

  * ## Constructor Details

    * ### RunEvalResult

public RunEvalResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalSetId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") evalId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") finalEvalStatus, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> evalMetricResults, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

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

Copyright (C) 2025\. All rights reserved.
