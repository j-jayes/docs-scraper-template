JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../ComputerState.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.computeruse](../package-summary.html)
  2. [ComputerState](../ComputerState.html)



# Uses of Class  
com.google.adk.tools.computeruse.ComputerState

Packages that use [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")

Package

Description

com.google.adk.tools.computeruse

 

  * ## Uses of [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse") in [com.google.adk.tools.computeruse](../package-summary.html)

Methods in [com.google.adk.tools.computeruse](../package-summary.html) that return [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")

Modifier and Type

Method

Description

`[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")`

ComputerState.Builder.`[build](../ComputerState.Builder.html#build\(\))()`

 

`static [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")`

ComputerState.`[create](../ComputerState.html#create\(byte%5B%5D\))(byte[] screenshot)`

 

`static [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")`

ComputerState.`[create](../ComputerState.html#create\(byte%5B%5D,java.lang.String\))(byte[] screenshot, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)`

 

Methods in [com.google.adk.tools.computeruse](../package-summary.html) that return types with arguments of type [ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[clickAt](../BaseComputer.html#clickAt\(int,int\))(int x, int y)`

Clicks at a specific x, y coordinate on the webpage.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[currentState](../BaseComputer.html#currentState\(\))()`

Returns current state.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[dragAndDrop](../BaseComputer.html#dragAndDrop\(int,int,int,int\))(int x, int y, int destinationX, int destinationY)`

Drag and drop.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[goBack](../BaseComputer.html#goBack\(\))()`

Navigates back.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[goForward](../BaseComputer.html#goForward\(\))()`

Navigates forward.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[hoverAt](../BaseComputer.html#hoverAt\(int,int\))(int x, int y)`

Hovers at a specific x, y coordinate on the webpage.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[keyCombination](../BaseComputer.html#keyCombination\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> keys)`

Presses key combination.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[navigate](../BaseComputer.html#navigate\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") url)`

Navigates to URL.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[openWebBrowser](../BaseComputer.html#openWebBrowser\(\))()`

Opens the web browser.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[scrollAt](../BaseComputer.html#scrollAt\(int,int,java.lang.String,int\))(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction, int magnitude)`

Scrolls at a specific x, y coordinate by magnitude.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[scrollDocument](../BaseComputer.html#scrollDocument\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") direction)`

Scrolls the entire webpage in a direction.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[search](../BaseComputer.html#search\(\))()`

Jumps to search.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[typeTextAt](../BaseComputer.html#typeTextAt\(int,int,java.lang.String,java.lang.Boolean,java.lang.Boolean\))(int x, int y, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") text, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") pressEnter, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") clearBeforeTyping)`

Types text at a specific x, y coordinate.

`io.reactivex.rxjava3.core.Single<[ComputerState](../ComputerState.html "class in com.google.adk.tools.computeruse")>`

BaseComputer.`[wait](../BaseComputer.html#wait\(java.time.Duration\))([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration)`

Waits for specified duration.




* * *

Copyright (C) 1980\. All rights reserved.
