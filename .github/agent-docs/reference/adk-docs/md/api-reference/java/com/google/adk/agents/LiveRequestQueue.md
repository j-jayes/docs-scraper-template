JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LiveRequestQueue.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LiveRequestQueue](LiveRequestQueue.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. LiveRequestQueue()
  5. Method Details
     1. close()
     2. content(Content)
     3. realtime(Blob)
     4. send(LiveRequest)
     5. get()

Hide sidebar  Show sidebar

# Class LiveRequestQueue

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.agents.LiveRequestQueue

* * *

public final class LiveRequestQueue extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

A queue of live requests to be sent to the model.

  * ## Constructor Summary

Constructors

Constructor

Description

`LiveRequestQueue()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

 

`void`

`content(com.google.genai.types.Content content)`

 

`io.reactivex.rxjava3.core.Flowable<[LiveRequest](LiveRequest.html "class in com.google.adk.agents")>`

`get()`

 

`void`

`realtime(com.google.genai.types.Blob blob)`

 

`void`

`send([LiveRequest](LiveRequest.html "class in com.google.adk.agents") request)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### LiveRequestQueue

public LiveRequestQueue()

  * ## Method Details

    * ### close

public void close()

    * ### content

public void content(com.google.genai.types.Content content)

    * ### realtime

public void realtime(com.google.genai.types.Blob blob)

    * ### send

public void send([LiveRequest](LiveRequest.html "class in com.google.adk.agents") request)

    * ### get

public io.reactivex.rxjava3.core.Flowable<[LiveRequest](LiveRequest.html "class in com.google.adk.agents")> get()




* * *

Copyright (C) 1980\. All rights reserved.
