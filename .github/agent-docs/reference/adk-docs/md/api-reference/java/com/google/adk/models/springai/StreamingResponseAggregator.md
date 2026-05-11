JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/StreamingResponseAggregator.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai](package-summary.html)
  2. [StreamingResponseAggregator](StreamingResponseAggregator.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. StreamingResponseAggregator()
  5. Method Details
     1. processStreamingResponse(LlmResponse)
     2. getFinalResponse()
     3. reset()
     4. isEmpty()
     5. getAccumulatedTextLength()

Hide sidebar  Show sidebar

# Class StreamingResponseAggregator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.StreamingResponseAggregator

* * *

public class StreamingResponseAggregator extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Aggregates streaming responses from Spring AI models. 

This class helps manage the accumulation of partial responses in streaming mode, ensuring that text content is properly concatenated and tool calls are correctly handled. 

**Thread Safety:** This class is thread-safe. All public methods are synchronized to ensure safe concurrent access. The internal state is protected using a combination of thread-safe data structures and synchronization locks.

  * ## Constructor Summary

Constructors

Constructor

Description

`StreamingResponseAggregator()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`int`

`getAccumulatedTextLength()`

Returns the current accumulated text length.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`getFinalResponse()`

Returns the final aggregated response and resets the aggregator.

`boolean`

`isEmpty()`

Returns true if no content has been processed yet.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`processStreamingResponse([LlmResponse](../LlmResponse.html "class in com.google.adk.models") response)`

Processes a streaming LlmResponse and returns the current aggregated state.

`void`

`reset()`

Resets the aggregator for reuse.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### StreamingResponseAggregator

public StreamingResponseAggregator()

  * ## Method Details

    * ### processStreamingResponse

public [LlmResponse](../LlmResponse.html "class in com.google.adk.models") processStreamingResponse([LlmResponse](../LlmResponse.html "class in com.google.adk.models") response)

Processes a streaming LlmResponse and returns the current aggregated state.

Parameters:
    `response` \- The streaming response to process
Returns:
    The current aggregated LlmResponse

    * ### getFinalResponse

public [LlmResponse](../LlmResponse.html "class in com.google.adk.models") getFinalResponse()

Returns the final aggregated response and resets the aggregator.

Returns:
    The final complete response

    * ### reset

public void reset()

Resets the aggregator for reuse.

    * ### isEmpty

public boolean isEmpty()

Returns true if no content has been processed yet.

    * ### getAccumulatedTextLength

public int getAccumulatedTextLength()

Returns the current accumulated text length.




* * *

Copyright (C) 1980\. All rights reserved.
