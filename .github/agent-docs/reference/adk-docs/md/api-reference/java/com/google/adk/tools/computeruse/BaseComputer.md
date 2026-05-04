JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BaseComputer.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.computeruse](package-summary.html)
  2. [BaseComputer](BaseComputer.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. screenSize()
     2. openWebBrowser()
     3. clickAt(int, int)
     4. hoverAt(int, int)
     5. typeTextAt(int, int, String, Boolean, Boolean)
     6. scrollDocument(String)
     7. scrollAt(int, int, String, int)
     8. wait(Duration)
     9. goBack()
     10. goForward()
     11. search()
     12. navigate(String)
     13. keyCombination(List)
     14. dragAndDrop(int, int, int, int)
     15. currentState()
     16. initialize()
     17. close()
     18. environment()

Hide sidebar  Show sidebar

# Interface BaseComputer

* * *

public interface BaseComputer

Defines an interface for computer environments. 

This interface defines the standard methods for controlling computer environments, including web browsers and other interactive systems.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`clickAt(int x, int y)`

Clicks at a specific x, y coordinate on the webpage.

`io.reactivex.rxjava3.core.Completable`

`close()`

Cleanup resources.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`currentState()`

Returns current state.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`dragAndDrop(int x, int y, int destinationX, int destinationY)`

Drag and drop.

`io.reactivex.rxjava3.core.Single<[ComputerEnvironment](ComputerEnvironment.html "enum class in com.google.adk.tools.computeruse")>`

`environment()`

Returns the environment.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`goBack()`

Navigates back.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`goForward()`

Navigates forward.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`hoverAt(int x, int y)`

Hovers at a specific x, y coordinate on the webpage.

`io.reactivex.rxjava3.core.Completable`

`initialize()`

Initialize the computer.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`keyCombination([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> keys)`

Presses key combination.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`navigate([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)`

Navigates to URL.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`openWebBrowser()`

Opens the web browser.

`io.reactivex.rxjava3.core.Single<int[]>`

`screenSize()`

Returns the screen size of the environment.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`scrollAt(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction, int magnitude)`

Scrolls at a specific x, y coordinate by magnitude.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`scrollDocument([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction)`

Scrolls the entire webpage in a direction.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`search()`

Jumps to search.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`typeTextAt(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") text, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") pressEnter, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") clearBeforeTyping)`

Types text at a specific x, y coordinate.

`io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")>`

`wait([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration)`

Waits for specified duration.




  * ## Method Details

    * ### screenSize

io.reactivex.rxjava3.core.Single<int[]> screenSize()

Returns the screen size of the environment.

    * ### openWebBrowser

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> openWebBrowser()

Opens the web browser.

    * ### clickAt

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> clickAt(int x, int y)

Clicks at a specific x, y coordinate on the webpage.

    * ### hoverAt

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> hoverAt(int x, int y)

Hovers at a specific x, y coordinate on the webpage.

    * ### typeTextAt

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> typeTextAt(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") text, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") pressEnter, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") clearBeforeTyping)

Types text at a specific x, y coordinate.

    * ### scrollDocument

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> scrollDocument([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction)

Scrolls the entire webpage in a direction.

    * ### scrollAt

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> scrollAt(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction, int magnitude)

Scrolls at a specific x, y coordinate by magnitude.

    * ### wait

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> wait([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration)

Waits for specified duration.

    * ### goBack

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> goBack()

Navigates back.

    * ### goForward

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> goForward()

Navigates forward.

    * ### search

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> search()

Jumps to search.

    * ### navigate

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> navigate([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)

Navigates to URL.

    * ### keyCombination

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> keyCombination([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> keys)

Presses key combination.

    * ### dragAndDrop

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> dragAndDrop(int x, int y, int destinationX, int destinationY)

Drag and drop.

    * ### currentState

io.reactivex.rxjava3.core.Single<[ComputerState](ComputerState.html "class in com.google.adk.tools.computeruse")> currentState()

Returns current state.

    * ### initialize

io.reactivex.rxjava3.core.Completable initialize()

Initialize the computer.

    * ### close

io.reactivex.rxjava3.core.Completable close()

Cleanup resources.

    * ### environment

io.reactivex.rxjava3.core.Single<[ComputerEnvironment](ComputerEnvironment.html "enum class in com.google.adk.tools.computeruse")> environment()

Returns the environment.




* * *

Copyright (C) 1980\. All rights reserved.
