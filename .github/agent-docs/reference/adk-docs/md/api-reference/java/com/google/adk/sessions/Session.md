JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Session.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.sessions](package-summary.html)
  2. [Session](Session.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
     1. Methods inherited from class JsonBaseModel
     2. Methods inherited from class Object
  4. Method Details
     1. builder(String)
     2. builder(SessionKey)
     3. sessionKey()
     4. id()
     5. state()
     6. events()
     7. immutableEvents()
     8. addEvent(Event)
     9. addEvents(Collection)
     10. appName()
     11. userId()
     12. lastUpdateTime(Instant)
     13. lastUpdateTime()
     14. getLastUpdateTimeAsDouble()
     15. toString()
     16. fromJson(String)

Hide sidebar  Show sidebar

# Class Session

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.sessions.Session

* * *

public final class Session extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

A [`Session`](Session.html "class in com.google.adk.sessions") object that encapsulates the [`State`](State.html "class in com.google.adk.sessions") and [`Event`](../events/Event.html "class in com.google.adk.events")s of a session.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

Builder for [`Session`](Session.html "class in com.google.adk.sessions").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`void`

`addEvent([Event](../events/Event.html "class in com.google.adk.events") event)`

Appends a single [`Event`](../events/Event.html "class in com.google.adk.events") to the session's event list while synchronizing on the backing `events()` list; prefer over `events().add(event)`.

`void`

`addEvents([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

Appends all [`Event`](../events/Event.html "class in com.google.adk.events")s in the given collection to the session's event list while synchronizing on the backing `events()` list; prefer over ` events().addAll(events)`.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`appName()`

 

`static [Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`builder([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new [`Session.Builder`](Session.Builder.html "class in com.google.adk.sessions") with the given session key.

`static [Session.Builder](Session.Builder.html "class in com.google.adk.sessions")`

`builder([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)`

 

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")>`

`events()`

Deprecated.

Prefer `immutableEvents()` when reading or iterating over events (to avoid [`ConcurrentModificationException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ConcurrentModificationException.html "class in java.util")), and `addEvent(Event)` or `addEvents(Collection)` when appending events.

`static [Session](Session.html "class in com.google.adk.sessions")`

`fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)`

 

`double`

`getLastUpdateTimeAsDouble()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`id()`

 

`com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>`

`immutableEvents()`

Returns a thread-safe, immutable snapshot of the session's events, synchronizing on the backing `events()` list.

`[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")`

`lastUpdateTime()`

 

`void`

`lastUpdateTime([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") lastUpdateTime)`

 

`[SessionKey](SessionKey.html "class in com.google.adk.sessions")`

`sessionKey()`

Returns the session key.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`state()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`userId()`

 

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### builder

public static [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") builder([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id)

    * ### builder

public static [Session.Builder](Session.Builder.html "class in com.google.adk.sessions") builder([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)

Creates a new [`Session.Builder`](Session.Builder.html "class in com.google.adk.sessions") with the given session key.

    * ### sessionKey

public [SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey()

Returns the session key.

    * ### id

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") id()

    * ### state

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state()

    * ### events

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events()

Deprecated.

Prefer `immutableEvents()` when reading or iterating over events (to avoid [`ConcurrentModificationException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ConcurrentModificationException.html "class in java.util")), and `addEvent(Event)` or `addEvents(Collection)` when appending events.

Returns the mutable list of events backing this session, which also serves as the monitor for all event-helper synchronization.

    * ### immutableEvents

public com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")> immutableEvents()

Returns a thread-safe, immutable snapshot of the session's events, synchronizing on the backing `events()` list. Use this method whenever reading, iterating, streaming, filtering, or slicing ([`List.subList(int, int)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList\(int,int\))) session events to avoid [`ConcurrentModificationException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ConcurrentModificationException.html "class in java.util") under concurrent modifications.

    * ### addEvent

public void addEvent([Event](../events/Event.html "class in com.google.adk.events") event)

Appends a single [`Event`](../events/Event.html "class in com.google.adk.events") to the session's event list while synchronizing on the backing `events()` list; prefer over `events().add(event)`.

    * ### addEvents

public void addEvents([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

Appends all [`Event`](../events/Event.html "class in com.google.adk.events")s in the given collection to the session's event list while synchronizing on the backing `events()` list; prefer over ` events().addAll(events)`.

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName()

    * ### userId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId()

    * ### lastUpdateTime

public void lastUpdateTime([Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") lastUpdateTime)

    * ### lastUpdateTime

public [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") lastUpdateTime()

    * ### getLastUpdateTimeAsDouble

public double getLastUpdateTimeAsDouble()

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`

    * ### fromJson

public static [Session](Session.html "class in com.google.adk.sessions") fromJson([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") json)




* * *

Copyright (C) 1980\. All rights reserved.
