[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AsyncQueue]()



# Class AsyncQueue<T>

A generic, single-consumer async queue that implements AsyncIterable, bridging a _push_ producer to a _pull_ consumer (`for await (const x of q)`).

Producers call push as values are produced and close (or fail) when finished. A single consumer drains the queue.

Semantics:

  * Buffered items are always delivered before an end/error signal.
  * close ends iteration cleanly (`done: true`); idempotent.
  * fail surfaces the error to the consumer _after_ any buffered items have been drained; it is sticky (first failure wins) and also closes the queue, so a later `close()` can't discard the error.
  * push after close/fail is ignored (the producer has already signalled completion).



#### Type Parameters

  * T



#### Implements

  * AsyncIterable<T>



  * Defined in [core/src/utils/async_queue.ts:23](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L23)



## Constructors

### constructor

  * new AsyncQueue<T>(): [AsyncQueue]()<T>

#### Type Parameters

    * T

#### Returns [AsyncQueue]()<T>




## Accessors

### isClosed

  * get isClosed(): boolean

Whether the queue has been closed or failed.

#### Returns boolean

    * Defined in [core/src/utils/async_queue.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L33)




### size

  * get size(): number

Number of items buffered and not yet consumed.

#### Returns number

    * Defined in [core/src/utils/async_queue.ts:38](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L38)




## Methods

### [asyncIterator]

  * "[asyncIterator]"(): AsyncIterator<T>

#### Returns AsyncIterator<T>

Implementation of AsyncIterable.[asyncIterator]

    * Defined in [core/src/utils/async_queue.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L87)




### close

  * close(): void

Signals that no more items will be produced. Any awaiting consumer receives `{done: true}`. Idempotent.

#### Returns void

    * Defined in [core/src/utils/async_queue.ts:79](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L79)




### error

  * error(err: unknown): void

#### Parameters

    * err: unknown

#### Returns void

#### Deprecated

Alias for fail; kept for existing callers.

    * Defined in [core/src/utils/async_queue.ts:71](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L71)




### fail

  * fail(error: unknown): void

Signals that production failed. Buffered items are still delivered first; once the buffer drains, the consumer's next `next()` rejects with `error`. Sticky (first failure wins) and closes the queue.

#### Parameters

    * error: unknown

#### Returns void

    * Defined in [core/src/utils/async_queue.ts:61](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L61)




### push

  * push(value: T): void

Enqueues a value. If a consumer is currently awaiting, it is resolved immediately; otherwise the value is buffered. No-op once closed/failed.

#### Parameters

    * value: T

#### Returns void

    * Defined in [core/src/utils/async_queue.ts:46](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/utils/async_queue.ts#L46)




Constructors

constructor

Accessors

isClosedsize

Methods

[asyncIterator]closeerrorfailpush

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


