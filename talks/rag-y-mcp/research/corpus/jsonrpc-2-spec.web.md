---
source_file: jsonrpc-2-spec
source_type: web-capture
ingested_at: 2026-08-14
---

# JSON-RPC 2.0 Specification

## Provenance
- Original location: `research/web/jsonrpc-2-spec/`
- Format: html. Texto tomado de `page.md` (~14.500 caracteres, 13 encabezados). **La extracción es excelente y prácticamente sin pérdida**: la spec es un documento corto y estructurado, y `page.md` conserva las tablas de miembros, la tabla de códigos de error y los 14 ejemplos de request/response completos. Es la captura más fiel de todo el conjunto.
- URL: https://www.jsonrpc.org/specification
- Autor / fuente: **JSON-RPC Working Group** (`json-rpc@googlegroups.com`).
- Fecha del original: **Origin Date 2010-03-26** (basado en la versión 2009-05-24). **Updated: 2013-01-04.** Copyright 2007-2010 del JSON-RPC Working Group.
- HTTP status: 200. `fetched_at`: 2026-08-14T16:57:33Z.
- Assets: **ninguno** (`assets: []`).

**Por qué está en el corpus.** MCP se transporta sobre JSON-RPC 2.0. Esta es la **única fuente normativa de todo el bloque MCP del deck** — ver la nota sobre la especificación de MCP faltante en `mcp-anuncio-anthropic-2024.web.md`. Es una especificación real, con lenguaje RFC 2119 (MUST / SHOULD / MAY), estable desde 2013.

## Key claims

- **JSON-RPC es un protocolo de llamada a procedimiento remoto (RPC) sin estado y liviano.** *"It is designed to be simple!"*
- **Es agnóstico del transporte.** *"the concepts can be used within the same process, over sockets, over http, or in many various message passing environments."* Esto es directamente relevante para el deck: MCP usa el mismo JSON-RPC sobre stdio, sobre SSE y sobre HTTP en streaming, y la spec de JSON-RPC no privilegia ninguno.
- **Usa JSON (RFC 4627) como formato de datos** y hereda su sistema de tipos: cuatro primitivos (String, Number, Boolean, Null) y dos estructurados (Object, Array).
- **La versión se declara en cada mensaje.** El miembro `jsonrpc` DEBE ser exactamente `"2.0"`. Es lo que permite distinguir 2.0 de 1.0, que no lo tiene.
- **Cliente y servidor son roles, no procesos.** *"One implementation of this specification could easily fill both of those roles, even at the same time."* El Cliente origina Requests y maneja Responses; el Servidor origina Responses y maneja Requests. Relevante para MCP, donde el servidor también envía notificaciones al cliente.
- **Una Request sin `id` es una Notificación, y el servidor NO DEBE responderla** — incluidas las que van dentro de un batch.
- **En una Response, `result` y `error` son mutuamente excluyentes**: uno de los dos DEBE estar, los dos NO DEBEN estar.
- **Los nombres de método que empiezan con `rpc.` están reservados** para métodos internos y extensiones del sistema, y NO DEBEN usarse para otra cosa.
- **El rango de códigos de error de -32768 a -32000 está reservado** para errores predefinidos.
- **El batch permite mandar varias Requests en un Array** y el servidor PUEDE procesarlas concurrentemente, en cualquier orden y con cualquier grado de paralelismo. Las respuestas PUEDEN volver en cualquier orden dentro del Array; el cliente DEBERÍA correlacionarlas por `id`.

## Definitions and terminology

**Request object.** Cuatro miembros:

| Miembro | Obligatoriedad | Definición (parafraseada de la spec) |
|---|---|---|
| `jsonrpc` | MUST | String con la versión del protocolo. **DEBE ser exactamente `"2.0"`.** |
| `method` | MUST | String con el nombre del método a invocar. Los que empiezan con `rpc` seguido de punto (U+002E) están **reservados** para métodos internos y extensiones. |
| `params` | MAY (puede omitirse) | Valor **estructurado** con los parámetros de la invocación. |
| `id` | condicional | Identificador establecido por el Cliente. Si se incluye, DEBE ser String, Number o NULL. **Si no se incluye, se asume que es una Notificación.** |

Sobre `id`: el servidor DEBE devolver el mismo valor en la Response. Dos notas al pie de la propia spec: (1) usar Null como `id` está desaconsejado, porque la spec usa Null para Responses con id desconocido y porque JSON-RPC 1.0 lo usaba para notificaciones; (2) los Numbers NO DEBERÍAN tener parte fraccionaria, porque muchas fracciones decimales no se representan exactamente en binario.

**Notification (Notificación).** *"A Notification is a Request object without an 'id' member."* Significa que al Cliente no le interesa la Response. **El Servidor NO DEBE responder a una Notificación**, incluidas las que van dentro de un batch. Consecuencia declarada: *"Notifications are not confirmable by definition, since they do not have a Response object to be returned. As such, the Client would not be aware of any errors (like e.g. 'Invalid params','Internal error')."* — es decir, con una notificación se pierde toda la información de error.

**Parameter Structures.** Si hay `params`, DEBEN ser un valor estructurado, de una de dos formas:
- **by-position**: `params` DEBE ser un **Array**, con los valores en el orden que espera el servidor.
- **by-name**: `params` DEBE ser un **Object**, con nombres de miembro que coincidan con los nombres de parámetro del servidor. Los nombres DEBEN coincidir exactamente, **incluidas mayúsculas y minúsculas**. La ausencia de nombres esperados PUEDE generar un error.

**Response object.** Cuatro miembros:

| Miembro | Obligatoriedad | Definición |
|---|---|---|
| `jsonrpc` | MUST | DEBE ser exactamente `"2.0"`. |
| `result` | REQUIRED on success | **NO DEBE existir si hubo error.** Su valor lo determina el método invocado. |
| `error` | REQUIRED on error | **NO DEBE existir si no hubo error.** DEBE ser un Object según la sección 5.1. |
| `id` | REQUIRED | DEBE ser igual al `id` de la Request. **Si hubo un error detectando el id (parse error / invalid request), DEBE ser Null.** |

**Error object.** Tres miembros: `code` (Number entero que indica el tipo de error), `message` (String, descripción corta; DEBERÍA limitarse a una oración concisa) y `data` (valor primitivo o estructurado con información adicional; puede omitirse, y su contenido lo define el servidor).

**Códigos de error predefinidos (tabla verbatim de la spec):**

| Código | Mensaje | Significado |
|---|---|---|
| **-32700** | Parse error | JSON inválido recibido por el servidor. Ocurrió un error parseando el texto JSON. |
| **-32600** | Invalid Request | El JSON enviado no es un Request object válido. |
| **-32601** | Method not found | El método no existe / no está disponible. |
| **-32602** | Invalid params | Parámetros de método inválidos. |
| **-32603** | Internal error | Error interno de JSON-RPC. |
| **-32000 a -32099** | Server error | Reservado para errores de servidor definidos por la implementación. |

El rango **-32768 a -32000** está reservado para errores predefinidos; cualquier código dentro de ese rango no definido explícitamente queda reservado para uso futuro. El resto del espacio queda disponible para errores definidos por la aplicación. La spec aclara que los códigos son casi los mismos que los sugeridos para XML-RPC.

**Batch.** Para enviar varias Requests a la vez, el Cliente PUEDE mandar un Array de Request objects. Reglas:
- El servidor DEBERÍA responder con un Array con las Responses correspondientes, **después** de procesar todas las Requests del batch.
- DEBERÍA haber una Response por cada Request, **excepto para las notificaciones**.
- El servidor PUEDE procesar el batch como un conjunto de tareas concurrentes, en cualquier orden y con cualquier grado de paralelismo.
- Las Responses PUEDEN volver en cualquier orden. El Cliente DEBERÍA correlacionar por `id`.
- Si el batch en sí no se reconoce como JSON válido o como Array con al menos un valor, la respuesta DEBE ser un **único** Response object (no un array).
- **Si no hay ninguna Response que devolver (batch enteramente de notificaciones), el servidor NO DEBE devolver un Array vacío: no debe devolver nada.**

**Extensions.** Los nombres de método que empiezan con `rpc.` están reservados para extensiones del sistema y NO DEBEN usarse para otra cosa. Cada extensión se define en una especificación relacionada. **Todas las extensiones del sistema son OPCIONALES.**

**Convenciones normativas.** MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY y OPTIONAL se interpretan según **RFC 2119**. Además: todos los nombres de miembro intercambiados entre Cliente y Servidor que se consideren para matching **deben tratarse como case-sensitive**. Los términos *function*, *method* y *procedure* son intercambiables.

**Compatibilidad con 1.0.** Los objetos de 2.0 pueden no funcionar con clientes o servidores 1.0. Distinguirlos es fácil: 2.0 siempre tiene el miembro `jsonrpc` con valor `"2.0"`, 1.0 no. La mayoría de las implementaciones 2.0 deberían intentar manejar objetos 1.0, aunque no los aspectos peer-to-peer ni de class hinting de 1.0.

## Evidence and examples

La spec trae 14 ejemplos completos. Notación: `-->` es dato enviado al Servidor, `<--` dato enviado al Cliente.

**Llamada con parámetros posicionales:**

```
--> {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}
<-- {"jsonrpc": "2.0", "result": 19, "id": 1}

--> {"jsonrpc": "2.0", "method": "subtract", "params": [23, 42], "id": 2}
<-- {"jsonrpc": "2.0", "result": -19, "id": 2}
```

El segundo par es pedagógicamente valioso: invertir el orden cambia el resultado. Es el argumento a favor de los parámetros por nombre.

**Llamada con parámetros nombrados** (el orden ya no importa):

```
--> {"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}
<-- {"jsonrpc": "2.0", "result": 19, "id": 3}

--> {"jsonrpc": "2.0", "method": "subtract", "params": {"minuend": 42, "subtrahend": 23}, "id": 4}
<-- {"jsonrpc": "2.0", "result": 19, "id": 4}
```

**Notificaciones** (sin `id`, sin respuesta):

```
--> {"jsonrpc": "2.0", "method": "update", "params": [1,2,3,4,5]}
--> {"jsonrpc": "2.0", "method": "foobar"}
```

**Método inexistente:**

```
--> {"jsonrpc": "2.0", "method": "foobar", "id": "1"}
<-- {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "1"}
```

**JSON inválido** (nótese `id: null` en la respuesta, porque no se pudo determinar el id):

```
--> {"jsonrpc": "2.0", "method": "foobar, "params": "bar", "baz]
<-- {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": null}
```

**Request object inválido** (`method` es un número, no un string):

```
--> {"jsonrpc": "2.0", "method": 1, "params": "bar"}
<-- {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
```

**Batch con JSON inválido** — respuesta **única**, no array:

```
--> [
  {"jsonrpc": "2.0", "method": "sum", "params": [1,2,4], "id": "1"},
  {"jsonrpc": "2.0", "method"
]
<-- {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": null}
```

**Array vacío** — también respuesta única:

```
--> []
<-- {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
```

**Batch inválido pero no vacío** — acá sí array, con un elemento:

```
--> [1]
<-- [
  {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
]
```

**Batch inválido de tres elementos** — un error por elemento:

```
--> [1,2,3]
<-- [
  {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null},
  {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null},
  {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
]
```

**Batch completo — el mejor ejemplo de la spec** (6 requests, 5 responses):

```
--> [
        {"jsonrpc": "2.0", "method": "sum", "params": [1,2,4], "id": "1"},
        {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
        {"jsonrpc": "2.0", "method": "subtract", "params": [42,23], "id": "2"},
        {"foo": "boo"},
        {"jsonrpc": "2.0", "method": "foo.get", "params": {"name": "myself"}, "id": "5"},
        {"jsonrpc": "2.0", "method": "get_data", "id": "9"}
    ]
<-- [
        {"jsonrpc": "2.0", "result": 7, "id": "1"},
        {"jsonrpc": "2.0", "result": 19, "id": "2"},
        {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null},
        {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "5"},
        {"jsonrpc": "2.0", "result": ["hello", 5], "id": "9"}
    ]
```

Este ejemplo condensa casi todo el protocolo en 12 líneas y es el candidato natural para una slide: **6 requests entran, 5 responses salen** — la notificación `notify_hello` no genera respuesta, el objeto basura `{"foo": "boo"}` genera un `Invalid Request` con `id: null`, y `foo.get` genera un `Method not found` conservando su `id: "5"`.

**Batch enteramente de notificaciones** — no se devuelve nada:

```
--> [
        {"jsonrpc": "2.0", "method": "notify_sum", "params": [1,2,4]},
        {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]}
    ]
<-- //Nothing is returned for all notification batches
```

## Inconsistencies / open questions

1. **La spec no dice nada sobre transporte, autenticación, autorización, cifrado, ni tamaño máximo de mensaje.** Es deliberado ("transport agnostic", "designed to be simple") pero significa que todo eso queda del lado de MCP — y el artículo de Microsoft Research (`tool-space-interference-msr.web.md`) documenta precisamente que MCP tampoco lo define: no hay guía sobre cuántos tokens puede devolver una llamada, ni sobre recursos provistos por el cliente, ni namespaces. **Las carencias se acumulan: JSON-RPC no lo define porque no es su problema, y MCP no lo definió tampoco.**
2. **JSON-RPC no tiene namespaces.** Los nombres de método son strings planos. El único mecanismo de espacio de nombres es la reserva del prefijo `rpc.`. Esto explica estructuralmente el hallazgo de MSR de 775 colisiones de nombres de herramientas en MCP: **el problema se hereda del protocolo de base**, y por eso los clientes (Claude Code) tienen que prefijar a mano.
3. **La spec referencia RFC 4627, que está obsoleta.** RFC 4627 fue reemplazada por RFC 7159 (2014) y luego por RFC 8259 (2017). El documento no se actualizó desde 2013-01-04. No cambia nada en la práctica, pero es un dato de higiene si alguien cita la spec como autoridad viva.
4. **Fricción entre notificaciones y observabilidad, admitida por la propia spec.** El texto reconoce que con notificaciones el cliente no se entera de ningún error. En un contexto agéntico eso es más grave de lo que era en 2010: si un servidor MCP falla al procesar una notificación, no hay ningún canal por el cual el agente se entere.
5. **Ambigüedad en el manejo de batch inválido.** Comparar dos ejemplos: `[]` (array vacío) devuelve un **objeto único**, mientras que `[1]` devuelve un **array de un elemento**. La regla está enunciada ("si el batch no se reconoce como Array con al menos un valor, respuesta única") pero es una arista que las implementaciones equivocan seguido.
6. **`SHOULD` en el batch, no `MUST`.** *"A Response object SHOULD exist for each Request object"* — es SHOULD, no MUST. Deja margen a implementaciones que no responden todo, y el cliente tiene que estar preparado.
7. **La página tiene una errata de tipeo en la nota de copyright**: "this document itself may not bemodified in any way" (falta el espacio en "be modified"). Está en el original, no es un artefacto de la extracción.
8. **`params` no se define para el caso de omisión.** La spec dice que `params` PUEDE omitirse, pero no aclara si omitir `params` es equivalente a `params: []` o a `params: {}`. El ejemplo `{"jsonrpc": "2.0", "method": "get_data", "id": "9"}` lo usa sin decir nada.

## Images / diagrams

Ninguna. `metadata.yaml` registra `assets: []` y la página no contiene imágenes, diagramas ni capturas — es una especificación de texto plano con tablas HTML y bloques de código. La carpeta compañera `research/corpus/jsonrpc-2-spec.web/images/` existe y está vacía, lo cual es válido.

## Raw / preserved excerpts

**Cabecera del documento (verbatim):**

> Origin Date: 2010-03-26 (based on the 2009-05-24 version) Updated: 2013-01-04 Author: JSON-RPC Working Group <json-rpc@googlegroups.com>

**Sección 1, Overview (verbatim, completa):**

> JSON-RPC is a stateless, light-weight remote procedure call (RPC) protocol. Primarily this specification defines several data structures and the rules around their processing. It is transport agnostic in that the concepts can be used within the same process, over sockets, over http, or in many various message passing environments. It uses JSON (RFC 4627) as data format.
>
> It is designed to be simple!

**Sección 2, Conventions (verbatim):**

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.
>
> Since JSON-RPC utilizes JSON, it has the same type system (see http://www.json.org or RFC 4627). JSON can represent four primitive types (Strings, Numbers, Booleans, and Null) and two structured types (Objects and Arrays). The term "Primitive" in this specification references any of those four primitive JSON types. The term "Structured" references either of the structured JSON types. Whenever this document refers to any JSON type, the first letter is always capitalized: Object, Array, String, Number, Boolean, Null. True and False are also capitalized.
>
> All member names exchanged between the Client and the Server that are considered for matching of any kind should be considered to be case-sensitive. The terms function, method, and procedure can be assumed to be interchangeable.
>
> The Client is defined as the origin of Request objects and the handler of Response objects.
> The Server is defined as the origin of Response objects and the handler of Request objects.
>
> One implementation of this specification could easily fill both of those roles, even at the same time, to other different clients or the same client. This specification does not address that layer of complexity.

**Sección 3, Compatibility (verbatim):**

> JSON-RPC 2.0 Request objects and Response objects may not work with existing JSON-RPC 1.0 clients or servers. However, it is easy to distinguish between the two versions as 2.0 always has a member named "jsonrpc" with a String value of "2.0" whereas 1.0 does not. Most 2.0 implementations should consider trying to handle 1.0 objects, even if not the peer-to-peer and class hinting aspects of 1.0.

**Sección 4, Request object — miembros (verbatim):**

> **jsonrpc** A String specifying the version of the JSON-RPC protocol. MUST be exactly "2.0".
> **method** A String containing the name of the method to be invoked. Method names that begin with the word rpc followed by a period character (U+002E or ASCII 46) are reserved for rpc-internal methods and extensions and MUST NOT be used for anything else.
> **params** A Structured value that holds the parameter values to be used during the invocation of the method. This member MAY be omitted.
> **id** An identifier established by the Client that MUST contain a String, Number, or NULL value if included. If it is not included it is assumed to be a notification. The value SHOULD normally not be Null and Numbers SHOULD NOT contain fractional parts
>
> The Server MUST reply with the same value in the Response object if included. This member is used to correlate the context between the two objects.

**Notas al pie sobre `id` (verbatim):**

> [1] The use of Null as a value for the id member in a Request object is discouraged, because this specification uses a value of Null for Responses with an unknown id. Also, because JSON-RPC 1.0 uses an id value of Null for Notifications this could cause confusion in handling.
>
> [2] Fractional parts may be problematic, since many decimal fractions cannot be represented exactly as binary fractions.

**Sección 4.1, Notification (verbatim, completa):**

> A Notification is a Request object without an "id" member. A Request object that is a Notification signifies the Client's lack of interest in the corresponding Response object, and as such no Response object needs to be returned to the client. The Server MUST NOT reply to a Notification, including those that are within a batch request.
>
> Notifications are not confirmable by definition, since they do not have a Response object to be returned. As such, the Client would not be aware of any errors (like e.g. "Invalid params","Internal error").

**Sección 4.2, Parameter Structures (verbatim):**

> If present, parameters for the rpc call MUST be provided as a Structured value. Either by-position through an Array or by-name through an Object.
>
> - by-position: params MUST be an Array, containing the values in the Server expected order.
> - by-name: params MUST be an Object, with member names that match the Server expected parameter names. The absence of expected names MAY result in an error being generated. The names MUST match exactly, including case, to the method's expected parameters.

**Sección 5, Response object (verbatim):**

> When a rpc call is made, the Server MUST reply with a Response, except for in the case of Notifications. The Response is expressed as a single JSON Object, with the following members:
>
> **jsonrpc** A String specifying the version of the JSON-RPC protocol. MUST be exactly "2.0".
> **result** This member is REQUIRED on success. This member MUST NOT exist if there was an error invoking the method. The value of this member is determined by the method invoked on the Server.
> **error** This member is REQUIRED on error. This member MUST NOT exist if there was no error triggered during invocation. The value for this member MUST be an Object as defined in section 5.1.
> **id** This member is REQUIRED. It MUST be the same as the value of the id member in the Request Object. If there was an error in detecting the id in the Request object (e.g. Parse error/Invalid Request), it MUST be Null.
>
> Either the result member or error member MUST be included, but both members MUST NOT be included.

**Sección 5.1, Error object (verbatim):**

> When a rpc call encounters an error, the Response Object MUST contain the error member with a value that is a Object with the following members:
>
> **code** A Number that indicates the error type that occurred. This MUST be an integer.
> **message** A String providing a short description of the error. The message SHOULD be limited to a concise single sentence.
> **data** A Primitive or Structured value that contains additional information about the error. This may be omitted. The value of this member is defined by the Server (e.g. detailed error information, nested errors etc.).
>
> The error codes from and including -32768 to -32000 are reserved for pre-defined errors. Any code within this range, but not defined explicitly below is reserved for future use. The error codes are nearly the same as those suggested for XML-RPC at the following url: http://xmlrpc-epi.sourceforge.net/specs/rfc.fault_codes.php
>
> The remainder of the space is available for application defined errors.

**Sección 6, Batch (verbatim, completa):**

> To send several Request objects at the same time, the Client MAY send an Array filled with Request objects.
>
> The Server should respond with an Array containing the corresponding Response objects, after all of the batch Request objects have been processed. A Response object SHOULD exist for each Request object, except that there SHOULD NOT be any Response objects for notifications. The Server MAY process a batch rpc call as a set of concurrent tasks, processing them in any order and with any width of parallelism.
>
> The Response objects being returned from a batch call MAY be returned in any order within the Array. The Client SHOULD match contexts between the set of Request objects and the resulting set of Response objects based on the id member within each Object.
>
> If the batch rpc call itself fails to be recognized as an valid JSON or as an Array with at least one value, the response from the Server MUST be a single Response object. If there are no Response objects contained within the Response array as it is to be sent to the client, the server MUST NOT return an empty Array and should return nothing at all.

**Sección 8, Extensions (verbatim, completa):**

> Method names that begin with rpc. are reserved for system extensions, and MUST NOT be used for anything else. Each system extension is defined in a related specification. All system extensions are OPTIONAL.

**Copyright (verbatim, con la errata del original):**

> Copyright (C) 2007-2010 by the JSON-RPC Working Group
>
> This document and translations of it may be used to implement JSON-RPC, it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this paragraph are included on all such copies and derivative works. However, this document itself may not bemodified in any way.
>
> The limited permissions granted above are perpetual and will not be revoked.
