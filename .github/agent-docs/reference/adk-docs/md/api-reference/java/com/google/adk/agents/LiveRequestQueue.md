JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LiveRequestQueue.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LiveRequestQueue](LiveRequestQueue.html)



Contents 

Hide sidebar ❮❯ Show sidebar

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



# Class LiveRequestQueue

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.LiveRequestQueue

* * *

public final class LiveRequestQueue extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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

Copyright (C) 2025\. All rights reserved.
