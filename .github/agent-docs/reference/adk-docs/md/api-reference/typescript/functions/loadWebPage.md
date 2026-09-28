[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [loadWebPage]()



# Function loadWebPage

  * loadWebPage(url: string, options?: [LoadWebPageOptions](../interfaces/LoadWebPageOptions.html)): Promise<string>

Fetches the content at `url` and returns its extracted, readable text.

Hardened against SSRF: only `http`/`https` URLs are fetched, the host is resolved and rejected up front if it is `localhost`-style or resolves to a private / loopback / link-local / shared / reserved / multicast address, and redirects are never followed. Never throws for expected failures (bad scheme, blocked host, non-200, timeout, network error); returns `Failed to fetch url: <url>` instead.

Known limitation: global `fetch` performs its own DNS resolution at connect time, so a residual time-of-check/time-of-use (DNS-rebinding) window exists between this pre-flight lookup and fetch's own lookup. Full connection IP-pinning (e.g. an `undici` Agent with a custom `lookup`) is a possible future hardening.

#### Parameters

    * url: string
    * `Optional`options: [LoadWebPageOptions](../interfaces/LoadWebPageOptions.html)

#### Returns Promise<string>

    * Defined in [core/src/tools/load_web_page.ts:286](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/load_web_page.ts#L286)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


