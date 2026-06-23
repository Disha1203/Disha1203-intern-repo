# Inspecting API Requests & Responses

## Goal

Learn how to inspect incoming API requests and outgoing responses to debug NestJS applications effectively.

## Reflections

### How can logging request payloads help with debugging?

* Logging request payloads helps verify that the API receives the expected data from clients.
* It can reveal missing fields, incorrect values, or malformed request bodies.
* Request logs help trace how data flows through the application.
* Logging headers can help diagnose authentication and authorization issues.
* Payload logging can assist in reproducing bugs reported by users.
* Structured request logs provide valuable context when investigating production issues.


### What tools can you use to inspect API requests and responses?

* Bruno can be used to send requests and inspect responses during development.
* Postman provides a graphical interface for testing APIs and viewing responses.
* cURL allows API testing directly from the command line.
* Browser developer tools can inspect requests made by web applications.
* NestJS logging and debugging tools can display request and response details.
* VS Code's debugger can inspect request objects and response data during execution.


### How would you debug an issue where an API returns the wrong status code?

* Reproduce the issue using an API testing tool such as Bruno or Postman.
* Verify the request payload, headers, and route parameters.
* Inspect controller logic to determine which response path is being executed.
* Check exception filters, guards, interceptors, and validation pipes that may affect responses.
* Use breakpoints or logs to follow the request through the application.
* Confirm that exceptions and HTTP responses are mapped to the correct status codes


### What are some security concerns when logging request data?

* Sensitive information such as passwords should never be logged.
* Authentication tokens and API keys should be excluded or masked in logs.
* Personal user information should be logged only when necessary and according to privacy requirements.
* Excessive logging may expose confidential data if logs are compromised.
* Log files should be protected with appropriate access controls.


## Screenshots

![Enhanced middleware logs](milestone-10/Screenshots/improved-middleware.png)