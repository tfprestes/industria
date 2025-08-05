# TODOs e FIXMEs Encontrados

---
- **C:\industria\analisador_projeto.py:43** — `num_todos = sum(1 for l in lines if 'TODO' in l or 'FIXME' in l)`
```
ext = os.path.splitext(file_path)[-1].lower()
    num_lines = len(lines)
    num_todos = sum(1 for l in lines if 'TODO' in l or 'FIXME' in l)
    sensitive_hits = [l for l in lines if any(kw in l.lower() for kw in SENSITIVE_KEYWORDS)]
    dangerous_hits = [l for l in lines if any(df in l for df in DANGEROUS_FUNCTIONS)]
```
---
- **C:\industria\relatorio_automatizado.py:21** — `if re.search(r'\b(TODO|FIXME)\b', line, re.IGNORECASE):`
```
with open(fp, encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if re.search(r'\b(TODO|FIXME)\b', line, re.IGNORECASE):
                            # Adiciona contexto (2 linhas antes e depois)
                            context = []
```
---
- **C:\industria\.venv\Lib\site-packages\anyio\_core\_fileio.py:416** — `def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it`
```
@property
        def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it
            return self._path.info
```
---
- **C:\industria\.venv\Lib\site-packages\blinker\base.py:135** — `# TODO no explanation or test for this`
```
)
            except TypeError:
                # TODO no explanation or test for this
                self.disconnect(receiver, sender)
                raise
```
---
- **C:\industria\.venv\Lib\site-packages\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\.venv\Lib\site-packages\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\.venv\Lib\site-packages\charset_normalizer\legacy.py:9** — `# TODO: remove this check when dropping Python 3.7 support`
```
from .constant import CHARDET_CORRESPONDENCE

# TODO: remove this check when dropping Python 3.7 support
if TYPE_CHECKING:
    from typing_extensions import TypedDict
```
---
- **C:\industria\.venv\Lib\site-packages\click\_termui_impl.py:525** — `# TODO: This never terminates if the passed generator never terminates.`
```
fd, filename = tempfile.mkstemp()
    # TODO: This never terminates if the passed generator never terminates.
    text = "".join(generator)
    if not color:
```
---
- **C:\industria\.venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric\rsa.py:221** — `# TODO: Replace with lcm(p - 1, q - 1) once the minimum`
```
# than necessary. (lambda_n always divides phi_n)
    #
    # TODO: Replace with lcm(p - 1, q - 1) once the minimum
    # supported Python version is >= 3.9.
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
```
---
- **C:\industria\.venv\Lib\site-packages\cryptography\x509\name.py:357** — `# TODO: this is relatively expensive, if this looks like a bottleneck`
```
def __hash__(self) -> int:
        # TODO: this is relatively expensive, if this looks like a bottleneck
        # for you, consider optimizing!
        return hash(tuple(self._attributes))
```
---
- **C:\industria\.venv\Lib\site-packages\dateutil\rrule.py:1182** — `# TODO: Check -numweeks for next year.`
```
if 1 in rr._byweekno:
                    # Check week number 1 of next year as well
                    # TODO: Check -numweeks for next year.
                    i = no1wkst+numweeks*7
                    if no1wkst != firstwkst:
```
---
- **C:\industria\.venv\Lib\site-packages\dateutil\parser\_parser.py:55** — `# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth`
```
# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth
# making public and/or figuring out if there is something we can
# take off their plate.
```
---
- **C:\industria\.venv\Lib\site-packages\dateutil\zoneinfo\__init__.py:25** — `except IOError as e:  # TODO  switch to FileNotFoundError?`
```
try:
        return BytesIO(get_data(__name__, ZONEFILENAME))
    except IOError as e:  # TODO  switch to FileNotFoundError?
        warnings.warn("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
```
---
- **C:\industria\.venv\Lib\site-packages\firebase_admin\_rfc3339.py:73** — `# TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex`
```
# Note: %z parses timezone offsets, but requires the timezone offset *not*
    # include a separating ':'. As of python 3.7, this was relaxed.
    # TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex
    # replacement.
    datestr_modified = re.sub(r'(\d\d):(\d\d)$', r'\1\2', datestr_modified)
```
---
- **C:\industria\.venv\Lib\site-packages\firebase_admin\_user_import.py:478** — `# TODO(rsgowman): This class used to be specific to importing users (hence`
```
as importing users or deleting multiple user accounts.
    """
    # TODO(rsgowman): This class used to be specific to importing users (hence
    # it's home in _user_import.py). It's now also used by bulk deletion of
    # users. Move this to a more common location.
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\bidi.py:291** — `# TODO: api_core should expose the future interface for wrapped`
```
request_generator.call = call

        # TODO: api_core should expose the future interface for wrapped
        # callables as well.
        if hasattr(call, "_wrapped"):  # pragma: NO COVER
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\client_logging.py:12** — `# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.`
```
# Fields to be included in the StructuredLogFormatter.
#
# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.
_recognized_logging_fields = [
    "httpRequest",
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\exceptions.py:498** — `# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.`
```
# to `format_http_response_error` which expects a more abstract response from google.auth and is
# compatible with both sync and async response types.
# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.
def format_http_response_error(
    response, method: str, url: str, payload: Optional[Dict] = None
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\extended_operation.py:138** — `# TODO(dovs): there is not currently a good way to determine whether the`
```
def cancelled(self):
        # TODO(dovs): there is not currently a good way to determine whether the
        # operation has been cancelled.
        # The best we can do is manually keep track of cancellation
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\grpc_helpers.py:295** — `# TODO(https://github.com/googleapis/python-api-core/issues/598):`
```
# Use grpc.compute_engine_channel_credentials in order to support Direct Path.
        # See https://grpc.github.io/grpc/python/grpc.html#grpc.compute_engine_channel_credentials
        # TODO(https://github.com/googleapis/python-api-core/issues/598):
        # Although `grpc.compute_engine_channel_credentials` returns channel credentials
        # outside of a Google Compute Engine environment (GCE), we should determine if
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\rest_streaming_async.py:54** — `# TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content`
```
self._response = response
        self._chunk_size = 1024
        # TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content
        # method as an async generator as it looks for the `yield` keyword in the implementation.
        # Given that the abstract method is not implemented, mypy fails to recognize it as an async generator.
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry_async.py:17** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry_async.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\operations_v1\operations_rest_client_async.py:109** — `# TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry``
```
name: str,
        *,
        # TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry`
        # to allow configuring retryable error codes.
        retry=gapic_v1.method_async.DEFAULT,
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\operations_v1\transports\base.py:52** — `# TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.`
```
*,
        host: str = DEFAULT_HOST,
        # TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\operations_v1\transports\rest.py:134** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\operations_v1\transports\rest_asyncio.py:84** — `# TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.`
```
http_options: Optional[Dict] = None,
        path_prefix: str = "v1",
        # TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/716): Add docstring for `scopes` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/717): Add docstring for `quota_project_id` to async REST transport.
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry\retry_streaming.py:113** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry\retry_streaming_async.py:116** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry\retry_unary.py:144** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry\retry_unary_async.py:155** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\.venv\Lib\site-packages\google\api_core\retry\__init__.py:33** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\.venv\Lib\site-packages\google\auth\_helpers.py:43** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.`
```
REFRESH_THRESHOLD = datetime.timedelta(minutes=3, seconds=45)

# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.
_SENSITIVE_FIELDS = {
    "accessToken",
```
---
- **C:\industria\.venv\Lib\site-packages\google\auth\aio\_helpers.py:42** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):`
```
return json_response
    except Exception:
        # TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):
        # Parse and return response payload as json based on different content types.
        return None
```
---
- **C:\industria\.venv\Lib\site-packages\google\auth\compute_engine\_metadata.py:82** — `# TODO: implement GCE residency detection on Windows`
```
if os.name == "nt":
        # TODO: implement GCE residency detection on Windows
        return False
```
---
- **C:\industria\.venv\Lib\site-packages\google\auth\transport\_aiohttp_requests.py:146** — `# TODO: Use auto_decompress property for aiohttp 3.7+`
```
def __init__(self, session=None):
        # TODO: Use auto_decompress property for aiohttp 3.7+
        if session is not None and session._auto_decompress:
            raise exceptions.InvalidOperation(
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\firestore_admin_v1\services\firestore_admin\transports\rest.py:1882** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\firestore_v1\watch.py:75** — `# TODO: Currently this uses a dict. Other implementations use a rbtree.`
```
class WatchDocTree(object):
    # TODO: Currently this uses a dict. Other implementations use a rbtree.
    # The performance of this implementation should be investigated and may
    # require modifying the underlying datastructure to a rbtree.
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\firestore_v1\_helpers.py:750** — `# TODO: other transforms`
```
def _apply_merge_all(self) -> None:
        self.data_merge = sorted(self.field_paths + self.deleted_fields)
        # TODO: other transforms
        self.transform_merge = self.transform_paths
        self.merge = sorted(self.data_merge + self.transform_paths)
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\firestore_v1\__init__.py:66** — `# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match`
```
from google.cloud.firestore_v1.watch import Watch

# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match
# firestore.py. So comment out until needed on customer level for certain.
# from .services.firestore import FirestoreClient
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\firestore_v1\services\firestore\transports\rest.py:970** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\storage\blob.py:4789** — `# TODO: After google-cloud-core 1.6.0 is stable and we upgrade it`
```
:returns: The host name.
    """
    # TODO: After google-cloud-core 1.6.0 is stable and we upgrade it
    # to 1.6.0 in setup.py, we no longer need to check the attribute
    # existence. We can simply return connection.get_api_base_url_for_mtls().
```
---
- **C:\industria\.venv\Lib\site-packages\google\cloud\storage\_http.py:54** — `# TODO: When metrics all use gccl, this should be removed #9552`
```
self._client_info.client_library_version = __version__

        # TODO: When metrics all use gccl, this should be removed #9552
        if self._client_info.user_agent is None:  # pragma: no branch
            self._client_info.user_agent = ""
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\descriptor.py:26** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
  _message = api_implementation._c_module
  # TODO: Remove this import after fix api_implementation
  if _message is None:
    from google.protobuf.pyext import _message
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\descriptor_database.py:139** — `# TODO: implement this API.`
```
def FindFileContainingExtension(self, extendee_name, extension_number):
    # TODO: implement this API.
    return None
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\descriptor_pool.py:1360** — `# TODO: This pool could be constructed from Python code, when we`
```
if _USE_C_DESCRIPTORS:
  # TODO: This pool could be constructed from Python code, when we
  # support a flag like 'use_cpp_generated_pool=True'.
  # pylint: disable=protected-access
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\message.py:8** — `# TODO: We should just make these methods all "pure-virtual" and move`
```
# https://developers.google.com/open-source/licenses/bsd

# TODO: We should just make these methods all "pure-virtual" and move
# all implementation out, into reflection.py for now.
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\message_factory.py:100** — `# TODO: Remove this check here. Duplicate extension`
```
_ = GetMessageClass(extension.containing_type)
      if api_implementation.Type() != 'python':
        # TODO: Remove this check here. Duplicate extension
        # register check should be in descriptor_pool.
        if extension is not pool.FindExtensionByNumber(
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\symbol_database.py:136** — `# TODO: Fix the differences with MessageFactory.`
```
def GetMessages(self, files):
    # TODO: Fix the differences with MessageFactory.
    """Gets all registered messages from a specified file.
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\text_format.py:22** — `# TODO Import thread contention leads to test failures.`
```
__author__ = 'kenton@google.com (Kenton Varda)'

# TODO Import thread contention leads to test failures.
import encodings.raw_unicode_escape  # pylint: disable=unused-import
import encodings.unicode_escape  # pylint: disable=unused-import
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\internal\api_implementation.py:88** — `# TODO: fail back to python`
```
del _message
  except ImportError:
    # TODO: fail back to python
    warnings.warn(
        'Selected implementation cpp is not available.')
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\internal\builder.py:96** — `# TODO: Remove this on-op`
```
file_des: FileDescriptor of the .proto file
  """
  # TODO: Remove this on-op
  return
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\internal\containers.py:98** — `# TODO: Remove this. BaseContainer does *not* conform to`
```
# TODO: Remove this. BaseContainer does *not* conform to
# MutableSequence, only its subclasses do.
collections.abc.MutableSequence.register(BaseContainer)
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\internal\extension_dict.py:37** — `# TODO: Unify error handling of "unknown extension" crap.`
```
# TODO: Unify error handling of "unknown extension" crap.
# TODO: Support iteritems()-style iteration over all
# extensions with the "has" bits turned on?
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\internal\python_message.py:10** — `# TODO: Helpers for verbose, common checks like seeing if a`
```
# This code is meant to work on Python 2.4 and above only.
#
# TODO: Helpers for verbose, common checks like seeing if a
# descriptor's cpp_type is CPPTYPE_MESSAGE.
```
---
- **C:\industria\.venv\Lib\site-packages\google\protobuf\pyext\cpp_message.py:21** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
_message = api_implementation._c_module
# TODO: Remove this import after fix api_implementation
if _message is None:
  from google.protobuf.pyext import _message
```
---
- **C:\industria\.venv\Lib\site-packages\googleapiclient\discovery.py:129** — `# TODO(dhermes): Remove 'userip' in 'v2'.`
```
DEFAULT_UNIVERSE = "googleapis.com"
# Parameters accepted by the stack, but not visible via discovery.
# TODO(dhermes): Remove 'userip' in 'v2'.
STACK_QUERY_PARAMETERS = frozenset(["trace", "pp", "userip", "strict"])
STACK_QUERY_PARAMETER_DEFAULT_VALUE = {"type": "string", "location": "query"}
```
---
- **C:\industria\.venv\Lib\site-packages\googleapiclient\http.py:40** — `# TODO(issue 221): Remove this conditional import jibbajabba.`
```
import httplib2

# TODO(issue 221): Remove this conditional import jibbajabba.
try:
    import ssl
```
---
- **C:\industria\.venv\Lib\site-packages\googleapiclient\schema.py:61** — `# TODO(jcgregorio) support format, enum, minimum, maximum`
```
from __future__ import absolute_import

# TODO(jcgregorio) support format, enum, minimum, maximum

__author__ = "jcgregorio@google.com (Joe Gregorio)"
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\_auth.py:37** — `# TODO(xuanwn): Give credentials an actual type.`
```
_credentials: Any

    # TODO(xuanwn): Give credentials an actual type.
    def __init__(self, credentials: Any):
        self._credentials = credentials
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\_channel.py:257** — `# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.`
```
# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.
# pylint: disable=too-many-statements
def _consume_request_iterator(
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\_observability.py:271** — `# TODO(xuanwn): use channel args to exclude those metrics.`
```
RPC.
    """
    # TODO(xuanwn): use channel args to exclude those metrics.
    for exclude_prefix in _SERVICES_TO_EXCLUDE:
        if exclude_prefix in state.method.encode("utf8"):
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\_server.py:1182** — `# TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.`
```
self.registered_method_handlers = {}

        # TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.
        self.rpc_states = set()
        self.due = set()
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\aio\_channel.py:409** — `# TODO(lidiz) drop this hack after 3.8 deprecation`
```
# but not available until 3.9 or 3.8.3. So, we have to keep it
                # for a while.
                # TODO(lidiz) drop this hack after 3.8 deprecation
                if "frame" in str(attribute_error):
                    continue
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\aio\_server.py:87** — `# TODO(xuanwn): Implement this for AsyncIO.`
```
method_handlers: Dict[str, grpc.RpcMethodHandler],
    ) -> None:
        # TODO(xuanwn): Implement this for AsyncIO.
        pass
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\beta\_client_adaptations.py:85** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
class _InvocationProtocolContext(interfaces.GRPCInvocationContext):
    def disable_next_request_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\.venv\Lib\site-packages\grpc\beta\_server_adaptations.py:43** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
def disable_next_response_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\.venv\Lib\site-packages\gunicorn\arbiter.py:365** — `# TODO: select.error is a subclass of OSError since Python 3.3.`
```
pass
        except OSError as e:
            # TODO: select.error is a subclass of OSError since Python 3.3.
            error_number = getattr(e, 'errno', e.args[0])
            if error_number not in [errno.EAGAIN, errno.EINTR]:
```
---
- **C:\industria\.venv\Lib\site-packages\gunicorn\config.py:2377** — `# FIXME: refactor all of this subclassing stdlib argparse`
```
def validate_header_map_behaviour(val):
    # FIXME: refactor all of this subclassing stdlib argparse

    if val is None:
```
---
- **C:\industria\.venv\Lib\site-packages\gunicorn\__main__.py:9** — `# todo: let runpy.run_module take care of argv[0] rewriting`
```
if __name__ == "__main__":
    # see config.py - argparse defaults to basename(argv[0]) == "__main__.py"
    # todo: let runpy.run_module take care of argv[0] rewriting
    run(prog="gunicorn")
```
---
- **C:\industria\.venv\Lib\site-packages\h11\_events.py:310** — `# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that`
```
# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that
# are forbidden to be sent in a trailer, since processing them as if they were
# present in the header section might bypass external security filters."
```
---
- **C:\industria\.venv\Lib\site-packages\h11\_readers.py:186** — `# XX FIXME: we discard chunk extensions. Does anyone care?`
```
chunk_header,
            )
            # XX FIXME: we discard chunk extensions. Does anyone care?
            self._bytes_in_chunk = int(matches["chunk_size"], base=16)
            if self._bytes_in_chunk == 0:
```
---
- **C:\industria\.venv\Lib\site-packages\h11\_writers.py:54** — `# XX FIXME: could at least make an effort to pull out the status message`
```
# status code is mandatory.)
    #
    # XX FIXME: could at least make an effort to pull out the status message
    # from stdlib's http.HTTPStatus table. Or maybe just steal their enums
    # (either by import or copy/paste). We already accept them as status codes
```
---
- **C:\industria\.venv\Lib\site-packages\h2\connection.py:1808** — `# FIXME: Should we split this into one event per active stream?`
```
)

            # FIXME: Should we split this into one event per active stream?
            window_updated_event = WindowUpdated()
            window_updated_event.stream_id = 0
```
---
- **C:\industria\.venv\Lib\site-packages\h2\utilities.py:417** — `# TODO: We should also guard against receiving duplicate Host headers,`
```
# enforced by the _reject_pseudo_header_fields() pipeline.
    #
    # TODO: We should also guard against receiving duplicate Host headers,
    # and against sending duplicate headers.
    authority_header_val = None
```
---
- **C:\industria\.venv\Lib\site-packages\h2\windows.py:116** — `# TODO: Can the window be smaller than 1024 bytes? If not, we can`
```
small DATA frames.
        """
        # TODO: Can the window be smaller than 1024 bytes? If not, we can
        # streamline this algorithm.
        if not self._bytes_processed:
```
---
- **C:\industria\.venv\Lib\site-packages\hpack\hpack.py:321** — `# header table unconditionally. It is a future todo to`
```
else:
            # Indexed literal. We are going to add header to the
            # header table unconditionally. It is a future todo to
            # filter out headers which are known to be ineffective for
            # indexing since they just take space in the table and
```
---
- **C:\industria\.venv\Lib\site-packages\httplib2\__init__.py:50** — `# TODO: remove this fallback and copypasted socksipy module upon py2/3 merge,`
```
import socks
except ImportError:
    # TODO: remove this fallback and copypasted socksipy module upon py2/3 merge,
    # idea is to have soft-dependency on any compatible module called socks
    from . import socks
```
---
- **C:\industria\.venv\Lib\site-packages\httpx\_auth.py:267** — `# TODO: implement auth-int`
```
path = request.url.raw_path
        A2 = b":".join((request.method.encode(), path))
        # TODO: implement auth-int
        HA2 = digest(A2)
```
---
- **C:\industria\.venv\Lib\site-packages\itsdangerous\timed.py:182** — `# TODO: Signature is incompatible because parameters were added`
```
return t.cast("cabc.Iterator[TimestampSigner]", super().iter_unsigners(salt))

    # TODO: Signature is incompatible because parameters were added
    #  before salt.
```
---
- **C:\industria\.venv\Lib\site-packages\jinja2\ext.py:251** — `# TODO: the i18n extension is currently reevaluating values in a few`
```
tags = {"trans"}

    # TODO: the i18n extension is currently reevaluating values in a few
    # situations.  Take this example:
    #   {% trans count=something() %}{{ count }} foo{% pluralize
```
---
- **C:\industria\.venv\Lib\site-packages\jinja2\nodes.py:212** — `todo = deque([self])`
```
targets and other nodes to a store context.
        """
        todo = deque([self])
        while todo:
            node = todo.popleft()
```
---
- **C:\industria\.venv\Lib\site-packages\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\conftest.py:105** — `# FIXME when yield tests are gone.`
```
pytest.exit("GIL re-enabled during tests", returncode=1)

# FIXME when yield tests are gone.
@pytest.hookimpl()
def pytest_itemcollected(item):
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\__init__.py:927** — `# TODO: Remove the environment variable entirely now that it is "weak"`
```
_core.multiarray._multiarray_umath._reload_guard()

    # TODO: Remove the environment variable entirely now that it is "weak"
    if (os.environ.get("NPY_PROMOTION_STATE", "weak") != "weak"):
        warnings.warn(
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\capi_maps.py:249** — `# TODO: support Fortran `len` function with optional kind parameter`
```
"""
    # TODO: support Fortran `len` function with optional kind parameter
    expr = re.sub(r'\blen\b', 'f2py_slen', expr)
    return expr
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\cfuncs.py:745** — `/* TODO: change the type of `len` so that we can remove this */`
```
}
    if (*len == -1) {
        /* TODO: change the type of `len` so that we can remove this */
        if (n > NPY_MAX_INT) {
            PyErr_SetString(PyExc_OverflowError,
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\crackfortran.py:133** — `TODO:`
```
In addition, the following attributes are used: check,depend,note

TODO:
    * Apply 'parameter' attribute (e.g. 'integer parameter :: i=2' 'real x(i)'
                                   -> 'real x(2)')
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\f2py2e.py:461** — `# TODO: Remove all this when scaninputline is replaced`
```
pyf_files, _ = filter_files("", "[.]pyf([.]src|)", comline_list)
    # Checks that no existing modulename is defined in a pyf file
    # TODO: Remove all this when scaninputline is replaced
    if args.module_name:
        if "-h" in comline_list:
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\symbolic.py:23** — `# TODO: support logical constants (Op.BOOLEAN)`
```
# contain C expressions that support here is implemented as well.
#
# TODO: support logical constants (Op.BOOLEAN)
# TODO: support logical operators (.AND., ...)
# TODO: support defined operators (.MYOP., ...)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\_isocbind.py:55** — `# TODO: See gh-25229`
```
}

# TODO: See gh-25229
isoc_c2pycode_map = {}
iso_c2py_map = {}
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\src\fortranobject.c:1371** — `// TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).`
```
sprintf(localbuf, "%s instance", Py_TYPE(obj)->tp_name);
  }
  // TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).
  strcpy(buf, localbuf);
  return 1;
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\tests\test_docs.py:64** — `# TODO: implement test methods for other example Fortran codes`
```
np.array([1, 45, 3], dtype=np.float32))

    # TODO: implement test methods for other example Fortran codes
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\f2py\tests\test_f2py2e.py:415** — `# TODO: Clean up to prevent passing --overwrite-signature`
```
capslo = re.compile(r"Block: hi")
    # Case I: --lower is implied by -h
    # TODO: Clean up to prevent passing --overwrite-signature
    monkeypatch.setattr(
        sys,
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\fft\__init__.py:203** — `# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should`
```
"""

# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should
# be deleted once downstream libraries move to `numpy.fft`.
from . import _helper, _pocketfft, helper
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\mixins.py:166** — `# TODO: handle the optional third argument for __pow__?`
```
__rdivmod__ = _reflected_binary_method(um.divmod, 'divmod')
    # __idivmod__ does not exist
    # TODO: handle the optional third argument for __pow__?
    __pow__, __rpow__, __ipow__ = _numeric_methods(um.power, 'pow')
    __lshift__, __rlshift__, __ilshift__ = _numeric_methods(
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\_datasource.py:71** — `# TODO: .zip support, .tar support?`
```
# deferring the import of lzma, bz2 and gzip until needed

# TODO: .zip support, .tar support?
class _FileOpeners:
    """
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\_function_base_impl.py:866** — `# TODO: This preserves the Python int, float, complex manually to get the`
```
raise ValueError("select with an empty condition list is not possible")

    # TODO: This preserves the Python int, float, complex manually to get the
    #       right `result_type` with NEP 50.  Most likely we will grow a better
    #       way to spell this (and this can be replaced).
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\_nanfunctions_impl.py:1689** — `# TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?`
```
See nanpercentile for parameter usage
    """
    # TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?
    arr1d, weights, overwrite_input = _remove_nan_1d(arr1d,
        second_arr1d=weights, overwrite_input=overwrite_input)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\_npyio_impl.py:249** — `# FIXME: This seems like it will copy strings around`
```
bytes.seek(0)
                if magic == format.MAGIC_PREFIX:
                    # FIXME: This seems like it will copy strings around
                    #   more than is strictly necessary.  The zipfile
                    #   will read the string and then
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\tests\test_function_base.py:3816** — `# TODO: Note that times have dubious rounding as of fixing NaTs!`
```
@pytest.mark.parametrize("pos", [0, 23, 10])
    def test_nat_basic(self, dtype, pos):
        # TODO: Note that times have dubious rounding as of fixing NaTs!
        # NaT and NaN should behave the same, do basic tests for NaT:
        a = np.arange(0, 24, dtype=dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\tests\test_io.py:323** — `sup.filter(ResourceWarning)  # TODO: specify exact message`
```
# collector, so we catch the warnings.
            with suppress_warnings() as sup:
                sup.filter(ResourceWarning)  # TODO: specify exact message
                for i in range(1, 1025):
                    try:
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\tests\test_recfunctions.py:560** — `# Fixme, this test looks incomplete and broken`
```
z = self.data[-1]

        # Fixme, this test looks incomplete and broken
        #test = merge_arrays((z, np.array([10, 20, 30]).view([('C', int)])))
        #control = np.array([('A', 1., 10), ('B', 2., 20), ('-1', -1, 20)],
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\lib\tests\test_type_check.py:279** — `# Fixme, wrong place, isfinite now ufunc`
```
class TestIsfinite:
    # Fixme, wrong place, isfinite now ufunc

    def test_goodvalues(self):
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\linalg\tests\test_linalg.py:1059** — `# FIXME the 'e' dtype might work in future`
```
noninv = array([[1, 0], [0, 0]])
    stacked = np.block([[[rshft_0]]] * 2)
    # FIXME the 'e' dtype might work in future
    dtnoinv = [object, np.dtype('e'), np.dtype('g'), np.dtype('G')]
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\ma\core.py:237** — `# TODO: This is probably a mess, but should best preserve behavior?`
```
# for integer casts, this allows the use of 99999 as a fill value
        # for int8.
        # TODO: This is probably a mess, but should best preserve behavior?
        vals = tuple(
                np.array(_recursive_fill_value(dtype[name], f))
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\ma\tests\test_core.py:5617** — `# TODO: Test masked_object, masked_equal, ...`
```
class TestMaskedWhereAliases:

    # TODO: Test masked_object, masked_equal, ...

    def test_masked_values(self):
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\ma\tests\test_old_ma.py:720** — `# TODO FIXME: Find out what the following raises a warning in r8247`
```
def test_testScalarArithmetic(self):
        xm = array(0, mask=1)
        # TODO FIXME: Find out what the following raises a warning in r8247
        with np.errstate(divide='ignore'):
            assert_((1 / array(0)).mask)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\polynomial\chebyshev.py:798** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(chebmul, c1, c2)`
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\polynomial\polynomial.py:405** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(polymul, c1, c2)`
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\polynomial\polyutils.py:538** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    lc1 = len(c1)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\polynomial\_polybase.py:432** — `# TODO: we're stuck with disabling math formatting until we handle`
```
@staticmethod
    def _repr_latex_scalar(x, parens=False):
        # TODO: we're stuck with disabling math formatting until we handle
        # exponents in this function
        return fr'\text{{{pu.format_float(x, parens=parens)}}}'
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\random\tests\test_random.py:1069** — `# TODO: Include test for randint once it can broadcast`
```
np.random.seed(self.seed)

    # TODO: Include test for randint once it can broadcast
    # Can steal the test written in PR #6938
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\arrayprint.py:1567** — `# TODO: Custom repr for user DTypes, logic should likely move.`
```
"""
    if type(dtype).__repr__ != np.dtype.__repr__:
        # TODO: Custom repr for user DTypes, logic should likely move.
        return repr(dtype)
    if dtype.names is not None:
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\fromnumeric.py:44** — `# but this follows what was done before. TODO: revisit this.`
```
conv = _array_converter(obj)
    # As this already tried the method, subok is maybe quite reasonable here
    # but this follows what was done before. TODO: revisit this.
    arr, = conv.as_arrays(subok=False)
    result = getattr(arr, method)(*args, **kwds)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\getlimits.py:374** — `TODO: MachAr should be retired completely ideally.  We currently only`
```
""" Create MachAr instance with found information on float types

    TODO: MachAr should be retired completely ideally.  We currently only
          ever use it system with broken longdouble (valgrind, WSL).
    """
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\numeric.py:545** — `# TODO: this works around .astype(bool) not working properly (gh-9847)`
```
a = asanyarray(a)

    # TODO: this works around .astype(bool) not working properly (gh-9847)
    if np.issubdtype(a.dtype, np.character):
        a_bool = a != a.dtype.type()
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\_add_newdocs.py:2276** — `assignment examples; TODO).`
```
Flattened version of the array as an iterator.  The iterator
        allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
        assignment examples; TODO).
    imag : ndarray
        Imaginary part of the array.
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\_add_newdocs_scalars.py:129** — `# TODO: These docs probably need an if to highlight the default rather than`
```
""")

# TODO: These docs probably need an if to highlight the default rather than
#       the C-types (and be correct).
add_newdoc_for_scalar_type('int_', [],
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\_dtype.py:174** — `# TODO: this path can never be reached`
```
return native.byteorder
    if byteorder == 'S':
        # TODO: this path can never be reached
        return swapped.byteorder
    elif byteorder == '|':
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\_methods.py:88** — `# TODO: Optimize case when `where` is broadcast along a non-reduction`
```
items = nt.intp(items)
    else:
        # TODO: Optimize case when `where` is broadcast along a non-reduction
        # axis and full sum is more excessive than needed.
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_array_coercion.py:452** — `# TODO: This discrepancy _should_ be resolved, either by relaxing the`
```
# case, and traditionally in most cases the behaviour is maintained
        # like this.  (`np.array(scalar, dtype="U6")` would have failed before)
        # TODO: This discrepancy _should_ be resolved, either by relaxing the
        #       cast, or by deprecating the first part.
        scalar = np.datetime64(val, unit)
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_casting_unittests.py:781** — `# TODO: While this test is fairly thorough, right now, it does not`
```
def test_structured_view_offsets_parametric(
            self, from_dt, to_dt, expected_off):
        # TODO: While this test is fairly thorough, right now, it does not
        # really test some paths that may have nonzero offsets (they don't
        # really exists).
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_datetime.py:1585** — `# TODO: Allowing unsafe casting by`
```
# should raise between datetime and timedelta
        #
        # TODO: Allowing unsafe casting by
        #       default in ufuncs strikes again... :(
        a = np.array(3, dtype='m8[h]')
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_machar.py:19** — `# Fixme, this needs to raise a 'skip' exception.`
```
MachAr(lambda v: array(v, hiprec))
        except AttributeError:
            # Fixme, this needs to raise a 'skip' exception.
            "Skipping test: no ntypes.float96 available on this platform."
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_multiarray.py:6360** — `# FIXME:`
```
# stats for integer types
        # FIXME:
        # this needs definition as there are lots places along the line
        # where type casting may take place.
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_scalarmath.py:103** — `# TODO: It would be nice to resolve this issue.`
```
# array**scalar special case can have different result dtype
        # (Other powers may have issues also, but are not hit here.)
        # TODO: It would be nice to resolve this issue.
        pytest.skip("array**2 can have incorrect/weird result dtype")
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_stringdtype.py:1521** — `# TODO: generalize to more ufuncs`
```
# accept more than one string argument and produce a string should
    # behave this way
    # TODO: generalize to more ufuncs
    inp = ["hello", "world"]
    arr = np.array(inp, dtype=StringDType(na_object=None))
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_umath.py:1152** — `# FIXME cinf not tested.`
```
one = np.array([1 + 0j])
        cnan = np.array([complex(np.nan, np.nan)])
        # FIXME cinf not tested.
        #cinf = np.array([complex(np.inf, 0)])
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_core\tests\test_umath_complex.py:17** — `# TODO: branch cuts (use Pauli code)`
```
)

# TODO: branch cuts (use Pauli code)
# TODO: conj 'symmetry'
# TODO: FPU exceptions
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_typing\_array_like.py:48** — `# TODO: Wait until mypy supports recursive objects in combination with typevars`
```
# TODO: Wait until mypy supports recursive objects in combination with typevars
_FiniteNestedSequence: TypeAlias = (
    _T
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_typing\_char_codes.py:211** — `# TODO: add `_StringCodes` once it has a scalar type`
```
_TD64Codes,
    _ObjectCodes,
    # TODO: add `_StringCodes` once it has a scalar type
    # _StringCodes,
]
```
---
- **C:\industria\.venv\Lib\site-packages\numpy\_typing\_dtype_like.py:31** — `_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types`
```
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True)

_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types
```
---
- **C:\industria\.venv\Lib\site-packages\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\.venv\Lib\site-packages\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\.venv\Lib\site-packages\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\_typing.py:386** — `# TODO(typing#684): add Ellipsis, see`
```
# PositionalIndexerTuple is extends the PositionalIndexer for 2D arrays
# These are used in various __getitem__ overloads
# TODO(typing#684): add Ellipsis, see
# https://github.com/python/typing/issues/684#issuecomment-548203158
# https://bugs.python.org/issue41810
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\api\typing\__init__.py:29** — `# TODO: Can't import Styler without importing jinja2`
```
)

# TODO: Can't import Styler without importing jinja2
# from pandas.io.formats.style import Styler
from pandas.io.json._json import JsonReader
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\algorithms.py:155** — `# e.g. Sparse[bool, False]  # TODO: no test cases get here`
```
return np.asarray(values).view("uint8")
        else:
            # e.g. Sparse[bool, False]  # TODO: no test cases get here
            return np.asarray(values).astype("uint8", copy=False)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\apply.py:922** — `# TODO: Avoid having to change state`
```
axis = self.axis

        # TODO: Avoid having to change state
        self.obj = self.obj if self.axis == 0 else self.obj.T
        self.axis = 0
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arraylike.py:361** — `# TODO: When we support multiple values in __finalize__, this`
```
result, **reconstruct_axes, **reconstruct_kwargs, copy=False
            )
        # TODO: When we support multiple values in __finalize__, this
        # should pass alignable to `__finalize__` instead of self.
        # Then `np.add(a, b)` would consider attrs from both a and b
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\base.py:227** — `# TODO: following GH#45287 can we now use .drop directly without`
```
# equivalent to `self.obj.drop(self.exclusions, axis=1)
            #  but this avoids consolidating and making a copy
            # TODO: following GH#45287 can we now use .drop directly without
            #  making a copy?
            return self.obj._drop_axis(self.exclusions, axis=1, only_slice=True)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\common.py:342** — `# TODO: used only once in indexing; belongs elsewhere?`
```
# TODO: used only once in indexing; belongs elsewhere?
def is_full_slice(obj, line: int) -> bool:
    """
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\config_init.py:426** — `# TODO(3.0): enforcing this deprecation will close GH#52501`
```
def use_inf_as_na_cb(key) -> None:
    # TODO(3.0): enforcing this deprecation will close GH#52501
    from pandas.core.dtypes.missing import _use_inf_as_na
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\construction.py:795** — `# TODO: test cases with arr.dtype.kind in "mM"`
```
elif dtype.kind == "U":
        # TODO: test cases with arr.dtype.kind in "mM"
        if is_ndarray:
            arr = cast(np.ndarray, arr)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\frame.py:896** — `# TODO(EA2D): special case not needed with 2D EAs`
```
# For data is a scalar extension dtype
            if isinstance(dtype, ExtensionDtype):
                # TODO(EA2D): special case not needed with 2D EAs

                values = [
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\generic.py:5587** — `# TODO: Decide if we care about having different examples for different`
```
See the :ref:`user guide <basics.reindexing>` for more.
        """
        # TODO: Decide if we care about having different examples for different
        # kinds
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexing.py:949** — `# FIXME: this assumes only one Ellipsis`
```
#  treat as a single null slice.
                i = tup.index(Ellipsis)
                # FIXME: this assumes only one Ellipsis
                new_key = tup[:i] + (_NS,) + tup[i + 1 :]
                return new_key
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\nanops.py:128** — `# TODO(GH-18976) update all the nanops methods to`
```
# Only applies for the default `min_count` of None
                # since that affects how empty arrays are handled.
                # TODO(GH-18976) update all the nanops methods to
                # correctly handle empty inputs and remove this check.
                # It *may* just be `var`
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\resample.py:448** — `# TODO: test_resample_apply_with_additional_args fails if we go`
```
try:
            if callable(how):
                # TODO: test_resample_apply_with_additional_args fails if we go
                #  through the non-lambda path, not clear that it should.
                func = lambda x: how(x, *args, **kwargs)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\series.py:2271** — `# TODO: integrate bottleneck`
```
# Statistics, overridden ndarray methods

    # TODO: integrate bottleneck
    def count(self) -> int:
        """
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\base.py:2170** — `# TODO(3.0): this can be removed once GH#33302 deprecation is enforced`
```
return result

    # TODO(3.0): this can be removed once GH#33302 deprecation is enforced
    def _fill_mask_inplace(
        self, method: str, limit: int | None, mask: npt.NDArray[np.bool_]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\categorical.py:2147** — `# TODO: GH#15362`
```
# max(np.uint64) as the missing value indicator
        #
        # TODO: GH#15362

        mask = self.isna()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\datetimelike.py:350** — `# TODO: Remove Datetime & DatetimeTZ formatters.`
```
def _formatter(self, boxed: bool = False):
        # TODO: Remove Datetime & DatetimeTZ formatters.
        return "'{}'".format
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\datetimes.py:286** — `# TODO: require any NAs be valid-for-DTA`
```
def _from_scalars(cls, scalars, *, dtype: DtypeObj) -> Self:
        if lib.infer_dtype(scalars, skipna=True) not in ["datetime", "datetime64"]:
            # TODO: require any NAs be valid-for-DTA
            # TODO: if dtype is passed, check for tzawareness compat?
            raise ValueError
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\interval.py:858** — `# TODO: in an IntervalIndex we can reuse the cached`
```
if ascending and kind == "quicksort" and na_position == "last":
            # TODO: in an IntervalIndex we can reuse the cached
            #  IntervalTree.left_sorter
            return np.lexsort((self.right, self.left))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\masked.py:290** — `# TODO: get this all from np_can_hold_element?`
```
"""
        kind = self.dtype.kind
        # TODO: get this all from np_can_hold_element?
        if kind == "b":
            if lib.is_bool(value):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\numeric.py:93** — `# TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed`
```
if isinstance(array, pyarrow.ChunkedArray):
            # TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed
            # combine_chunks for empty arrays https://github.com/apache/arrow/pull/13757
            if array.num_chunks == 0:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\numpy_.py:301** — `# TODO: assert we have floating dtype?`
```
out_data = self._ndarray.copy()

        # TODO: assert we have floating dtype?
        missing.interpolate_2d_inplace(
            out_data,
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\period.py:702** — `# TODO: other cases?`
```
elif diff == 1:
                    dta._freq = self.freq.base
                # TODO: other cases?
            return dta
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\string_.py:198** — `# TODO add more informative repr`
```
return f"{self.name}[{self.storage}]"
        else:
            # TODO add more informative repr
            return self.name
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py:74** — `# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from`
```
# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from
# ObjectStringArrayMixin because we want to have the object-dtype based methods as
# fallback for the ones that pyarrow doesn't yet support
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\_mixins.py:363** — `# TODO: NumpyExtensionArray didn't used to copy, need tests`
```
npvalues = npvalues.T

                # TODO: NumpyExtensionArray didn't used to copy, need tests
                #  for this
                new_values = self._from_backing_data(npvalues)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\arrow\accessors.py:151** — `# TODO: Support negative key but pyarrow does not allow`
```
if isinstance(key, int):
            # TODO: Support negative key but pyarrow does not allow
            # element index to be an array.
            # if key < 0:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\arrow\array.py:133** — `# TODO: Replace with pyarrow floordiv kernel.`
```
right: pa.ChunkedArray | pa.Array | pa.Scalar,
    ) -> pa.ChunkedArray:
        # TODO: Replace with pyarrow floordiv kernel.
        # https://github.com/apache/arrow/issues/39386
        if pa.types.is_integer(left.type) and pa.types.is_integer(right.type):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\arrays\sparse\array.py:384** — `# TODO: make kind=None, and use data.kind?`
```
if dtype is None:
                dtype = data.dtype
            # TODO: make kind=None, and use data.kind?
            data = data.sp_values
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\array_algos\putmask.py:78** — `# TODO: this prob needs some better checking for 2D cases`
```
new = new.astype(values.dtype, copy=False)

    # TODO: this prob needs some better checking for 2D cases
    nlocs = mask.sum()
    if nlocs > 0 and is_list_like(new) and getattr(new, "ndim", 1) == 1:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\array_algos\replace.py:85** — `# TODO: should use missing.mask_missing?`
```
if not regex or not should_use_regex(regex, b):
        # TODO: should use missing.mask_missing?
        op = lambda x: operator.eq(x, b)
    else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\array_algos\take.py:361** — `# FIXME: if we get here with dt64/td64 we need to be sure we have`
```
out = out.view(out_dtype)
        if fill_wrap is not None:
            # FIXME: if we get here with dt64/td64 we need to be sure we have
            #  matching resos
            if fill_value.dtype.kind == "m":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\computation\eval.py:66** — `# TODO: validate this in a more general way (thinking of future engines`
```
)

    # TODO: validate this in a more general way (thinking of future engines
    # that won't necessarily be import-able)
    # Could potentially be done on engine instantiation
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\computation\expr.py:547** — `# TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min`
```
return self.term_type(node.id, self.env, **kwargs)

    # TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min
    def visit_NameConstant(self, node, **kwargs) -> Term:
        return self.const_type(node.value, self.env)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\computation\pytables.py:441** — `# TODO: return None might never be reached`
```
elif isinstance(node.op, ast.UAdd):
            raise NotImplementedError("Unary addition not supported")
        # TODO: return None might never be reached
        return None
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\dtypes\cast.py:286** — `# TODO: complex?  what if result is already non-object?`
```
else:
                # TODO: complex?  what if result is already non-object?
                dtype = "object"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\dtypes\common.py:1519** — `# TODO: Implement this properly`
```
pass
        if hasattr(dtype, "numpy_dtype"):
            # TODO: Implement this properly
            # https://github.com/pandas-dev/pandas/issues/52576
            return dtype.numpy_dtype.type
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\dtypes\dtypes.py:209** — `# TODO: Document public vs. private API`
```
"""

    # TODO: Document public vs. private API
    name = "category"
    type: type[CategoricalDtypeType] = CategoricalDtypeType
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\dtypes\missing.py:520** — `# TODO: fastpath for pandas' StringDtype`
```
return _array_equivalent_datetimelike(left, right)
        elif is_string_or_object_np_dtype(left.dtype):
            # TODO: fastpath for pandas' StringDtype
            return _array_equivalent_object(left, right, strict_nan)
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\groupby\generic.py:116** — `# TODO(typing) the return value on this callable should be any *scalar*.`
```
from pandas.core.generic import NDFrame

# TODO(typing) the return value on this callable should be any *scalar*.
AggScalar = Union[str, Callable[..., Any]]
# TODO: validate types on ScalarResult and move to _typing
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\groupby\groupby.py:792** — `# TODO: Better repr for GroupBy object`
```
@final
    def __repr__(self) -> str:
        # TODO: Better repr for GroupBy object
        return object.__repr__(self)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\groupby\grouper.py:358** — `# TODO: What are we assuming about subsequent calls?`
```
# Keep self._grouper value before overriding
        if self._grouper is None:
            # TODO: What are we assuming about subsequent calls?
            self._grouper = gpr_index
            self._indexer = self._indexer_deprecated
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\groupby\ops.py:468** — `# TODO: min_count`
```
raise NotImplementedError(f"{self.how} is not implemented")
        else:
            # TODO: min_count
            if self.how != "rank":
                # TODO: should rank take result_mask?
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\api.py:145** — `# TODO: handle index names!`
```
Index
    """
    # TODO: handle index names!
    indexes = _get_distinct_objs(indexes)
    if len(indexes) == 0:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\base.py:1465** — `# TODO: why do we need different justify for these cases?`
```
or isinstance(self.dtype, (IntervalDtype, CategoricalDtype))
        ):
            # TODO: why do we need different justify for these cases?
            justify = "all"
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\datetimelike.py:230** — `# TODO: not reached in tests 2023-10-11`
```
self, *, header: list[str], na_rep: str, date_format: str | None = None
    ) -> list[str]:
        # TODO: not reached in tests 2023-10-11
        # matches base class except for whitespace padding and date_format
        return header + list(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\datetimes.py:98** — `# TODO: If we knew what was going in to **d, we might be able to`
```
else:
        with warnings.catch_warnings():
            # TODO: If we knew what was going in to **d, we might be able to
            #  go through _simple_new instead
            warnings.simplefilter("ignore")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\frozen.py:70** — `# TODO: Consider deprecating these in favor of `union` (xref gh-15506)`
```
return type(self)(temp)

    # TODO: Consider deprecating these in favor of `union` (xref gh-15506)
    # error: Incompatible types in assignment (expression has type
    # "Callable[[FrozenList, Any], FrozenList]", base class "list" defined the
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\interval.py:685** — `# TODO: DO this in maybe_booleans_to_slice?`
```
res = lib.maybe_booleans_to_slice(mask.view("u1"))
        if isinstance(res, slice) and res.stop is None:
            # TODO: DO this in maybe_booleans_to_slice?
            res = slice(res.start, len(self), res.step)
        return res
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\multi.py:2996** — `# TODO: need is_valid_na_for_dtype(key, level_index.dtype)`
```
"""
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\period.py:302** — `# TODO: We can do some of these with no-copy / coercion?`
```
if freq and isinstance(data, cls) and data.freq != freq:
                # TODO: We can do some of these with no-copy / coercion?
                # e.g. D -> 2D seems to be OK
                data = data.asfreq(freq)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\indexes\range.py:1108** — `# TODO: if other is a RangeIndex we may have more efficient options`
```
step = op

        # TODO: if other is a RangeIndex we may have more efficient options
        right = extract_array(other, extract_numpy=True, extract_range=True)
        left = self
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\interchange\column.py:115** — `# TODO: chunks are implemented now, probably this should return something`
```
Offset of first element. Always zero.
        """
        # TODO: chunks are implemented now, probably this should return something
        return 0
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\interchange\dataframe_protocol.py:407** — `# TODO: not happy with Optional, but need to flag it may be expensive`
```
@abstractmethod
    def num_rows(self) -> int | None:
        # TODO: not happy with Optional, but need to flag it may be expensive
        #       why include it if it may be None - what do we expect consumers
        #       to do here?
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\interchange\from_dataframe.py:470** — `# TODO: No DLPack yet, so need to construct a new ndarray from the data pointer`
```
raise NotImplementedError(f"Conversion for {dtype} is not yet supported.")

    # TODO: No DLPack yet, so need to construct a new ndarray from the data pointer
    # and size in the buffer plus the dtype on the column. Use DLPack as NumPy supports
    # it since https://github.com/numpy/numpy/pull/19083
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\interchange\utils.py:139** — `# TODO(infer_string) this should be LARGE_STRING for pyarrow storage,`
```
if isinstance(dtype, pd.StringDtype):
        # TODO(infer_string) this should be LARGE_STRING for pyarrow storage,
        # but current tests don't cover this distinction
        return ArrowCTypes.STRING
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\array_manager.py:366** — `# TODO what is this used for?`
```
def is_view(self) -> bool:
        """return a boolean if we are a single block and are a view"""
        # TODO what is this used for?
        return False
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\base.py:66** — `# TODO share more methods/attributes`
```
class DataManager(PandasObject):
    # TODO share more methods/attributes

    axes: list[Index]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\blocks.py:420** — `# TODO(EA2D): unnecessary with 2D EAs`
```
# See also: split_and_operate
        if result.ndim > 1 and isinstance(result.dtype, ExtensionDtype):
            # TODO(EA2D): unnecessary with 2D EAs
            # if we get a 2D ExtensionArray, we need to split it into 1D pieces
            nbs = []
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\concat.py:114** — `# TODO(ArrayManager) this assumes that all managers are of the same type`
```
needs_copy = copy and concat_axis == 0

    # TODO(ArrayManager) this assumes that all managers are of the same type
    if isinstance(mgrs_indexers[0][0], ArrayManager):
        mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\construction.py:397** — `# TODO: check len(values) == 0?`
```
if len(columns) == 0:
        # TODO: check len(values) == 0?
        block_values = []
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\managers.py:536** — `# FIXME: optimization potential`
```
return self.make_empty()

        # FIXME: optimization potential
        indexer = np.sort(np.concatenate([b.mgr_locs.as_array for b in blocks]))
        inv_indexer = lib.get_reverse_indexer(indexer, self.shape[0])
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\internals\ops.py:120** — `# TODO(EA2D): with 2D EAs only this first clause would be needed`
```
assert rblk.mgr_locs.is_slice_like, rblk.mgr_locs

    # TODO(EA2D): with 2D EAs only this first clause would be needed
    if not (left_ea or right_ea):
        # error: No overload variant of "__getitem__" of "ExtensionArray" matches
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\ops\array_ops.py:234** — `# TODO: can remove this after dropping some future numpy version?`
```
# numpy returned a scalar instead of operating element-wise
        # e.g. numeric array vs str
        # TODO: can remove this after dropping some future numpy version?
        return invalid_comparison(left, right, op)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\concat.py:534** — `# TODO: retain levels?`
```
if isinstance(keys, MultiIndex):
                # TODO: retain levels?
                keys = type(keys).from_tuples(clean_keys, names=keys.names)
            else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\melt.py:477** — `# TODO: anything else to catch?`
```
newdf[j] = to_numeric(newdf[j])
        except (TypeError, ValueError, OverflowError):
            # TODO: anything else to catch?
            pass
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\merge.py:285** — `# TODO, should merge_pieces do this?`
```
# make sure join keys are in the merged
        # TODO, should merge_pieces do this?
        merged[by] = key
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\pivot.py:60** — `# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency`
```
# Note: We need to make sure `frame` is imported before `pivot`, otherwise
# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency
@Substitution("\ndata : DataFrame")
@Appender(_shared_docs["pivot_table"], indents=1)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\reshape.py:229** — `# TODO: in all tests we have mask.any(0).all(); can we rely on that?`
```
new_values, mask = self.get_new_values(dummy_arr, fill_value=-1)
        return new_values, mask.any(0)
        # TODO: in all tests we have mask.any(0).all(); can we rely on that?

    def get_result(self, values, value_columns, fill_value) -> DataFrame:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\reshape\tile.py:503** — `# TODO: handle mismatch between categorical label order and pandas.cut order.`
```
ordered=ordered,
            )
        # TODO: handle mismatch between categorical label order and pandas.cut order.
        np.putmask(ids, na_mask, 0)
        result = algos.take_nd(labels, ids - 1)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\strings\accessor.py:186** — `# TODO: Dispatch all the methods`
```
# Note: see the docstring in pandas.core.strings.__init__
    # for an explanation of the implementation.
    # TODO: Dispatch all the methods
    # Currently the following are not dispatched to the array
    # * cat
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\strings\object_array.py:92** — `# FIXME: this should be totally avoidable`
```
if len(err.args) >= 1 and re.search(p_err, err.args[0]):
                # FIXME: this should be totally avoidable
                raise err
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\tools\datetimes.py:370** — `# TODO: Combine with above if DTI/DTA supports Arrow timestamps`
```
elif isinstance(arg_dtype, ArrowDtype) and arg_dtype.type is Timestamp:
        # TODO: Combine with above if DTI/DTA supports Arrow timestamps
        if utc:
            # pyarrow uses UTC, not lowercase utc
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\window\rolling.py:391** — `# TODO: sure we want to overwrite results?`
```
extra_col = Series(self._on, index=self.obj.index, name=name, copy=False)
            if name in result.columns:
                # TODO: sure we want to overwrite results?
                result[name] = extra_col
            elif name in result.index.names:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\_numba\executor.py:125** — `# TODO: Preserve complex dtypes`
```
# TODO: Preserve complex dtypes

float_dtype_mapping: dict[np.dtype, Any] = {
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\core\_numba\extensions.py:66** — `# TODO: Range index support`
```
# TODO: Range index support
# (this currently lowers OK, but does not round-trip)
class IndexType(types.Type):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\common.py:373** — `# TODO: fsspec can also handle HTTP via requests, but leaving this`
```
if isinstance(filepath_or_buffer, str) and is_url(filepath_or_buffer):
        # TODO: fsspec can also handle HTTP via requests, but leaving this
        # unchanged. using fsspec appears to break the ability to infer if the
        # server responded with gzipped data
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\pytables.py:1222** — `#  _table_mod.NoSuchNodeError.  TODO: Catch only these?`
```
except Exception as err:
            # In tests we get here with ClosedFileError, TypeError, and
            #  _table_mod.NoSuchNodeError.  TODO: Catch only these?

            if where is not None:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\sql.py:120** — `# TODO: not reached 2023-10-27; needed?`
```
return to_datetime(col, **format)
            except (TypeError, ValueError):
                # TODO: not reached 2023-10-27; needed?
                return col
        return to_datetime(col, errors=error, **format)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\stata.py:339** — `# TODO(non-nano): If/when pandas supports more than datetime64[ns], this`
```
return base + deltas

    # TODO(non-nano): If/when pandas supports more than datetime64[ns], this
    #  should be improved to use correct range, e.g. datetime[Y] for yearly
    bad_locs = np.isnan(dates)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\clipboard\__init__.py:274** — `# TODO: https://github.com/asweigart/pyperclip/issues/43`
```
# Workaround for https://bugs.kde.org/show_bug.cgi?id=342874
        # TODO: https://github.com/asweigart/pyperclip/issues/43
        clipboardContents = stdout.decode(ENCODING)
        # even if blank, Klipper will append a newline at the end
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\excel\_pyxlsb.py:63** — `# TODO: hack in buffer capability`
```
from pyxlsb import open_workbook

        # TODO: hack in buffer capability
        # This might need some modifications to the Pyxlsb library
        # Actual work for opening it is in xlsbpackage.py, line 20-ish
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\excel\_xlsxwriter.py:134** — `# TODO: support other fill patterns`
```
if isinstance(props.get("pattern"), str):
            # TODO: support other fill patterns
            props["pattern"] = 0 if props["pattern"] == "none" else 1
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\formats\css.py:106** — `# TODO: Can we use current color as initial value to comply with CSS standards?`
```
)

        # TODO: Can we use current color as initial value to comply with CSS standards?
        border_declarations = {
            f"border{side}-color": "black",
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\formats\excel.py:238** — `# TODO: handle cell width and height: needs support in pandas.io.excel`
```
}

        # TODO: handle cell width and height: needs support in pandas.io.excel

        def remove_none(d: dict[str, str | None]) -> None:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\formats\format.py:1227** — `# TODO(3.0): this will be unreachable when use_inf_as_na`
```
return str(NA)
                elif lib.is_float(x) and np.isinf(x):
                    # TODO(3.0): this will be unreachable when use_inf_as_na
                    #  deprecation is enforced
                    return str(x)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\formats\html.py:337** — `# TODO: Refactor to remove code duplication with code`
```
# MultiIndex Columns and Index.
                # Initially fill row with blank cells before column names.
                # TODO: Refactor to remove code duplication with code
                # block below for standard columns index.
                row = [""] * (self.row_levels - 1)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\formats\style_render.py:878** — `# TODO try to consolidate the concat visible rows`
```
row_indices: list[int] = []
            _concatenated_visible_rows(obj, 0, row_indices)
            # TODO try to consolidate the concat visible rows
            # methods to a single function / recursion for simplicity
            return row_indices
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\json\_json.py:374** — `# TODO: Do this timedelta properly in objToJSON.c See GH #15137`
```
)

        # TODO: Do this timedelta properly in objToJSON.c See GH #15137
        if (
            (obj.ndim == 1)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\json\_normalize.py:466** — `# TODO: handle record value which are lists, at least error`
```
#  {VeryLong: { b: 1,c:2}} -> {VeryLong.b:1 ,VeryLong.c:@}
            #
            # TODO: handle record value which are lists, at least error
            #       reasonably
            data = nested_to_record(data, sep=sep, max_level=max_level)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\parsers\base_parser.py:813** — `# TODO: this is for consistency with`
```
if not is_object_dtype(values.dtype) and not known_cats:
                # TODO: this is for consistency with
                # c-parser which parses all categories
                # as strings
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\parsers\python_parser.py:461** — `# TODO: Use pandas.io.common.dedup_names instead (see #50371)`
```
] + this_unnamed_cols

                    # TODO: Use pandas.io.common.dedup_names instead (see #50371)
                    for i in col_loop_order:
                        col = this_columns[i]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\io\parsers\readers.py:1654** — `# TODO: Refactor this logic, its pretty convoluted`
```
if engine != "c" and value != default:
                    # TODO: Refactor this logic, its pretty convoluted
                    if "python" in engine and argname not in _python_unsupported:
                        pass
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\plotting\_matplotlib\converter.py:823** — `# TODO: Check the following : is it really info['fmt'] ?`
```
quarter_start = (dates_ % 3 == 0).nonzero()
        info_maj[year_start] = True
        # TODO: Check the following : is it really info['fmt'] ?
        #  2023-09-15 this is reached in test_finder_monthly
        info["fmt"][quarter_start] = True
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\plotting\_matplotlib\core.py:182** — `# TODO: Might deprecate `column` argument in future PR (#28373)`
```
# Assign the rest of columns into self.columns if by is explicitly defined
        # while column is not, only need `columns` in hist/box plot when it's DF
        # TODO: Might deprecate `column` argument in future PR (#28373)
        if isinstance(data, DataFrame):
            if column:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\plotting\_matplotlib\misc.py:300** — `# TODO: is the failure mentioned below still relevant?`
```
import matplotlib.pyplot as plt

    # TODO: is the failure mentioned below still relevant?
    # random.sample(ndarray, int) fails on python 3.3, sigh
    data = list(series.values)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\plotting\_matplotlib\timeseries.py:1** — `# TODO: Use the fact that axis can have units to simplify the process`
```
# TODO: Use the fact that axis can have units to simplify the process

from __future__ import annotations
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\test_algos.py:68** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
tm.assert_numpy_array_equal(uniques, expected_uniques)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("sort", [True, False])
    def test_factorize(self, index_or_series_obj, sort):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\test_downstream.py:310** — `# TODO: could check with arraylike of Period objects`
```
# Note: we dont do this for PeriodArray bc _from_sequence won't accept
    #  an array of integers
    # TODO: could check with arraylike of Period objects
    arr, data = array_likes
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\test_multilevel.py:161** — `# TODO groupby with level_values drops names`
```
expected = ymd.groupby([k1, k2]).mean()

        # TODO groupby with level_values drops names
        tm.assert_frame_equal(result, expected, check_names=False)
        assert result.index.names == ymd.index.names[:2]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\apply\test_frame_apply.py:1709** — `# TODO: the result below is wrong, should be fixed (GH53325)`
```
tm.assert_frame_equal(result, expected)

    # TODO: the result below is wrong, should be fixed (GH53325)
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = df.agg({"x": foo1}, 0, 3, c=4)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arithmetic\test_datetime64.py:161** — `# TODO: moved from tests.series.test_operators; needs cleanup`
```
class TestDatetime64SeriesComparison:
    # TODO: moved from tests.series.test_operators; needs cleanup

    @pytest.mark.parametrize(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arithmetic\test_numeric.py:50** — `# TODO: add more  dtypes here`
```
@pytest.fixture(
    params=[
        # TODO: add more  dtypes here
        Index(np.arange(5, dtype="float64")),
        Index(np.arange(5, dtype="int64")),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arithmetic\test_object.py:96** — `# TODO: parametrize`
```
tm.assert_index_equal(result, expected)

    # TODO: parametrize
    def test_pow_ops_object(self):
        # GH#22922
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arithmetic\test_period.py:208** — `# TODO: parameterize over boxes`
```
class TestPeriodIndexComparisons:
    # TODO: parameterize over boxes

    def test_pi_cmp_period(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arithmetic\test_timedelta64.py:171** — `# TODO: All of these need to be parametrized over box`
```
class TestTimedelta64ArrayComparisons:
    # TODO: All of these need to be parametrized over box

    @pytest.mark.parametrize("dtype", [None, object])
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\test_datetimelike.py:33** — `# TODO: more freq variants`
```
# TODO: more freq variants
@pytest.fixture(params=["D", "B", "W", "ME", "QE", "YE"])
def freqstr(request):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\test_datetimes.py:93** — `# TODO: simplify once we can just .astype to other unit`
```
assert not dta.is_normalized

        # TODO: simplify once we can just .astype to other unit
        exp = np.asarray(dti.normalize()).astype(f"M8[{unit}]")
        expected = DatetimeArray._simple_new(exp, dtype=exp.dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\test_timedeltas.py:106** — `# TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert`
```
assert result.isna().all()

    # TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert
    #  or tz_localize with non-nano; implement tests specific to that.
    def test_add_datetimelike_scalar(self, tda, tz_naive_fixture):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_arithmetic.py:122** — `# TODO(extension) numpy's mul with object array sees booleans as numbers`
```
# invalid array-likes
    if op not in ("__mul__", "__rmul__"):
        # TODO(extension) numpy's mul with object array sees booleans as numbers
        msg = "|".join(
            [
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_construction.py:155** — `# TODO this is currently not public API`
```
def test_coerce_to_array():
    # TODO this is currently not public API
    values = np.array([True, False, True, False], dtype="bool")
    mask = np.array([False, False, False, True], dtype="bool")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_logical.py:123** — `# TODO: test True & False`
```
)
    def test_kleene_or_scalar(self, other, expected):
        # TODO: test True & False
        a = pd.array([True, False, None], dtype="boolean")
        result = a | other
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\categorical\test_analytics.py:47** — `# TODO: raises if we pass axis=0  (on Index and Categorical, not Series)`
```
assert np.minimum.reduce(obj) == "a"
        assert np.maximum.reduce(obj) == "d"
        # TODO: raises if we pass axis=0  (on Index and Categorical, not Series)

        cat = Categorical(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\categorical\test_indexing.py:374** — `# TODO(Categorical): identify other places where this may be`
```
"""

    # TODO(Categorical): identify other places where this may be
    # useful and move to a conftest.py
    def array(self, dtype=None):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\floating\test_arithmetic.py:39** — `# TODO pending NA/NaN discussion`
```
@pytest.mark.parametrize("zero, negative", [(0, False), (0.0, False), (-0.0, True)])
def test_divide_by_zero(dtype, zero, negative):
    # TODO pending NA/NaN discussion
    # https://github.com/pandas-dev/pandas/issues/32265/
    a = pd.array([0, 1, -1, None], dtype=dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\floating\test_construction.py:172** — `# TODO can we specify "floating" in general?`
```
# for integer dtypes, the itemsize is not preserved
    # TODO can we specify "floating" in general?
    result = pd.array(np.array([1, 2], dtype="int32"), dtype="Float64")
    assert result.dtype == Float64Dtype()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\integer\test_arithmetic.py:196** — `# TODO: doing this fillna to keep tests passing as we make`
```
expected = pd.Series(["foo" * x for x in data], index=s.index)
        expected = expected.fillna(np.nan)
        # TODO: doing this fillna to keep tests passing as we make
        #  assert_almost_equal stricter, but the expected with pd.NA seems
        #  more-correct than np.nan here.
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\integer\test_function.py:199** — `# TODO(jreback) - these need testing / are broken`
```
# TODO(jreback) - these need testing / are broken

# shift
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\interval\test_overlaps.py:62** — `# TODO: modify this test when implemented`
```
@pytest.mark.parametrize("other_constructor", [IntervalArray, IntervalIndex])
    def test_overlaps_interval_container(self, constructor, other_constructor):
        # TODO: modify this test when implemented
        interval_container = constructor.from_breaks(range(5))
        other_container = other_constructor.from_breaks(range(5))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\masked\test_arithmetic.py:57** — `# TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))`
```
scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)

    # TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))
    for scalar in [scalar, data.dtype.type(scalar)]:
        if is_bool_not_implemented(data, all_arithmetic_operators):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\masked\test_indexing.py:22** — `# FIXME: don't leave commented-out`
```
arr[[0]] = invalid

        # FIXME: don't leave commented-out
        # with pytest.raises(TypeError):
        #    arr[[0]] = [invalid]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_constructors.py:106** — `# TODO: actionable?`
```
def test_constructor_spindex_dtype(self):
        arr = SparseArray(data=[1, 2], sparse_index=IntIndex(4, [1, 2]))
        # TODO: actionable?
        # XXX: Behavior change: specifying SparseIndex no longer changes the
        # fill_value
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_indexing.py:208** — `# TODO: actionable?`
```
tm.assert_sp_array_equal(result, expected)

        # TODO: actionable?
        # XXX: test change: fill_value=True -> allow_fill=True
        result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_reductions.py:265** — `# TODO: pin down whether we wrap datetime64("NaT")`
```
result = getattr(arr, func)()
        if expected is NaT:
            # TODO: pin down whether we wrap datetime64("NaT")
            assert result is NaT or np.isnat(result)
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\base\test_misc.py:155** — `# TODO: Should Series cases also raise? Looks like they use numpy`
```
)
    elif obj.dtype.kind == "c" and isinstance(obj, Index):
        # TODO: Should Series cases also raise? Looks like they use numpy
        #  comparison semantics https://github.com/numpy/numpy/issues/15981
        mark = pytest.mark.xfail(reason="complex objects are not comparable")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\base\test_value_counts.py:50** — `# TODO(GH#32514): Order of entries with the same count is inconsistent`
```
expected = expected.astype("Int64")

    # TODO(GH#32514): Order of entries with the same count is inconsistent
    #  on CI (gh-32449)
    if obj.duplicated().any():
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\computation\test_eval.py:98** — `# TODO: using range(5) here is a kludge`
```
# TODO: using range(5) here is a kludge
@pytest.fixture(
    params=list(range(5)),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_astype.py:137** — `# TODO(infer_string) this test can be removed after 3.0 (once str is the default)`
```
def test_astype_str_copy_on_pickle_roundrip():
    # TODO(infer_string) this test can be removed after 3.0 (once str is the default)
    # https://github.com/pandas-dev/pandas/issues/54654
    # ensure_string_array may alter array inplace
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_chained_assignment_deprecation.py:74** — `# TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+`
```
df = df_orig.copy()
    df["a"]  # populate the item_cache
    # TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+
    if using_copy_on_write:
        with tm.raises_chained_assignment_error(not PY311):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_core_functionalities.py:54** — `# TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100``
```
arr = get_array(df, "a")
    view = None  # noqa: F841
    # TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100`
    # which introduces additional refs, even when those of `view` go out of scopes
    with tm.assert_cow_warning(warn_copy_on_write):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_indexing.py:816** — `# TODO add more tests modifying the parent`
```
# TODO add more tests modifying the parent
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_methods.py:148** — `# TODO copy=False without CoW still returns a copy in this case`
```
if request.node.callspec.id.startswith("reindex-"):
        # TODO copy=False without CoW still returns a copy in this case
        if not using_copy_on_write and not using_array_manager and copy is False:
            share_memory = False
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\copy_view\test_replace.py:21** — `# TODO: Add these in a further optimization`
```
{"to_replace": {"b": 4}, "value": -1},
        {"to_replace": {"b": {4: 1}}},
        # TODO: Add these in a further optimization
        # We would need to see which columns got replaced in the mask
        # which could be expensive
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\dtypes\cast\test_downcast.py:46** — `# TODO: similar for dt64, dt64tz, Period, Interval?`
```
np.array([1, 2], dtype="m8[D]").astype("m8[ns]"),
        ),
        # TODO: similar for dt64, dt64tz, Period, Interval?
    ],
)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\conftest.py:126** — `TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)`
```
The scalar missing value for this type. Default dtype.na_value.

    TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)
    """
    return dtype.na_value
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_arrow.py:77** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_categorical.py:80** — `# TODO: Is this deliberate?`
```
@pytest.mark.xfail(reason="Memory usage doesn't match")
    def test_memory_usage(self, data):
        # TODO: Is this deliberate?
        super().test_memory_usage(data)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_interval.py:119** — `# TODO: either belongs in tests.arrays.interval or move into base tests.`
```
# TODO: either belongs in tests.arrays.interval or move into base tests.
def test_fillna_non_scalar_raises(data_missing):
    msg = "can only insert Interval objects and NA into an IntervalArray"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_masked.py:267** — `# TODO: patching self is a bad pattern here`
```
def test_combine_le(self, data_repeated):
        # TODO: patching self is a bad pattern here
        orig_data1, orig_data2 = data_repeated(2)
        if orig_data1.dtype.kind == "b":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_numpy.py:219** — `# TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which`
```
@skip_nested
    def test_searchsorted(self, data_for_sorting, as_series):
        # TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which
        #  isn't quite what we want in nested data cases. Instead we need to
        #  adapt something like libindex._bin_search.
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_sparse.py:254** — `# TODO: this fails bc we do not pass through data_missing. If we did,`
```
def test_fillna_series(self, data_missing):
        # this one looks doable.
        # TODO: this fails bc we do not pass through data_missing. If we did,
        #  the 0-fill case would xpass
        super().test_fillna_series()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\test_string.py:247** — `# TODO(infer_string)`
```
and (HAS_PYARROW or dtype.storage == "pyarrow")
        ):
            # TODO(infer_string)
            mark = pytest.mark.xfail(
                reason="The pointwise operation result will be inferred to "
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\accumulate.py:39** — `# TODO: require TypeError for things that will _never_ work?`
```
else:
            with pytest.raises((NotImplementedError, TypeError)):
                # TODO: require TypeError for things that will _never_ work?
                getattr(ser, op_name)(skipna=skipna)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\dim2.py:31** — `# TODO: is there a less hacky way of checking this?`
```
test_func = node._obj
            if test_func.__qualname__.startswith("Dim2CompatTests"):
                # TODO: is there a less hacky way of checking this?
                pytest.skip(f"{dtype} does not support 2D.")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\getitem.py:124** — `# TODO: box over scalar, [scalar], (scalar,)?`
```
def test_getitem_invalid(self, data):
        # TODO: box over scalar, [scalar], (scalar,)?

        msg = (
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\methods.py:70** — `# TODO: avoid special-casing`
```
if isinstance(data.dtype, pd.StringDtype) and data.dtype.na_value is np.nan:
            # TODO: avoid special-casing
            expected = expected.astype("float64")
        elif getattr(data.dtype, "storage", "") == "pyarrow" or isinstance(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\missing.py:30** — `# TODO: GH 57739`
```
mask = getattr(result, na_func)()
        if isinstance(mask.dtype, pd.SparseDtype):
            # TODO: GH 57739
            mask = np.array(mask)
            mask.flags.writeable = True
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\reduce.py:86** — `# TODO: the message being checked here isn't actually checking anything`
```
if not self._supports_reduction(ser, op_name):
            # TODO: the message being checked here isn't actually checking anything
            msg = (
                "[Cc]annot perform|Categorical is not ordered for operation|"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\base\setitem.py:220** — `# TODO(xfail) this raises KeyError about labels not found (it tries label-based)`
```
arr = data.copy()

        # TODO(xfail) this raises KeyError about labels not found (it tries label-based)
        # for list of labels with Series
        if box_in_series:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\json\array.py:263** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    return [
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\json\test_json.py:185** — `# TODO (EA.factorize): see if _values_for_factorize allows this.`
```
@unhashable
    def test_sort_values_frame(self):
        # TODO (EA.factorize): see if _values_for_factorize allows this.
        super().test_sort_values_frame()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\extension\list\array.py:130** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    data = np.empty(100, dtype=object)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_arithmetic.py:304** — `# TODO: test_bool_flex_frame needs a better name`
```
class TestFrameFlexComparisons:
    # TODO: test_bool_flex_frame needs a better name
    @pytest.mark.parametrize("op", ["eq", "ne", "gt", "lt", "ge", "le"])
    def test_bool_flex_frame(self, op):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_block_internals.py:29** — `# TODO(ArrayManager) check which of those tests need to be rewritten to test the`
```
# TODO(ArrayManager) check which of those tests need to be rewritten to test the
# equivalent for ArrayManager
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_constructors.py:317** — `# TODO(CoW-warn) this should warn`
```
if not using_array_manager and not using_copy_on_write:
            should_be_view = DataFrame(df.values, dtype=df[0].dtype)
            # TODO(CoW-warn) this should warn
            # with tm.assert_cow_warning(warn_copy_on_write):
            should_be_view.iloc[0, 0] = 97
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_cumulative.py:31** — `# TODO(wesm): do something with this?`
```
dm = DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=range(5))
        # TODO(wesm): do something with this?
        dm.cumsum()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_logical_ops.py:155** — `_check_unary_op(operator.inv)  # TODO: belongs elsewhere`
```
_check_bin_op(operator.xor)

        _check_unary_op(operator.inv)  # TODO: belongs elsewhere

    @pytest.mark.filterwarnings("ignore:Downcasting object dtype arrays:FutureWarning")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_reductions.py:1774** — `# TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead`
```
df.median()

        # TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead
        #  of expected.values
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_ufunc.py:150** — `# TODO(FloatArray): this will be Float64Dtype.`
```
np.array([[1, 3], [np.nan, np.nan], [3, 4]]),
    )
    # TODO(FloatArray): this will be Float64Dtype.
    expected = pd.DataFrame(expected, index=["a", "b", "c"], columns=["A", "B"])
    tm.assert_frame_equal(result, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\test_unary.py:167** — `# TODO: assert that we have copies?`
```
res_ufunc = np.positive(df)
        expected = df
        # TODO: assert that we have copies?
        tm.assert_frame_equal(result, expected)
        tm.assert_frame_equal(res_ufunc, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_coercion.py:45** — `# TODO: i think this isn't about MultiIndex and could be done with iloc?`
```
assert (A.dtypes == np.float32).all()

        # TODO: i think this isn't about MultiIndex and could be done with iloc?
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_indexing.py:644** — `@td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values`
```
assert ix[idx, col] == ts[idx]

    @td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values
    def test_setitem_fancy_scalar(self, float_frame):
        f = float_frame
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_setitem.py:725** — `# TODO(ArrayManager) set column with 2d column array, see #44788`
```
tm.assert_frame_equal(df, expected)

    # TODO(ArrayManager) set column with 2d column array, see #44788
    @td.skip_array_manager_not_yet_implemented
    def test_setitem_npmatrix_2d(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_where.py:727** — `# TODO: ideally we would get Int64 instead of object`
```
mask[1, :] = False

        # TODO: ideally we would get Int64 instead of object
        result = df.where(mask, ser, axis=0)
        expected = DataFrame({"A": [1, np.nan, 3], "B": [4, np.nan, 6]})
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_xs.py:153** — `# TODO: more descriptive name`
```
class TestXSWithMultiIndex:
    def test_xs_doc_example(self):
        # TODO: more descriptive name
        # based on example in advanced.rst
        arrays = [
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_asfreq.py:154** — `# TODO: actually check that this worked.`
```
rule_monthly.asfreq("B", method="pad")
        # TODO: actually check that this worked.

        # don't forget!
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_astype.py:129** — `# TODO(wesm): verification?`
```
tf.astype(np.float32, copy=False)

        # TODO(wesm): verification?
        tf = float_frame.astype(np.float64)
        tf.astype(np.int64, copy=False)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_clip.py:159** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_combine_first.py:212** — `# TODO: this must be int64`
```
tm.assert_frame_equal(res, exp)
        assert res["a"].dtype == "datetime64[ns]"
        # TODO: this must be int64
        assert res["b"].dtype == "int64"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_compare.py:269** — `# GH#18463 TODO: is this really the desired behavior?`
```
)
    if val1 is pd.NA and val2 is pd.NA:
        # GH#18463 TODO: is this really the desired behavior?
        expected.loc[1, ("a", "self")] = np.nan
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_fillna.py:32** — `# TODO(CoW-warn) better warning message`
```
orig = df[:]

        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df.fillna({"A": 2}, inplace=True)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_info.py:535** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_memory_usage_empty_no_warning(using_infer_string):
    # GH#50066
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_interpolate.py:335** — `# TODO: assert something?`
```
)
        df.interpolate(axis=0)
        # TODO: assert something?

    @pytest.mark.parametrize(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_quantile.py:729** — `# GH#18463 TODO: would we prefer NaTs here?`
```
exp = exp.astype(object)
        if interpolation == "nearest":
            # GH#18463 TODO: would we prefer NaTs here?
            msg = "The 'downcast' keyword in fillna is deprecated"
            with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_rank.py:504** — `# TODO nullable string[python] should also return nullable Int64`
```
)
        if string_dtype_no_object.storage == "python":
            # TODO nullable string[python] should also return nullable Int64
            exp_dtype = "float64"
        expected = Series([1, 2, None, 3], dtype=exp_dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_rename.py:388** — `# TODO: can we construct this without merge?`
```
),
        )
        # TODO: can we construct this without merge?
        k = merge(df4, df5, how="inner", left_index=True, right_index=True)
        result = k.rename(columns={"TClose_x": "TClose", "TClose_y": "QT_Close"})
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_replace.py:751** — `# TODO: what is this even testing?`
```
msg = "DataFrame.fillna with 'method' is deprecated"
        with tm.assert_produces_warning(FutureWarning, match=msg):
            # TODO: what is this even testing?
            result = tsframe.fillna(method="bfill")
            tm.assert_frame_equal(result, tsframe.fillna(method="bfill"))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_shift.py:469** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support`
```
tm.assert_frame_equal(result, expected)

    @td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support
    def test_shift_axis1_multiple_blocks_with_int_fill(self):
        # GH#42719
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_sort_index.py:596** — `# TODO: better name, de-duplicate with test_sort_index_level above`
```
assert result.columns.is_monotonic_increasing

    # TODO: better name, de-duplicate with test_sort_index_level above
    def test_sort_index_level2(self, multiindex_dataframe_random_data):
        frame = multiindex_dataframe_random_data
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_to_csv.py:547** — `# TODO to_csv drops column name`
```
df = self.read_csv(path, index_col=[0, 1], parse_dates=False)

            # TODO to_csv drops column name
            tm.assert_frame_equal(frame, df, check_names=False)
            assert frame.index.names == df.index.names
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_to_dict_of_blocks.py:40** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_to_dict_of_blocks_item_cache(using_copy_on_write, warn_copy_on_write):
    # Calling to_dict_of_blocks should not poison item_cache
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_tz_convert.py:93** — `# TODO: untested`
```
df4 = DataFrame(np.ones(5), MultiIndex.from_arrays([int_idx, l0]))

            # TODO: untested
            getattr(df4, fn)("US/Pacific", level=1)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\frame\methods\test_update.py:186** — `# TODO(CoW-warn) better warning message`
```
df2_orig = df2.copy()
        result_view = df2[:]
        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df2.update(df)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\generic\test_duplicate_labels.py:51** — `# TODO: frame`
```
"other", [pd.Series(0, index=["a", "b", "c"]), pd.Series(0, index=["a", "b"])]
    )
    # TODO: frame
    @not_implemented
    def test_align(self, other):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\generic\test_finalize.py:13** — `# TODO:`
```
import pandas._testing as tm

# TODO:
# * Binary methods (mul, div, etc.)
# * Binary outputs (align, etc.)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_apply.py:461** — `# TODO(GH#34306): Use assert_frame_equal when column name is not np.nan`
```
result = grouped.apply(len)
    expected = grouped.count().rename(columns={"C": np.nan}).drop(columns="D")
    # TODO(GH#34306): Use assert_frame_equal when column name is not np.nan
    tm.assert_index_equal(result.index, expected.index)
    tm.assert_numpy_array_equal(result.values, expected.values)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_categorical.py:86** — `def test_basic(using_infer_string):  # TODO: split this test`
```
def test_basic(using_infer_string):  # TODO: split this test
    cats = Categorical(
        ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_groupby.py:313** — `# TODO: try to get this more consistent?`
```
expected = DataFrame(ex_data).T
    if not as_index:
        # TODO: try to get this more consistent?
        expected.index = Index(range(2))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_groupby_dropna.py:612** — `# TODO: Should this be 3?`
```
na_group = df["x"].nunique(dropna=False) - 1
            else:
                # TODO: Should this be 3?
                na_group = df["x"].nunique(dropna=False) - 1
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_grouping.py:936** — `# TODO: should prob allow a str of Interval work as well`
```
g = d.groupby(pd.cut(d[0], bins), observed=observed)

        # TODO: should prob allow a str of Interval work as well
        # IOW '(0, 5]'
        result = g.get_group(pd.Interval(0, 5))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_numeric_only.py:93** — `# TODO: min, max *should* handle`
```
@pytest.mark.parametrize("method", ["min", "max"])
    def test_extrema(self, df, method):
        # TODO: min, max *should* handle
        # categorical (ordered) dtype
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_raises.py:634** — `# TODO: empty_groups should be true due to unobserved categorical combinations`
```
):
        assert not empty_groups
        # TODO: empty_groups should be true due to unobserved categorical combinations
        empty_groups = True
    if how == "transform":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_reductions.py:747** — `# TODO: For skipna=False, bool(pd.NA) raises; should groupby?`
```
if reduction_func in ["all", "any"]:
        expected_dtype = "bool"
        # TODO: For skipna=False, bool(pd.NA) raises; should groupby?
        expected_value = False if reduction_func == "any" else True
    elif reduction_func in ["count", "nunique", "size"]:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\test_timegrouper.py:78** — `# TODO(infer_string) resample sum introduces 0's`
```
class TestGroupBy:
    # TODO(infer_string) resample sum introduces 0's
    # https://github.com/pandas-dev/pandas/issues/60229
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_aggregate.py:1356** — `# TODO: agg should raise for functions that don't aggregate`
```
def test_nonagg_agg():
    # GH 35490 - Single/Multiple agg of non-agg function give same results
    # TODO: agg should raise for functions that don't aggregate
    df = DataFrame({"a": [1, 1, 2, 2], "b": [1, 2, 2, 1]})
    g = df.groupby("a")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_numba.py:181** — `# FIXME`
```
[
        ({"func": lambda values, index: values.sum()}, "sum"),
        # FIXME
        pytest.param(
            {
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_other.py:444** — `# FIXME: the original version of this test called `gb.agg(sum)``
```
tm.assert_frame_equal(result, expected)

    # FIXME: the original version of this test called `gb.agg(sum)`
    #  and that raises TypeError if `numeric_only=False` is passed
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\methods\test_quantile.py:65** — `# TODO(non-nano): this should be unnecessary once array_to_datetime`
```
)
    if all_vals.dtype.kind == "M" and expected.dtypes.values[0].kind == "M":
        # TODO(non-nano): this should be unnecessary once array_to_datetime
        #  correctly infers non-nano from Timestamp.unit
        expected = expected.astype(all_vals.dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\methods\test_value_counts.py:427** — `# TODO(nullable) also string[python] should return nullable dtypes`
```
expected["proportion"] /= expected_group_size
        if dtype == "string[pyarrow]":
            # TODO(nullable) also string[python] should return nullable dtypes
            expected["proportion"] = expected["proportion"].convert_dtypes()
    else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\transform\test_numba.py:149** — `# TODO: Test more than just reductions (e.g. actually test transformations once we have`
```
# TODO: Test more than just reductions (e.g. actually test transformations once we have
@pytest.mark.parametrize(
    "agg_func", [["min", "max"], "min", {"B": ["min", "max"], "C": "sum"}]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\groupby\transform\test_transform.py:872** — `# TODO: create xfail condition given other params`
```
{"level": 0},
        {"by": "string"},
        # TODO: create xfail condition given other params
        # {"by": 'string_missing'},
        {"by": ["int", "string"]},
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_any_index.py:50** — `# TODO: could work that into the 'exact="equiv"'?`
```
if index.dtype == object and result.dtype in [bool, "string"]:
        assert (index == result).all()
        # TODO: could work that into the 'exact="equiv"'?
        return  # FIXME: doesn't belong in this file anymore!
    tm.assert_index_equal(result, index, exact="equiv")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_base.py:57** — `# TODO: a bunch of scattered tests check this deprecation is enforced.`
```
@pytest.mark.parametrize("index", ["datetime"], indirect=True)
    def test_new_axis(self, index):
        # TODO: a bunch of scattered tests check this deprecation is enforced.
        #  de-duplicate/centralize them.
        with pytest.raises(ValueError, match="Multi-dimensional indexing"):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_common.py:169** — `# TODO: belongs in series arithmetic tests?`
```
assert second.name == "mario"

        # TODO: belongs in series arithmetic tests?
        s1 = pd.Series(2, index=first)
        s2 = pd.Series(3, index=second[:-1])
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_indexing.py:157** — `return  # TODO: do we want this to raise?`
```
def test_contains_requires_hashable_raises(self, index):
        if isinstance(index, MultiIndex):
            return  # TODO: do we want this to raise?

        msg = "unhashable type: 'list'"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_numpy_compat.py:155** — `# TODO: overlap with tests.series.test_ufunc.test_reductions`
```
@pytest.mark.parametrize("func", [np.maximum, np.minimum])
def test_numpy_ufuncs_reductions(index, func, request):
    # TODO: overlap with tests.series.test_ufunc.test_reductions
    if len(index) == 0:
        pytest.skip("Test doesn't make sense for empty index.")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\test_setops.py:197** — `# TODO: pin down desired dtype; do we want it to be commutative?`
```
# Testing name retention
    # TODO: pin down desired dtype; do we want it to be commutative?
    result = a.intersection(b)
    assert result.name == names[2]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\base_class\test_reshape.py:41** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
def test_insert_missing(self, request, nulls_fixture, using_infer_string):
        if using_infer_string and nulls_fixture is pd.NA:
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH#22295
        # test there is no mangling of NA values
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimelike_\test_equals.py:56** — `# TODO: de-duplicate with other test_equals2 methods`
```
return period_range("2013-01-01", periods=5, freq="D")

    # TODO: de-duplicate with other test_equals2 methods
    @pytest.mark.parametrize("freq", ["D", "M"])
    def test_equals2(self, freq):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_constructors.py:85** — `# TODO: better place for tests shared by DTI/TDI?`
```
DatetimeIndex([pd.NaT, Timestamp("2011-01-01")._value], freq="D")

    # TODO: better place for tests shared by DTI/TDI?
    @pytest.mark.parametrize(
        "index",
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_datetime.py:73** — `# TODO: belongs in frame groupby tests?`
```
assert isinstance(next(iter(result.values()))[0], Timestamp)

    # TODO: belongs in frame groupby tests?
    def test_groupby_function_tuple_1677(self):
        df = DataFrame(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_date_range.py:1303** — `#    # TODO give a more useful or informative message?`
```
msg = "Use a lower freq or a higher unit instead"
        with pytest.raises(ValueError, match=msg):
            #    # TODO give a more useful or informative message?
            date_range("2016-01-01", "2016-01-02", freq="ns", unit="ms")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_formats.py:189** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_dti_representation_to_series(self, unit):
        idx1 = DatetimeIndex([], freq="D")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_indexing.py:294** — `# TODO: This method came from test_datetime; de-dup with version above`
```
idx.take(indices, mode="clip")

    # TODO: This method came from test_datetime; de-dup with version above
    @pytest.mark.parametrize("tz", [None, "US/Eastern", "Asia/Tokyo"])
    def test_take2(self, tz):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_setops.py:43** — `# TODO: moved from test_datetimelike; dedup with version below`
```
]

    # TODO: moved from test_datetimelike; dedup with version below
    def test_union2(self, sort):
        everything = date_range("2020-01-01", periods=10)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_delete.py:117** — `# TODO: belongs in Series.drop tests?`
```
assert result.freq == expected.freq

    # TODO: belongs in Series.drop tests?
    @pytest.mark.parametrize("tz", [None, "Asia/Tokyo", "US/Pacific"])
    def test_delete_slice2(self, tz, unit):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_insert.py:180** — `# TODO: also changes DataFrame.__setitem__ with expansion`
```
assert result.freq is None

    # TODO: also changes DataFrame.__setitem__ with expansion
    def test_insert_mismatched_tzawareness(self):
        # see GH#7299
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_formats.py:18** — `# TODO: this is a test for DataFrame/Series, not IntervalIndex`
```
class TestIntervalIndexRendering:
    # TODO: this is a test for DataFrame/Series, not IntervalIndex
    @pytest.mark.parametrize(
        "constructor,expected",
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_indexing.py:369** — `# TODO: with mismatched resolution get_indexer currently raises;`
```
def test_get_indexer_datetime(self):
        ii = IntervalIndex.from_breaks(date_range("2018-01-01", periods=4))
        # TODO: with mismatched resolution get_indexer currently raises;
        #  this should probably coerce?
        target = DatetimeIndex(["2018-01-02"], dtype="M8[ns]")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_setops.py:184** — `# TODO: standardize return type of non-union setops type(self vs other)`
```
set_op = getattr(index, op_name)

        # TODO: standardize return type of non-union setops type(self vs other)
        # non-IntervalIndex
        if op_name == "difference":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_analytics.py:76** — `# TODO: reshape`
```
# TODO: reshape
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_indexing.py:85** — `# TODO: Try creating a UnicodeDecodeError in exception message`
```
with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(timedelta(seconds=30))
        # TODO: Try creating a UnicodeDecodeError in exception message
        with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(df.index[1], (16, "a"))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_reshape.py:69** — `# FIXME data types changes to float because`
```
)
    right.set_index(["1st", "2nd"], inplace=True)
    # FIXME data types changes to float because
    # of intermediate nan insertion;
    tm.assert_frame_equal(left, right, check_dtype=False)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_setops.py:233** — `# TODO: this is raising in constructing a Categorical when calling`
```
other = MultiIndex.from_product([[3, pd.Timestamp("2000"), 4], ["c", "d"]])

    # TODO: this is raising in constructing a Categorical when calling
    #  algos.safe_sort. Should we catch and re-raise with a better message?
    msg = "'values' is not ordered, please explicitly specify the categories order "
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\numeric\test_numeric.py:535** — `# TODO: we could plausibly try to infer down to int16 here`
```
idx = Index(np.array([1, 2, 3], dtype=np.int8))
    result = idx.map(lambda x: x * 1000)
    # TODO: we could plausibly try to infer down to int16 here
    expected = Index([1000, 2000, 3000], dtype=np.int64)
    tm.assert_index_equal(result, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\period\test_formats.py:115** — `# TODO: These are Series.__repr__ tests`
```
assert result == expected

    # TODO: These are Series.__repr__ tests
    def test_representation_to_series(self):
        # GH#10971
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\period\test_indexing.py:480** — `# TODO: This method came from test_period; de-dup with version above`
```
tm.assert_numpy_array_equal(result[1], expected_missing)

    # TODO: This method came from test_period; de-dup with version above
    def test_get_indexer2(self):
        idx = period_range("2000-01-01", periods=3).asfreq("h", how="start")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\period\test_partial_slicing.py:44** — `# Todo: fix these accessors!`
```
pi = PeriodIndex(["2Q05", "3Q05", "4Q05", "1Q06", "2Q06"], freq="Q")
        ser = Series(np.random.default_rng(2).random(len(pi)), index=pi).cumsum()
        # Todo: fix these accessors!
        assert ser["05Q4"] == ser.iloc[2]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_astype.py:83** — `# TODO: de-duplicate this version (from test_ops) with the one above`
```
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)

    # TODO: de-duplicate this version (from test_ops) with the one above
    # (from test_period)
    def test_astype_object2(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_to_timestamp.py:30** — `# TODO: can we get the freq to round-trip?`
```
result = pi._data[::2].to_timestamp()
        expected = dti._data[::2]
        # TODO: can we get the freq to round-trip?
        tm.assert_datetime_array_equal(result, expected, check_freq=False)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_formats.py:54** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_representation_to_series(self):
        idx1 = TimedeltaIndex([], freq="D")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_scalar_compat.py:98** — `# TODO: de-duplicate with test_tdi_round`
```
t1._data.round(freq)

    # TODO: de-duplicate with test_tdi_round
    def test_round(self):
        t1 = timedelta_range("1 days", periods=3, freq="1 min 2 s 3 us")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_at.py:166** — `# TODO: De-duplicate/parametrize`
```
class TestAtErrors:
    # TODO: De-duplicate/parametrize
    #  test_at_series_raises_key_error2, test_at_frame_raises_key_error2
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_chaining_and_caching.py:561** — `# TODO(ArrayManager) fast_xs with array-like scalars is not yet working`
```
tm.assert_frame_equal(df, df_original)

    # TODO(ArrayManager) fast_xs with array-like scalars is not yet working
    @td.skip_array_manager_not_yet_implemented
    def test_chained_getitem_with_lists(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_coercion.py:351** — `# TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"`
```
tm.assert_index_equal(result, expected)

            # TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"
            #  casts that string to Period[M], not clear that is desirable
            if not isinstance(insert, pd.Timestamp):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_iloc.py:550** — `# TODO: GH#27620 this test used to compare iloc against ix; check if this`
```
tm.assert_frame_equal(df, expected)

    # TODO: GH#27620 this test used to compare iloc against ix; check if this
    #  is redundant with another test comparing iloc against loc
    def test_iloc_getitem_frame(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_indexing.py:911** — `# TODO(EA2D): we can make this no-copy in tz-naive case too`
```
if tz is None:
            # TODO(EA2D): we can make this no-copy in tz-naive case too
            assert ser.dtype == dti.dtype
            assert ser._values._ndarray is values._ndarray
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_loc.py:152** — `# TODO: test something?`
```
def test_loc_getitem_label_array_like(self):
        # TODO: test something?
        # array like
        pass
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\test_partial.py:4** — `TODO: these should be split among the indexer tests`
```
test setting *parts* of objects both positionally and label based

TODO: these should be split among the indexer tests
"""
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\interval\test_interval_new.py:171** — `# TODO KeyError is the appropriate error?`
```
if indexer_sl is tm.loc:
            # slices with scalar raise for overlapping intervals
            # TODO KeyError is the appropriate error?
            with pytest.raises(KeyError, match=msg):
                ser.loc[1:4]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_loc.py:828** — `# TODO: standardize return type for MultiIndex.get_loc`
```
loc = mi.append(mi).get_loc("2001-01")
    expected = index.append(index).get_loc("2001-01")
    # TODO: standardize return type for MultiIndex.get_loc
    tm.assert_numpy_array_equal(loc.nonzero()[0], expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_partial.py:121** — `# TODO(ArrayManager) rewrite test to not use .values`
```
df.loc[("a", "foo"), :]

    # TODO(ArrayManager) rewrite test to not use .values
    # exp.loc[2000, 4].values[:] select multiple columns -> .values is not a view
    @td.skip_array_manager_invalid_test
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_setitem.py:129** — `# TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in`
```
)

    # TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in
    # all NaNs -> doesn't work in the "split" path (also for BlockManager actually)
    @td.skip_array_manager_not_yet_implemented
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\interchange\test_impl.py:371** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\interchange\test_utils.py:7** — `# TODO: use ArrowSchema to get reference C-string.`
```
from pandas.core.interchange.utils import dtype_to_arrow_c_fmt

# TODO: use ArrowSchema to get reference C-string.
# At the time, there is no way to access ArrowSchema holding a type format string
# from python. The only way to access it is to export the structure to a C-pointer,
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\internals\test_internals.py:48** — `# TODO(ArrayManager) factor out interleave_dtype tests`
```
# this file contains BlockManager specific tests
# TODO(ArrayManager) factor out interleave_dtype tests
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_clipboard.py:354** — `# TODO avoid this exception?`
```
pa = pytest.importorskip("pyarrow")
            if engine == "c" and string_storage == "pyarrow":
                # TODO avoid this exception?
                string_dtype = pd.ArrowDtype(pa.large_string())
            else:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_common.py:316** — `marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),`
```
("io", "data", "legacy_hdf", "datetimetz_object.h5"),
                # cleaned-up in https://github.com/pandas-dev/pandas/pull/57387 on main
                marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),
            ),
            (pd.read_stata, "os", ("io", "data", "stata", "stata10_115.dta")),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_fsspec.py:199** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet`
```
@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet
def test_fastparquet_options(fsspectest):
    """Regression test for writing to a not-yet-existent GCS Parquet file."""
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_http_headers.py:105** — `# TODO(ArrayManager) fastparquet`
```
parquetfastparquet_responder,
            partial(pd.read_parquet, engine="fastparquet"),
            # TODO(ArrayManager) fastparquet
            marks=[
                td.skip_if_no("fastparquet"),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_parquet.py:53** — `# TODO(ArrayManager) fastparquet relies on BlockManager internals`
```
# TODO(ArrayManager) fastparquet relies on BlockManager internals

pytestmark = [
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_spss.py:14** — `# TODO(CoW) - detection of chained assignment in cython`
```
# TODO(CoW) - detection of chained assignment in cython
# https://github.com/pandas-dev/pandas/issues/51315
@pytest.mark.filterwarnings("ignore::pandas.errors.ChainedAssignmentError")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_sql.py:1860** — `# TODO: clean up types_data_frame fixture`
```
)
    if "postgres" in conn_name:
        # TODO: clean up types_data_frame fixture
        result["BoolCol"] = result["BoolCol"].astype(int)
        result["BoolColWithNull"] = result["BoolColWithNull"].astype(float)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\test_stata.py:188** — `# FIXME: don't leave commented-out`
```
with tm.assert_produces_warning(UserWarning):
            parsed_117 = self.read_dta(path3)
            # FIXME: don't leave commented-out
            # 113 is buggy due to limits of date format support in Stata
            # parsed_113 = self.read_dta(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\excel\test_readers.py:248** — `# TODO add index to xls file)`
```
)

        # TODO add index to xls file)
        tm.assert_frame_equal(df1, expected)
        tm.assert_frame_equal(df2, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\excel\test_style.py:29** — `# TODO: should find a better way to check equality`
```
def assert_equal_cell_styles(cell1, cell2):
    # TODO: should find a better way to check equality
    assert cell1.alignment.__dict__ == cell2.alignment.__dict__
    assert cell1.border.__dict__ == cell2.border.__dict__
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\formats\test_format.py:1253** — `# FIXME: don't leave commented-out`
```
assert not has_non_verbose_info_repr(df)

        # FIXME: don't leave commented-out
        # test verbose overrides
        # set_option('display.max_info_columns', 4)  # exceeded
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\formats\test_to_html.py:373** — `# TODO: split this test`
```
@pytest.mark.parametrize("biggie_df_fixture", ["mixed"], indirect=True)
def test_to_html(biggie_df_fixture):
    # TODO: split this test
    df = biggie_df_fixture
    s = df.to_html()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\formats\test_to_string.py:391** — `# TODO: assert that these match??`
```
result = df.to_string()
        expected = "   0\n0  0\n1  0\n2 -0"
        # TODO: assert that these match??

    def test_to_string_complex_float_formatting(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\formats\style\test_style.py:441** — `# test execution added to todo`
```
}

    # test execution added to todo
    result = getattr(df.style, f"{method}_index")(func[method], axis=axis)
    assert len(result._todo) == 1
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\json\test_json_table_schema.py:212** — `# TODO: datedate.date? datetime.time?`
```
)
    def test_as_json_table_type_date_dtypes(self, date_dtype):
        # TODO: datedate.date? datetime.time?
        assert as_json_table_type(date_dtype) == "datetime"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\json\test_pandas.py:177** — `# TODO: a to_epoch method would also solve; see GH 14772`
```
# in milliseconds; these are internally stored in nanosecond,
                # so divide to get where we need
                # TODO: a to_epoch method would also solve; see GH 14772
                expected.isetitem(0, expected.iloc[:, 0].astype(np.int64) // 1000000)
        elif orient == "split":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\parser\test_encoding.py:190** — `# FIXME: this is bad!`
```
if parser.engine == "pyarrow" and pass_encoding is True and utf_value in [16, 32]:
        # FIXME: this is bad!
        pytest.skip("These cases freeze")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\parser\test_na_values.py:686** — `# TODO: this test isn't about the na_values keyword, it is about the empty entries`
```
# TODO: this test isn't about the na_values keyword, it is about the empty entries
#  being returned with NaN entries, whereas the pyarrow engine returns "nan"
@xfail_pyarrow  # mismatched shapes
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\parser\test_network.py:41** — `pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")`
```
# extension inference
    if compression_only == "tar":
        pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")

    extension = compression_to_extension[compression_only]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\parser\test_parse_dates.py:1015** — `# TODO: make unit check more specific`
```
result = parser.read_csv(StringIO(data), index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\parser\common\test_common_basic.py:96** — `# TODO: make unit check more specific`
```
fname = prefix + str(os.path.abspath(csv1))
    result = parser.read_csv(fname, index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_append.py:254** — `# TODO: Test is incorrect when not using_infer_string.`
```
expected = df
            if using_infer_string:
                # TODO: Test is incorrect when not using_infer_string.
                #       Should take the last 4 rows uncondiationally.
                expected = expected[-4:]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_file_handling.py:366** — `# TODO:(3.0): once Categorical replace deprecation is enforced,`
```
retr = read_hdf(store, key)

    # TODO:(3.0): once Categorical replace deprecation is enforced,
    #  we may be able to re-simplify the construction of s_nan
    if dtype == "category":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_put.py:302** — `# TODO(infer_string) make this work for string dtype`
```
with ensure_clean_store(setup_path) as store:
        if using_infer_string:
            # TODO(infer_string) make this work for string dtype
            msg = "Saving a MultiIndex with an extension dtype is not supported."
            with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_read.py:232** — `# TODO(infer_string) make this work for string dtype`
```
path = tmp_path / setup_path
    if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_round_trip.py:438** — `# TODO(infer_string) make this work for string dtype`
```
if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_select.py:892** — `# FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds

        # multiple (diff selector)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\io\pytables\test_store.py:745** — `# FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None
        #  but expect freq="18B"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\libs\test_hashtable.py:264** — `# TODO: moved from test_algos; may be redundancies with other tests`
```
class TestHashTableUnsorted:
    # TODO: moved from test_algos; may be redundancies with other tests
    def test_string_hashtable_set_item_signature(self):
        # GH#30419 fix typing in StringHashTable.set_item to prevent segfault
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\plotting\test_datetimelike.py:775** — `# TODO`
```
def test_mixed_freq_regular_first(self):
        # TODO
        s1 = Series(
            np.arange(20, dtype=np.float64),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\plotting\test_series.py:983** — `# TODO(3.0): this can be removed once Period[B] deprecation is enforced`
```
def test_plot_no_warning(self, ts):
        # GH 55138
        # TODO(3.0): this can be removed once Period[B] deprecation is enforced
        with tm.assert_produces_warning(False):
            _ = ts.plot()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\plotting\frame\test_frame.py:343** — `# TODO add MultiIndex test`
```
# columns.inferred_type == 'mixed'
        # TODO add MultiIndex test

    @pytest.mark.parametrize(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\resample\test_base.py:269** — `# TODO: no tests with len(df.columns) > 0`
```
result = getattr(rs, resample_method)()
    if resample_method == "ohlc":
        # TODO: no tests with len(df.columns) > 0
        mi = MultiIndex.from_product([df.columns, ["open", "high", "low", "close"]])
        expected = DataFrame(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\resample\test_datetime_index.py:2219** — `reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",`
```
marks=pytest.mark.xfail(
                condition=is_platform_windows(),
                reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",
            ),
        ),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\resample\test_period_index.py:316** — `# TODO: should this raise at the resample call instead of at the mean call?`
```
rs = ser.resample("W")
        with pytest.raises(IncompatibleFrequency, match=msg):
            # TODO: should this raise at the resample call instead of at the mean call?
            rs.mean()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\resample\test_resample_api.py:380** — `# TODO(GH#14008): once GH 14008 is fixed, move these tests into`
```
# TODO(GH#14008): once GH 14008 is fixed, move these tests into
# `Base` test class
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\resample\test_time_grouper.py:250** — `expected.index = dti._with_freq(None)  # TODO: is this desired?`
```
unit=dt_df["key"]._values.unit,
    )
    expected.index = dti._with_freq(None)  # TODO: is this desired?
    tm.assert_frame_equal(expected, dt_result)
    assert dt_result.index.name == "key"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\test_cut.py:584** — `# TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating`
```
if unit == "s":
        # TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating
        #  the first entry here raises in array_to_datetime. Should truncate
        #  instead of raising?
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\test_melt.py:1205** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
if using_infer_string and any_string_dtype == "object":
            # triggers object dtype inference warning of dtype=object
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH46044
        df = DataFrame({"id": ["1", "2"], "a-1": [100, 200], "a-2": [300, 400]})
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\test_pivot.py:2625** — `using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"`
```
# while at that point None was converted to NaN
    @pytest.mark.xfail(
        using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"
    )
    def test_pivot_columns_is_none(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_append.py:370** — `# TODO: expected used to be `other.astype(object)` which is a more`
```
expected = other.astype(object)
        if isinstance(val, str) and dtype_str != "int64" and not using_array_manager:
            # TODO: expected used to be `other.astype(object)` which is a more
            #  reasonable result.  This was changed when tightening
            #  assert_frame_equal's treatment of mismatched NAs to match the
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_concat.py:50** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# test is not written to work with string dtype (checks .base)
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_copy(self, using_array_manager, using_copy_on_write):
        df = DataFrame(np.random.default_rng(2).standard_normal((4, 3)))
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_datetimes.py:233** — `# TODO: setting nan here is to keep the test passing as we`
```
if item is pd.NaT and not using_array_manager:
                # GH#18463
                # TODO: setting nan here is to keep the test passing as we
                #  make assert_frame_equal stricter, but is nan really the
                #  ideal behavior here?
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_empty.py:244** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_inner_join_empty(self):
        # GH 15328
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_join.py:347** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_join_empty_bug(self):
        # generated an exception in 0.4.3
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge.py:569** — `# TODO: should the next loop be un-indented? doing so breaks this test`
```
tm.assert_frame_equal(result, exp)

            # TODO: should the next loop be un-indented? doing so breaks this test
            for kwarg in [
                {"left_index": True, "right_index": True},
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge_asof.py:3141** — `# TODO(GH#32306): may be relevant to the expected behavior here.`
```
#  np.array([np.nan, 1]).  Other than that, I (@jbrockmendel)
        #  have NO IDEA what the expected behavior is.
        # TODO(GH#32306): may be relevant to the expected behavior here.

        arr = pd.array([pd.NA, 0, 1], dtype=any_numeric_ea_dtype)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\scalar\period\test_period.py:87** — `# TODO: raise in the future an error when passing lowercase freq`
```
# GH#54105 - Period can be confusingly instantiated with lowercase freq
        # TODO: raise in the future an error when passing lowercase freq
        i1 = Period("2005", freq="Y")
        i2 = Period("2005")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_constructors.py:141** — `# TODO(2.0): the desired output dtype may have non-nano resolution`
```
dtype="m8[ns]",
        )
        # TODO(2.0): the desired output dtype may have non-nano resolution
        msg = f"'{unit}' is deprecated and will be removed in a future version."
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_timedelta.py:401** — `# TODO: this is a test of to_timedelta string parsing`
```
assert tup.nanoseconds == 0

    # TODO: this is a test of to_timedelta string parsing
    def test_iso_conversion(self):
        # GH #21877
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\scalar\timestamp\test_constructors.py:313** — `# TODO: if we passed microsecond with a keyword we would mess up`
```
@pytest.mark.parametrize("kwd", ["nanosecond", "microsecond", "second", "minute"])
    def test_constructor_positional_keyword_mixed_with_tzinfo(self, kwd, request):
        # TODO: if we passed microsecond with a keyword we would mess up
        #  xref GH#45307
        if kwd != "nanosecond":
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\test_arithmetic.py:763** — `# TODO: belongs in tests/arithmetic?`
```
ser_utc + ser

    # TODO: belongs in tests/arithmetic?
    def test_datetime_understood(self, unit):
        # Ensures it doesn't fail to create the right series
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\test_constructors.py:571** — `# TODO should this be raising at all?`
```
expected = Series([0, 1, 2], index=index, dtype=int)
        with pytest.raises(AssertionError, match="Series classes are different"):
            # TODO should this be raising at all?
            # https://github.com/pandas-dev/pandas/issues/56131
            tm.assert_series_equal(result, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\test_logical_ops.py:363** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
tm.assert_series_equal(result, expected)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_logical_ops_label_based(self, using_infer_string):
        # GH#4947
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\test_ufunc.py:173** — `@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp`
```
@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp
@pytest.mark.parametrize("shuffle", [True, False])
@pytest.mark.filterwarnings("ignore:divide by zero:RuntimeWarning")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\indexing\test_setitem.py:437** — `# TODO: ser.where(~mask, alt) unnecessarily upcasts to int64`
```
tm.assert_series_equal(ser2, expected)

        # TODO: ser.where(~mask, alt) unnecessarily upcasts to int64
        ser3 = orig.copy()
        res = ser3.where(~mask, alt)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\methods\test_align.py:210** — `# TODO: assert something?`
```
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

    # TODO: assert something?
    ts.align(ts[::2], join=join_type)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\methods\test_astype.py:403** — `# TODO: same for EA float/uint dtypes, signed integers?`
```
):
        # GH#45151 We don't cast negative numbers to nonsense values
        # TODO: same for EA float/uint dtypes, signed integers?
        arr = np.arange(5).astype(float_numpy_dtype) - 3  # includes negatives
        ser = Series(arr)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\methods\test_clip.py:73** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
# GH#19992
        msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\methods\test_convert_dtypes.py:186** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
class TestSeriesConvertDtypes:
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("params", product(*[(True, False)] * 5))
    def test_convert_dtypes(
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\series\methods\test_diff.py:14** — `# TODO(__array_function__): could make np.diff return a Series`
```
class TestSeriesDiff:
    def test_diff_np(self):
        # TODO(__array_function__): could make np.diff return a Series
        #  matching ser.diff()
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\strings\test_cat.py:359** — `# TODO: Strimg option, this should return string dtype`
```
expected = Series([np.nan] * 4, index=s.index, dtype=s.dtype)
    else:  # box == Index
        # TODO: Strimg option, this should return string dtype
        expected = Index([np.nan] * 4, dtype=object)
    result = s.str.cat(t, join="left")
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\strings\test_extract.py:19** — `# TODO: should this raise TypeError`
```
def test_extract_expand_kwarg_wrong_type_raises(any_string_dtype):
    # TODO: should this raise TypeError
    values = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)
    with pytest.raises(ValueError, match="expand must be True or False"):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\strings\test_find_replace.py:258** — `# TODO(infer_string)`
```
tm.assert_series_equal(result, expected)

    # TODO(infer_string)
    # this particular combination of events is broken on 2.3
    # would require cherry picking #58483, which in turn requires #57481
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\strings\test_split_partition.py:385** — `# TODO see GH 18463`
```
# check that these are actually np.nan/pd.NA and not None
    # TODO see GH 18463
    # tm.assert_frame_equal does not differentiate
    if is_object_or_nan_string_dtype(any_string_dtype):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\tools\test_to_datetime.py:579** — `# TODO: Timestamp raises ValueError("could not convert string to Timestamp")`
```
def test_to_datetime_overflow(self):
        # we should get an OutOfBoundsDatetime, NOT OverflowError
        # TODO: Timestamp raises ValueError("could not convert string to Timestamp")
        #  can we make these more consistent?
        arg = "08335394550"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_business_hour.py:986** — `# TODO(GH#55564): as_unit will be unnecessary`
```
tm.assert_index_equal(t1, expected)

        # TODO(GH#55564): as_unit will be unnecessary
        pointwise = DatetimeIndex([x + off for x in idx]).as_unit(exp_unit)
        tm.assert_index_equal(pointwise, expected)
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_offsets.py:573** — `# TODO: belongs in arithmetic tests?`
```
assert hash(off) is not None

    # TODO: belongs in arithmetic tests?
    @pytest.mark.filterwarnings(
        "ignore:Non-vectorized DateOffset being applied to Series or DatetimeIndex"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_year.py:330** — `# TODO(cython3): "arg: datetime" annotation will impose`
```
result = ts + off
    # TODO(cython3): "arg: datetime" annotation will impose
    # datetime limitations on Timestamp. The fused type below works in cy3
    # ctypedef fused datetimelike:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\tslibs\test_array_to_datetime.py:27** — `# TODO: tests that include tzs, ints`
```
class TestArrayToDatetimeResolutionInference:
    # TODO: tests that include tzs, ints

    def test_infer_all_nat(self):
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\util\test_assert_almost_equal.py:341** — `# TODO: to get the same deprecation in assert_numpy_array_equal we need`
```
_assert_almost_equal_both(left, right, check_dtype=False)

        # TODO: to get the same deprecation in assert_numpy_array_equal we need
        #  to change/deprecate the default for strict_nan to become True
        # TODO: to get the same deprecation in assert_index_equal we need to
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\window\test_expanding.py:576** — `# TODO: xref gh-15826`
```
[[5, 6], [2, 1]], index=[0, 2], columns=Index(["X", "Y"], name="foo")
    )
    # TODO: xref gh-15826
    # .loc is not preserving the names
    result1 = df1.expanding().cov(df2, pairwise=True).loc[2]
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\tests\window\test_pairwise.py:299** — `# TODO: We're missing a flag somewhere in meson`
```
lambda x, y: x.expanding().corr(y, pairwise=True),
            lambda x, y: x.rolling(window=3).cov(y, pairwise=True),
            # TODO: We're missing a flag somewhere in meson
            pytest.param(
                lambda x, y: x.rolling(window=3).corr(y, pairwise=True),
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\_testing\asserters.py:599** — `# TODO(infer_string) this special case could be avoided if we have`
```
left = repr(left)
    elif isinstance(left, StringDtype):
        # TODO(infer_string) this special case could be avoided if we have
        # a more informative repr https://github.com/pandas-dev/pandas/issues/59342
        left = f"StringDtype(storage={left.storage}, na_value={left.na_value})"
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\_testing\contexts.py:225** — `# TODO update match`
```
else:
            warning = FutureWarning  # type: ignore[assignment]
            # TODO update match
            match = "ChainedAssignmentError"
        if extra_warnings:
```
---
- **C:\industria\.venv\Lib\site-packages\pandas\_testing\__init__.py:226** — `# TODO: Add container like pyarrow types:`
```
BOOL_PYARROW_DTYPES = [pa.bool_()]

    # TODO: Add container like pyarrow types:
    #  https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions
    ALL_PYARROW_DTYPES = (
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\FpxImagePlugin.py:178** — `# FIXME: the fill decoder is not implemented`
```
elif compression == 1:
                # FIXME: the fill decoder is not implemented
                self.tile.append(
                    ImageFile._Tile(
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\GifImagePlugin.py:120** — `self._fp = self.fp  # FIXME: hack`
```
self.global_palette = self.palette = p

        self._fp = self.fp  # FIXME: hack
        self.__rewind = self.fp.tell()
        self._n_frames: int | None = None
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\IcoImagePlugin.py:75** — `# TODO: invent a more convenient method for proportional scalings`
```
break
        else:
            # TODO: invent a more convenient method for proportional scalings
            frame = provided_im.copy()
            frame.thumbnail(size, Image.Resampling.LANCZOS, reducing_gap=None)
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\Image.py:544** — `# FIXME: take "new" parameters / other image?`
```
def __init__(self) -> None:
        # FIXME: take "new" parameters / other image?
        self._im: core.ImagingCore | DeferredError | None = None
        self._mode = ""
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageCms.py:1103** — `# FIXME: I get different results for the same data w. different`
```
if not isinstance(profile, ImageCmsProfile):
            profile = ImageCmsProfile(profile)
        # FIXME: I get different results for the same data w. different
        # compilers.  Bug in LittleCMS or in the binding?
        if profile.profile.is_intent_supported(intent, direction):
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageDraw.py:102** — `# FIXME: fix Fill2 to properly support matte for I+F images`
```
self.ink = self.draw.draw_ink(-1)
        if mode in ("1", "P", "I", "F"):
            # FIXME: fix Fill2 to properly support matte for I+F images
            self.fontmode = "1"
        else:
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageDraw2.py:54** — `# FIXME: add support for bitmap fonts`
```
self, color: str, file: StrOrBytesPath | BinaryIO, size: float = 12
    ) -> None:
        # FIXME: add support for bitmap fonts
        self.color = ImageColor.getrgb(color)
        self.font = ImageFont.truetype(file, size)
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageFile.py:341** — `# FIXME: This is a hack to handle TIFF's JpegTables tag.`
```
self.tile.sort(key=_tilesort)

            # FIXME: This is a hack to handle TIFF's JpegTables tag.
            prefix = getattr(self, "tile_prefix", b"")
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageFont.py:19** — `# Todo:`
```
# 2003-09-27 fl   added support for truetype charmap encodings
#
# Todo:
# Adapt to PILFONT2 format (16-bit fonts, compressed, single file)
#
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageOps.py:54** — `# FIXME: apply to lookup table, not image data`
```
def _lut(image: Image.Image, lut: list[int]) -> Image.Image:
    if image.mode == "P":
        # FIXME: apply to lookup table, not image data
        msg = "mode P support coming soon"
        raise NotImplementedError(msg)
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImagePalette.py:229** — `raise NotImplementedError(msg)  # FIXME`
```
msg = "unavailable when black is non-zero"
    raise NotImplementedError(msg)  # FIXME
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImageQt.py:140** — `# FIXME - is this really the best way to do this?`
```
# handle filename, if given instead of image name
    if hasattr(im, "toUtf8"):
        # FIXME - is this really the best way to do this?
        im = str(im.toUtf8(), "utf-8")
    if is_path(im):
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\ImImagePlugin.py:152** — `# FIXME: this may read whole file if not a text file`
```
break

            # FIXME: this may read whole file if not a text file
            s = s + self.fp.readline()
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\JpegImagePlugin.py:110** — `self.info["flashpix"] = s  # FIXME: value will change`
```
elif marker == 0xFFE2 and s.startswith(b"FPXR\0"):
        # extract FlashPix information (incomplete)
        self.info["flashpix"] = s  # FIXME: value will change
    elif marker == 0xFFE2 and s.startswith(b"ICC_PROFILE\0"):
        # Since an ICC profile can be larger than the maximum size of
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\McIdasImagePlugin.py:55** — `# FIXME: add memory map support`
```
mode = rawmode = "I;16B"
        elif w[11] == 4:
            # FIXME: add memory map support
            mode = "I"
            rawmode = "I;32B"
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\MpoImagePlugin.py:128** — `self._fp = self.fp  # FIXME: hack`
```
del self.info["mpoffset"]  # no longer needed
        self.is_animated = self.n_frames > 1
        self._fp = self.fp  # FIXME: hack
        self._fp.seek(self.__mpoffsets[0])  # get ready to read first frame
        self.__frame = 0
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\MspImagePlugin.py:184** — `header[12] = checksum  # FIXME: is this the right field?`
```
for h in header:
        checksum = checksum ^ h
    header[12] = checksum  # FIXME: is this the right field?

    # header
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PcdImagePlugin.py:49** — `self._size = 768, 512  # FIXME: not correct for rotated images!`
```
self._mode = "RGB"
        self._size = 768, 512  # FIXME: not correct for rotated images!
        self.tile = [ImageFile._Tile("pcd", (0, 0) + self.size, 96 * 2048)]
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PcxImagePlugin.py:96** — `# FIXME: hey, this doesn't work with the incremental loader !!!`
```
elif version == 5 and bits == 8 and planes == 1:
            mode = rawmode = "L"
            # FIXME: hey, this doesn't work with the incremental loader !!!
            self.fp.seek(-769, io.SEEK_END)
            s = self.fp.read(769)
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PdfImagePlugin.py:57** — `# FIXME: Should replace ASCIIHexDecode with RunLengthDecode`
```
image_refs: list[PdfParser.IndirectReference],
) -> tuple[PdfParser.IndirectReference, str]:
    # FIXME: Should replace ASCIIHexDecode with RunLengthDecode
    # (packbits) or LZWDecode (tiff/lzw compression).  Note that
    # PDF 1.2 also supports Flatedecode (zip compression).
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PdfParser.py:616** — `# TODO: support reuse of deleted objects`
```
def next_object_id(self, offset: int | None = None) -> IndirectReference:
        try:
            # TODO: support reuse of deleted objects
            reference = IndirectReference(max(self.xref_table.keys()) + 1, 0)
        except ValueError:
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PixarImagePlugin.py:61** — `# FIXME: to be continued...`
```
if mode == (14, 2):
            self._mode = "RGB"
        # FIXME: to be continued...

        # create tile descriptor (assuming "dumped")
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PngImagePlugin.py:445** — `icc_profile = None  # FIXME`
```
raise
        except zlib.error:
            icc_profile = None  # FIXME
        self.im_info["icc_profile"] = icc_profile
        return s
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PsdImagePlugin.py:40** — `(7, 8): ("L", 1),  # FIXME: multilayer`
```
(3, 8): ("RGB", 3),
    (4, 8): ("CMYK", 4),
    (7, 8): ("L", 1),  # FIXME: multilayer
    (8, 8): ("L", 1),  # duotone
    (9, 8): ("LAB", 3),
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\PSDraw.py:44** — `# FIXME: incomplete`
```
def begin_document(self, id: str | None = None) -> None:
        """Set up printing of a document. (Write PostScript DSC header.)"""
        # FIXME: incomplete
        self.fp.write(
            b"%!PS-Adobe-3.0\n"
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\SpiderImagePlugin.py:161** — `self._fp = self.fp  # FIXME: hack`
```
self.tile = [ImageFile._Tile("raw", (0, 0) + self.size, offset, self.rawmode)]
        self._fp = self.fp  # FIXME: hack

    @property
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\TiffImagePlugin.py:962** — `# FIXME What about tagdata?`
```
def tobytes(self, offset: int = 0) -> bytes:
        # FIXME What about tagdata?
        result = self._pack("Q" if self._bigtiff else "H", len(self._tags_v2))
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\TiffTags.py:209** — `# FIXME add more tags here`
```
33723: ("IptcNaaInfo", UNDEFINED, 1),
    34377: ("PhotoshopInfo", BYTE, 0),
    # FIXME add more tags here
    34665: ("ExifIFD", LONG, 1),
    34675: ("ICCProfile", UNDEFINED, 1),
```
---
- **C:\industria\.venv\Lib\site-packages\PIL\XVThumbImagePlugin.py:17** — `# FIXME: make save work (this requires quantization support)`
```
#
# To do:
# FIXME: make save work (this requires quantization support)
#
from __future__ import annotations
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\build_env.py:200** — `# FIXME: Consider direct URL?`
```
if not req.specifier.contains(dist.version, prereleases=True):
                    conflicting.add((installed_req_str, req_str))
                # FIXME: Consider direct URL?
        return conflicting, missing
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\cache.py:278** — `# TODO: use DirectUrl.equivalent when`
```
)
            else:
                # TODO: use DirectUrl.equivalent when
                # https://github.com/pypa/pip/pull/10564 is merged.
                if origin.url != download_info.url:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\cli\base_command.py:204** — `# TODO: Try to get these passing down from the command?`
```
sys.exit(ERROR)

        # TODO: Try to get these passing down from the command?
        #       without resorting to os.environ to hold these.
        #       This also affects isolated builds and it should.
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\commands\inspect.py:60** — `# TODO tags? scheme?`
```
"installed": [self._dist_to_dict(dist) for dist in dists],
            "environment": default_environment(),
            # TODO tags? scheme?
        }
        print_json(data=output)
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\index\collector.py:344** — `# TODO: In the future, it would be nice if pip supported PEP 691`
```
if not url.endswith("/"):
            url += "/"
        # TODO: In the future, it would be nice if pip supported PEP 691
        #       style responses in the file:// URLs, however there's no
        #       standard file extension for application/vnd.pypi.simple.v1+json
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\locations\base.py:15** — `# FIXME doesn't account for venv linked to global site-packages`
```
USER_CACHE_DIR = appdirs.user_cache_dir("pip")

# FIXME doesn't account for venv linked to global site-packages
site_packages: str = sysconfig.get_path("purelib")
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\metadata\base.py:37** — `from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.`
```
DirectUrlValidationError,
)
from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.
from pip._internal.utils.egg_link import egg_link_path_from_sys_path
from pip._internal.utils.misc import is_local, normalize_path
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\models\installation_report.py:50** — `# TODO: currently, the resolver uses the default environment to evaluate`
```
],
            # https://peps.python.org/pep-0508/#environment-markers
            # TODO: currently, the resolver uses the default environment to evaluate
            # environment markers, so that is what we report here. In the future, it
            # should also take into account options such as --python-version or
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\models\selection_prefs.py:6** — `# TODO: This needs Python 3.10's improved slots support for dataclasses`
```
# TODO: This needs Python 3.10's improved slots support for dataclasses
# to be converted into a dataclass.
class SelectionPreferences:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\network\lazy_wheel.py:174** — `# TODO: Get range requests to be correctly cached`
```
headers = base_headers.copy()
        headers["Range"] = f"bytes={start}-{end}"
        # TODO: Get range requests to be correctly cached
        headers["Cache-Control"] = "no-cache"
        return self._session.get(self._url, headers=headers, stream=True)
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\operations\prepare.py:557** — `# TODO: separate this part out from RequirementPreparer when the v1`
```
self._prepare_linked_requirement(req, parallel_builds)

        # TODO: separate this part out from RequirementPreparer when the v1
        # resolver can be removed!
        self._complete_partial_requirements(
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\req\constructors.py:285** — `# TODO: The is_installable_dir test here might not be necessary`
```
if is_installable_dir(path):
            return path_to_url(path)
        # TODO: The is_installable_dir test here might not be necessary
        #       now that it is done in load_pyproject_toml too.
        raise InstallationError(
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\req\req_file.py:107** — `# TODO: replace this with slots=True when dropping Python 3.9 support.`
```
@dataclass(frozen=True)
class ParsedRequirement:
    # TODO: replace this with slots=True when dropping Python 3.9 support.
    __slots__ = (
        "requirement",
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\req\req_install.py:371** — `# FIXME: Is there a better place to create the build_dir? (hg and bzr`
```
dir_name = f"{dir_name}_{uuid.uuid4().hex}"

        # FIXME: Is there a better place to create the build_dir? (hg and bzr
        # need this)
        if not os.path.exists(build_dir):
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\req\req_set.py:75** — `TODO remove this property together with the legacy resolver, since the new`
```
"""Return the list of requirements that need to be installed.

        TODO remove this property together with the legacy resolver, since the new
             resolver only returns requirements that need to be installed.
        """
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\req\req_uninstall.py:480** — `# FIXME: need a test for this elif block`
```
for installed_file in installed_files:
                    paths_to_remove.add(os.path.join(dist_location, installed_file))
            # FIXME: need a test for this elif block
            # occurs with --single-version-externally-managed/--record outside
            # of pip
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py:227** — `# TODO performance: this means we iterate the dependencies at least twice,`
```
)
        # check dependencies are valid
        # TODO performance: this means we iterate the dependencies at least twice,
        # we may want to cache parsed Requires-Dist
        try:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\resolution\resolvelib\factory.py:201** — `# TODO: Check already installed candidate, and use it if the link and`
```
version: Optional[Version],
    ) -> Optional[BaseCandidate]:
        # TODO: Check already installed candidate, and use it if the link and
        # editable flag match.
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\utils\unpacking.py:326** — `# FIXME: handle?`
```
untar_file(filename, location)
    else:
        # FIXME: handle?
        # FIXME: magic signatures?
        logger.critical(
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_internal\vcs\subversion.py:59** — `# FIXME: should we warn?`
```
entries_fn = os.path.join(base, cls.dirname, "entries")
            if not os.path.exists(entries_fn):
                # FIXME: should we warn?
                continue
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\typing_extensions.py:1020** — `# TODO: Use inspect.VALUE here, and make the annotations lazily evaluated`
```
own_annotations = ns["__annotations__"]
            elif "__annotate__" in ns:
                # TODO: Use inspect.VALUE here, and make the annotations lazily evaluated
                own_annotations = ns["__annotate__"](1)
            else:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\database.py:933** — `# FIXME handle the case where zipfile is not available`
```
requires = parse_requires_path(req_path)
            else:
                # FIXME handle the case where zipfile is not available
                zipf = zipimport.zipimporter(path)
                fileobj = StringIO(zipf.get_data('EGG-INFO/PKG-INFO').decode('utf8'))
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\locators.py:760** — `XXX TODO Note: this cache is never actually cleared. It's assumed that`
```
Get the HTML for an URL, possibly from an in-memory cache.

        XXX TODO Note: this cache is never actually cleared. It's assumed that
        the data won't get stale over the lifetime of a locator instance (not
        necessarily true for the default_locator).
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\metadata.py:239** — `# TODO document the mapping API and UNKNOWN default key`
```
"""

    # TODO document the mapping API and UNKNOWN default key

    def __init__(self, path=None, fileobj=None, mapping=None, scheme='default'):
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\resources.py:190** — `todo = [resource]`
```
resource = self.find(resource_name)
        if resource is not None:
            todo = [resource]
            while todo:
                resource = todo.pop(0)
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\util.py:401** — `# TODO check k, v for valid values`
```
cp = configparser.ConfigParser()
    for k, v in exports.items():
        # TODO check k, v for valid values
        cp.add_section(k)
        for entry in v.values():
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\version.py:267** — `TODO: fill this out`
```
1.2.3c1
        1.2.3.4
        TODO: fill this out

    Bad:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:839** — `# TODO version verification`
```
# wv = message['Wheel-Version'].split('.', 1)
            # file_version = tuple([int(i) for i in wv])
            # TODO version verification

            records = {}
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\pkg_resources\__init__.py:1** — `# TODO: Add Generic type annotations to initialized collections.`
```
# TODO: Add Generic type annotations to initialized collections.
# For now we'd simply use implicit Any/Unknown which would add redundant annotations
# mypy: disable-error-code="var-annotated"
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\pygments\lexer.py:863** — `TODO: clean up the code here.`
```
The result is a combined token stream.

    TODO: clean up the code here.
    """
    insertions = iter(insertions)
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\pygments\filters\__init__.py:72** — `highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.`
```
`codetags` : list of strings
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.

    .. versionchanged:: 2.13
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\pygments\lexers\python.py:715** — `# different tokens.  TODO: DelegatingLexer should support this`
```
tblexer = Python2TracebackLexer
        # We have two auxiliary lexers. Use DelegatingLexer twice with
        # different tokens.  TODO: DelegatingLexer should support this
        # directly, by accepting a tuplet of auxiliary lexers and a tuple of
        # distinguishing tokens. Then we wouldn't need this intermediary
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\pygments\lexers\_mapping.py:535** — `'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),`
```
'TlbLexer': ('pip._vendor.pygments.lexers.tlb', 'Tl-b', ('tlb',), ('*.tlb',), ()),
    'TlsLexer': ('pip._vendor.pygments.lexers.tls', 'TLS Presentation Language', ('tls',), (), ()),
    'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),
    'TransactSqlLexer': ('pip._vendor.pygments.lexers.sql', 'Transact-SQL', ('tsql', 't-sql'), ('*.sql',), ('text/x-tsql',)),
    'TreetopLexer': ('pip._vendor.pygments.lexers.parsers', 'Treetop', ('treetop',), ('*.treetop', '*.tt'), ()),
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\rich\text.py:562** — `# TODO: This is a little inefficient, it is only used by full justify`
```
Style: A Style instance.
        """
        # TODO: This is a little inefficient, it is only used by full justify
        if offset < 0:
            offset = len(self) + offset
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\truststore\_macos.py:558** — `# TODO: Not sure if we need the SecTrustResultType for anything?`
```
)

            # TODO: Not sure if we need the SecTrustResultType for anything?
            # We only care whether or not it's a success or failure for now.
            sec_trust_result_type = Security.SecTrustResultType()
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:199** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self.sock = conn
        if self._is_using_tunnel():
            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
            # Mark this connection as not reusable
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\connectionpool.py:522** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, host, port = get_host(url)
        if host is not None:
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\exceptions.py:289** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme):
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\response.py:441** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.")
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\contrib\pyopenssl.py:371** — `# FIXME rethrow compatible exceptions should we ever use this`
```
def shutdown(self):
        # FIXME rethrow compatible exceptions should we ever use this
        self.connection.shutdown()
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\contrib\securetransport.py:659** — `# TODO: should I do clean shutdown here? Do I have to?`
```
def close(self):
        # TODO: should I do clean shutdown here? Do I have to?
        if self._makefile_refs < 1:
            self._closed = True
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\util\response.py:103** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method = response._method
    if isinstance(method, int):  # Platform-specific: Appengine
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:31** — `# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.`
```
# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.
_Default = object()
```
---
- **C:\industria\.venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:402** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\.venv\Lib\site-packages\proto\_package_info.py:40** — `# TODO: Revert to empty string as a package value after protobuf fix.`
```
# A package should be present; get the marshal from there.
    # TODO: Revert to empty string as a package value after protobuf fix.
    # When package is empty, upb based protobuf fails with an
    # "TypeError: Couldn't build proto file into descriptor pool: invalid name: empty part ()' means"
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\codec\ber\decoder.py:48** — `raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?`
```
The decoder is allowed to consume as many bytes as necessary.
        """
        raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?

    def indefLenValueDecoder(self, substrate, asn1Spec,
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\codec\ber\encoder.py:189** — `# TODO: try to avoid ASN.1 schema instantiation`
```
def encodeValue(self, value, asn1Spec, encodeFun, **options):
        if asn1Spec is not None:
            # TODO: try to avoid ASN.1 schema instantiation
            value = asn1Spec.clone(value)
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\codec\cer\decoder.py:51** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
BitStringPayloadDecoder = decoder.BitStringPayloadDecoder
OctetStringPayloadDecoder = decoder.OctetStringPayloadDecoder
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\codec\der\decoder.py:23** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
RealPayloadDecoder = decoder.RealPayloadDecoder
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\codec\der\encoder.py:34** — `# TODO: move out of sorting key function`
```
return component.getComponent().tagSet
            else:
                # TODO: move out of sorting key function
                names = [namedType.name for namedType in asn1Spec.componentType.namedTypes
                         if namedType.name in component]
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\type\constraint.py:85** — `# TODO: fix possible comparison of set vs scalars here`
```
def isSuperTypeOf(self, otherConstraint):
        # TODO: fix possible comparison of set vs scalars here
        return (otherConstraint is self or
                not self._values or
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1\type\univ.py:1724** — `# TODO: remove when Py2.5 support is gone`
```
indices, values = zip(*self._componentValues.items())

        # TODO: remove when Py2.5 support is gone
        values = list(values)
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1_modules\rfc2459.py:4** — `# Updated by Russ Housley to resolve the TODO regarding the Certificate`
```
# This file is part of pyasn1-modules software.
#
# Updated by Russ Housley to resolve the TODO regarding the Certificate
#   Policies Certificate Extension.
#
```
---
- **C:\industria\.venv\Lib\site-packages\pyasn1_modules\rfc2985.py:86** — `# TODO:`
```
# TODO:
# Need a place to import PKCS15Token; it does not yet appear in an RFC
```
---
- **C:\industria\.venv\Lib\site-packages\pyparsing\helpers.py:898** — `# TODO - determine why this statement can't be included in the following`
```
match_lookahead.show_in_diagram = False

        # TODO - determine why this statement can't be included in the following
        #  if pa block
        matchExpr = match_lookahead + matchExpr
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\graphics\renderPDF.py:72** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\graphics\renderPS.py:772** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\graphics\renderSVG.py:803** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\graphics\widgetbase.py:62** — `# TODO when we need it, but not before -`
```
from reportlab.lib.validators import isValidChild

        # TODO when we need it, but not before -
        # expose sequence contents?
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\platypus\paragraph.py:1272** — `#TODO fix this to use binary search for the split points`
```
then push those new words onto words
    '''
    #TODO fix this to use binary search for the split points
    R = []
    aR = R.append
```
---
- **C:\industria\.venv\Lib\site-packages\reportlab\platypus\xpreformatted.py:209** — `breakLinesCJK = breakLines  #TODO fixme fixme fixme`
```
return lines

    breakLinesCJK = breakLines  #TODO fixme fixme fixme

    # we need this her to get the right splitter
```
---
- **C:\industria\.venv\Lib\site-packages\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\.venv\Lib\site-packages\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\.venv\Lib\site-packages\uritemplate\variable.py:72** — `# TODO: Re-enable after un-commenting 3.9`
```
def reserved_characters(self) -> str:
        # TODO: Re-enable after un-commenting 3.9
        # match self:
        #     case Operator.reserved:
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\connection.py:330** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self._has_connected_to_proxy = True

            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\connectionpool.py:578** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, _, host, port, *_ = parse_url(url)
        scheme = scheme or "http"
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\exceptions.py:306** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme: str | None) -> None:
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\response.py:782** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout as e:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.") from e  # type: ignore[arg-type]
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\_base_connection.py:20** — `# TODO: Remove this in favor of a better`
```
class _ResponseOptions(typing.NamedTuple):
    # TODO: Remove this in favor of a better
    # HTTP request/response lifecycle tracking.
    request_method: str
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\http2\connection.py:144** — `# TODO SKIPPABLE_HEADERS from urllib3 are ignored.`
```
def putheader(self, header: str | bytes, *values: str | bytes) -> None:  # type: ignore[override]
        # TODO SKIPPABLE_HEADERS from urllib3 are ignored.
        header = header.encode() if isinstance(header, str) else header
        header = header.lower()  # A lot of upstream code uses capitalized headers.
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\http2\__init__.py:38** — `# TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.`
```
urllib3_connection.HTTPSConnection = HTTP2Connection  # type: ignore[misc]

    # TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.
    urllib3_util.ALPN_PROTOCOLS = ["h2"]
    urllib3_util_ssl.ALPN_PROTOCOLS = ["h2"]
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\util\request.py:229** — `# File-like object, TODO: use seek() and tell() for length?`
```
content_length = len(chunks[0])

    # File-like object, TODO: use seek() and tell() for length?
    elif hasattr(body, "read"):
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\util\response.py:99** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method_str = response._method  # type: str  # type: ignore[attr-defined]
    return method_str.upper() == "HEAD"
```
---
- **C:\industria\.venv\Lib\site-packages\urllib3\util\url.py:454** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\.venv\Lib\site-packages\werkzeug\http.py:1343** — `# TODO Remove encoding dance, it seems like clients accept UTF-8 keys`
```
# Send a non-ASCII key as mojibake. Everything else should already be ASCII.
    # TODO Remove encoding dance, it seems like clients accept UTF-8 keys
    buf = [f"{key.encode().decode('latin1')}={value}"]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\anyio\_core\_fileio.py:416** — `def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it`
```
@property
        def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it
            return self._path.info
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\blinker\base.py:135** — `# TODO no explanation or test for this`
```
)
            except TypeError:
                # TODO no explanation or test for this
                self.disconnect(receiver, sender)
                raise
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\charset_normalizer\legacy.py:9** — `# TODO: remove this check when dropping Python 3.7 support`
```
from .constant import CHARDET_CORRESPONDENCE

# TODO: remove this check when dropping Python 3.7 support
if TYPE_CHECKING:
    from typing_extensions import TypedDict
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\click\_termui_impl.py:525** — `# TODO: This never terminates if the passed generator never terminates.`
```
fd, filename = tempfile.mkstemp()
    # TODO: This never terminates if the passed generator never terminates.
    text = "".join(generator)
    if not color:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric\rsa.py:221** — `# TODO: Replace with lcm(p - 1, q - 1) once the minimum`
```
# than necessary. (lambda_n always divides phi_n)
    #
    # TODO: Replace with lcm(p - 1, q - 1) once the minimum
    # supported Python version is >= 3.9.
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\cryptography\x509\name.py:357** — `# TODO: this is relatively expensive, if this looks like a bottleneck`
```
def __hash__(self) -> int:
        # TODO: this is relatively expensive, if this looks like a bottleneck
        # for you, consider optimizing!
        return hash(tuple(self._attributes))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\dateutil\rrule.py:1182** — `# TODO: Check -numweeks for next year.`
```
if 1 in rr._byweekno:
                    # Check week number 1 of next year as well
                    # TODO: Check -numweeks for next year.
                    i = no1wkst+numweeks*7
                    if no1wkst != firstwkst:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\dateutil\parser\_parser.py:55** — `# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth`
```
# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth
# making public and/or figuring out if there is something we can
# take off their plate.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\dateutil\zoneinfo\__init__.py:25** — `except IOError as e:  # TODO  switch to FileNotFoundError?`
```
try:
        return BytesIO(get_data(__name__, ZONEFILENAME))
    except IOError as e:  # TODO  switch to FileNotFoundError?
        warnings.warn("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\admin\checks.py:739** — `# Skip ordering in the format field1__field2 (FIXME: checking`
```
return []
        elif LOOKUP_SEP in field_name:
            # Skip ordering in the format field1__field2 (FIXME: checking
            # this format would be nice, but it's a little fiddly).
            return []
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\admin\options.py:437** — `# TODO: this should be handled by some parameter to the ChangeList.`
```
"""
        qs = self.model._default_manager.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\admin\static\admin\js\vendor\jquery\jquery.js:4132** — `//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)`
```
//		paths to a single mechanism.
//	3. Use the same single mechanism to support "private" and "user" data.
//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)
//	5. Avoid exposing implementation details on user objects (eg. expando properties)
//	6. Provide a clear path for implementation upgrade to WeakMap in 2014
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\admin\static\admin\js\vendor\xregexp\xregexp.js:2792** — `// TODO: Remove from `core-js@4``
```
require('../../modules/esnext.symbol.metadata');
require('../../modules/esnext.symbol.observable');
// TODO: Remove from `core-js@4`
require('../../modules/esnext.symbol.pattern-match');
// TODO: Remove from `core-js@4`
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\auth\management\__init__.py:119** — `# TODO: Drop ImportError and KeyError when dropping support for PY312.`
```
result = getpass.getuser()
    except (ImportError, KeyError, OSError):
        # TODO: Drop ImportError and KeyError when dropping support for PY312.
        # KeyError (Python <3.13) or OSError (Python 3.13+) will be raised by
        # os.getpwuid() (called by getuser()) if there is no corresponding
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\db\backends\base\models.py:15** — `# TODO: Is caching really necessary here?  Is complexity worth it?`
```
Return a GDAL SpatialReference object.
        """
        # TODO: Is caching really necessary here?  Is complexity worth it?
        if hasattr(self, "_srs"):
            # Returning a clone of the cached SpatialReference object.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\introspection.py:33** — `# TODO: Research way to find a more specific geometry field type for`
```
) from exc

            # TODO: Research way to find a more specific geometry field type for
            # the column's contents.
            field_type = "GeometryField"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\models.py:21** — `# TODO: Add support for `diminfo` column (type MDSYS.SDO_DIM_ARRAY).`
```
column_name = models.CharField(max_length=1024)
    srid = models.IntegerField(primary_key=True)
    # TODO: Add support for `diminfo` column (type MDSYS.SDO_DIM_ARRAY).

    class Meta:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\operations.py:108** — `),  # TODO: Is this really the same as ST_Intersects()?`
```
"intersects": SDOOperator(
            func="SDO_OVERLAPBDYINTERSECT"
        ),  # TODO: Is this really the same as ST_Intersects()?
        "equals": SDOOperator(func="SDO_EQUAL"),
        "exact": SDOOperator(func="SDO_EQUAL"),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\db\backends\postgis\operations.py:247** — `# TODO: Support 'M' extension.`
```
# Type-based geometries.
        # TODO: Support 'M' extension.
        if f.dim == 3:
            geom_type = f.geom_type + "Z"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\gdal\envelope.py:193** — `# TODO: Fix significant figures.`
```
def wkt(self):
        "Return WKT representing a Polygon for this envelope."
        # TODO: Fix significant figures.
        return "POLYGON((%s %s,%s %s,%s %s,%s %s,%s %s))" % (
            self.min_x,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\gdal\field.py:189** — `# TODO: Adapt timezone information.`
```
def value(self):
        "Return a Python `datetime` object for this OFTDateTime field."
        # TODO: Adapt timezone information.
        #  See https://lists.osgeo.org/pipermail/gdal-dev/2006-February/007990.html
        #  The `tz` variable has values of: 0=unknown, 1=localtime (ambiguous),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\gdal\geometries.py:266** — `# TODO: Fix Envelope() for Point geometries.`
```
def envelope(self):
        "Return the envelope for this Geometry."
        # TODO: Fix Envelope() for Point geometries.
        return Envelope(capi.get_envelope(self.ptr, byref(OGREnvelope())))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\static\gis\js\OLMapWidget.js:39** — `// TODO: allow deleting individual features (#8972)`
```
}

// TODO: allow deleting individual features (#8972)
class MapWidget {
    constructor(options) {
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\utils\layermapping.py:198** — `# TODO: Support more than one geometry field / model.  However, this`
```
"""
        # The geometry field of the model is set here.
        # TODO: Support more than one geometry field / model.  However, this
        # depends on the GDAL Driver in use.
        self.geom_field = False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\contrib\gis\utils\ogrinspect.py:242** — `# TODO: Autodetection of multigeometry types (see #7218).`
```
raise TypeError("Unknown field type %s in %s" % (field_type, mfield))

    # TODO: Autodetection of multigeometry types (see #7218).
    gtype = layer.geom_type
    if multi_geom:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\core\handlers\asgi.py:56** — `# TODO: Better is-prefix checking, slash handling?`
```
self.script_name = get_script_prefix(scope)
        if self.script_name:
            # TODO: Better is-prefix checking, slash handling?
            self.path_info = scope["path"].removeprefix(self.script_name)
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\backends\oracle\operations.py:45** — `# TODO: colorize this SQL code with style.SQL_KEYWORD(), etc.`
```
set_operators = {**BaseDatabaseOperations.set_operators, "difference": "MINUS"}

    # TODO: colorize this SQL code with style.SQL_KEYWORD(), etc.
    _sequence_reset_sql = """
DECLARE
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\migrations\graph.py:272** — `todo = set(self.nodes)`
```
# Algo from GvR:
        # https://neopythonic.blogspot.com/2009/01/detecting-cycles-in-directed-graph.html
        todo = set(self.nodes)
        while todo:
            node = todo.pop()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\migrations\state.py:295** — `# TODO: investigate if old relational fields must be reloaded or if`
```
else:
            fields[name] = field
        # TODO: investigate if old relational fields must be reloaded or if
        # it's sufficient if the new field is (#27737).
        # Delay rendering of relationships if it's not a relational field and
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\models\base.py:1489** — `# TODO: Handle multiple backends with different feature flags.`
```
f = self._meta.get_field(field_name)
                lookup_value = getattr(self, f.attname)
                # TODO: Handle multiple backends with different feature flags.
                if lookup_value is None or (
                    lookup_value == ""
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\models\expressions.py:947** — `# FIXME: Rename possibly_multivalued to multivalued and fix detection`
```
f"{self.name}."
            )
        # FIXME: Rename possibly_multivalued to multivalued and fix detection
        # for non-multivalued JOINs (e.g. foreign key fields). This should take
        # into account only many-to-many and one-to-many relationships.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1306** — `# TODO: Handle multiple backends with different feature flags.`
```
# the value in the form field (to pass into widget for example).
        defaults = {"max_length": self.max_length}
        # TODO: Handle multiple backends with different feature flags.
        if self.null and not connection.features.interprets_empty_strings_as_nulls:
            defaults["empty_value"] = None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\db\models\sql\query.py:2659** — `# TODO: It might be possible to trim more joins from the start of the`
```
self.where.add(extra_restriction, AND)
        else:
            # TODO: It might be possible to trim more joins from the start of the
            # inner query if it happens to have a longer join chain containing the
            # values in select_fields. Lets punt this one for now.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\forms\models.py:612** — `# Create the inner Meta class. FIXME: ideally, we should be able to`
```
field class.
    """
    # Create the inner Meta class. FIXME: ideally, we should be able to
    # construct a ModelForm without creating and passing in a temporary
    # inner class.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\http\multipartparser.py:408** — `# FIXME: this currently assumes that upload handlers store the file as 'file'`
```
def _close_files(self):
        # Free up all file handles.
        # FIXME: this currently assumes that upload handlers store the file as 'file'
        # We should document that...
        # (Maybe add handler.free_file to complement new_file)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\test\testcases.py:1689** — `# TODO: Modify if/when that internal API is refactored`
```
# Emulate behavior of django.contrib.staticfiles.views.serve() when it
        # invokes staticfiles' finders functionality.
        # TODO: Modify if/when that internal API is refactored
        final_rel_path = os_rel_path.replace("\\", "/").lstrip("/")
        return serve(request, final_rel_path, document_root=self.get_base_dir())
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\django\utils\regex_helper.py:87** — `# FIXME: One day we'll should do this, but not in 1.0.`
```
result.append(".")
            elif ch == "|":
                # FIXME: One day we'll should do this, but not in 1.0.
                raise NotImplementedError("Awaiting Implementation")
            elif ch == "^":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\firebase_admin\_rfc3339.py:73** — `# TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex`
```
# Note: %z parses timezone offsets, but requires the timezone offset *not*
    # include a separating ':'. As of python 3.7, this was relaxed.
    # TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex
    # replacement.
    datestr_modified = re.sub(r'(\d\d):(\d\d)$', r'\1\2', datestr_modified)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\firebase_admin\_user_import.py:478** — `# TODO(rsgowman): This class used to be specific to importing users (hence`
```
as importing users or deleting multiple user accounts.
    """
    # TODO(rsgowman): This class used to be specific to importing users (hence
    # it's home in _user_import.py). It's now also used by bulk deletion of
    # users. Move this to a more common location.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\bidi.py:291** — `# TODO: api_core should expose the future interface for wrapped`
```
request_generator.call = call

        # TODO: api_core should expose the future interface for wrapped
        # callables as well.
        if hasattr(call, "_wrapped"):  # pragma: NO COVER
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\client_logging.py:12** — `# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.`
```
# Fields to be included in the StructuredLogFormatter.
#
# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.
_recognized_logging_fields = [
    "httpRequest",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\exceptions.py:498** — `# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.`
```
# to `format_http_response_error` which expects a more abstract response from google.auth and is
# compatible with both sync and async response types.
# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.
def format_http_response_error(
    response, method: str, url: str, payload: Optional[Dict] = None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\extended_operation.py:138** — `# TODO(dovs): there is not currently a good way to determine whether the`
```
def cancelled(self):
        # TODO(dovs): there is not currently a good way to determine whether the
        # operation has been cancelled.
        # The best we can do is manually keep track of cancellation
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\grpc_helpers.py:295** — `# TODO(https://github.com/googleapis/python-api-core/issues/598):`
```
# Use grpc.compute_engine_channel_credentials in order to support Direct Path.
        # See https://grpc.github.io/grpc/python/grpc.html#grpc.compute_engine_channel_credentials
        # TODO(https://github.com/googleapis/python-api-core/issues/598):
        # Although `grpc.compute_engine_channel_credentials` returns channel credentials
        # outside of a Google Compute Engine environment (GCE), we should determine if
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\rest_streaming_async.py:54** — `# TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content`
```
self._response = response
        self._chunk_size = 1024
        # TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content
        # method as an async generator as it looks for the `yield` keyword in the implementation.
        # Given that the abstract method is not implemented, mypy fails to recognize it as an async generator.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry_async.py:17** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry_async.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\operations_v1\operations_rest_client_async.py:109** — `# TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry``
```
name: str,
        *,
        # TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry`
        # to allow configuring retryable error codes.
        retry=gapic_v1.method_async.DEFAULT,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\operations_v1\transports\base.py:52** — `# TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.`
```
*,
        host: str = DEFAULT_HOST,
        # TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\operations_v1\transports\rest.py:134** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\operations_v1\transports\rest_asyncio.py:84** — `# TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.`
```
http_options: Optional[Dict] = None,
        path_prefix: str = "v1",
        # TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/716): Add docstring for `scopes` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/717): Add docstring for `quota_project_id` to async REST transport.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry\retry_streaming.py:113** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry\retry_streaming_async.py:116** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry\retry_unary.py:144** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry\retry_unary_async.py:155** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\api_core\retry\__init__.py:33** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\auth\_helpers.py:43** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.`
```
REFRESH_THRESHOLD = datetime.timedelta(minutes=3, seconds=45)

# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.
_SENSITIVE_FIELDS = {
    "accessToken",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\auth\aio\_helpers.py:42** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):`
```
return json_response
    except Exception:
        # TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):
        # Parse and return response payload as json based on different content types.
        return None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\auth\compute_engine\_metadata.py:82** — `# TODO: implement GCE residency detection on Windows`
```
if os.name == "nt":
        # TODO: implement GCE residency detection on Windows
        return False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\auth\transport\_aiohttp_requests.py:146** — `# TODO: Use auto_decompress property for aiohttp 3.7+`
```
def __init__(self, session=None):
        # TODO: Use auto_decompress property for aiohttp 3.7+
        if session is not None and session._auto_decompress:
            raise exceptions.InvalidOperation(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\firestore_admin_v1\services\firestore_admin\transports\rest.py:1882** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\firestore_v1\watch.py:75** — `# TODO: Currently this uses a dict. Other implementations use a rbtree.`
```
class WatchDocTree(object):
    # TODO: Currently this uses a dict. Other implementations use a rbtree.
    # The performance of this implementation should be investigated and may
    # require modifying the underlying datastructure to a rbtree.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\firestore_v1\_helpers.py:750** — `# TODO: other transforms`
```
def _apply_merge_all(self) -> None:
        self.data_merge = sorted(self.field_paths + self.deleted_fields)
        # TODO: other transforms
        self.transform_merge = self.transform_paths
        self.merge = sorted(self.data_merge + self.transform_paths)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\firestore_v1\__init__.py:66** — `# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match`
```
from google.cloud.firestore_v1.watch import Watch

# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match
# firestore.py. So comment out until needed on customer level for certain.
# from .services.firestore import FirestoreClient
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\firestore_v1\services\firestore\transports\rest.py:970** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\storage\blob.py:4789** — `# TODO: After google-cloud-core 1.6.0 is stable and we upgrade it`
```
:returns: The host name.
    """
    # TODO: After google-cloud-core 1.6.0 is stable and we upgrade it
    # to 1.6.0 in setup.py, we no longer need to check the attribute
    # existence. We can simply return connection.get_api_base_url_for_mtls().
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\cloud\storage\_http.py:54** — `# TODO: When metrics all use gccl, this should be removed #9552`
```
self._client_info.client_library_version = __version__

        # TODO: When metrics all use gccl, this should be removed #9552
        if self._client_info.user_agent is None:  # pragma: no branch
            self._client_info.user_agent = ""
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\descriptor.py:26** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
  _message = api_implementation._c_module
  # TODO: Remove this import after fix api_implementation
  if _message is None:
    from google.protobuf.pyext import _message
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\descriptor_database.py:139** — `# TODO: implement this API.`
```
def FindFileContainingExtension(self, extendee_name, extension_number):
    # TODO: implement this API.
    return None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\descriptor_pool.py:1360** — `# TODO: This pool could be constructed from Python code, when we`
```
if _USE_C_DESCRIPTORS:
  # TODO: This pool could be constructed from Python code, when we
  # support a flag like 'use_cpp_generated_pool=True'.
  # pylint: disable=protected-access
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\message.py:8** — `# TODO: We should just make these methods all "pure-virtual" and move`
```
# https://developers.google.com/open-source/licenses/bsd

# TODO: We should just make these methods all "pure-virtual" and move
# all implementation out, into reflection.py for now.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\message_factory.py:100** — `# TODO: Remove this check here. Duplicate extension`
```
_ = GetMessageClass(extension.containing_type)
      if api_implementation.Type() != 'python':
        # TODO: Remove this check here. Duplicate extension
        # register check should be in descriptor_pool.
        if extension is not pool.FindExtensionByNumber(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\symbol_database.py:136** — `# TODO: Fix the differences with MessageFactory.`
```
def GetMessages(self, files):
    # TODO: Fix the differences with MessageFactory.
    """Gets all registered messages from a specified file.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\text_format.py:22** — `# TODO Import thread contention leads to test failures.`
```
__author__ = 'kenton@google.com (Kenton Varda)'

# TODO Import thread contention leads to test failures.
import encodings.raw_unicode_escape  # pylint: disable=unused-import
import encodings.unicode_escape  # pylint: disable=unused-import
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\internal\api_implementation.py:88** — `# TODO: fail back to python`
```
del _message
  except ImportError:
    # TODO: fail back to python
    warnings.warn(
        'Selected implementation cpp is not available.')
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\internal\builder.py:96** — `# TODO: Remove this on-op`
```
file_des: FileDescriptor of the .proto file
  """
  # TODO: Remove this on-op
  return
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\internal\containers.py:98** — `# TODO: Remove this. BaseContainer does *not* conform to`
```
# TODO: Remove this. BaseContainer does *not* conform to
# MutableSequence, only its subclasses do.
collections.abc.MutableSequence.register(BaseContainer)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\internal\extension_dict.py:37** — `# TODO: Unify error handling of "unknown extension" crap.`
```
# TODO: Unify error handling of "unknown extension" crap.
# TODO: Support iteritems()-style iteration over all
# extensions with the "has" bits turned on?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\internal\python_message.py:10** — `# TODO: Helpers for verbose, common checks like seeing if a`
```
# This code is meant to work on Python 2.4 and above only.
#
# TODO: Helpers for verbose, common checks like seeing if a
# descriptor's cpp_type is CPPTYPE_MESSAGE.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\google\protobuf\pyext\cpp_message.py:21** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
_message = api_implementation._c_module
# TODO: Remove this import after fix api_implementation
if _message is None:
  from google.protobuf.pyext import _message
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\_auth.py:37** — `# TODO(xuanwn): Give credentials an actual type.`
```
_credentials: Any

    # TODO(xuanwn): Give credentials an actual type.
    def __init__(self, credentials: Any):
        self._credentials = credentials
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\_channel.py:257** — `# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.`
```
# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.
# pylint: disable=too-many-statements
def _consume_request_iterator(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\_observability.py:271** — `# TODO(xuanwn): use channel args to exclude those metrics.`
```
RPC.
    """
    # TODO(xuanwn): use channel args to exclude those metrics.
    for exclude_prefix in _SERVICES_TO_EXCLUDE:
        if exclude_prefix in state.method.encode("utf8"):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\_server.py:1182** — `# TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.`
```
self.registered_method_handlers = {}

        # TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.
        self.rpc_states = set()
        self.due = set()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\aio\_channel.py:409** — `# TODO(lidiz) drop this hack after 3.8 deprecation`
```
# but not available until 3.9 or 3.8.3. So, we have to keep it
                # for a while.
                # TODO(lidiz) drop this hack after 3.8 deprecation
                if "frame" in str(attribute_error):
                    continue
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\aio\_server.py:87** — `# TODO(xuanwn): Implement this for AsyncIO.`
```
method_handlers: Dict[str, grpc.RpcMethodHandler],
    ) -> None:
        # TODO(xuanwn): Implement this for AsyncIO.
        pass
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\beta\_client_adaptations.py:85** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
class _InvocationProtocolContext(interfaces.GRPCInvocationContext):
    def disable_next_request_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\grpc\beta\_server_adaptations.py:43** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
def disable_next_response_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\gunicorn\arbiter.py:365** — `# TODO: select.error is a subclass of OSError since Python 3.3.`
```
pass
        except OSError as e:
            # TODO: select.error is a subclass of OSError since Python 3.3.
            error_number = getattr(e, 'errno', e.args[0])
            if error_number not in [errno.EAGAIN, errno.EINTR]:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\gunicorn\config.py:2377** — `# FIXME: refactor all of this subclassing stdlib argparse`
```
def validate_header_map_behaviour(val):
    # FIXME: refactor all of this subclassing stdlib argparse

    if val is None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\gunicorn\__main__.py:9** — `# todo: let runpy.run_module take care of argv[0] rewriting`
```
if __name__ == "__main__":
    # see config.py - argparse defaults to basename(argv[0]) == "__main__.py"
    # todo: let runpy.run_module take care of argv[0] rewriting
    run(prog="gunicorn")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h11\_events.py:310** — `# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that`
```
# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that
# are forbidden to be sent in a trailer, since processing them as if they were
# present in the header section might bypass external security filters."
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h11\_readers.py:186** — `# XX FIXME: we discard chunk extensions. Does anyone care?`
```
chunk_header,
            )
            # XX FIXME: we discard chunk extensions. Does anyone care?
            self._bytes_in_chunk = int(matches["chunk_size"], base=16)
            if self._bytes_in_chunk == 0:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h11\_writers.py:54** — `# XX FIXME: could at least make an effort to pull out the status message`
```
# status code is mandatory.)
    #
    # XX FIXME: could at least make an effort to pull out the status message
    # from stdlib's http.HTTPStatus table. Or maybe just steal their enums
    # (either by import or copy/paste). We already accept them as status codes
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h2\connection.py:1808** — `# FIXME: Should we split this into one event per active stream?`
```
)

            # FIXME: Should we split this into one event per active stream?
            window_updated_event = WindowUpdated()
            window_updated_event.stream_id = 0
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h2\utilities.py:417** — `# TODO: We should also guard against receiving duplicate Host headers,`
```
# enforced by the _reject_pseudo_header_fields() pipeline.
    #
    # TODO: We should also guard against receiving duplicate Host headers,
    # and against sending duplicate headers.
    authority_header_val = None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\h2\windows.py:116** — `# TODO: Can the window be smaller than 1024 bytes? If not, we can`
```
small DATA frames.
        """
        # TODO: Can the window be smaller than 1024 bytes? If not, we can
        # streamline this algorithm.
        if not self._bytes_processed:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\hpack\hpack.py:321** — `# header table unconditionally. It is a future todo to`
```
else:
            # Indexed literal. We are going to add header to the
            # header table unconditionally. It is a future todo to
            # filter out headers which are known to be ineffective for
            # indexing since they just take space in the table and
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\httpx\_auth.py:267** — `# TODO: implement auth-int`
```
path = request.url.raw_path
        A2 = b":".join((request.method.encode(), path))
        # TODO: implement auth-int
        HA2 = digest(A2)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\itsdangerous\timed.py:182** — `# TODO: Signature is incompatible because parameters were added`
```
return t.cast("cabc.Iterator[TimestampSigner]", super().iter_unsigners(salt))

    # TODO: Signature is incompatible because parameters were added
    #  before salt.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\jinja2\ext.py:251** — `# TODO: the i18n extension is currently reevaluating values in a few`
```
tags = {"trans"}

    # TODO: the i18n extension is currently reevaluating values in a few
    # situations.  Take this example:
    #   {% trans count=something() %}{{ count }} foo{% pluralize
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\jinja2\nodes.py:212** — `todo = deque([self])`
```
targets and other nodes to a store context.
        """
        todo = deque([self])
        while todo:
            node = todo.popleft()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\conftest.py:105** — `# FIXME when yield tests are gone.`
```
pytest.exit("GIL re-enabled during tests", returncode=1)

# FIXME when yield tests are gone.
@pytest.hookimpl()
def pytest_itemcollected(item):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\__init__.py:927** — `# TODO: Remove the environment variable entirely now that it is "weak"`
```
_core.multiarray._multiarray_umath._reload_guard()

    # TODO: Remove the environment variable entirely now that it is "weak"
    if (os.environ.get("NPY_PROMOTION_STATE", "weak") != "weak"):
        warnings.warn(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\capi_maps.py:249** — `# TODO: support Fortran `len` function with optional kind parameter`
```
"""
    # TODO: support Fortran `len` function with optional kind parameter
    expr = re.sub(r'\blen\b', 'f2py_slen', expr)
    return expr
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\cfuncs.py:745** — `/* TODO: change the type of `len` so that we can remove this */`
```
}
    if (*len == -1) {
        /* TODO: change the type of `len` so that we can remove this */
        if (n > NPY_MAX_INT) {
            PyErr_SetString(PyExc_OverflowError,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\crackfortran.py:133** — `TODO:`
```
In addition, the following attributes are used: check,depend,note

TODO:
    * Apply 'parameter' attribute (e.g. 'integer parameter :: i=2' 'real x(i)'
                                   -> 'real x(2)')
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\f2py2e.py:461** — `# TODO: Remove all this when scaninputline is replaced`
```
pyf_files, _ = filter_files("", "[.]pyf([.]src|)", comline_list)
    # Checks that no existing modulename is defined in a pyf file
    # TODO: Remove all this when scaninputline is replaced
    if args.module_name:
        if "-h" in comline_list:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\symbolic.py:23** — `# TODO: support logical constants (Op.BOOLEAN)`
```
# contain C expressions that support here is implemented as well.
#
# TODO: support logical constants (Op.BOOLEAN)
# TODO: support logical operators (.AND., ...)
# TODO: support defined operators (.MYOP., ...)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\_isocbind.py:55** — `# TODO: See gh-25229`
```
}

# TODO: See gh-25229
isoc_c2pycode_map = {}
iso_c2py_map = {}
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\src\fortranobject.c:1371** — `// TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).`
```
sprintf(localbuf, "%s instance", Py_TYPE(obj)->tp_name);
  }
  // TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).
  strcpy(buf, localbuf);
  return 1;
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\tests\test_docs.py:64** — `# TODO: implement test methods for other example Fortran codes`
```
np.array([1, 45, 3], dtype=np.float32))

    # TODO: implement test methods for other example Fortran codes
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\f2py\tests\test_f2py2e.py:415** — `# TODO: Clean up to prevent passing --overwrite-signature`
```
capslo = re.compile(r"Block: hi")
    # Case I: --lower is implied by -h
    # TODO: Clean up to prevent passing --overwrite-signature
    monkeypatch.setattr(
        sys,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\fft\__init__.py:203** — `# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should`
```
"""

# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should
# be deleted once downstream libraries move to `numpy.fft`.
from . import _helper, _pocketfft, helper
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\mixins.py:166** — `# TODO: handle the optional third argument for __pow__?`
```
__rdivmod__ = _reflected_binary_method(um.divmod, 'divmod')
    # __idivmod__ does not exist
    # TODO: handle the optional third argument for __pow__?
    __pow__, __rpow__, __ipow__ = _numeric_methods(um.power, 'pow')
    __lshift__, __rlshift__, __ilshift__ = _numeric_methods(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\_datasource.py:71** — `# TODO: .zip support, .tar support?`
```
# deferring the import of lzma, bz2 and gzip until needed

# TODO: .zip support, .tar support?
class _FileOpeners:
    """
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\_function_base_impl.py:866** — `# TODO: This preserves the Python int, float, complex manually to get the`
```
raise ValueError("select with an empty condition list is not possible")

    # TODO: This preserves the Python int, float, complex manually to get the
    #       right `result_type` with NEP 50.  Most likely we will grow a better
    #       way to spell this (and this can be replaced).
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\_nanfunctions_impl.py:1689** — `# TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?`
```
See nanpercentile for parameter usage
    """
    # TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?
    arr1d, weights, overwrite_input = _remove_nan_1d(arr1d,
        second_arr1d=weights, overwrite_input=overwrite_input)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\_npyio_impl.py:249** — `# FIXME: This seems like it will copy strings around`
```
bytes.seek(0)
                if magic == format.MAGIC_PREFIX:
                    # FIXME: This seems like it will copy strings around
                    #   more than is strictly necessary.  The zipfile
                    #   will read the string and then
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\tests\test_function_base.py:3816** — `# TODO: Note that times have dubious rounding as of fixing NaTs!`
```
@pytest.mark.parametrize("pos", [0, 23, 10])
    def test_nat_basic(self, dtype, pos):
        # TODO: Note that times have dubious rounding as of fixing NaTs!
        # NaT and NaN should behave the same, do basic tests for NaT:
        a = np.arange(0, 24, dtype=dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\tests\test_io.py:323** — `sup.filter(ResourceWarning)  # TODO: specify exact message`
```
# collector, so we catch the warnings.
            with suppress_warnings() as sup:
                sup.filter(ResourceWarning)  # TODO: specify exact message
                for i in range(1, 1025):
                    try:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\tests\test_recfunctions.py:560** — `# Fixme, this test looks incomplete and broken`
```
z = self.data[-1]

        # Fixme, this test looks incomplete and broken
        #test = merge_arrays((z, np.array([10, 20, 30]).view([('C', int)])))
        #control = np.array([('A', 1., 10), ('B', 2., 20), ('-1', -1, 20)],
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\lib\tests\test_type_check.py:279** — `# Fixme, wrong place, isfinite now ufunc`
```
class TestIsfinite:
    # Fixme, wrong place, isfinite now ufunc

    def test_goodvalues(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\linalg\tests\test_linalg.py:1059** — `# FIXME the 'e' dtype might work in future`
```
noninv = array([[1, 0], [0, 0]])
    stacked = np.block([[[rshft_0]]] * 2)
    # FIXME the 'e' dtype might work in future
    dtnoinv = [object, np.dtype('e'), np.dtype('g'), np.dtype('G')]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\ma\core.py:237** — `# TODO: This is probably a mess, but should best preserve behavior?`
```
# for integer casts, this allows the use of 99999 as a fill value
        # for int8.
        # TODO: This is probably a mess, but should best preserve behavior?
        vals = tuple(
                np.array(_recursive_fill_value(dtype[name], f))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\ma\tests\test_core.py:5617** — `# TODO: Test masked_object, masked_equal, ...`
```
class TestMaskedWhereAliases:

    # TODO: Test masked_object, masked_equal, ...

    def test_masked_values(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\ma\tests\test_old_ma.py:720** — `# TODO FIXME: Find out what the following raises a warning in r8247`
```
def test_testScalarArithmetic(self):
        xm = array(0, mask=1)
        # TODO FIXME: Find out what the following raises a warning in r8247
        with np.errstate(divide='ignore'):
            assert_((1 / array(0)).mask)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\polynomial\chebyshev.py:798** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(chebmul, c1, c2)`
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\polynomial\polynomial.py:405** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(polymul, c1, c2)`
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\polynomial\polyutils.py:538** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    lc1 = len(c1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\polynomial\_polybase.py:432** — `# TODO: we're stuck with disabling math formatting until we handle`
```
@staticmethod
    def _repr_latex_scalar(x, parens=False):
        # TODO: we're stuck with disabling math formatting until we handle
        # exponents in this function
        return fr'\text{{{pu.format_float(x, parens=parens)}}}'
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\random\tests\test_random.py:1069** — `# TODO: Include test for randint once it can broadcast`
```
np.random.seed(self.seed)

    # TODO: Include test for randint once it can broadcast
    # Can steal the test written in PR #6938
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\arrayprint.py:1567** — `# TODO: Custom repr for user DTypes, logic should likely move.`
```
"""
    if type(dtype).__repr__ != np.dtype.__repr__:
        # TODO: Custom repr for user DTypes, logic should likely move.
        return repr(dtype)
    if dtype.names is not None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\fromnumeric.py:44** — `# but this follows what was done before. TODO: revisit this.`
```
conv = _array_converter(obj)
    # As this already tried the method, subok is maybe quite reasonable here
    # but this follows what was done before. TODO: revisit this.
    arr, = conv.as_arrays(subok=False)
    result = getattr(arr, method)(*args, **kwds)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\getlimits.py:374** — `TODO: MachAr should be retired completely ideally.  We currently only`
```
""" Create MachAr instance with found information on float types

    TODO: MachAr should be retired completely ideally.  We currently only
          ever use it system with broken longdouble (valgrind, WSL).
    """
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\numeric.py:545** — `# TODO: this works around .astype(bool) not working properly (gh-9847)`
```
a = asanyarray(a)

    # TODO: this works around .astype(bool) not working properly (gh-9847)
    if np.issubdtype(a.dtype, np.character):
        a_bool = a != a.dtype.type()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\_add_newdocs.py:2276** — `assignment examples; TODO).`
```
Flattened version of the array as an iterator.  The iterator
        allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
        assignment examples; TODO).
    imag : ndarray
        Imaginary part of the array.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\_add_newdocs_scalars.py:129** — `# TODO: These docs probably need an if to highlight the default rather than`
```
""")

# TODO: These docs probably need an if to highlight the default rather than
#       the C-types (and be correct).
add_newdoc_for_scalar_type('int_', [],
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\_dtype.py:174** — `# TODO: this path can never be reached`
```
return native.byteorder
    if byteorder == 'S':
        # TODO: this path can never be reached
        return swapped.byteorder
    elif byteorder == '|':
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\_methods.py:88** — `# TODO: Optimize case when `where` is broadcast along a non-reduction`
```
items = nt.intp(items)
    else:
        # TODO: Optimize case when `where` is broadcast along a non-reduction
        # axis and full sum is more excessive than needed.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_array_coercion.py:452** — `# TODO: This discrepancy _should_ be resolved, either by relaxing the`
```
# case, and traditionally in most cases the behaviour is maintained
        # like this.  (`np.array(scalar, dtype="U6")` would have failed before)
        # TODO: This discrepancy _should_ be resolved, either by relaxing the
        #       cast, or by deprecating the first part.
        scalar = np.datetime64(val, unit)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_casting_unittests.py:781** — `# TODO: While this test is fairly thorough, right now, it does not`
```
def test_structured_view_offsets_parametric(
            self, from_dt, to_dt, expected_off):
        # TODO: While this test is fairly thorough, right now, it does not
        # really test some paths that may have nonzero offsets (they don't
        # really exists).
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_datetime.py:1585** — `# TODO: Allowing unsafe casting by`
```
# should raise between datetime and timedelta
        #
        # TODO: Allowing unsafe casting by
        #       default in ufuncs strikes again... :(
        a = np.array(3, dtype='m8[h]')
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_machar.py:19** — `# Fixme, this needs to raise a 'skip' exception.`
```
MachAr(lambda v: array(v, hiprec))
        except AttributeError:
            # Fixme, this needs to raise a 'skip' exception.
            "Skipping test: no ntypes.float96 available on this platform."
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_multiarray.py:6360** — `# FIXME:`
```
# stats for integer types
        # FIXME:
        # this needs definition as there are lots places along the line
        # where type casting may take place.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_scalarmath.py:103** — `# TODO: It would be nice to resolve this issue.`
```
# array**scalar special case can have different result dtype
        # (Other powers may have issues also, but are not hit here.)
        # TODO: It would be nice to resolve this issue.
        pytest.skip("array**2 can have incorrect/weird result dtype")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_stringdtype.py:1521** — `# TODO: generalize to more ufuncs`
```
# accept more than one string argument and produce a string should
    # behave this way
    # TODO: generalize to more ufuncs
    inp = ["hello", "world"]
    arr = np.array(inp, dtype=StringDType(na_object=None))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_umath.py:1152** — `# FIXME cinf not tested.`
```
one = np.array([1 + 0j])
        cnan = np.array([complex(np.nan, np.nan)])
        # FIXME cinf not tested.
        #cinf = np.array([complex(np.inf, 0)])
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_core\tests\test_umath_complex.py:17** — `# TODO: branch cuts (use Pauli code)`
```
)

# TODO: branch cuts (use Pauli code)
# TODO: conj 'symmetry'
# TODO: FPU exceptions
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_typing\_array_like.py:48** — `# TODO: Wait until mypy supports recursive objects in combination with typevars`
```
# TODO: Wait until mypy supports recursive objects in combination with typevars
_FiniteNestedSequence: TypeAlias = (
    _T
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_typing\_char_codes.py:211** — `# TODO: add `_StringCodes` once it has a scalar type`
```
_TD64Codes,
    _ObjectCodes,
    # TODO: add `_StringCodes` once it has a scalar type
    # _StringCodes,
]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\numpy\_typing\_dtype_like.py:31** — `_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types`
```
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True)

_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\_typing.py:386** — `# TODO(typing#684): add Ellipsis, see`
```
# PositionalIndexerTuple is extends the PositionalIndexer for 2D arrays
# These are used in various __getitem__ overloads
# TODO(typing#684): add Ellipsis, see
# https://github.com/python/typing/issues/684#issuecomment-548203158
# https://bugs.python.org/issue41810
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\api\typing\__init__.py:29** — `# TODO: Can't import Styler without importing jinja2`
```
)

# TODO: Can't import Styler without importing jinja2
# from pandas.io.formats.style import Styler
from pandas.io.json._json import JsonReader
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\algorithms.py:155** — `# e.g. Sparse[bool, False]  # TODO: no test cases get here`
```
return np.asarray(values).view("uint8")
        else:
            # e.g. Sparse[bool, False]  # TODO: no test cases get here
            return np.asarray(values).astype("uint8", copy=False)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\apply.py:922** — `# TODO: Avoid having to change state`
```
axis = self.axis

        # TODO: Avoid having to change state
        self.obj = self.obj if self.axis == 0 else self.obj.T
        self.axis = 0
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arraylike.py:361** — `# TODO: When we support multiple values in __finalize__, this`
```
result, **reconstruct_axes, **reconstruct_kwargs, copy=False
            )
        # TODO: When we support multiple values in __finalize__, this
        # should pass alignable to `__finalize__` instead of self.
        # Then `np.add(a, b)` would consider attrs from both a and b
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\base.py:227** — `# TODO: following GH#45287 can we now use .drop directly without`
```
# equivalent to `self.obj.drop(self.exclusions, axis=1)
            #  but this avoids consolidating and making a copy
            # TODO: following GH#45287 can we now use .drop directly without
            #  making a copy?
            return self.obj._drop_axis(self.exclusions, axis=1, only_slice=True)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\common.py:342** — `# TODO: used only once in indexing; belongs elsewhere?`
```
# TODO: used only once in indexing; belongs elsewhere?
def is_full_slice(obj, line: int) -> bool:
    """
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\config_init.py:426** — `# TODO(3.0): enforcing this deprecation will close GH#52501`
```
def use_inf_as_na_cb(key) -> None:
    # TODO(3.0): enforcing this deprecation will close GH#52501
    from pandas.core.dtypes.missing import _use_inf_as_na
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\construction.py:795** — `# TODO: test cases with arr.dtype.kind in "mM"`
```
elif dtype.kind == "U":
        # TODO: test cases with arr.dtype.kind in "mM"
        if is_ndarray:
            arr = cast(np.ndarray, arr)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\frame.py:896** — `# TODO(EA2D): special case not needed with 2D EAs`
```
# For data is a scalar extension dtype
            if isinstance(dtype, ExtensionDtype):
                # TODO(EA2D): special case not needed with 2D EAs

                values = [
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\generic.py:5587** — `# TODO: Decide if we care about having different examples for different`
```
See the :ref:`user guide <basics.reindexing>` for more.
        """
        # TODO: Decide if we care about having different examples for different
        # kinds
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexing.py:949** — `# FIXME: this assumes only one Ellipsis`
```
#  treat as a single null slice.
                i = tup.index(Ellipsis)
                # FIXME: this assumes only one Ellipsis
                new_key = tup[:i] + (_NS,) + tup[i + 1 :]
                return new_key
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\nanops.py:128** — `# TODO(GH-18976) update all the nanops methods to`
```
# Only applies for the default `min_count` of None
                # since that affects how empty arrays are handled.
                # TODO(GH-18976) update all the nanops methods to
                # correctly handle empty inputs and remove this check.
                # It *may* just be `var`
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\resample.py:448** — `# TODO: test_resample_apply_with_additional_args fails if we go`
```
try:
            if callable(how):
                # TODO: test_resample_apply_with_additional_args fails if we go
                #  through the non-lambda path, not clear that it should.
                func = lambda x: how(x, *args, **kwargs)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\series.py:2271** — `# TODO: integrate bottleneck`
```
# Statistics, overridden ndarray methods

    # TODO: integrate bottleneck
    def count(self) -> int:
        """
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\base.py:2170** — `# TODO(3.0): this can be removed once GH#33302 deprecation is enforced`
```
return result

    # TODO(3.0): this can be removed once GH#33302 deprecation is enforced
    def _fill_mask_inplace(
        self, method: str, limit: int | None, mask: npt.NDArray[np.bool_]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\categorical.py:2147** — `# TODO: GH#15362`
```
# max(np.uint64) as the missing value indicator
        #
        # TODO: GH#15362

        mask = self.isna()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\datetimelike.py:350** — `# TODO: Remove Datetime & DatetimeTZ formatters.`
```
def _formatter(self, boxed: bool = False):
        # TODO: Remove Datetime & DatetimeTZ formatters.
        return "'{}'".format
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\datetimes.py:286** — `# TODO: require any NAs be valid-for-DTA`
```
def _from_scalars(cls, scalars, *, dtype: DtypeObj) -> Self:
        if lib.infer_dtype(scalars, skipna=True) not in ["datetime", "datetime64"]:
            # TODO: require any NAs be valid-for-DTA
            # TODO: if dtype is passed, check for tzawareness compat?
            raise ValueError
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\interval.py:858** — `# TODO: in an IntervalIndex we can reuse the cached`
```
if ascending and kind == "quicksort" and na_position == "last":
            # TODO: in an IntervalIndex we can reuse the cached
            #  IntervalTree.left_sorter
            return np.lexsort((self.right, self.left))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\masked.py:290** — `# TODO: get this all from np_can_hold_element?`
```
"""
        kind = self.dtype.kind
        # TODO: get this all from np_can_hold_element?
        if kind == "b":
            if lib.is_bool(value):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\numeric.py:93** — `# TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed`
```
if isinstance(array, pyarrow.ChunkedArray):
            # TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed
            # combine_chunks for empty arrays https://github.com/apache/arrow/pull/13757
            if array.num_chunks == 0:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\numpy_.py:301** — `# TODO: assert we have floating dtype?`
```
out_data = self._ndarray.copy()

        # TODO: assert we have floating dtype?
        missing.interpolate_2d_inplace(
            out_data,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\period.py:702** — `# TODO: other cases?`
```
elif diff == 1:
                    dta._freq = self.freq.base
                # TODO: other cases?
            return dta
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\string_.py:198** — `# TODO add more informative repr`
```
return f"{self.name}[{self.storage}]"
        else:
            # TODO add more informative repr
            return self.name
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py:74** — `# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from`
```
# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from
# ObjectStringArrayMixin because we want to have the object-dtype based methods as
# fallback for the ones that pyarrow doesn't yet support
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\_mixins.py:363** — `# TODO: NumpyExtensionArray didn't used to copy, need tests`
```
npvalues = npvalues.T

                # TODO: NumpyExtensionArray didn't used to copy, need tests
                #  for this
                new_values = self._from_backing_data(npvalues)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\arrow\accessors.py:151** — `# TODO: Support negative key but pyarrow does not allow`
```
if isinstance(key, int):
            # TODO: Support negative key but pyarrow does not allow
            # element index to be an array.
            # if key < 0:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\arrow\array.py:133** — `# TODO: Replace with pyarrow floordiv kernel.`
```
right: pa.ChunkedArray | pa.Array | pa.Scalar,
    ) -> pa.ChunkedArray:
        # TODO: Replace with pyarrow floordiv kernel.
        # https://github.com/apache/arrow/issues/39386
        if pa.types.is_integer(left.type) and pa.types.is_integer(right.type):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\arrays\sparse\array.py:384** — `# TODO: make kind=None, and use data.kind?`
```
if dtype is None:
                dtype = data.dtype
            # TODO: make kind=None, and use data.kind?
            data = data.sp_values
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\array_algos\putmask.py:78** — `# TODO: this prob needs some better checking for 2D cases`
```
new = new.astype(values.dtype, copy=False)

    # TODO: this prob needs some better checking for 2D cases
    nlocs = mask.sum()
    if nlocs > 0 and is_list_like(new) and getattr(new, "ndim", 1) == 1:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\array_algos\replace.py:85** — `# TODO: should use missing.mask_missing?`
```
if not regex or not should_use_regex(regex, b):
        # TODO: should use missing.mask_missing?
        op = lambda x: operator.eq(x, b)
    else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\array_algos\take.py:361** — `# FIXME: if we get here with dt64/td64 we need to be sure we have`
```
out = out.view(out_dtype)
        if fill_wrap is not None:
            # FIXME: if we get here with dt64/td64 we need to be sure we have
            #  matching resos
            if fill_value.dtype.kind == "m":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\computation\eval.py:66** — `# TODO: validate this in a more general way (thinking of future engines`
```
)

    # TODO: validate this in a more general way (thinking of future engines
    # that won't necessarily be import-able)
    # Could potentially be done on engine instantiation
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\computation\expr.py:547** — `# TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min`
```
return self.term_type(node.id, self.env, **kwargs)

    # TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min
    def visit_NameConstant(self, node, **kwargs) -> Term:
        return self.const_type(node.value, self.env)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\computation\pytables.py:441** — `# TODO: return None might never be reached`
```
elif isinstance(node.op, ast.UAdd):
            raise NotImplementedError("Unary addition not supported")
        # TODO: return None might never be reached
        return None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\dtypes\cast.py:286** — `# TODO: complex?  what if result is already non-object?`
```
else:
                # TODO: complex?  what if result is already non-object?
                dtype = "object"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\dtypes\common.py:1519** — `# TODO: Implement this properly`
```
pass
        if hasattr(dtype, "numpy_dtype"):
            # TODO: Implement this properly
            # https://github.com/pandas-dev/pandas/issues/52576
            return dtype.numpy_dtype.type
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\dtypes\dtypes.py:209** — `# TODO: Document public vs. private API`
```
"""

    # TODO: Document public vs. private API
    name = "category"
    type: type[CategoricalDtypeType] = CategoricalDtypeType
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\dtypes\missing.py:520** — `# TODO: fastpath for pandas' StringDtype`
```
return _array_equivalent_datetimelike(left, right)
        elif is_string_or_object_np_dtype(left.dtype):
            # TODO: fastpath for pandas' StringDtype
            return _array_equivalent_object(left, right, strict_nan)
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\groupby\generic.py:116** — `# TODO(typing) the return value on this callable should be any *scalar*.`
```
from pandas.core.generic import NDFrame

# TODO(typing) the return value on this callable should be any *scalar*.
AggScalar = Union[str, Callable[..., Any]]
# TODO: validate types on ScalarResult and move to _typing
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\groupby\groupby.py:792** — `# TODO: Better repr for GroupBy object`
```
@final
    def __repr__(self) -> str:
        # TODO: Better repr for GroupBy object
        return object.__repr__(self)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\groupby\grouper.py:358** — `# TODO: What are we assuming about subsequent calls?`
```
# Keep self._grouper value before overriding
        if self._grouper is None:
            # TODO: What are we assuming about subsequent calls?
            self._grouper = gpr_index
            self._indexer = self._indexer_deprecated
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\groupby\ops.py:468** — `# TODO: min_count`
```
raise NotImplementedError(f"{self.how} is not implemented")
        else:
            # TODO: min_count
            if self.how != "rank":
                # TODO: should rank take result_mask?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\api.py:145** — `# TODO: handle index names!`
```
Index
    """
    # TODO: handle index names!
    indexes = _get_distinct_objs(indexes)
    if len(indexes) == 0:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\base.py:1465** — `# TODO: why do we need different justify for these cases?`
```
or isinstance(self.dtype, (IntervalDtype, CategoricalDtype))
        ):
            # TODO: why do we need different justify for these cases?
            justify = "all"
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\datetimelike.py:230** — `# TODO: not reached in tests 2023-10-11`
```
self, *, header: list[str], na_rep: str, date_format: str | None = None
    ) -> list[str]:
        # TODO: not reached in tests 2023-10-11
        # matches base class except for whitespace padding and date_format
        return header + list(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\datetimes.py:98** — `# TODO: If we knew what was going in to **d, we might be able to`
```
else:
        with warnings.catch_warnings():
            # TODO: If we knew what was going in to **d, we might be able to
            #  go through _simple_new instead
            warnings.simplefilter("ignore")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\frozen.py:70** — `# TODO: Consider deprecating these in favor of `union` (xref gh-15506)`
```
return type(self)(temp)

    # TODO: Consider deprecating these in favor of `union` (xref gh-15506)
    # error: Incompatible types in assignment (expression has type
    # "Callable[[FrozenList, Any], FrozenList]", base class "list" defined the
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\interval.py:685** — `# TODO: DO this in maybe_booleans_to_slice?`
```
res = lib.maybe_booleans_to_slice(mask.view("u1"))
        if isinstance(res, slice) and res.stop is None:
            # TODO: DO this in maybe_booleans_to_slice?
            res = slice(res.start, len(self), res.step)
        return res
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\multi.py:2996** — `# TODO: need is_valid_na_for_dtype(key, level_index.dtype)`
```
"""
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\period.py:302** — `# TODO: We can do some of these with no-copy / coercion?`
```
if freq and isinstance(data, cls) and data.freq != freq:
                # TODO: We can do some of these with no-copy / coercion?
                # e.g. D -> 2D seems to be OK
                data = data.asfreq(freq)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\indexes\range.py:1108** — `# TODO: if other is a RangeIndex we may have more efficient options`
```
step = op

        # TODO: if other is a RangeIndex we may have more efficient options
        right = extract_array(other, extract_numpy=True, extract_range=True)
        left = self
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\interchange\column.py:115** — `# TODO: chunks are implemented now, probably this should return something`
```
Offset of first element. Always zero.
        """
        # TODO: chunks are implemented now, probably this should return something
        return 0
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\interchange\dataframe_protocol.py:407** — `# TODO: not happy with Optional, but need to flag it may be expensive`
```
@abstractmethod
    def num_rows(self) -> int | None:
        # TODO: not happy with Optional, but need to flag it may be expensive
        #       why include it if it may be None - what do we expect consumers
        #       to do here?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\interchange\from_dataframe.py:470** — `# TODO: No DLPack yet, so need to construct a new ndarray from the data pointer`
```
raise NotImplementedError(f"Conversion for {dtype} is not yet supported.")

    # TODO: No DLPack yet, so need to construct a new ndarray from the data pointer
    # and size in the buffer plus the dtype on the column. Use DLPack as NumPy supports
    # it since https://github.com/numpy/numpy/pull/19083
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\interchange\utils.py:139** — `# TODO(infer_string) this should be LARGE_STRING for pyarrow storage,`
```
if isinstance(dtype, pd.StringDtype):
        # TODO(infer_string) this should be LARGE_STRING for pyarrow storage,
        # but current tests don't cover this distinction
        return ArrowCTypes.STRING
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\array_manager.py:366** — `# TODO what is this used for?`
```
def is_view(self) -> bool:
        """return a boolean if we are a single block and are a view"""
        # TODO what is this used for?
        return False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\base.py:66** — `# TODO share more methods/attributes`
```
class DataManager(PandasObject):
    # TODO share more methods/attributes

    axes: list[Index]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\blocks.py:420** — `# TODO(EA2D): unnecessary with 2D EAs`
```
# See also: split_and_operate
        if result.ndim > 1 and isinstance(result.dtype, ExtensionDtype):
            # TODO(EA2D): unnecessary with 2D EAs
            # if we get a 2D ExtensionArray, we need to split it into 1D pieces
            nbs = []
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\concat.py:114** — `# TODO(ArrayManager) this assumes that all managers are of the same type`
```
needs_copy = copy and concat_axis == 0

    # TODO(ArrayManager) this assumes that all managers are of the same type
    if isinstance(mgrs_indexers[0][0], ArrayManager):
        mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\construction.py:397** — `# TODO: check len(values) == 0?`
```
if len(columns) == 0:
        # TODO: check len(values) == 0?
        block_values = []
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\managers.py:536** — `# FIXME: optimization potential`
```
return self.make_empty()

        # FIXME: optimization potential
        indexer = np.sort(np.concatenate([b.mgr_locs.as_array for b in blocks]))
        inv_indexer = lib.get_reverse_indexer(indexer, self.shape[0])
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\internals\ops.py:120** — `# TODO(EA2D): with 2D EAs only this first clause would be needed`
```
assert rblk.mgr_locs.is_slice_like, rblk.mgr_locs

    # TODO(EA2D): with 2D EAs only this first clause would be needed
    if not (left_ea or right_ea):
        # error: No overload variant of "__getitem__" of "ExtensionArray" matches
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\ops\array_ops.py:234** — `# TODO: can remove this after dropping some future numpy version?`
```
# numpy returned a scalar instead of operating element-wise
        # e.g. numeric array vs str
        # TODO: can remove this after dropping some future numpy version?
        return invalid_comparison(left, right, op)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\concat.py:534** — `# TODO: retain levels?`
```
if isinstance(keys, MultiIndex):
                # TODO: retain levels?
                keys = type(keys).from_tuples(clean_keys, names=keys.names)
            else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\melt.py:477** — `# TODO: anything else to catch?`
```
newdf[j] = to_numeric(newdf[j])
        except (TypeError, ValueError, OverflowError):
            # TODO: anything else to catch?
            pass
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\merge.py:285** — `# TODO, should merge_pieces do this?`
```
# make sure join keys are in the merged
        # TODO, should merge_pieces do this?
        merged[by] = key
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\pivot.py:60** — `# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency`
```
# Note: We need to make sure `frame` is imported before `pivot`, otherwise
# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency
@Substitution("\ndata : DataFrame")
@Appender(_shared_docs["pivot_table"], indents=1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\reshape.py:229** — `# TODO: in all tests we have mask.any(0).all(); can we rely on that?`
```
new_values, mask = self.get_new_values(dummy_arr, fill_value=-1)
        return new_values, mask.any(0)
        # TODO: in all tests we have mask.any(0).all(); can we rely on that?

    def get_result(self, values, value_columns, fill_value) -> DataFrame:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\reshape\tile.py:503** — `# TODO: handle mismatch between categorical label order and pandas.cut order.`
```
ordered=ordered,
            )
        # TODO: handle mismatch between categorical label order and pandas.cut order.
        np.putmask(ids, na_mask, 0)
        result = algos.take_nd(labels, ids - 1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\strings\accessor.py:186** — `# TODO: Dispatch all the methods`
```
# Note: see the docstring in pandas.core.strings.__init__
    # for an explanation of the implementation.
    # TODO: Dispatch all the methods
    # Currently the following are not dispatched to the array
    # * cat
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\strings\object_array.py:92** — `# FIXME: this should be totally avoidable`
```
if len(err.args) >= 1 and re.search(p_err, err.args[0]):
                # FIXME: this should be totally avoidable
                raise err
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\tools\datetimes.py:370** — `# TODO: Combine with above if DTI/DTA supports Arrow timestamps`
```
elif isinstance(arg_dtype, ArrowDtype) and arg_dtype.type is Timestamp:
        # TODO: Combine with above if DTI/DTA supports Arrow timestamps
        if utc:
            # pyarrow uses UTC, not lowercase utc
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\window\rolling.py:391** — `# TODO: sure we want to overwrite results?`
```
extra_col = Series(self._on, index=self.obj.index, name=name, copy=False)
            if name in result.columns:
                # TODO: sure we want to overwrite results?
                result[name] = extra_col
            elif name in result.index.names:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\_numba\executor.py:125** — `# TODO: Preserve complex dtypes`
```
# TODO: Preserve complex dtypes

float_dtype_mapping: dict[np.dtype, Any] = {
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\core\_numba\extensions.py:66** — `# TODO: Range index support`
```
# TODO: Range index support
# (this currently lowers OK, but does not round-trip)
class IndexType(types.Type):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\common.py:373** — `# TODO: fsspec can also handle HTTP via requests, but leaving this`
```
if isinstance(filepath_or_buffer, str) and is_url(filepath_or_buffer):
        # TODO: fsspec can also handle HTTP via requests, but leaving this
        # unchanged. using fsspec appears to break the ability to infer if the
        # server responded with gzipped data
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\pytables.py:1222** — `#  _table_mod.NoSuchNodeError.  TODO: Catch only these?`
```
except Exception as err:
            # In tests we get here with ClosedFileError, TypeError, and
            #  _table_mod.NoSuchNodeError.  TODO: Catch only these?

            if where is not None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\sql.py:120** — `# TODO: not reached 2023-10-27; needed?`
```
return to_datetime(col, **format)
            except (TypeError, ValueError):
                # TODO: not reached 2023-10-27; needed?
                return col
        return to_datetime(col, errors=error, **format)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\stata.py:339** — `# TODO(non-nano): If/when pandas supports more than datetime64[ns], this`
```
return base + deltas

    # TODO(non-nano): If/when pandas supports more than datetime64[ns], this
    #  should be improved to use correct range, e.g. datetime[Y] for yearly
    bad_locs = np.isnan(dates)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\clipboard\__init__.py:274** — `# TODO: https://github.com/asweigart/pyperclip/issues/43`
```
# Workaround for https://bugs.kde.org/show_bug.cgi?id=342874
        # TODO: https://github.com/asweigart/pyperclip/issues/43
        clipboardContents = stdout.decode(ENCODING)
        # even if blank, Klipper will append a newline at the end
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\excel\_pyxlsb.py:63** — `# TODO: hack in buffer capability`
```
from pyxlsb import open_workbook

        # TODO: hack in buffer capability
        # This might need some modifications to the Pyxlsb library
        # Actual work for opening it is in xlsbpackage.py, line 20-ish
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\excel\_xlsxwriter.py:134** — `# TODO: support other fill patterns`
```
if isinstance(props.get("pattern"), str):
            # TODO: support other fill patterns
            props["pattern"] = 0 if props["pattern"] == "none" else 1
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\formats\css.py:106** — `# TODO: Can we use current color as initial value to comply with CSS standards?`
```
)

        # TODO: Can we use current color as initial value to comply with CSS standards?
        border_declarations = {
            f"border{side}-color": "black",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\formats\excel.py:238** — `# TODO: handle cell width and height: needs support in pandas.io.excel`
```
}

        # TODO: handle cell width and height: needs support in pandas.io.excel

        def remove_none(d: dict[str, str | None]) -> None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\formats\format.py:1227** — `# TODO(3.0): this will be unreachable when use_inf_as_na`
```
return str(NA)
                elif lib.is_float(x) and np.isinf(x):
                    # TODO(3.0): this will be unreachable when use_inf_as_na
                    #  deprecation is enforced
                    return str(x)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\formats\html.py:337** — `# TODO: Refactor to remove code duplication with code`
```
# MultiIndex Columns and Index.
                # Initially fill row with blank cells before column names.
                # TODO: Refactor to remove code duplication with code
                # block below for standard columns index.
                row = [""] * (self.row_levels - 1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\formats\style_render.py:878** — `# TODO try to consolidate the concat visible rows`
```
row_indices: list[int] = []
            _concatenated_visible_rows(obj, 0, row_indices)
            # TODO try to consolidate the concat visible rows
            # methods to a single function / recursion for simplicity
            return row_indices
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\json\_json.py:374** — `# TODO: Do this timedelta properly in objToJSON.c See GH #15137`
```
)

        # TODO: Do this timedelta properly in objToJSON.c See GH #15137
        if (
            (obj.ndim == 1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\json\_normalize.py:466** — `# TODO: handle record value which are lists, at least error`
```
#  {VeryLong: { b: 1,c:2}} -> {VeryLong.b:1 ,VeryLong.c:@}
            #
            # TODO: handle record value which are lists, at least error
            #       reasonably
            data = nested_to_record(data, sep=sep, max_level=max_level)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\parsers\base_parser.py:813** — `# TODO: this is for consistency with`
```
if not is_object_dtype(values.dtype) and not known_cats:
                # TODO: this is for consistency with
                # c-parser which parses all categories
                # as strings
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\parsers\python_parser.py:461** — `# TODO: Use pandas.io.common.dedup_names instead (see #50371)`
```
] + this_unnamed_cols

                    # TODO: Use pandas.io.common.dedup_names instead (see #50371)
                    for i in col_loop_order:
                        col = this_columns[i]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\io\parsers\readers.py:1654** — `# TODO: Refactor this logic, its pretty convoluted`
```
if engine != "c" and value != default:
                    # TODO: Refactor this logic, its pretty convoluted
                    if "python" in engine and argname not in _python_unsupported:
                        pass
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\plotting\_matplotlib\converter.py:823** — `# TODO: Check the following : is it really info['fmt'] ?`
```
quarter_start = (dates_ % 3 == 0).nonzero()
        info_maj[year_start] = True
        # TODO: Check the following : is it really info['fmt'] ?
        #  2023-09-15 this is reached in test_finder_monthly
        info["fmt"][quarter_start] = True
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\plotting\_matplotlib\core.py:182** — `# TODO: Might deprecate `column` argument in future PR (#28373)`
```
# Assign the rest of columns into self.columns if by is explicitly defined
        # while column is not, only need `columns` in hist/box plot when it's DF
        # TODO: Might deprecate `column` argument in future PR (#28373)
        if isinstance(data, DataFrame):
            if column:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\plotting\_matplotlib\misc.py:300** — `# TODO: is the failure mentioned below still relevant?`
```
import matplotlib.pyplot as plt

    # TODO: is the failure mentioned below still relevant?
    # random.sample(ndarray, int) fails on python 3.3, sigh
    data = list(series.values)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\plotting\_matplotlib\timeseries.py:1** — `# TODO: Use the fact that axis can have units to simplify the process`
```
# TODO: Use the fact that axis can have units to simplify the process

from __future__ import annotations
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\test_algos.py:68** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
tm.assert_numpy_array_equal(uniques, expected_uniques)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("sort", [True, False])
    def test_factorize(self, index_or_series_obj, sort):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\test_downstream.py:310** — `# TODO: could check with arraylike of Period objects`
```
# Note: we dont do this for PeriodArray bc _from_sequence won't accept
    #  an array of integers
    # TODO: could check with arraylike of Period objects
    arr, data = array_likes
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\test_multilevel.py:161** — `# TODO groupby with level_values drops names`
```
expected = ymd.groupby([k1, k2]).mean()

        # TODO groupby with level_values drops names
        tm.assert_frame_equal(result, expected, check_names=False)
        assert result.index.names == ymd.index.names[:2]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\apply\test_frame_apply.py:1709** — `# TODO: the result below is wrong, should be fixed (GH53325)`
```
tm.assert_frame_equal(result, expected)

    # TODO: the result below is wrong, should be fixed (GH53325)
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = df.agg({"x": foo1}, 0, 3, c=4)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arithmetic\test_datetime64.py:161** — `# TODO: moved from tests.series.test_operators; needs cleanup`
```
class TestDatetime64SeriesComparison:
    # TODO: moved from tests.series.test_operators; needs cleanup

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arithmetic\test_numeric.py:50** — `# TODO: add more  dtypes here`
```
@pytest.fixture(
    params=[
        # TODO: add more  dtypes here
        Index(np.arange(5, dtype="float64")),
        Index(np.arange(5, dtype="int64")),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arithmetic\test_object.py:96** — `# TODO: parametrize`
```
tm.assert_index_equal(result, expected)

    # TODO: parametrize
    def test_pow_ops_object(self):
        # GH#22922
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arithmetic\test_period.py:208** — `# TODO: parameterize over boxes`
```
class TestPeriodIndexComparisons:
    # TODO: parameterize over boxes

    def test_pi_cmp_period(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arithmetic\test_timedelta64.py:171** — `# TODO: All of these need to be parametrized over box`
```
class TestTimedelta64ArrayComparisons:
    # TODO: All of these need to be parametrized over box

    @pytest.mark.parametrize("dtype", [None, object])
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\test_datetimelike.py:33** — `# TODO: more freq variants`
```
# TODO: more freq variants
@pytest.fixture(params=["D", "B", "W", "ME", "QE", "YE"])
def freqstr(request):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\test_datetimes.py:93** — `# TODO: simplify once we can just .astype to other unit`
```
assert not dta.is_normalized

        # TODO: simplify once we can just .astype to other unit
        exp = np.asarray(dti.normalize()).astype(f"M8[{unit}]")
        expected = DatetimeArray._simple_new(exp, dtype=exp.dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\test_timedeltas.py:106** — `# TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert`
```
assert result.isna().all()

    # TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert
    #  or tz_localize with non-nano; implement tests specific to that.
    def test_add_datetimelike_scalar(self, tda, tz_naive_fixture):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_arithmetic.py:122** — `# TODO(extension) numpy's mul with object array sees booleans as numbers`
```
# invalid array-likes
    if op not in ("__mul__", "__rmul__"):
        # TODO(extension) numpy's mul with object array sees booleans as numbers
        msg = "|".join(
            [
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_construction.py:155** — `# TODO this is currently not public API`
```
def test_coerce_to_array():
    # TODO this is currently not public API
    values = np.array([True, False, True, False], dtype="bool")
    mask = np.array([False, False, False, True], dtype="bool")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\boolean\test_logical.py:123** — `# TODO: test True & False`
```
)
    def test_kleene_or_scalar(self, other, expected):
        # TODO: test True & False
        a = pd.array([True, False, None], dtype="boolean")
        result = a | other
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\categorical\test_analytics.py:47** — `# TODO: raises if we pass axis=0  (on Index and Categorical, not Series)`
```
assert np.minimum.reduce(obj) == "a"
        assert np.maximum.reduce(obj) == "d"
        # TODO: raises if we pass axis=0  (on Index and Categorical, not Series)

        cat = Categorical(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\categorical\test_indexing.py:374** — `# TODO(Categorical): identify other places where this may be`
```
"""

    # TODO(Categorical): identify other places where this may be
    # useful and move to a conftest.py
    def array(self, dtype=None):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\floating\test_arithmetic.py:39** — `# TODO pending NA/NaN discussion`
```
@pytest.mark.parametrize("zero, negative", [(0, False), (0.0, False), (-0.0, True)])
def test_divide_by_zero(dtype, zero, negative):
    # TODO pending NA/NaN discussion
    # https://github.com/pandas-dev/pandas/issues/32265/
    a = pd.array([0, 1, -1, None], dtype=dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\floating\test_construction.py:172** — `# TODO can we specify "floating" in general?`
```
# for integer dtypes, the itemsize is not preserved
    # TODO can we specify "floating" in general?
    result = pd.array(np.array([1, 2], dtype="int32"), dtype="Float64")
    assert result.dtype == Float64Dtype()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\integer\test_arithmetic.py:196** — `# TODO: doing this fillna to keep tests passing as we make`
```
expected = pd.Series(["foo" * x for x in data], index=s.index)
        expected = expected.fillna(np.nan)
        # TODO: doing this fillna to keep tests passing as we make
        #  assert_almost_equal stricter, but the expected with pd.NA seems
        #  more-correct than np.nan here.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\integer\test_function.py:199** — `# TODO(jreback) - these need testing / are broken`
```
# TODO(jreback) - these need testing / are broken

# shift
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\interval\test_overlaps.py:62** — `# TODO: modify this test when implemented`
```
@pytest.mark.parametrize("other_constructor", [IntervalArray, IntervalIndex])
    def test_overlaps_interval_container(self, constructor, other_constructor):
        # TODO: modify this test when implemented
        interval_container = constructor.from_breaks(range(5))
        other_container = other_constructor.from_breaks(range(5))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\masked\test_arithmetic.py:57** — `# TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))`
```
scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)

    # TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))
    for scalar in [scalar, data.dtype.type(scalar)]:
        if is_bool_not_implemented(data, all_arithmetic_operators):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\masked\test_indexing.py:22** — `# FIXME: don't leave commented-out`
```
arr[[0]] = invalid

        # FIXME: don't leave commented-out
        # with pytest.raises(TypeError):
        #    arr[[0]] = [invalid]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_constructors.py:106** — `# TODO: actionable?`
```
def test_constructor_spindex_dtype(self):
        arr = SparseArray(data=[1, 2], sparse_index=IntIndex(4, [1, 2]))
        # TODO: actionable?
        # XXX: Behavior change: specifying SparseIndex no longer changes the
        # fill_value
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_indexing.py:208** — `# TODO: actionable?`
```
tm.assert_sp_array_equal(result, expected)

        # TODO: actionable?
        # XXX: test change: fill_value=True -> allow_fill=True
        result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\arrays\sparse\test_reductions.py:265** — `# TODO: pin down whether we wrap datetime64("NaT")`
```
result = getattr(arr, func)()
        if expected is NaT:
            # TODO: pin down whether we wrap datetime64("NaT")
            assert result is NaT or np.isnat(result)
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\base\test_misc.py:155** — `# TODO: Should Series cases also raise? Looks like they use numpy`
```
)
    elif obj.dtype.kind == "c" and isinstance(obj, Index):
        # TODO: Should Series cases also raise? Looks like they use numpy
        #  comparison semantics https://github.com/numpy/numpy/issues/15981
        mark = pytest.mark.xfail(reason="complex objects are not comparable")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\base\test_value_counts.py:50** — `# TODO(GH#32514): Order of entries with the same count is inconsistent`
```
expected = expected.astype("Int64")

    # TODO(GH#32514): Order of entries with the same count is inconsistent
    #  on CI (gh-32449)
    if obj.duplicated().any():
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\computation\test_eval.py:98** — `# TODO: using range(5) here is a kludge`
```
# TODO: using range(5) here is a kludge
@pytest.fixture(
    params=list(range(5)),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_astype.py:137** — `# TODO(infer_string) this test can be removed after 3.0 (once str is the default)`
```
def test_astype_str_copy_on_pickle_roundrip():
    # TODO(infer_string) this test can be removed after 3.0 (once str is the default)
    # https://github.com/pandas-dev/pandas/issues/54654
    # ensure_string_array may alter array inplace
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_chained_assignment_deprecation.py:74** — `# TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+`
```
df = df_orig.copy()
    df["a"]  # populate the item_cache
    # TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+
    if using_copy_on_write:
        with tm.raises_chained_assignment_error(not PY311):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_core_functionalities.py:54** — `# TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100``
```
arr = get_array(df, "a")
    view = None  # noqa: F841
    # TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100`
    # which introduces additional refs, even when those of `view` go out of scopes
    with tm.assert_cow_warning(warn_copy_on_write):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_indexing.py:816** — `# TODO add more tests modifying the parent`
```
# TODO add more tests modifying the parent
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_methods.py:148** — `# TODO copy=False without CoW still returns a copy in this case`
```
if request.node.callspec.id.startswith("reindex-"):
        # TODO copy=False without CoW still returns a copy in this case
        if not using_copy_on_write and not using_array_manager and copy is False:
            share_memory = False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\copy_view\test_replace.py:21** — `# TODO: Add these in a further optimization`
```
{"to_replace": {"b": 4}, "value": -1},
        {"to_replace": {"b": {4: 1}}},
        # TODO: Add these in a further optimization
        # We would need to see which columns got replaced in the mask
        # which could be expensive
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\dtypes\cast\test_downcast.py:46** — `# TODO: similar for dt64, dt64tz, Period, Interval?`
```
np.array([1, 2], dtype="m8[D]").astype("m8[ns]"),
        ),
        # TODO: similar for dt64, dt64tz, Period, Interval?
    ],
)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\conftest.py:126** — `TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)`
```
The scalar missing value for this type. Default dtype.na_value.

    TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)
    """
    return dtype.na_value
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_arrow.py:77** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_categorical.py:80** — `# TODO: Is this deliberate?`
```
@pytest.mark.xfail(reason="Memory usage doesn't match")
    def test_memory_usage(self, data):
        # TODO: Is this deliberate?
        super().test_memory_usage(data)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_interval.py:119** — `# TODO: either belongs in tests.arrays.interval or move into base tests.`
```
# TODO: either belongs in tests.arrays.interval or move into base tests.
def test_fillna_non_scalar_raises(data_missing):
    msg = "can only insert Interval objects and NA into an IntervalArray"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_masked.py:267** — `# TODO: patching self is a bad pattern here`
```
def test_combine_le(self, data_repeated):
        # TODO: patching self is a bad pattern here
        orig_data1, orig_data2 = data_repeated(2)
        if orig_data1.dtype.kind == "b":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_numpy.py:219** — `# TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which`
```
@skip_nested
    def test_searchsorted(self, data_for_sorting, as_series):
        # TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which
        #  isn't quite what we want in nested data cases. Instead we need to
        #  adapt something like libindex._bin_search.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_sparse.py:254** — `# TODO: this fails bc we do not pass through data_missing. If we did,`
```
def test_fillna_series(self, data_missing):
        # this one looks doable.
        # TODO: this fails bc we do not pass through data_missing. If we did,
        #  the 0-fill case would xpass
        super().test_fillna_series()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\test_string.py:247** — `# TODO(infer_string)`
```
and (HAS_PYARROW or dtype.storage == "pyarrow")
        ):
            # TODO(infer_string)
            mark = pytest.mark.xfail(
                reason="The pointwise operation result will be inferred to "
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\accumulate.py:39** — `# TODO: require TypeError for things that will _never_ work?`
```
else:
            with pytest.raises((NotImplementedError, TypeError)):
                # TODO: require TypeError for things that will _never_ work?
                getattr(ser, op_name)(skipna=skipna)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\dim2.py:31** — `# TODO: is there a less hacky way of checking this?`
```
test_func = node._obj
            if test_func.__qualname__.startswith("Dim2CompatTests"):
                # TODO: is there a less hacky way of checking this?
                pytest.skip(f"{dtype} does not support 2D.")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\getitem.py:124** — `# TODO: box over scalar, [scalar], (scalar,)?`
```
def test_getitem_invalid(self, data):
        # TODO: box over scalar, [scalar], (scalar,)?

        msg = (
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\methods.py:70** — `# TODO: avoid special-casing`
```
if isinstance(data.dtype, pd.StringDtype) and data.dtype.na_value is np.nan:
            # TODO: avoid special-casing
            expected = expected.astype("float64")
        elif getattr(data.dtype, "storage", "") == "pyarrow" or isinstance(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\missing.py:30** — `# TODO: GH 57739`
```
mask = getattr(result, na_func)()
        if isinstance(mask.dtype, pd.SparseDtype):
            # TODO: GH 57739
            mask = np.array(mask)
            mask.flags.writeable = True
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\reduce.py:86** — `# TODO: the message being checked here isn't actually checking anything`
```
if not self._supports_reduction(ser, op_name):
            # TODO: the message being checked here isn't actually checking anything
            msg = (
                "[Cc]annot perform|Categorical is not ordered for operation|"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\base\setitem.py:220** — `# TODO(xfail) this raises KeyError about labels not found (it tries label-based)`
```
arr = data.copy()

        # TODO(xfail) this raises KeyError about labels not found (it tries label-based)
        # for list of labels with Series
        if box_in_series:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\json\array.py:263** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    return [
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\json\test_json.py:185** — `# TODO (EA.factorize): see if _values_for_factorize allows this.`
```
@unhashable
    def test_sort_values_frame(self):
        # TODO (EA.factorize): see if _values_for_factorize allows this.
        super().test_sort_values_frame()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\extension\list\array.py:130** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    data = np.empty(100, dtype=object)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_arithmetic.py:304** — `# TODO: test_bool_flex_frame needs a better name`
```
class TestFrameFlexComparisons:
    # TODO: test_bool_flex_frame needs a better name
    @pytest.mark.parametrize("op", ["eq", "ne", "gt", "lt", "ge", "le"])
    def test_bool_flex_frame(self, op):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_block_internals.py:29** — `# TODO(ArrayManager) check which of those tests need to be rewritten to test the`
```
# TODO(ArrayManager) check which of those tests need to be rewritten to test the
# equivalent for ArrayManager
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_constructors.py:317** — `# TODO(CoW-warn) this should warn`
```
if not using_array_manager and not using_copy_on_write:
            should_be_view = DataFrame(df.values, dtype=df[0].dtype)
            # TODO(CoW-warn) this should warn
            # with tm.assert_cow_warning(warn_copy_on_write):
            should_be_view.iloc[0, 0] = 97
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_cumulative.py:31** — `# TODO(wesm): do something with this?`
```
dm = DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=range(5))
        # TODO(wesm): do something with this?
        dm.cumsum()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_logical_ops.py:155** — `_check_unary_op(operator.inv)  # TODO: belongs elsewhere`
```
_check_bin_op(operator.xor)

        _check_unary_op(operator.inv)  # TODO: belongs elsewhere

    @pytest.mark.filterwarnings("ignore:Downcasting object dtype arrays:FutureWarning")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_reductions.py:1774** — `# TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead`
```
df.median()

        # TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead
        #  of expected.values
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_ufunc.py:150** — `# TODO(FloatArray): this will be Float64Dtype.`
```
np.array([[1, 3], [np.nan, np.nan], [3, 4]]),
    )
    # TODO(FloatArray): this will be Float64Dtype.
    expected = pd.DataFrame(expected, index=["a", "b", "c"], columns=["A", "B"])
    tm.assert_frame_equal(result, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\test_unary.py:167** — `# TODO: assert that we have copies?`
```
res_ufunc = np.positive(df)
        expected = df
        # TODO: assert that we have copies?
        tm.assert_frame_equal(result, expected)
        tm.assert_frame_equal(res_ufunc, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_coercion.py:45** — `# TODO: i think this isn't about MultiIndex and could be done with iloc?`
```
assert (A.dtypes == np.float32).all()

        # TODO: i think this isn't about MultiIndex and could be done with iloc?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_indexing.py:644** — `@td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values`
```
assert ix[idx, col] == ts[idx]

    @td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values
    def test_setitem_fancy_scalar(self, float_frame):
        f = float_frame
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_setitem.py:725** — `# TODO(ArrayManager) set column with 2d column array, see #44788`
```
tm.assert_frame_equal(df, expected)

    # TODO(ArrayManager) set column with 2d column array, see #44788
    @td.skip_array_manager_not_yet_implemented
    def test_setitem_npmatrix_2d(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_where.py:727** — `# TODO: ideally we would get Int64 instead of object`
```
mask[1, :] = False

        # TODO: ideally we would get Int64 instead of object
        result = df.where(mask, ser, axis=0)
        expected = DataFrame({"A": [1, np.nan, 3], "B": [4, np.nan, 6]})
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\indexing\test_xs.py:153** — `# TODO: more descriptive name`
```
class TestXSWithMultiIndex:
    def test_xs_doc_example(self):
        # TODO: more descriptive name
        # based on example in advanced.rst
        arrays = [
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_asfreq.py:154** — `# TODO: actually check that this worked.`
```
rule_monthly.asfreq("B", method="pad")
        # TODO: actually check that this worked.

        # don't forget!
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_astype.py:129** — `# TODO(wesm): verification?`
```
tf.astype(np.float32, copy=False)

        # TODO(wesm): verification?
        tf = float_frame.astype(np.float64)
        tf.astype(np.int64, copy=False)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_clip.py:159** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_combine_first.py:212** — `# TODO: this must be int64`
```
tm.assert_frame_equal(res, exp)
        assert res["a"].dtype == "datetime64[ns]"
        # TODO: this must be int64
        assert res["b"].dtype == "int64"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_compare.py:269** — `# GH#18463 TODO: is this really the desired behavior?`
```
)
    if val1 is pd.NA and val2 is pd.NA:
        # GH#18463 TODO: is this really the desired behavior?
        expected.loc[1, ("a", "self")] = np.nan
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_fillna.py:32** — `# TODO(CoW-warn) better warning message`
```
orig = df[:]

        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df.fillna({"A": 2}, inplace=True)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_info.py:535** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_memory_usage_empty_no_warning(using_infer_string):
    # GH#50066
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_interpolate.py:335** — `# TODO: assert something?`
```
)
        df.interpolate(axis=0)
        # TODO: assert something?

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_quantile.py:729** — `# GH#18463 TODO: would we prefer NaTs here?`
```
exp = exp.astype(object)
        if interpolation == "nearest":
            # GH#18463 TODO: would we prefer NaTs here?
            msg = "The 'downcast' keyword in fillna is deprecated"
            with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_rank.py:504** — `# TODO nullable string[python] should also return nullable Int64`
```
)
        if string_dtype_no_object.storage == "python":
            # TODO nullable string[python] should also return nullable Int64
            exp_dtype = "float64"
        expected = Series([1, 2, None, 3], dtype=exp_dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_rename.py:388** — `# TODO: can we construct this without merge?`
```
),
        )
        # TODO: can we construct this without merge?
        k = merge(df4, df5, how="inner", left_index=True, right_index=True)
        result = k.rename(columns={"TClose_x": "TClose", "TClose_y": "QT_Close"})
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_replace.py:751** — `# TODO: what is this even testing?`
```
msg = "DataFrame.fillna with 'method' is deprecated"
        with tm.assert_produces_warning(FutureWarning, match=msg):
            # TODO: what is this even testing?
            result = tsframe.fillna(method="bfill")
            tm.assert_frame_equal(result, tsframe.fillna(method="bfill"))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_shift.py:469** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support`
```
tm.assert_frame_equal(result, expected)

    @td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support
    def test_shift_axis1_multiple_blocks_with_int_fill(self):
        # GH#42719
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_sort_index.py:596** — `# TODO: better name, de-duplicate with test_sort_index_level above`
```
assert result.columns.is_monotonic_increasing

    # TODO: better name, de-duplicate with test_sort_index_level above
    def test_sort_index_level2(self, multiindex_dataframe_random_data):
        frame = multiindex_dataframe_random_data
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_to_csv.py:547** — `# TODO to_csv drops column name`
```
df = self.read_csv(path, index_col=[0, 1], parse_dates=False)

            # TODO to_csv drops column name
            tm.assert_frame_equal(frame, df, check_names=False)
            assert frame.index.names == df.index.names
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_to_dict_of_blocks.py:40** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_to_dict_of_blocks_item_cache(using_copy_on_write, warn_copy_on_write):
    # Calling to_dict_of_blocks should not poison item_cache
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_tz_convert.py:93** — `# TODO: untested`
```
df4 = DataFrame(np.ones(5), MultiIndex.from_arrays([int_idx, l0]))

            # TODO: untested
            getattr(df4, fn)("US/Pacific", level=1)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\frame\methods\test_update.py:186** — `# TODO(CoW-warn) better warning message`
```
df2_orig = df2.copy()
        result_view = df2[:]
        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df2.update(df)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\generic\test_duplicate_labels.py:51** — `# TODO: frame`
```
"other", [pd.Series(0, index=["a", "b", "c"]), pd.Series(0, index=["a", "b"])]
    )
    # TODO: frame
    @not_implemented
    def test_align(self, other):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\generic\test_finalize.py:13** — `# TODO:`
```
import pandas._testing as tm

# TODO:
# * Binary methods (mul, div, etc.)
# * Binary outputs (align, etc.)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_apply.py:461** — `# TODO(GH#34306): Use assert_frame_equal when column name is not np.nan`
```
result = grouped.apply(len)
    expected = grouped.count().rename(columns={"C": np.nan}).drop(columns="D")
    # TODO(GH#34306): Use assert_frame_equal when column name is not np.nan
    tm.assert_index_equal(result.index, expected.index)
    tm.assert_numpy_array_equal(result.values, expected.values)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_categorical.py:86** — `def test_basic(using_infer_string):  # TODO: split this test`
```
def test_basic(using_infer_string):  # TODO: split this test
    cats = Categorical(
        ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_groupby.py:313** — `# TODO: try to get this more consistent?`
```
expected = DataFrame(ex_data).T
    if not as_index:
        # TODO: try to get this more consistent?
        expected.index = Index(range(2))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_groupby_dropna.py:612** — `# TODO: Should this be 3?`
```
na_group = df["x"].nunique(dropna=False) - 1
            else:
                # TODO: Should this be 3?
                na_group = df["x"].nunique(dropna=False) - 1
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_grouping.py:936** — `# TODO: should prob allow a str of Interval work as well`
```
g = d.groupby(pd.cut(d[0], bins), observed=observed)

        # TODO: should prob allow a str of Interval work as well
        # IOW '(0, 5]'
        result = g.get_group(pd.Interval(0, 5))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_numeric_only.py:93** — `# TODO: min, max *should* handle`
```
@pytest.mark.parametrize("method", ["min", "max"])
    def test_extrema(self, df, method):
        # TODO: min, max *should* handle
        # categorical (ordered) dtype
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_raises.py:634** — `# TODO: empty_groups should be true due to unobserved categorical combinations`
```
):
        assert not empty_groups
        # TODO: empty_groups should be true due to unobserved categorical combinations
        empty_groups = True
    if how == "transform":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_reductions.py:747** — `# TODO: For skipna=False, bool(pd.NA) raises; should groupby?`
```
if reduction_func in ["all", "any"]:
        expected_dtype = "bool"
        # TODO: For skipna=False, bool(pd.NA) raises; should groupby?
        expected_value = False if reduction_func == "any" else True
    elif reduction_func in ["count", "nunique", "size"]:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\test_timegrouper.py:78** — `# TODO(infer_string) resample sum introduces 0's`
```
class TestGroupBy:
    # TODO(infer_string) resample sum introduces 0's
    # https://github.com/pandas-dev/pandas/issues/60229
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_aggregate.py:1356** — `# TODO: agg should raise for functions that don't aggregate`
```
def test_nonagg_agg():
    # GH 35490 - Single/Multiple agg of non-agg function give same results
    # TODO: agg should raise for functions that don't aggregate
    df = DataFrame({"a": [1, 1, 2, 2], "b": [1, 2, 2, 1]})
    g = df.groupby("a")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_numba.py:181** — `# FIXME`
```
[
        ({"func": lambda values, index: values.sum()}, "sum"),
        # FIXME
        pytest.param(
            {
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_other.py:444** — `# FIXME: the original version of this test called `gb.agg(sum)``
```
tm.assert_frame_equal(result, expected)

    # FIXME: the original version of this test called `gb.agg(sum)`
    #  and that raises TypeError if `numeric_only=False` is passed
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\methods\test_quantile.py:65** — `# TODO(non-nano): this should be unnecessary once array_to_datetime`
```
)
    if all_vals.dtype.kind == "M" and expected.dtypes.values[0].kind == "M":
        # TODO(non-nano): this should be unnecessary once array_to_datetime
        #  correctly infers non-nano from Timestamp.unit
        expected = expected.astype(all_vals.dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\methods\test_value_counts.py:427** — `# TODO(nullable) also string[python] should return nullable dtypes`
```
expected["proportion"] /= expected_group_size
        if dtype == "string[pyarrow]":
            # TODO(nullable) also string[python] should return nullable dtypes
            expected["proportion"] = expected["proportion"].convert_dtypes()
    else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\transform\test_numba.py:149** — `# TODO: Test more than just reductions (e.g. actually test transformations once we have`
```
# TODO: Test more than just reductions (e.g. actually test transformations once we have
@pytest.mark.parametrize(
    "agg_func", [["min", "max"], "min", {"B": ["min", "max"], "C": "sum"}]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\groupby\transform\test_transform.py:872** — `# TODO: create xfail condition given other params`
```
{"level": 0},
        {"by": "string"},
        # TODO: create xfail condition given other params
        # {"by": 'string_missing'},
        {"by": ["int", "string"]},
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_any_index.py:50** — `# TODO: could work that into the 'exact="equiv"'?`
```
if index.dtype == object and result.dtype in [bool, "string"]:
        assert (index == result).all()
        # TODO: could work that into the 'exact="equiv"'?
        return  # FIXME: doesn't belong in this file anymore!
    tm.assert_index_equal(result, index, exact="equiv")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_base.py:57** — `# TODO: a bunch of scattered tests check this deprecation is enforced.`
```
@pytest.mark.parametrize("index", ["datetime"], indirect=True)
    def test_new_axis(self, index):
        # TODO: a bunch of scattered tests check this deprecation is enforced.
        #  de-duplicate/centralize them.
        with pytest.raises(ValueError, match="Multi-dimensional indexing"):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_common.py:169** — `# TODO: belongs in series arithmetic tests?`
```
assert second.name == "mario"

        # TODO: belongs in series arithmetic tests?
        s1 = pd.Series(2, index=first)
        s2 = pd.Series(3, index=second[:-1])
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_indexing.py:157** — `return  # TODO: do we want this to raise?`
```
def test_contains_requires_hashable_raises(self, index):
        if isinstance(index, MultiIndex):
            return  # TODO: do we want this to raise?

        msg = "unhashable type: 'list'"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_numpy_compat.py:155** — `# TODO: overlap with tests.series.test_ufunc.test_reductions`
```
@pytest.mark.parametrize("func", [np.maximum, np.minimum])
def test_numpy_ufuncs_reductions(index, func, request):
    # TODO: overlap with tests.series.test_ufunc.test_reductions
    if len(index) == 0:
        pytest.skip("Test doesn't make sense for empty index.")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\test_setops.py:197** — `# TODO: pin down desired dtype; do we want it to be commutative?`
```
# Testing name retention
    # TODO: pin down desired dtype; do we want it to be commutative?
    result = a.intersection(b)
    assert result.name == names[2]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\base_class\test_reshape.py:41** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
def test_insert_missing(self, request, nulls_fixture, using_infer_string):
        if using_infer_string and nulls_fixture is pd.NA:
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH#22295
        # test there is no mangling of NA values
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimelike_\test_equals.py:56** — `# TODO: de-duplicate with other test_equals2 methods`
```
return period_range("2013-01-01", periods=5, freq="D")

    # TODO: de-duplicate with other test_equals2 methods
    @pytest.mark.parametrize("freq", ["D", "M"])
    def test_equals2(self, freq):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_constructors.py:85** — `# TODO: better place for tests shared by DTI/TDI?`
```
DatetimeIndex([pd.NaT, Timestamp("2011-01-01")._value], freq="D")

    # TODO: better place for tests shared by DTI/TDI?
    @pytest.mark.parametrize(
        "index",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_datetime.py:73** — `# TODO: belongs in frame groupby tests?`
```
assert isinstance(next(iter(result.values()))[0], Timestamp)

    # TODO: belongs in frame groupby tests?
    def test_groupby_function_tuple_1677(self):
        df = DataFrame(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_date_range.py:1303** — `#    # TODO give a more useful or informative message?`
```
msg = "Use a lower freq or a higher unit instead"
        with pytest.raises(ValueError, match=msg):
            #    # TODO give a more useful or informative message?
            date_range("2016-01-01", "2016-01-02", freq="ns", unit="ms")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_formats.py:189** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_dti_representation_to_series(self, unit):
        idx1 = DatetimeIndex([], freq="D")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_indexing.py:294** — `# TODO: This method came from test_datetime; de-dup with version above`
```
idx.take(indices, mode="clip")

    # TODO: This method came from test_datetime; de-dup with version above
    @pytest.mark.parametrize("tz", [None, "US/Eastern", "Asia/Tokyo"])
    def test_take2(self, tz):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_setops.py:43** — `# TODO: moved from test_datetimelike; dedup with version below`
```
]

    # TODO: moved from test_datetimelike; dedup with version below
    def test_union2(self, sort):
        everything = date_range("2020-01-01", periods=10)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_delete.py:117** — `# TODO: belongs in Series.drop tests?`
```
assert result.freq == expected.freq

    # TODO: belongs in Series.drop tests?
    @pytest.mark.parametrize("tz", [None, "Asia/Tokyo", "US/Pacific"])
    def test_delete_slice2(self, tz, unit):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_insert.py:180** — `# TODO: also changes DataFrame.__setitem__ with expansion`
```
assert result.freq is None

    # TODO: also changes DataFrame.__setitem__ with expansion
    def test_insert_mismatched_tzawareness(self):
        # see GH#7299
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_formats.py:18** — `# TODO: this is a test for DataFrame/Series, not IntervalIndex`
```
class TestIntervalIndexRendering:
    # TODO: this is a test for DataFrame/Series, not IntervalIndex
    @pytest.mark.parametrize(
        "constructor,expected",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_indexing.py:369** — `# TODO: with mismatched resolution get_indexer currently raises;`
```
def test_get_indexer_datetime(self):
        ii = IntervalIndex.from_breaks(date_range("2018-01-01", periods=4))
        # TODO: with mismatched resolution get_indexer currently raises;
        #  this should probably coerce?
        target = DatetimeIndex(["2018-01-02"], dtype="M8[ns]")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\interval\test_setops.py:184** — `# TODO: standardize return type of non-union setops type(self vs other)`
```
set_op = getattr(index, op_name)

        # TODO: standardize return type of non-union setops type(self vs other)
        # non-IntervalIndex
        if op_name == "difference":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_analytics.py:76** — `# TODO: reshape`
```
# TODO: reshape
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_indexing.py:85** — `# TODO: Try creating a UnicodeDecodeError in exception message`
```
with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(timedelta(seconds=30))
        # TODO: Try creating a UnicodeDecodeError in exception message
        with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(df.index[1], (16, "a"))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_reshape.py:69** — `# FIXME data types changes to float because`
```
)
    right.set_index(["1st", "2nd"], inplace=True)
    # FIXME data types changes to float because
    # of intermediate nan insertion;
    tm.assert_frame_equal(left, right, check_dtype=False)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\multi\test_setops.py:233** — `# TODO: this is raising in constructing a Categorical when calling`
```
other = MultiIndex.from_product([[3, pd.Timestamp("2000"), 4], ["c", "d"]])

    # TODO: this is raising in constructing a Categorical when calling
    #  algos.safe_sort. Should we catch and re-raise with a better message?
    msg = "'values' is not ordered, please explicitly specify the categories order "
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\numeric\test_numeric.py:535** — `# TODO: we could plausibly try to infer down to int16 here`
```
idx = Index(np.array([1, 2, 3], dtype=np.int8))
    result = idx.map(lambda x: x * 1000)
    # TODO: we could plausibly try to infer down to int16 here
    expected = Index([1000, 2000, 3000], dtype=np.int64)
    tm.assert_index_equal(result, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\period\test_formats.py:115** — `# TODO: These are Series.__repr__ tests`
```
assert result == expected

    # TODO: These are Series.__repr__ tests
    def test_representation_to_series(self):
        # GH#10971
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\period\test_indexing.py:480** — `# TODO: This method came from test_period; de-dup with version above`
```
tm.assert_numpy_array_equal(result[1], expected_missing)

    # TODO: This method came from test_period; de-dup with version above
    def test_get_indexer2(self):
        idx = period_range("2000-01-01", periods=3).asfreq("h", how="start")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\period\test_partial_slicing.py:44** — `# Todo: fix these accessors!`
```
pi = PeriodIndex(["2Q05", "3Q05", "4Q05", "1Q06", "2Q06"], freq="Q")
        ser = Series(np.random.default_rng(2).random(len(pi)), index=pi).cumsum()
        # Todo: fix these accessors!
        assert ser["05Q4"] == ser.iloc[2]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_astype.py:83** — `# TODO: de-duplicate this version (from test_ops) with the one above`
```
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)

    # TODO: de-duplicate this version (from test_ops) with the one above
    # (from test_period)
    def test_astype_object2(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_to_timestamp.py:30** — `# TODO: can we get the freq to round-trip?`
```
result = pi._data[::2].to_timestamp()
        expected = dti._data[::2]
        # TODO: can we get the freq to round-trip?
        tm.assert_datetime_array_equal(result, expected, check_freq=False)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_formats.py:54** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_representation_to_series(self):
        idx1 = TimedeltaIndex([], freq="D")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_scalar_compat.py:98** — `# TODO: de-duplicate with test_tdi_round`
```
t1._data.round(freq)

    # TODO: de-duplicate with test_tdi_round
    def test_round(self):
        t1 = timedelta_range("1 days", periods=3, freq="1 min 2 s 3 us")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_at.py:166** — `# TODO: De-duplicate/parametrize`
```
class TestAtErrors:
    # TODO: De-duplicate/parametrize
    #  test_at_series_raises_key_error2, test_at_frame_raises_key_error2
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_chaining_and_caching.py:561** — `# TODO(ArrayManager) fast_xs with array-like scalars is not yet working`
```
tm.assert_frame_equal(df, df_original)

    # TODO(ArrayManager) fast_xs with array-like scalars is not yet working
    @td.skip_array_manager_not_yet_implemented
    def test_chained_getitem_with_lists(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_coercion.py:351** — `# TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"`
```
tm.assert_index_equal(result, expected)

            # TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"
            #  casts that string to Period[M], not clear that is desirable
            if not isinstance(insert, pd.Timestamp):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_iloc.py:550** — `# TODO: GH#27620 this test used to compare iloc against ix; check if this`
```
tm.assert_frame_equal(df, expected)

    # TODO: GH#27620 this test used to compare iloc against ix; check if this
    #  is redundant with another test comparing iloc against loc
    def test_iloc_getitem_frame(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_indexing.py:911** — `# TODO(EA2D): we can make this no-copy in tz-naive case too`
```
if tz is None:
            # TODO(EA2D): we can make this no-copy in tz-naive case too
            assert ser.dtype == dti.dtype
            assert ser._values._ndarray is values._ndarray
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_loc.py:152** — `# TODO: test something?`
```
def test_loc_getitem_label_array_like(self):
        # TODO: test something?
        # array like
        pass
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\test_partial.py:4** — `TODO: these should be split among the indexer tests`
```
test setting *parts* of objects both positionally and label based

TODO: these should be split among the indexer tests
"""
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\interval\test_interval_new.py:171** — `# TODO KeyError is the appropriate error?`
```
if indexer_sl is tm.loc:
            # slices with scalar raise for overlapping intervals
            # TODO KeyError is the appropriate error?
            with pytest.raises(KeyError, match=msg):
                ser.loc[1:4]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_loc.py:828** — `# TODO: standardize return type for MultiIndex.get_loc`
```
loc = mi.append(mi).get_loc("2001-01")
    expected = index.append(index).get_loc("2001-01")
    # TODO: standardize return type for MultiIndex.get_loc
    tm.assert_numpy_array_equal(loc.nonzero()[0], expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_partial.py:121** — `# TODO(ArrayManager) rewrite test to not use .values`
```
df.loc[("a", "foo"), :]

    # TODO(ArrayManager) rewrite test to not use .values
    # exp.loc[2000, 4].values[:] select multiple columns -> .values is not a view
    @td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_setitem.py:129** — `# TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in`
```
)

    # TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in
    # all NaNs -> doesn't work in the "split" path (also for BlockManager actually)
    @td.skip_array_manager_not_yet_implemented
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\interchange\test_impl.py:371** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\interchange\test_utils.py:7** — `# TODO: use ArrowSchema to get reference C-string.`
```
from pandas.core.interchange.utils import dtype_to_arrow_c_fmt

# TODO: use ArrowSchema to get reference C-string.
# At the time, there is no way to access ArrowSchema holding a type format string
# from python. The only way to access it is to export the structure to a C-pointer,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\internals\test_internals.py:48** — `# TODO(ArrayManager) factor out interleave_dtype tests`
```
# this file contains BlockManager specific tests
# TODO(ArrayManager) factor out interleave_dtype tests
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_clipboard.py:354** — `# TODO avoid this exception?`
```
pa = pytest.importorskip("pyarrow")
            if engine == "c" and string_storage == "pyarrow":
                # TODO avoid this exception?
                string_dtype = pd.ArrowDtype(pa.large_string())
            else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_common.py:316** — `marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),`
```
("io", "data", "legacy_hdf", "datetimetz_object.h5"),
                # cleaned-up in https://github.com/pandas-dev/pandas/pull/57387 on main
                marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),
            ),
            (pd.read_stata, "os", ("io", "data", "stata", "stata10_115.dta")),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_fsspec.py:199** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet`
```
@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet
def test_fastparquet_options(fsspectest):
    """Regression test for writing to a not-yet-existent GCS Parquet file."""
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_http_headers.py:105** — `# TODO(ArrayManager) fastparquet`
```
parquetfastparquet_responder,
            partial(pd.read_parquet, engine="fastparquet"),
            # TODO(ArrayManager) fastparquet
            marks=[
                td.skip_if_no("fastparquet"),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_parquet.py:53** — `# TODO(ArrayManager) fastparquet relies on BlockManager internals`
```
# TODO(ArrayManager) fastparquet relies on BlockManager internals

pytestmark = [
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_spss.py:14** — `# TODO(CoW) - detection of chained assignment in cython`
```
# TODO(CoW) - detection of chained assignment in cython
# https://github.com/pandas-dev/pandas/issues/51315
@pytest.mark.filterwarnings("ignore::pandas.errors.ChainedAssignmentError")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_sql.py:1860** — `# TODO: clean up types_data_frame fixture`
```
)
    if "postgres" in conn_name:
        # TODO: clean up types_data_frame fixture
        result["BoolCol"] = result["BoolCol"].astype(int)
        result["BoolColWithNull"] = result["BoolColWithNull"].astype(float)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\test_stata.py:188** — `# FIXME: don't leave commented-out`
```
with tm.assert_produces_warning(UserWarning):
            parsed_117 = self.read_dta(path3)
            # FIXME: don't leave commented-out
            # 113 is buggy due to limits of date format support in Stata
            # parsed_113 = self.read_dta(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\excel\test_readers.py:248** — `# TODO add index to xls file)`
```
)

        # TODO add index to xls file)
        tm.assert_frame_equal(df1, expected)
        tm.assert_frame_equal(df2, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\excel\test_style.py:29** — `# TODO: should find a better way to check equality`
```
def assert_equal_cell_styles(cell1, cell2):
    # TODO: should find a better way to check equality
    assert cell1.alignment.__dict__ == cell2.alignment.__dict__
    assert cell1.border.__dict__ == cell2.border.__dict__
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\formats\test_format.py:1253** — `# FIXME: don't leave commented-out`
```
assert not has_non_verbose_info_repr(df)

        # FIXME: don't leave commented-out
        # test verbose overrides
        # set_option('display.max_info_columns', 4)  # exceeded
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\formats\test_to_html.py:373** — `# TODO: split this test`
```
@pytest.mark.parametrize("biggie_df_fixture", ["mixed"], indirect=True)
def test_to_html(biggie_df_fixture):
    # TODO: split this test
    df = biggie_df_fixture
    s = df.to_html()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\formats\test_to_string.py:391** — `# TODO: assert that these match??`
```
result = df.to_string()
        expected = "   0\n0  0\n1  0\n2 -0"
        # TODO: assert that these match??

    def test_to_string_complex_float_formatting(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\formats\style\test_style.py:441** — `# test execution added to todo`
```
}

    # test execution added to todo
    result = getattr(df.style, f"{method}_index")(func[method], axis=axis)
    assert len(result._todo) == 1
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\json\test_json_table_schema.py:212** — `# TODO: datedate.date? datetime.time?`
```
)
    def test_as_json_table_type_date_dtypes(self, date_dtype):
        # TODO: datedate.date? datetime.time?
        assert as_json_table_type(date_dtype) == "datetime"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\json\test_pandas.py:177** — `# TODO: a to_epoch method would also solve; see GH 14772`
```
# in milliseconds; these are internally stored in nanosecond,
                # so divide to get where we need
                # TODO: a to_epoch method would also solve; see GH 14772
                expected.isetitem(0, expected.iloc[:, 0].astype(np.int64) // 1000000)
        elif orient == "split":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\parser\test_encoding.py:190** — `# FIXME: this is bad!`
```
if parser.engine == "pyarrow" and pass_encoding is True and utf_value in [16, 32]:
        # FIXME: this is bad!
        pytest.skip("These cases freeze")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\parser\test_na_values.py:686** — `# TODO: this test isn't about the na_values keyword, it is about the empty entries`
```
# TODO: this test isn't about the na_values keyword, it is about the empty entries
#  being returned with NaN entries, whereas the pyarrow engine returns "nan"
@xfail_pyarrow  # mismatched shapes
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\parser\test_network.py:41** — `pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")`
```
# extension inference
    if compression_only == "tar":
        pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")

    extension = compression_to_extension[compression_only]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\parser\test_parse_dates.py:1015** — `# TODO: make unit check more specific`
```
result = parser.read_csv(StringIO(data), index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\parser\common\test_common_basic.py:96** — `# TODO: make unit check more specific`
```
fname = prefix + str(os.path.abspath(csv1))
    result = parser.read_csv(fname, index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_append.py:254** — `# TODO: Test is incorrect when not using_infer_string.`
```
expected = df
            if using_infer_string:
                # TODO: Test is incorrect when not using_infer_string.
                #       Should take the last 4 rows uncondiationally.
                expected = expected[-4:]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_file_handling.py:366** — `# TODO:(3.0): once Categorical replace deprecation is enforced,`
```
retr = read_hdf(store, key)

    # TODO:(3.0): once Categorical replace deprecation is enforced,
    #  we may be able to re-simplify the construction of s_nan
    if dtype == "category":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_put.py:302** — `# TODO(infer_string) make this work for string dtype`
```
with ensure_clean_store(setup_path) as store:
        if using_infer_string:
            # TODO(infer_string) make this work for string dtype
            msg = "Saving a MultiIndex with an extension dtype is not supported."
            with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_read.py:232** — `# TODO(infer_string) make this work for string dtype`
```
path = tmp_path / setup_path
    if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_round_trip.py:438** — `# TODO(infer_string) make this work for string dtype`
```
if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_select.py:892** — `# FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds

        # multiple (diff selector)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\io\pytables\test_store.py:745** — `# FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None
        #  but expect freq="18B"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\libs\test_hashtable.py:264** — `# TODO: moved from test_algos; may be redundancies with other tests`
```
class TestHashTableUnsorted:
    # TODO: moved from test_algos; may be redundancies with other tests
    def test_string_hashtable_set_item_signature(self):
        # GH#30419 fix typing in StringHashTable.set_item to prevent segfault
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\plotting\test_datetimelike.py:775** — `# TODO`
```
def test_mixed_freq_regular_first(self):
        # TODO
        s1 = Series(
            np.arange(20, dtype=np.float64),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\plotting\test_series.py:983** — `# TODO(3.0): this can be removed once Period[B] deprecation is enforced`
```
def test_plot_no_warning(self, ts):
        # GH 55138
        # TODO(3.0): this can be removed once Period[B] deprecation is enforced
        with tm.assert_produces_warning(False):
            _ = ts.plot()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\plotting\frame\test_frame.py:343** — `# TODO add MultiIndex test`
```
# columns.inferred_type == 'mixed'
        # TODO add MultiIndex test

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\resample\test_base.py:269** — `# TODO: no tests with len(df.columns) > 0`
```
result = getattr(rs, resample_method)()
    if resample_method == "ohlc":
        # TODO: no tests with len(df.columns) > 0
        mi = MultiIndex.from_product([df.columns, ["open", "high", "low", "close"]])
        expected = DataFrame(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\resample\test_datetime_index.py:2219** — `reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",`
```
marks=pytest.mark.xfail(
                condition=is_platform_windows(),
                reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",
            ),
        ),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\resample\test_period_index.py:316** — `# TODO: should this raise at the resample call instead of at the mean call?`
```
rs = ser.resample("W")
        with pytest.raises(IncompatibleFrequency, match=msg):
            # TODO: should this raise at the resample call instead of at the mean call?
            rs.mean()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\resample\test_resample_api.py:380** — `# TODO(GH#14008): once GH 14008 is fixed, move these tests into`
```
# TODO(GH#14008): once GH 14008 is fixed, move these tests into
# `Base` test class
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\resample\test_time_grouper.py:250** — `expected.index = dti._with_freq(None)  # TODO: is this desired?`
```
unit=dt_df["key"]._values.unit,
    )
    expected.index = dti._with_freq(None)  # TODO: is this desired?
    tm.assert_frame_equal(expected, dt_result)
    assert dt_result.index.name == "key"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\test_cut.py:584** — `# TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating`
```
if unit == "s":
        # TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating
        #  the first entry here raises in array_to_datetime. Should truncate
        #  instead of raising?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\test_melt.py:1205** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
if using_infer_string and any_string_dtype == "object":
            # triggers object dtype inference warning of dtype=object
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH46044
        df = DataFrame({"id": ["1", "2"], "a-1": [100, 200], "a-2": [300, 400]})
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\test_pivot.py:2625** — `using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"`
```
# while at that point None was converted to NaN
    @pytest.mark.xfail(
        using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"
    )
    def test_pivot_columns_is_none(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_append.py:370** — `# TODO: expected used to be `other.astype(object)` which is a more`
```
expected = other.astype(object)
        if isinstance(val, str) and dtype_str != "int64" and not using_array_manager:
            # TODO: expected used to be `other.astype(object)` which is a more
            #  reasonable result.  This was changed when tightening
            #  assert_frame_equal's treatment of mismatched NAs to match the
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_concat.py:50** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# test is not written to work with string dtype (checks .base)
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_copy(self, using_array_manager, using_copy_on_write):
        df = DataFrame(np.random.default_rng(2).standard_normal((4, 3)))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_datetimes.py:233** — `# TODO: setting nan here is to keep the test passing as we`
```
if item is pd.NaT and not using_array_manager:
                # GH#18463
                # TODO: setting nan here is to keep the test passing as we
                #  make assert_frame_equal stricter, but is nan really the
                #  ideal behavior here?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\concat\test_empty.py:244** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_inner_join_empty(self):
        # GH 15328
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_join.py:347** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_join_empty_bug(self):
        # generated an exception in 0.4.3
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge.py:569** — `# TODO: should the next loop be un-indented? doing so breaks this test`
```
tm.assert_frame_equal(result, exp)

            # TODO: should the next loop be un-indented? doing so breaks this test
            for kwarg in [
                {"left_index": True, "right_index": True},
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge_asof.py:3141** — `# TODO(GH#32306): may be relevant to the expected behavior here.`
```
#  np.array([np.nan, 1]).  Other than that, I (@jbrockmendel)
        #  have NO IDEA what the expected behavior is.
        # TODO(GH#32306): may be relevant to the expected behavior here.

        arr = pd.array([pd.NA, 0, 1], dtype=any_numeric_ea_dtype)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\scalar\period\test_period.py:87** — `# TODO: raise in the future an error when passing lowercase freq`
```
# GH#54105 - Period can be confusingly instantiated with lowercase freq
        # TODO: raise in the future an error when passing lowercase freq
        i1 = Period("2005", freq="Y")
        i2 = Period("2005")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_constructors.py:141** — `# TODO(2.0): the desired output dtype may have non-nano resolution`
```
dtype="m8[ns]",
        )
        # TODO(2.0): the desired output dtype may have non-nano resolution
        msg = f"'{unit}' is deprecated and will be removed in a future version."
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_timedelta.py:401** — `# TODO: this is a test of to_timedelta string parsing`
```
assert tup.nanoseconds == 0

    # TODO: this is a test of to_timedelta string parsing
    def test_iso_conversion(self):
        # GH #21877
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\scalar\timestamp\test_constructors.py:313** — `# TODO: if we passed microsecond with a keyword we would mess up`
```
@pytest.mark.parametrize("kwd", ["nanosecond", "microsecond", "second", "minute"])
    def test_constructor_positional_keyword_mixed_with_tzinfo(self, kwd, request):
        # TODO: if we passed microsecond with a keyword we would mess up
        #  xref GH#45307
        if kwd != "nanosecond":
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\test_arithmetic.py:763** — `# TODO: belongs in tests/arithmetic?`
```
ser_utc + ser

    # TODO: belongs in tests/arithmetic?
    def test_datetime_understood(self, unit):
        # Ensures it doesn't fail to create the right series
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\test_constructors.py:571** — `# TODO should this be raising at all?`
```
expected = Series([0, 1, 2], index=index, dtype=int)
        with pytest.raises(AssertionError, match="Series classes are different"):
            # TODO should this be raising at all?
            # https://github.com/pandas-dev/pandas/issues/56131
            tm.assert_series_equal(result, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\test_logical_ops.py:363** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
tm.assert_series_equal(result, expected)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_logical_ops_label_based(self, using_infer_string):
        # GH#4947
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\test_ufunc.py:173** — `@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp`
```
@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp
@pytest.mark.parametrize("shuffle", [True, False])
@pytest.mark.filterwarnings("ignore:divide by zero:RuntimeWarning")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\indexing\test_setitem.py:437** — `# TODO: ser.where(~mask, alt) unnecessarily upcasts to int64`
```
tm.assert_series_equal(ser2, expected)

        # TODO: ser.where(~mask, alt) unnecessarily upcasts to int64
        ser3 = orig.copy()
        res = ser3.where(~mask, alt)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\methods\test_align.py:210** — `# TODO: assert something?`
```
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

    # TODO: assert something?
    ts.align(ts[::2], join=join_type)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\methods\test_astype.py:403** — `# TODO: same for EA float/uint dtypes, signed integers?`
```
):
        # GH#45151 We don't cast negative numbers to nonsense values
        # TODO: same for EA float/uint dtypes, signed integers?
        arr = np.arange(5).astype(float_numpy_dtype) - 3  # includes negatives
        ser = Series(arr)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\methods\test_clip.py:73** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
# GH#19992
        msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\methods\test_convert_dtypes.py:186** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
class TestSeriesConvertDtypes:
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("params", product(*[(True, False)] * 5))
    def test_convert_dtypes(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\series\methods\test_diff.py:14** — `# TODO(__array_function__): could make np.diff return a Series`
```
class TestSeriesDiff:
    def test_diff_np(self):
        # TODO(__array_function__): could make np.diff return a Series
        #  matching ser.diff()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\strings\test_cat.py:359** — `# TODO: Strimg option, this should return string dtype`
```
expected = Series([np.nan] * 4, index=s.index, dtype=s.dtype)
    else:  # box == Index
        # TODO: Strimg option, this should return string dtype
        expected = Index([np.nan] * 4, dtype=object)
    result = s.str.cat(t, join="left")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\strings\test_extract.py:19** — `# TODO: should this raise TypeError`
```
def test_extract_expand_kwarg_wrong_type_raises(any_string_dtype):
    # TODO: should this raise TypeError
    values = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)
    with pytest.raises(ValueError, match="expand must be True or False"):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\strings\test_find_replace.py:258** — `# TODO(infer_string)`
```
tm.assert_series_equal(result, expected)

    # TODO(infer_string)
    # this particular combination of events is broken on 2.3
    # would require cherry picking #58483, which in turn requires #57481
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\strings\test_split_partition.py:385** — `# TODO see GH 18463`
```
# check that these are actually np.nan/pd.NA and not None
    # TODO see GH 18463
    # tm.assert_frame_equal does not differentiate
    if is_object_or_nan_string_dtype(any_string_dtype):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\tools\test_to_datetime.py:579** — `# TODO: Timestamp raises ValueError("could not convert string to Timestamp")`
```
def test_to_datetime_overflow(self):
        # we should get an OutOfBoundsDatetime, NOT OverflowError
        # TODO: Timestamp raises ValueError("could not convert string to Timestamp")
        #  can we make these more consistent?
        arg = "08335394550"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_business_hour.py:986** — `# TODO(GH#55564): as_unit will be unnecessary`
```
tm.assert_index_equal(t1, expected)

        # TODO(GH#55564): as_unit will be unnecessary
        pointwise = DatetimeIndex([x + off for x in idx]).as_unit(exp_unit)
        tm.assert_index_equal(pointwise, expected)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_offsets.py:573** — `# TODO: belongs in arithmetic tests?`
```
assert hash(off) is not None

    # TODO: belongs in arithmetic tests?
    @pytest.mark.filterwarnings(
        "ignore:Non-vectorized DateOffset being applied to Series or DatetimeIndex"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\tseries\offsets\test_year.py:330** — `# TODO(cython3): "arg: datetime" annotation will impose`
```
result = ts + off
    # TODO(cython3): "arg: datetime" annotation will impose
    # datetime limitations on Timestamp. The fused type below works in cy3
    # ctypedef fused datetimelike:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\tslibs\test_array_to_datetime.py:27** — `# TODO: tests that include tzs, ints`
```
class TestArrayToDatetimeResolutionInference:
    # TODO: tests that include tzs, ints

    def test_infer_all_nat(self):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\util\test_assert_almost_equal.py:341** — `# TODO: to get the same deprecation in assert_numpy_array_equal we need`
```
_assert_almost_equal_both(left, right, check_dtype=False)

        # TODO: to get the same deprecation in assert_numpy_array_equal we need
        #  to change/deprecate the default for strict_nan to become True
        # TODO: to get the same deprecation in assert_index_equal we need to
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\window\test_expanding.py:576** — `# TODO: xref gh-15826`
```
[[5, 6], [2, 1]], index=[0, 2], columns=Index(["X", "Y"], name="foo")
    )
    # TODO: xref gh-15826
    # .loc is not preserving the names
    result1 = df1.expanding().cov(df2, pairwise=True).loc[2]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\tests\window\test_pairwise.py:299** — `# TODO: We're missing a flag somewhere in meson`
```
lambda x, y: x.expanding().corr(y, pairwise=True),
            lambda x, y: x.rolling(window=3).cov(y, pairwise=True),
            # TODO: We're missing a flag somewhere in meson
            pytest.param(
                lambda x, y: x.rolling(window=3).corr(y, pairwise=True),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\_testing\asserters.py:599** — `# TODO(infer_string) this special case could be avoided if we have`
```
left = repr(left)
    elif isinstance(left, StringDtype):
        # TODO(infer_string) this special case could be avoided if we have
        # a more informative repr https://github.com/pandas-dev/pandas/issues/59342
        left = f"StringDtype(storage={left.storage}, na_value={left.na_value})"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\_testing\contexts.py:225** — `# TODO update match`
```
else:
            warning = FutureWarning  # type: ignore[assignment]
            # TODO update match
            match = "ChainedAssignmentError"
        if extra_warnings:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pandas\_testing\__init__.py:226** — `# TODO: Add container like pyarrow types:`
```
BOOL_PYARROW_DTYPES = [pa.bool_()]

    # TODO: Add container like pyarrow types:
    #  https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions
    ALL_PYARROW_DTYPES = (
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\FpxImagePlugin.py:178** — `# FIXME: the fill decoder is not implemented`
```
elif compression == 1:
                # FIXME: the fill decoder is not implemented
                self.tile.append(
                    ImageFile._Tile(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\GifImagePlugin.py:120** — `self._fp = self.fp  # FIXME: hack`
```
self.global_palette = self.palette = p

        self._fp = self.fp  # FIXME: hack
        self.__rewind = self.fp.tell()
        self._n_frames: int | None = None
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\IcoImagePlugin.py:75** — `# TODO: invent a more convenient method for proportional scalings`
```
break
        else:
            # TODO: invent a more convenient method for proportional scalings
            frame = provided_im.copy()
            frame.thumbnail(size, Image.Resampling.LANCZOS, reducing_gap=None)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\Image.py:544** — `# FIXME: take "new" parameters / other image?`
```
def __init__(self) -> None:
        # FIXME: take "new" parameters / other image?
        self._im: core.ImagingCore | DeferredError | None = None
        self._mode = ""
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageCms.py:1103** — `# FIXME: I get different results for the same data w. different`
```
if not isinstance(profile, ImageCmsProfile):
            profile = ImageCmsProfile(profile)
        # FIXME: I get different results for the same data w. different
        # compilers.  Bug in LittleCMS or in the binding?
        if profile.profile.is_intent_supported(intent, direction):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageDraw.py:102** — `# FIXME: fix Fill2 to properly support matte for I+F images`
```
self.ink = self.draw.draw_ink(-1)
        if mode in ("1", "P", "I", "F"):
            # FIXME: fix Fill2 to properly support matte for I+F images
            self.fontmode = "1"
        else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageDraw2.py:54** — `# FIXME: add support for bitmap fonts`
```
self, color: str, file: StrOrBytesPath | BinaryIO, size: float = 12
    ) -> None:
        # FIXME: add support for bitmap fonts
        self.color = ImageColor.getrgb(color)
        self.font = ImageFont.truetype(file, size)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageFile.py:341** — `# FIXME: This is a hack to handle TIFF's JpegTables tag.`
```
self.tile.sort(key=_tilesort)

            # FIXME: This is a hack to handle TIFF's JpegTables tag.
            prefix = getattr(self, "tile_prefix", b"")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageFont.py:19** — `# Todo:`
```
# 2003-09-27 fl   added support for truetype charmap encodings
#
# Todo:
# Adapt to PILFONT2 format (16-bit fonts, compressed, single file)
#
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageOps.py:54** — `# FIXME: apply to lookup table, not image data`
```
def _lut(image: Image.Image, lut: list[int]) -> Image.Image:
    if image.mode == "P":
        # FIXME: apply to lookup table, not image data
        msg = "mode P support coming soon"
        raise NotImplementedError(msg)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImagePalette.py:229** — `raise NotImplementedError(msg)  # FIXME`
```
msg = "unavailable when black is non-zero"
    raise NotImplementedError(msg)  # FIXME
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImageQt.py:140** — `# FIXME - is this really the best way to do this?`
```
# handle filename, if given instead of image name
    if hasattr(im, "toUtf8"):
        # FIXME - is this really the best way to do this?
        im = str(im.toUtf8(), "utf-8")
    if is_path(im):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\ImImagePlugin.py:152** — `# FIXME: this may read whole file if not a text file`
```
break

            # FIXME: this may read whole file if not a text file
            s = s + self.fp.readline()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\JpegImagePlugin.py:110** — `self.info["flashpix"] = s  # FIXME: value will change`
```
elif marker == 0xFFE2 and s.startswith(b"FPXR\0"):
        # extract FlashPix information (incomplete)
        self.info["flashpix"] = s  # FIXME: value will change
    elif marker == 0xFFE2 and s.startswith(b"ICC_PROFILE\0"):
        # Since an ICC profile can be larger than the maximum size of
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\McIdasImagePlugin.py:55** — `# FIXME: add memory map support`
```
mode = rawmode = "I;16B"
        elif w[11] == 4:
            # FIXME: add memory map support
            mode = "I"
            rawmode = "I;32B"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\MpoImagePlugin.py:128** — `self._fp = self.fp  # FIXME: hack`
```
del self.info["mpoffset"]  # no longer needed
        self.is_animated = self.n_frames > 1
        self._fp = self.fp  # FIXME: hack
        self._fp.seek(self.__mpoffsets[0])  # get ready to read first frame
        self.__frame = 0
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\MspImagePlugin.py:184** — `header[12] = checksum  # FIXME: is this the right field?`
```
for h in header:
        checksum = checksum ^ h
    header[12] = checksum  # FIXME: is this the right field?

    # header
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PcdImagePlugin.py:49** — `self._size = 768, 512  # FIXME: not correct for rotated images!`
```
self._mode = "RGB"
        self._size = 768, 512  # FIXME: not correct for rotated images!
        self.tile = [ImageFile._Tile("pcd", (0, 0) + self.size, 96 * 2048)]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PcxImagePlugin.py:96** — `# FIXME: hey, this doesn't work with the incremental loader !!!`
```
elif version == 5 and bits == 8 and planes == 1:
            mode = rawmode = "L"
            # FIXME: hey, this doesn't work with the incremental loader !!!
            self.fp.seek(-769, io.SEEK_END)
            s = self.fp.read(769)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PdfImagePlugin.py:57** — `# FIXME: Should replace ASCIIHexDecode with RunLengthDecode`
```
image_refs: list[PdfParser.IndirectReference],
) -> tuple[PdfParser.IndirectReference, str]:
    # FIXME: Should replace ASCIIHexDecode with RunLengthDecode
    # (packbits) or LZWDecode (tiff/lzw compression).  Note that
    # PDF 1.2 also supports Flatedecode (zip compression).
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PdfParser.py:616** — `# TODO: support reuse of deleted objects`
```
def next_object_id(self, offset: int | None = None) -> IndirectReference:
        try:
            # TODO: support reuse of deleted objects
            reference = IndirectReference(max(self.xref_table.keys()) + 1, 0)
        except ValueError:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PixarImagePlugin.py:61** — `# FIXME: to be continued...`
```
if mode == (14, 2):
            self._mode = "RGB"
        # FIXME: to be continued...

        # create tile descriptor (assuming "dumped")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PngImagePlugin.py:445** — `icc_profile = None  # FIXME`
```
raise
        except zlib.error:
            icc_profile = None  # FIXME
        self.im_info["icc_profile"] = icc_profile
        return s
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PsdImagePlugin.py:40** — `(7, 8): ("L", 1),  # FIXME: multilayer`
```
(3, 8): ("RGB", 3),
    (4, 8): ("CMYK", 4),
    (7, 8): ("L", 1),  # FIXME: multilayer
    (8, 8): ("L", 1),  # duotone
    (9, 8): ("LAB", 3),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\PSDraw.py:44** — `# FIXME: incomplete`
```
def begin_document(self, id: str | None = None) -> None:
        """Set up printing of a document. (Write PostScript DSC header.)"""
        # FIXME: incomplete
        self.fp.write(
            b"%!PS-Adobe-3.0\n"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\SpiderImagePlugin.py:161** — `self._fp = self.fp  # FIXME: hack`
```
self.tile = [ImageFile._Tile("raw", (0, 0) + self.size, offset, self.rawmode)]
        self._fp = self.fp  # FIXME: hack

    @property
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\TiffImagePlugin.py:962** — `# FIXME What about tagdata?`
```
def tobytes(self, offset: int = 0) -> bytes:
        # FIXME What about tagdata?
        result = self._pack("Q" if self._bigtiff else "H", len(self._tags_v2))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\TiffTags.py:209** — `# FIXME add more tags here`
```
33723: ("IptcNaaInfo", UNDEFINED, 1),
    34377: ("PhotoshopInfo", BYTE, 0),
    # FIXME add more tags here
    34665: ("ExifIFD", LONG, 1),
    34675: ("ICCProfile", UNDEFINED, 1),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\PIL\XVThumbImagePlugin.py:17** — `# FIXME: make save work (this requires quantization support)`
```
#
# To do:
# FIXME: make save work (this requires quantization support)
#
from __future__ import annotations
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\build_env.py:200** — `# FIXME: Consider direct URL?`
```
if not req.specifier.contains(dist.version, prereleases=True):
                    conflicting.add((installed_req_str, req_str))
                # FIXME: Consider direct URL?
        return conflicting, missing
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\cache.py:278** — `# TODO: use DirectUrl.equivalent when`
```
)
            else:
                # TODO: use DirectUrl.equivalent when
                # https://github.com/pypa/pip/pull/10564 is merged.
                if origin.url != download_info.url:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\cli\base_command.py:204** — `# TODO: Try to get these passing down from the command?`
```
sys.exit(ERROR)

        # TODO: Try to get these passing down from the command?
        #       without resorting to os.environ to hold these.
        #       This also affects isolated builds and it should.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\commands\inspect.py:60** — `# TODO tags? scheme?`
```
"installed": [self._dist_to_dict(dist) for dist in dists],
            "environment": default_environment(),
            # TODO tags? scheme?
        }
        print_json(data=output)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\index\collector.py:344** — `# TODO: In the future, it would be nice if pip supported PEP 691`
```
if not url.endswith("/"):
            url += "/"
        # TODO: In the future, it would be nice if pip supported PEP 691
        #       style responses in the file:// URLs, however there's no
        #       standard file extension for application/vnd.pypi.simple.v1+json
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\locations\base.py:15** — `# FIXME doesn't account for venv linked to global site-packages`
```
USER_CACHE_DIR = appdirs.user_cache_dir("pip")

# FIXME doesn't account for venv linked to global site-packages
site_packages: str = sysconfig.get_path("purelib")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\metadata\base.py:37** — `from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.`
```
DirectUrlValidationError,
)
from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.
from pip._internal.utils.egg_link import egg_link_path_from_sys_path
from pip._internal.utils.misc import is_local, normalize_path
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\models\installation_report.py:50** — `# TODO: currently, the resolver uses the default environment to evaluate`
```
],
            # https://peps.python.org/pep-0508/#environment-markers
            # TODO: currently, the resolver uses the default environment to evaluate
            # environment markers, so that is what we report here. In the future, it
            # should also take into account options such as --python-version or
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\models\selection_prefs.py:6** — `# TODO: This needs Python 3.10's improved slots support for dataclasses`
```
# TODO: This needs Python 3.10's improved slots support for dataclasses
# to be converted into a dataclass.
class SelectionPreferences:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\network\lazy_wheel.py:174** — `# TODO: Get range requests to be correctly cached`
```
headers = base_headers.copy()
        headers["Range"] = f"bytes={start}-{end}"
        # TODO: Get range requests to be correctly cached
        headers["Cache-Control"] = "no-cache"
        return self._session.get(self._url, headers=headers, stream=True)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\operations\prepare.py:557** — `# TODO: separate this part out from RequirementPreparer when the v1`
```
self._prepare_linked_requirement(req, parallel_builds)

        # TODO: separate this part out from RequirementPreparer when the v1
        # resolver can be removed!
        self._complete_partial_requirements(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\req\constructors.py:285** — `# TODO: The is_installable_dir test here might not be necessary`
```
if is_installable_dir(path):
            return path_to_url(path)
        # TODO: The is_installable_dir test here might not be necessary
        #       now that it is done in load_pyproject_toml too.
        raise InstallationError(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\req\req_file.py:107** — `# TODO: replace this with slots=True when dropping Python 3.9 support.`
```
@dataclass(frozen=True)
class ParsedRequirement:
    # TODO: replace this with slots=True when dropping Python 3.9 support.
    __slots__ = (
        "requirement",
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\req\req_install.py:371** — `# FIXME: Is there a better place to create the build_dir? (hg and bzr`
```
dir_name = f"{dir_name}_{uuid.uuid4().hex}"

        # FIXME: Is there a better place to create the build_dir? (hg and bzr
        # need this)
        if not os.path.exists(build_dir):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\req\req_set.py:75** — `TODO remove this property together with the legacy resolver, since the new`
```
"""Return the list of requirements that need to be installed.

        TODO remove this property together with the legacy resolver, since the new
             resolver only returns requirements that need to be installed.
        """
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\req\req_uninstall.py:480** — `# FIXME: need a test for this elif block`
```
for installed_file in installed_files:
                    paths_to_remove.add(os.path.join(dist_location, installed_file))
            # FIXME: need a test for this elif block
            # occurs with --single-version-externally-managed/--record outside
            # of pip
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py:227** — `# TODO performance: this means we iterate the dependencies at least twice,`
```
)
        # check dependencies are valid
        # TODO performance: this means we iterate the dependencies at least twice,
        # we may want to cache parsed Requires-Dist
        try:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\resolution\resolvelib\factory.py:201** — `# TODO: Check already installed candidate, and use it if the link and`
```
version: Optional[Version],
    ) -> Optional[BaseCandidate]:
        # TODO: Check already installed candidate, and use it if the link and
        # editable flag match.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\utils\unpacking.py:326** — `# FIXME: handle?`
```
untar_file(filename, location)
    else:
        # FIXME: handle?
        # FIXME: magic signatures?
        logger.critical(
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_internal\vcs\subversion.py:59** — `# FIXME: should we warn?`
```
entries_fn = os.path.join(base, cls.dirname, "entries")
            if not os.path.exists(entries_fn):
                # FIXME: should we warn?
                continue
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\typing_extensions.py:1020** — `# TODO: Use inspect.VALUE here, and make the annotations lazily evaluated`
```
own_annotations = ns["__annotations__"]
            elif "__annotate__" in ns:
                # TODO: Use inspect.VALUE here, and make the annotations lazily evaluated
                own_annotations = ns["__annotate__"](1)
            else:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\database.py:933** — `# FIXME handle the case where zipfile is not available`
```
requires = parse_requires_path(req_path)
            else:
                # FIXME handle the case where zipfile is not available
                zipf = zipimport.zipimporter(path)
                fileobj = StringIO(zipf.get_data('EGG-INFO/PKG-INFO').decode('utf8'))
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\locators.py:760** — `XXX TODO Note: this cache is never actually cleared. It's assumed that`
```
Get the HTML for an URL, possibly from an in-memory cache.

        XXX TODO Note: this cache is never actually cleared. It's assumed that
        the data won't get stale over the lifetime of a locator instance (not
        necessarily true for the default_locator).
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\metadata.py:239** — `# TODO document the mapping API and UNKNOWN default key`
```
"""

    # TODO document the mapping API and UNKNOWN default key

    def __init__(self, path=None, fileobj=None, mapping=None, scheme='default'):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\resources.py:190** — `todo = [resource]`
```
resource = self.find(resource_name)
        if resource is not None:
            todo = [resource]
            while todo:
                resource = todo.pop(0)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\util.py:401** — `# TODO check k, v for valid values`
```
cp = configparser.ConfigParser()
    for k, v in exports.items():
        # TODO check k, v for valid values
        cp.add_section(k)
        for entry in v.values():
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\version.py:267** — `TODO: fill this out`
```
1.2.3c1
        1.2.3.4
        TODO: fill this out

    Bad:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:839** — `# TODO version verification`
```
# wv = message['Wheel-Version'].split('.', 1)
            # file_version = tuple([int(i) for i in wv])
            # TODO version verification

            records = {}
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\pkg_resources\__init__.py:1** — `# TODO: Add Generic type annotations to initialized collections.`
```
# TODO: Add Generic type annotations to initialized collections.
# For now we'd simply use implicit Any/Unknown which would add redundant annotations
# mypy: disable-error-code="var-annotated"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\pygments\lexer.py:863** — `TODO: clean up the code here.`
```
The result is a combined token stream.

    TODO: clean up the code here.
    """
    insertions = iter(insertions)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\pygments\filters\__init__.py:72** — `highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.`
```
`codetags` : list of strings
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.

    .. versionchanged:: 2.13
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\pygments\lexers\python.py:715** — `# different tokens.  TODO: DelegatingLexer should support this`
```
tblexer = Python2TracebackLexer
        # We have two auxiliary lexers. Use DelegatingLexer twice with
        # different tokens.  TODO: DelegatingLexer should support this
        # directly, by accepting a tuplet of auxiliary lexers and a tuple of
        # distinguishing tokens. Then we wouldn't need this intermediary
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\pygments\lexers\_mapping.py:535** — `'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),`
```
'TlbLexer': ('pip._vendor.pygments.lexers.tlb', 'Tl-b', ('tlb',), ('*.tlb',), ()),
    'TlsLexer': ('pip._vendor.pygments.lexers.tls', 'TLS Presentation Language', ('tls',), (), ()),
    'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),
    'TransactSqlLexer': ('pip._vendor.pygments.lexers.sql', 'Transact-SQL', ('tsql', 't-sql'), ('*.sql',), ('text/x-tsql',)),
    'TreetopLexer': ('pip._vendor.pygments.lexers.parsers', 'Treetop', ('treetop',), ('*.treetop', '*.tt'), ()),
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\rich\text.py:562** — `# TODO: This is a little inefficient, it is only used by full justify`
```
Style: A Style instance.
        """
        # TODO: This is a little inefficient, it is only used by full justify
        if offset < 0:
            offset = len(self) + offset
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\truststore\_macos.py:558** — `# TODO: Not sure if we need the SecTrustResultType for anything?`
```
)

            # TODO: Not sure if we need the SecTrustResultType for anything?
            # We only care whether or not it's a success or failure for now.
            sec_trust_result_type = Security.SecTrustResultType()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:199** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self.sock = conn
        if self._is_using_tunnel():
            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
            # Mark this connection as not reusable
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\connectionpool.py:522** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, host, port = get_host(url)
        if host is not None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\exceptions.py:289** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\response.py:441** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.")
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\contrib\pyopenssl.py:371** — `# FIXME rethrow compatible exceptions should we ever use this`
```
def shutdown(self):
        # FIXME rethrow compatible exceptions should we ever use this
        self.connection.shutdown()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\contrib\securetransport.py:659** — `# TODO: should I do clean shutdown here? Do I have to?`
```
def close(self):
        # TODO: should I do clean shutdown here? Do I have to?
        if self._makefile_refs < 1:
            self._closed = True
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\util\response.py:103** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method = response._method
    if isinstance(method, int):  # Platform-specific: Appengine
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:31** — `# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.`
```
# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.
_Default = object()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:402** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\proto\_package_info.py:40** — `# TODO: Revert to empty string as a package value after protobuf fix.`
```
# A package should be present; get the marshal from there.
    # TODO: Revert to empty string as a package value after protobuf fix.
    # When package is empty, upb based protobuf fails with an
    # "TypeError: Couldn't build proto file into descriptor pool: invalid name: empty part ()' means"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\codec\ber\decoder.py:48** — `raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?`
```
The decoder is allowed to consume as many bytes as necessary.
        """
        raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?

    def indefLenValueDecoder(self, substrate, asn1Spec,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\codec\ber\encoder.py:189** — `# TODO: try to avoid ASN.1 schema instantiation`
```
def encodeValue(self, value, asn1Spec, encodeFun, **options):
        if asn1Spec is not None:
            # TODO: try to avoid ASN.1 schema instantiation
            value = asn1Spec.clone(value)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\codec\cer\decoder.py:51** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
BitStringPayloadDecoder = decoder.BitStringPayloadDecoder
OctetStringPayloadDecoder = decoder.OctetStringPayloadDecoder
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\codec\der\decoder.py:23** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
RealPayloadDecoder = decoder.RealPayloadDecoder
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\codec\der\encoder.py:34** — `# TODO: move out of sorting key function`
```
return component.getComponent().tagSet
            else:
                # TODO: move out of sorting key function
                names = [namedType.name for namedType in asn1Spec.componentType.namedTypes
                         if namedType.name in component]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\type\constraint.py:85** — `# TODO: fix possible comparison of set vs scalars here`
```
def isSuperTypeOf(self, otherConstraint):
        # TODO: fix possible comparison of set vs scalars here
        return (otherConstraint is self or
                not self._values or
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1\type\univ.py:1724** — `# TODO: remove when Py2.5 support is gone`
```
indices, values = zip(*self._componentValues.items())

        # TODO: remove when Py2.5 support is gone
        values = list(values)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1_modules\rfc2459.py:4** — `# Updated by Russ Housley to resolve the TODO regarding the Certificate`
```
# This file is part of pyasn1-modules software.
#
# Updated by Russ Housley to resolve the TODO regarding the Certificate
#   Policies Certificate Extension.
#
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\pyasn1_modules\rfc2985.py:86** — `# TODO:`
```
# TODO:
# Need a place to import PKCS15Token; it does not yet appear in an RFC
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\graphics\renderPDF.py:72** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\graphics\renderPS.py:772** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\graphics\renderSVG.py:803** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\graphics\widgetbase.py:62** — `# TODO when we need it, but not before -`
```
from reportlab.lib.validators import isValidChild

        # TODO when we need it, but not before -
        # expose sequence contents?
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\platypus\paragraph.py:1272** — `#TODO fix this to use binary search for the split points`
```
then push those new words onto words
    '''
    #TODO fix this to use binary search for the split points
    R = []
    aR = R.append
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\reportlab\platypus\xpreformatted.py:209** — `breakLinesCJK = breakLines  #TODO fixme fixme fixme`
```
return lines

    breakLinesCJK = breakLines  #TODO fixme fixme fixme

    # we need this her to get the right splitter
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\cli.py:30** — `# TODO: Add CLI Tests`
```
# TODO: Add CLI Tests
# TODO: Simplify formatter by using argparse `type` arguments
def create_parser():
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\keywords.py:41** — `# FIXME(andi): VALUES shouldn't be listed here`
```
(r'\\\w+', tokens.Command),

    # FIXME(andi): VALUES shouldn't be listed here
    # see https://github.com/andialbrecht/sqlparse/pull/64
    # AS and IN are special, it may be followed by a parenthesis, but
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\sql.py:109** — `# TODO: Add test for regex with is_keyboard = false`
```
if regex:
            # TODO: Add test for regex with is_keyboard = false
            flag = re.IGNORECASE if self.is_keyword else 0
            values = (re.compile(v, flag) for v in values)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\engine\grouping.py:335** — `# TODO: convert this to eidx instead of end token.`
```
else:
            end = tlist.tokens[eidx - 1]
        # TODO: convert this to eidx instead of end token.
        # i think above values are len(tlist) and eidx-1
        eidx = tlist.token_index(end)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\engine\statement_splitter.py:58** — `# FIXME(andi): This makes no sense.  ## this comment neither`
```
self._begin_depth += 1
            if self._is_create:
                # FIXME(andi): This makes no sense.  ## this comment neither
                return 1
            return 0
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\filters\others.py:19** — `# TODO(andi) Comment types should be unified, see related issue38`
```
def _process(tlist):
        def get_next_comment(idx=-1):
            # TODO(andi) Comment types should be unified, see related issue38
            return tlist.token_next_by(i=sql.Comment, t=T.Comment, idx=idx)
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\sqlparse\filters\right_margin.py:13** — `# FIXME: Doesn't work`
```
# FIXME: Doesn't work
class RightMarginFilter:
    keep_together = (
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\connection.py:330** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self._has_connected_to_proxy = True

            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\connectionpool.py:578** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, _, host, port, *_ = parse_url(url)
        scheme = scheme or "http"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\exceptions.py:306** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme: str | None) -> None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\response.py:782** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout as e:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.") from e  # type: ignore[arg-type]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\_base_connection.py:20** — `# TODO: Remove this in favor of a better`
```
class _ResponseOptions(typing.NamedTuple):
    # TODO: Remove this in favor of a better
    # HTTP request/response lifecycle tracking.
    request_method: str
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\http2\connection.py:144** — `# TODO SKIPPABLE_HEADERS from urllib3 are ignored.`
```
def putheader(self, header: str | bytes, *values: str | bytes) -> None:  # type: ignore[override]
        # TODO SKIPPABLE_HEADERS from urllib3 are ignored.
        header = header.encode() if isinstance(header, str) else header
        header = header.lower()  # A lot of upstream code uses capitalized headers.
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\http2\__init__.py:38** — `# TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.`
```
urllib3_connection.HTTPSConnection = HTTP2Connection  # type: ignore[misc]

    # TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.
    urllib3_util.ALPN_PROTOCOLS = ["h2"]
    urllib3_util_ssl.ALPN_PROTOCOLS = ["h2"]
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\util\request.py:229** — `# File-like object, TODO: use seek() and tell() for length?`
```
content_length = len(chunks[0])

    # File-like object, TODO: use seek() and tell() for length?
    elif hasattr(body, "read"):
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\util\response.py:99** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method_str = response._method  # type: str  # type: ignore[attr-defined]
    return method_str.upper() == "HEAD"
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\urllib3\util\url.py:454** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\connectit_django\.venv\Lib\site-packages\werkzeug\http.py:1343** — `# TODO Remove encoding dance, it seems like clients accept UTF-8 keys`
```
# Send a non-ASCII key as mojibake. Everything else should already be ASCII.
    # TODO Remove encoding dance, it seems like clients accept UTF-8 keys
    buf = [f"{key.encode().decode('latin1')}={value}"]
```
---
- **C:\industria\connectit_django\docs_migrados\sector_routes.py:182** — `# TODO: A verificação de dependência pode ser expandida para outros módulos.`
```
"""
    try:
        # TODO: A verificação de dependência pode ser expandida para outros módulos.
        sector = get_document('sectors', sector_id)
        if not sector:
```
---
- **C:\industria\connectit_django\docs_migrados\supplier_routes.py:197** — `# TODO: Adicionar lógica para apagar os ficheiros de anexo do disco.`
```
flash('Fornecedor não encontrado.', 'danger')
        else:
            # TODO: Adicionar lógica para apagar os ficheiros de anexo do disco.
            delete_document('suppliers', supplier_id)
            flash(f'Fornecedor "{supplier.get("name")}" excluído com sucesso!', 'success')
```
---
- **C:\industria\connectit_django\docs_migrados\unit_routes.py:150** — `# TODO: Implementar verificação de dependência (se ativos, etc., usam esta unidade)`
```
"""
    try:
        # TODO: Implementar verificação de dependência (se ativos, etc., usam esta unidade)
        unit = get_document('units', unit_id)
        if not unit:
```
---
- **C:\industria\connectit_django\staticfiles_collected\admin\js\vendor\jquery\jquery.js:4132** — `//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)`
```
//		paths to a single mechanism.
//	3. Use the same single mechanism to support "private" and "user" data.
//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)
//	5. Avoid exposing implementation details on user objects (eg. expando properties)
//	6. Provide a clear path for implementation upgrade to WeakMap in 2014
```
---
- **C:\industria\connectit_django\staticfiles_collected\admin\js\vendor\xregexp\xregexp.js:2792** — `// TODO: Remove from `core-js@4``
```
require('../../modules/esnext.symbol.metadata');
require('../../modules/esnext.symbol.observable');
// TODO: Remove from `core-js@4`
require('../../modules/esnext.symbol.pattern-match');
// TODO: Remove from `core-js@4`
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\anyio\_core\_fileio.py:416** — `def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it`
```
@property
        def info(self) -> Any:  # TODO: add return type annotation when Typeshed gets it
            return self._path.info
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\blinker\base.py:135** — `# TODO no explanation or test for this`
```
)
            except TypeError:
                # TODO no explanation or test for this
                self.disconnect(receiver, sender)
                raise
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\charset_normalizer\legacy.py:9** — `# TODO: remove this check when dropping Python 3.7 support`
```
from .constant import CHARDET_CORRESPONDENCE

# TODO: remove this check when dropping Python 3.7 support
if TYPE_CHECKING:
    from typing_extensions import TypedDict
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\click\_termui_impl.py:525** — `# TODO: This never terminates if the passed generator never terminates.`
```
fd, filename = tempfile.mkstemp()
    # TODO: This never terminates if the passed generator never terminates.
    text = "".join(generator)
    if not color:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\cryptography\hazmat\primitives\asymmetric\rsa.py:221** — `# TODO: Replace with lcm(p - 1, q - 1) once the minimum`
```
# than necessary. (lambda_n always divides phi_n)
    #
    # TODO: Replace with lcm(p - 1, q - 1) once the minimum
    # supported Python version is >= 3.9.
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\cryptography\x509\name.py:357** — `# TODO: this is relatively expensive, if this looks like a bottleneck`
```
def __hash__(self) -> int:
        # TODO: this is relatively expensive, if this looks like a bottleneck
        # for you, consider optimizing!
        return hash(tuple(self._attributes))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\dateutil\rrule.py:1182** — `# TODO: Check -numweeks for next year.`
```
if 1 in rr._byweekno:
                    # Check week number 1 of next year as well
                    # TODO: Check -numweeks for next year.
                    i = no1wkst+numweeks*7
                    if no1wkst != firstwkst:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\dateutil\parser\_parser.py:55** — `# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth`
```
# TODO: pandas.core.tools.datetimes imports this explicitly.  Might be worth
# making public and/or figuring out if there is something we can
# take off their plate.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\dateutil\zoneinfo\__init__.py:25** — `except IOError as e:  # TODO  switch to FileNotFoundError?`
```
try:
        return BytesIO(get_data(__name__, ZONEFILENAME))
    except IOError as e:  # TODO  switch to FileNotFoundError?
        warnings.warn("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\admin\checks.py:739** — `# Skip ordering in the format field1__field2 (FIXME: checking`
```
return []
        elif LOOKUP_SEP in field_name:
            # Skip ordering in the format field1__field2 (FIXME: checking
            # this format would be nice, but it's a little fiddly).
            return []
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\admin\options.py:437** — `# TODO: this should be handled by some parameter to the ChangeList.`
```
"""
        qs = self.model._default_manager.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\admin\static\admin\js\vendor\jquery\jquery.js:4132** — `//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)`
```
//		paths to a single mechanism.
//	3. Use the same single mechanism to support "private" and "user" data.
//	4. _Never_ expose "private" data to user code (TODO: Drop _data, _removeData)
//	5. Avoid exposing implementation details on user objects (eg. expando properties)
//	6. Provide a clear path for implementation upgrade to WeakMap in 2014
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\admin\static\admin\js\vendor\xregexp\xregexp.js:2792** — `// TODO: Remove from `core-js@4``
```
require('../../modules/esnext.symbol.metadata');
require('../../modules/esnext.symbol.observable');
// TODO: Remove from `core-js@4`
require('../../modules/esnext.symbol.pattern-match');
// TODO: Remove from `core-js@4`
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\auth\management\__init__.py:119** — `# TODO: Drop ImportError and KeyError when dropping support for PY312.`
```
result = getpass.getuser()
    except (ImportError, KeyError, OSError):
        # TODO: Drop ImportError and KeyError when dropping support for PY312.
        # KeyError (Python <3.13) or OSError (Python 3.13+) will be raised by
        # os.getpwuid() (called by getuser()) if there is no corresponding
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\db\backends\base\models.py:15** — `# TODO: Is caching really necessary here?  Is complexity worth it?`
```
Return a GDAL SpatialReference object.
        """
        # TODO: Is caching really necessary here?  Is complexity worth it?
        if hasattr(self, "_srs"):
            # Returning a clone of the cached SpatialReference object.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\introspection.py:33** — `# TODO: Research way to find a more specific geometry field type for`
```
) from exc

            # TODO: Research way to find a more specific geometry field type for
            # the column's contents.
            field_type = "GeometryField"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\models.py:21** — `# TODO: Add support for `diminfo` column (type MDSYS.SDO_DIM_ARRAY).`
```
column_name = models.CharField(max_length=1024)
    srid = models.IntegerField(primary_key=True)
    # TODO: Add support for `diminfo` column (type MDSYS.SDO_DIM_ARRAY).

    class Meta:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\db\backends\oracle\operations.py:108** — `),  # TODO: Is this really the same as ST_Intersects()?`
```
"intersects": SDOOperator(
            func="SDO_OVERLAPBDYINTERSECT"
        ),  # TODO: Is this really the same as ST_Intersects()?
        "equals": SDOOperator(func="SDO_EQUAL"),
        "exact": SDOOperator(func="SDO_EQUAL"),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\db\backends\postgis\operations.py:247** — `# TODO: Support 'M' extension.`
```
# Type-based geometries.
        # TODO: Support 'M' extension.
        if f.dim == 3:
            geom_type = f.geom_type + "Z"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\gdal\envelope.py:193** — `# TODO: Fix significant figures.`
```
def wkt(self):
        "Return WKT representing a Polygon for this envelope."
        # TODO: Fix significant figures.
        return "POLYGON((%s %s,%s %s,%s %s,%s %s,%s %s))" % (
            self.min_x,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\gdal\field.py:189** — `# TODO: Adapt timezone information.`
```
def value(self):
        "Return a Python `datetime` object for this OFTDateTime field."
        # TODO: Adapt timezone information.
        #  See https://lists.osgeo.org/pipermail/gdal-dev/2006-February/007990.html
        #  The `tz` variable has values of: 0=unknown, 1=localtime (ambiguous),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\gdal\geometries.py:266** — `# TODO: Fix Envelope() for Point geometries.`
```
def envelope(self):
        "Return the envelope for this Geometry."
        # TODO: Fix Envelope() for Point geometries.
        return Envelope(capi.get_envelope(self.ptr, byref(OGREnvelope())))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\static\gis\js\OLMapWidget.js:39** — `// TODO: allow deleting individual features (#8972)`
```
}

// TODO: allow deleting individual features (#8972)
class MapWidget {
    constructor(options) {
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\utils\layermapping.py:198** — `# TODO: Support more than one geometry field / model.  However, this`
```
"""
        # The geometry field of the model is set here.
        # TODO: Support more than one geometry field / model.  However, this
        # depends on the GDAL Driver in use.
        self.geom_field = False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\contrib\gis\utils\ogrinspect.py:242** — `# TODO: Autodetection of multigeometry types (see #7218).`
```
raise TypeError("Unknown field type %s in %s" % (field_type, mfield))

    # TODO: Autodetection of multigeometry types (see #7218).
    gtype = layer.geom_type
    if multi_geom:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\core\handlers\asgi.py:56** — `# TODO: Better is-prefix checking, slash handling?`
```
self.script_name = get_script_prefix(scope)
        if self.script_name:
            # TODO: Better is-prefix checking, slash handling?
            self.path_info = scope["path"].removeprefix(self.script_name)
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\backends\oracle\operations.py:45** — `# TODO: colorize this SQL code with style.SQL_KEYWORD(), etc.`
```
set_operators = {**BaseDatabaseOperations.set_operators, "difference": "MINUS"}

    # TODO: colorize this SQL code with style.SQL_KEYWORD(), etc.
    _sequence_reset_sql = """
DECLARE
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\migrations\graph.py:272** — `todo = set(self.nodes)`
```
# Algo from GvR:
        # https://neopythonic.blogspot.com/2009/01/detecting-cycles-in-directed-graph.html
        todo = set(self.nodes)
        while todo:
            node = todo.pop()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\migrations\state.py:295** — `# TODO: investigate if old relational fields must be reloaded or if`
```
else:
            fields[name] = field
        # TODO: investigate if old relational fields must be reloaded or if
        # it's sufficient if the new field is (#27737).
        # Delay rendering of relationships if it's not a relational field and
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\models\base.py:1489** — `# TODO: Handle multiple backends with different feature flags.`
```
f = self._meta.get_field(field_name)
                lookup_value = getattr(self, f.attname)
                # TODO: Handle multiple backends with different feature flags.
                if lookup_value is None or (
                    lookup_value == ""
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\models\expressions.py:947** — `# FIXME: Rename possibly_multivalued to multivalued and fix detection`
```
f"{self.name}."
            )
        # FIXME: Rename possibly_multivalued to multivalued and fix detection
        # for non-multivalued JOINs (e.g. foreign key fields). This should take
        # into account only many-to-many and one-to-many relationships.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\models\fields\__init__.py:1306** — `# TODO: Handle multiple backends with different feature flags.`
```
# the value in the form field (to pass into widget for example).
        defaults = {"max_length": self.max_length}
        # TODO: Handle multiple backends with different feature flags.
        if self.null and not connection.features.interprets_empty_strings_as_nulls:
            defaults["empty_value"] = None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\db\models\sql\query.py:2659** — `# TODO: It might be possible to trim more joins from the start of the`
```
self.where.add(extra_restriction, AND)
        else:
            # TODO: It might be possible to trim more joins from the start of the
            # inner query if it happens to have a longer join chain containing the
            # values in select_fields. Lets punt this one for now.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\forms\models.py:612** — `# Create the inner Meta class. FIXME: ideally, we should be able to`
```
field class.
    """
    # Create the inner Meta class. FIXME: ideally, we should be able to
    # construct a ModelForm without creating and passing in a temporary
    # inner class.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\http\multipartparser.py:408** — `# FIXME: this currently assumes that upload handlers store the file as 'file'`
```
def _close_files(self):
        # Free up all file handles.
        # FIXME: this currently assumes that upload handlers store the file as 'file'
        # We should document that...
        # (Maybe add handler.free_file to complement new_file)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\test\testcases.py:1689** — `# TODO: Modify if/when that internal API is refactored`
```
# Emulate behavior of django.contrib.staticfiles.views.serve() when it
        # invokes staticfiles' finders functionality.
        # TODO: Modify if/when that internal API is refactored
        final_rel_path = os_rel_path.replace("\\", "/").lstrip("/")
        return serve(request, final_rel_path, document_root=self.get_base_dir())
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\django\utils\regex_helper.py:87** — `# FIXME: One day we'll should do this, but not in 1.0.`
```
result.append(".")
            elif ch == "|":
                # FIXME: One day we'll should do this, but not in 1.0.
                raise NotImplementedError("Awaiting Implementation")
            elif ch == "^":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\firebase_admin\_rfc3339.py:73** — `# TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex`
```
# Note: %z parses timezone offsets, but requires the timezone offset *not*
    # include a separating ':'. As of python 3.7, this was relaxed.
    # TODO(rsgowman): Once python3.7 becomes our floor, we can drop the regex
    # replacement.
    datestr_modified = re.sub(r'(\d\d):(\d\d)$', r'\1\2', datestr_modified)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\firebase_admin\_user_import.py:478** — `# TODO(rsgowman): This class used to be specific to importing users (hence`
```
as importing users or deleting multiple user accounts.
    """
    # TODO(rsgowman): This class used to be specific to importing users (hence
    # it's home in _user_import.py). It's now also used by bulk deletion of
    # users. Move this to a more common location.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\bidi.py:291** — `# TODO: api_core should expose the future interface for wrapped`
```
request_generator.call = call

        # TODO: api_core should expose the future interface for wrapped
        # callables as well.
        if hasattr(call, "_wrapped"):  # pragma: NO COVER
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\client_logging.py:12** — `# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.`
```
# Fields to be included in the StructuredLogFormatter.
#
# TODO(https://github.com/googleapis/python-api-core/issues/761): Update this list to support additional logging fields.
_recognized_logging_fields = [
    "httpRequest",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\exceptions.py:498** — `# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.`
```
# to `format_http_response_error` which expects a more abstract response from google.auth and is
# compatible with both sync and async response types.
# TODO(https://github.com/googleapis/python-api-core/issues/691): Add type hint for response.
def format_http_response_error(
    response, method: str, url: str, payload: Optional[Dict] = None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\extended_operation.py:138** — `# TODO(dovs): there is not currently a good way to determine whether the`
```
def cancelled(self):
        # TODO(dovs): there is not currently a good way to determine whether the
        # operation has been cancelled.
        # The best we can do is manually keep track of cancellation
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\grpc_helpers.py:295** — `# TODO(https://github.com/googleapis/python-api-core/issues/598):`
```
# Use grpc.compute_engine_channel_credentials in order to support Direct Path.
        # See https://grpc.github.io/grpc/python/grpc.html#grpc.compute_engine_channel_credentials
        # TODO(https://github.com/googleapis/python-api-core/issues/598):
        # Although `grpc.compute_engine_channel_credentials` returns channel credentials
        # outside of a Google Compute Engine environment (GCE), we should determine if
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\rest_streaming_async.py:54** — `# TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content`
```
self._response = response
        self._chunk_size = 1024
        # TODO(https://github.com/googleapis/python-api-core/issues/703): mypy does not recognize the abstract content
        # method as an async generator as it looks for the `yield` keyword in the implementation.
        # Given that the abstract method is not implemented, mypy fails to recognize it as an async generator.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry_async.py:17** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry_async.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\operations_v1\operations_rest_client_async.py:109** — `# TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry``
```
name: str,
        *,
        # TODO(https://github.com/googleapis/python-api-core/issues/722): Leverage `retry`
        # to allow configuring retryable error codes.
        retry=gapic_v1.method_async.DEFAULT,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\operations_v1\transports\base.py:52** — `# TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.`
```
*,
        host: str = DEFAULT_HOST,
        # TODO(https://github.com/googleapis/python-api-core/issues/709): update type hint for credentials to include `google.auth.aio.Credentials`.
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\operations_v1\transports\rest.py:134** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\operations_v1\transports\rest_asyncio.py:84** — `# TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.`
```
http_options: Optional[Dict] = None,
        path_prefix: str = "v1",
        # TODO(https://github.com/googleapis/python-api-core/issues/715): Add docstring for `credentials_file` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/716): Add docstring for `scopes` to async REST transport.
        # TODO(https://github.com/googleapis/python-api-core/issues/717): Add docstring for `quota_project_id` to async REST transport.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry\retry_streaming.py:113** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry\retry_streaming_async.py:116** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        # Start a new retry loop
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry\retry_unary.py:144** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry\retry_unary_async.py:155** — `# TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535`
```
# continue trying until an attempt completes, or a terminal exception is raised in _retry_error_helper
    # TODO: support max_attempts argument: https://github.com/googleapis/python-api-core/issues/535
    while True:
        try:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\api_core\retry\__init__.py:33** — `# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)`
```
# The following imports are for backwards compatibility with https://github.com/googleapis/python-api-core/blob/4d7d2edee2c108d43deb151e6e0fdceb56b73275/google/api_core/retry.py
#
# TODO: Revert these imports on the next major version release (https://github.com/googleapis/python-api-core/issues/576)
from google.api_core import datetime_helpers  # noqa: F401
from google.api_core import exceptions  # noqa: F401
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\auth\_helpers.py:43** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.`
```
REFRESH_THRESHOLD = datetime.timedelta(minutes=3, seconds=45)

# TODO(https://github.com/googleapis/google-auth-library-python/issues/1684): Audit and update the list below.
_SENSITIVE_FIELDS = {
    "accessToken",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\auth\aio\_helpers.py:42** — `# TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):`
```
return json_response
    except Exception:
        # TODO(https://github.com/googleapis/google-auth-library-python/issues/1745):
        # Parse and return response payload as json based on different content types.
        return None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\auth\compute_engine\_metadata.py:82** — `# TODO: implement GCE residency detection on Windows`
```
if os.name == "nt":
        # TODO: implement GCE residency detection on Windows
        return False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\auth\transport\_aiohttp_requests.py:146** — `# TODO: Use auto_decompress property for aiohttp 3.7+`
```
def __init__(self, session=None):
        # TODO: Use auto_decompress property for aiohttp 3.7+
        if session is not None and session._auto_decompress:
            raise exceptions.InvalidOperation(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\firestore_admin_v1\services\firestore_admin\transports\rest.py:1882** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\firestore_v1\watch.py:75** — `# TODO: Currently this uses a dict. Other implementations use a rbtree.`
```
class WatchDocTree(object):
    # TODO: Currently this uses a dict. Other implementations use a rbtree.
    # The performance of this implementation should be investigated and may
    # require modifying the underlying datastructure to a rbtree.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\firestore_v1\_helpers.py:750** — `# TODO: other transforms`
```
def _apply_merge_all(self) -> None:
        self.data_merge = sorted(self.field_paths + self.deleted_fields)
        # TODO: other transforms
        self.transform_merge = self.transform_paths
        self.merge = sorted(self.data_merge + self.transform_paths)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\firestore_v1\__init__.py:66** — `# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match`
```
from google.cloud.firestore_v1.watch import Watch

# TODO(https://github.com/googleapis/python-firestore/issues/93): this is all on the generated surface. We require this to match
# firestore.py. So comment out until needed on customer level for certain.
# from .services.firestore import FirestoreClient
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\firestore_v1\services\firestore\transports\rest.py:970** — `# TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.`
```
"""
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\storage\blob.py:4789** — `# TODO: After google-cloud-core 1.6.0 is stable and we upgrade it`
```
:returns: The host name.
    """
    # TODO: After google-cloud-core 1.6.0 is stable and we upgrade it
    # to 1.6.0 in setup.py, we no longer need to check the attribute
    # existence. We can simply return connection.get_api_base_url_for_mtls().
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\cloud\storage\_http.py:54** — `# TODO: When metrics all use gccl, this should be removed #9552`
```
self._client_info.client_library_version = __version__

        # TODO: When metrics all use gccl, this should be removed #9552
        if self._client_info.user_agent is None:  # pragma: no branch
            self._client_info.user_agent = ""
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\descriptor.py:27** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
  _message = api_implementation._c_module
  # TODO: Remove this import after fix api_implementation
  if _message is None:
    from google.protobuf.pyext import _message
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\descriptor_database.py:139** — `# TODO: implement this API.`
```
def FindFileContainingExtension(self, extendee_name, extension_number):
    # TODO: implement this API.
    return None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\descriptor_pool.py:1361** — `# TODO: This pool could be constructed from Python code, when we`
```
if _USE_C_DESCRIPTORS:
  # TODO: This pool could be constructed from Python code, when we
  # support a flag like 'use_cpp_generated_pool=True'.
  # pylint: disable=protected-access
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\message.py:8** — `# TODO: We should just make these methods all "pure-virtual" and move`
```
# https://developers.google.com/open-source/licenses/bsd

# TODO: We should just make these methods all "pure-virtual" and move
# all implementation out, into reflection.py for now.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\message_factory.py:100** — `# TODO: Remove this check here. Duplicate extension`
```
_ = GetMessageClass(extension.containing_type)
      if api_implementation.Type() != 'python':
        # TODO: Remove this check here. Duplicate extension
        # register check should be in descriptor_pool.
        if extension is not pool.FindExtensionByNumber(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\symbol_database.py:136** — `# TODO: Fix the differences with MessageFactory.`
```
def GetMessages(self, files):
    # TODO: Fix the differences with MessageFactory.
    """Gets all registered messages from a specified file.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\text_format.py:22** — `# TODO Import thread contention leads to test failures.`
```
__author__ = 'kenton@google.com (Kenton Varda)'

# TODO Import thread contention leads to test failures.
import encodings.raw_unicode_escape  # pylint: disable=unused-import
import encodings.unicode_escape  # pylint: disable=unused-import
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\internal\api_implementation.py:88** — `# TODO: fail back to python`
```
del _message
  except ImportError:
    # TODO: fail back to python
    warnings.warn(
        'Selected implementation cpp is not available.')
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\internal\builder.py:96** — `# TODO: Remove this on-op`
```
file_des: FileDescriptor of the .proto file
  """
  # TODO: Remove this on-op
  return
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\internal\containers.py:98** — `# TODO: Remove this. BaseContainer does *not* conform to`
```
# TODO: Remove this. BaseContainer does *not* conform to
# MutableSequence, only its subclasses do.
collections.abc.MutableSequence.register(BaseContainer)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\internal\extension_dict.py:37** — `# TODO: Unify error handling of "unknown extension" crap.`
```
# TODO: Unify error handling of "unknown extension" crap.
# TODO: Support iteritems()-style iteration over all
# extensions with the "has" bits turned on?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\internal\python_message.py:10** — `# TODO: Helpers for verbose, common checks like seeing if a`
```
# This code is meant to work on Python 2.4 and above only.
#
# TODO: Helpers for verbose, common checks like seeing if a
# descriptor's cpp_type is CPPTYPE_MESSAGE.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\google\protobuf\pyext\cpp_message.py:21** — `# TODO: Remove this import after fix api_implementation`
```
# pylint: disable=protected-access
_message = api_implementation._c_module
# TODO: Remove this import after fix api_implementation
if _message is None:
  from google.protobuf.pyext import _message
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\_auth.py:37** — `# TODO(xuanwn): Give credentials an actual type.`
```
_credentials: Any

    # TODO(xuanwn): Give credentials an actual type.
    def __init__(self, credentials: Any):
        self._credentials = credentials
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\_channel.py:257** — `# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.`
```
# TODO(xuanwn): Create a base class for IntegratedCall and SegregatedCall.
# pylint: disable=too-many-statements
def _consume_request_iterator(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\_observability.py:280** — `# TODO(xuanwn): use channel args to exclude those metrics.`
```
RPC.
    """
    # TODO(xuanwn): use channel args to exclude those metrics.
    for exclude_prefix in _SERVICES_TO_EXCLUDE:
        if exclude_prefix in state.method.encode("utf8"):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\_server.py:1182** — `# TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.`
```
self.registered_method_handlers = {}

        # TODO(https://github.com/grpc/grpc/issues/6597): eliminate these fields.
        self.rpc_states = set()
        self.due = set()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\aio\_channel.py:409** — `# TODO(lidiz) drop this hack after 3.8 deprecation`
```
# but not available until 3.9 or 3.8.3. So, we have to keep it
                # for a while.
                # TODO(lidiz) drop this hack after 3.8 deprecation
                if "frame" in str(attribute_error):
                    continue
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\aio\_server.py:87** — `# TODO(xuanwn): Implement this for AsyncIO.`
```
method_handlers: Dict[str, grpc.RpcMethodHandler],
    ) -> None:
        # TODO(xuanwn): Implement this for AsyncIO.
        pass
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\beta\_client_adaptations.py:85** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
class _InvocationProtocolContext(interfaces.GRPCInvocationContext):
    def disable_next_request_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\grpc\beta\_server_adaptations.py:43** — `pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.`
```
def disable_next_response_compression(self):
        pass  # TODO(https://github.com/grpc/grpc/issues/4078): design, implement.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\gunicorn\arbiter.py:365** — `# TODO: select.error is a subclass of OSError since Python 3.3.`
```
pass
        except OSError as e:
            # TODO: select.error is a subclass of OSError since Python 3.3.
            error_number = getattr(e, 'errno', e.args[0])
            if error_number not in [errno.EAGAIN, errno.EINTR]:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\gunicorn\config.py:2377** — `# FIXME: refactor all of this subclassing stdlib argparse`
```
def validate_header_map_behaviour(val):
    # FIXME: refactor all of this subclassing stdlib argparse

    if val is None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\gunicorn\__main__.py:9** — `# todo: let runpy.run_module take care of argv[0] rewriting`
```
if __name__ == "__main__":
    # see config.py - argparse defaults to basename(argv[0]) == "__main__.py"
    # todo: let runpy.run_module take care of argv[0] rewriting
    run(prog="gunicorn")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h11\_events.py:310** — `# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that`
```
# XX FIXME: "A recipient MUST ignore (or consider as an error) any fields that
# are forbidden to be sent in a trailer, since processing them as if they were
# present in the header section might bypass external security filters."
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h11\_readers.py:186** — `# XX FIXME: we discard chunk extensions. Does anyone care?`
```
chunk_header,
            )
            # XX FIXME: we discard chunk extensions. Does anyone care?
            self._bytes_in_chunk = int(matches["chunk_size"], base=16)
            if self._bytes_in_chunk == 0:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h11\_writers.py:54** — `# XX FIXME: could at least make an effort to pull out the status message`
```
# status code is mandatory.)
    #
    # XX FIXME: could at least make an effort to pull out the status message
    # from stdlib's http.HTTPStatus table. Or maybe just steal their enums
    # (either by import or copy/paste). We already accept them as status codes
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h2\connection.py:1808** — `# FIXME: Should we split this into one event per active stream?`
```
)

            # FIXME: Should we split this into one event per active stream?
            window_updated_event = WindowUpdated()
            window_updated_event.stream_id = 0
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h2\utilities.py:417** — `# TODO: We should also guard against receiving duplicate Host headers,`
```
# enforced by the _reject_pseudo_header_fields() pipeline.
    #
    # TODO: We should also guard against receiving duplicate Host headers,
    # and against sending duplicate headers.
    authority_header_val = None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\h2\windows.py:116** — `# TODO: Can the window be smaller than 1024 bytes? If not, we can`
```
small DATA frames.
        """
        # TODO: Can the window be smaller than 1024 bytes? If not, we can
        # streamline this algorithm.
        if not self._bytes_processed:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\hpack\hpack.py:321** — `# header table unconditionally. It is a future todo to`
```
else:
            # Indexed literal. We are going to add header to the
            # header table unconditionally. It is a future todo to
            # filter out headers which are known to be ineffective for
            # indexing since they just take space in the table and
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\httpx\_auth.py:267** — `# TODO: implement auth-int`
```
path = request.url.raw_path
        A2 = b":".join((request.method.encode(), path))
        # TODO: implement auth-int
        HA2 = digest(A2)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\itsdangerous\timed.py:182** — `# TODO: Signature is incompatible because parameters were added`
```
return t.cast("cabc.Iterator[TimestampSigner]", super().iter_unsigners(salt))

    # TODO: Signature is incompatible because parameters were added
    #  before salt.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\jinja2\ext.py:251** — `# TODO: the i18n extension is currently reevaluating values in a few`
```
tags = {"trans"}

    # TODO: the i18n extension is currently reevaluating values in a few
    # situations.  Take this example:
    #   {% trans count=something() %}{{ count }} foo{% pluralize
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\jinja2\nodes.py:212** — `todo = deque([self])`
```
targets and other nodes to a store context.
        """
        todo = deque([self])
        while todo:
            node = todo.popleft()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\conftest.py:105** — `# FIXME when yield tests are gone.`
```
pytest.exit("GIL re-enabled during tests", returncode=1)

# FIXME when yield tests are gone.
@pytest.hookimpl()
def pytest_itemcollected(item):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\__init__.py:927** — `# TODO: Remove the environment variable entirely now that it is "weak"`
```
_core.multiarray._multiarray_umath._reload_guard()

    # TODO: Remove the environment variable entirely now that it is "weak"
    if (os.environ.get("NPY_PROMOTION_STATE", "weak") != "weak"):
        warnings.warn(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\capi_maps.py:249** — `# TODO: support Fortran `len` function with optional kind parameter`
```
"""
    # TODO: support Fortran `len` function with optional kind parameter
    expr = re.sub(r'\blen\b', 'f2py_slen', expr)
    return expr
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\cfuncs.py:745** — `/* TODO: change the type of `len` so that we can remove this */`
```
}
    if (*len == -1) {
        /* TODO: change the type of `len` so that we can remove this */
        if (n > NPY_MAX_INT) {
            PyErr_SetString(PyExc_OverflowError,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\crackfortran.py:133** — `TODO:`
```
In addition, the following attributes are used: check,depend,note

TODO:
    * Apply 'parameter' attribute (e.g. 'integer parameter :: i=2' 'real x(i)'
                                   -> 'real x(2)')
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\f2py2e.py:461** — `# TODO: Remove all this when scaninputline is replaced`
```
pyf_files, _ = filter_files("", "[.]pyf([.]src|)", comline_list)
    # Checks that no existing modulename is defined in a pyf file
    # TODO: Remove all this when scaninputline is replaced
    if args.module_name:
        if "-h" in comline_list:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\symbolic.py:23** — `# TODO: support logical constants (Op.BOOLEAN)`
```
# contain C expressions that support here is implemented as well.
#
# TODO: support logical constants (Op.BOOLEAN)
# TODO: support logical operators (.AND., ...)
# TODO: support defined operators (.MYOP., ...)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\_isocbind.py:55** — `# TODO: See gh-25229`
```
}

# TODO: See gh-25229
isoc_c2pycode_map = {}
iso_c2py_map = {}
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\src\fortranobject.c:1371** — `// TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).`
```
sprintf(localbuf, "%s instance", Py_TYPE(obj)->tp_name);
  }
  // TODO: detect the size of buf and make sure that size(buf) >= size(localbuf).
  strcpy(buf, localbuf);
  return 1;
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\tests\test_docs.py:64** — `# TODO: implement test methods for other example Fortran codes`
```
np.array([1, 45, 3], dtype=np.float32))

    # TODO: implement test methods for other example Fortran codes
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\f2py\tests\test_f2py2e.py:415** — `# TODO: Clean up to prevent passing --overwrite-signature`
```
capslo = re.compile(r"Block: hi")
    # Case I: --lower is implied by -h
    # TODO: Clean up to prevent passing --overwrite-signature
    monkeypatch.setattr(
        sys,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\fft\__init__.py:203** — `# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should`
```
"""

# TODO: `numpy.fft.helper`` was deprecated in NumPy 2.0. It should
# be deleted once downstream libraries move to `numpy.fft`.
from . import _helper, _pocketfft, helper
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\mixins.py:166** — `# TODO: handle the optional third argument for __pow__?`
```
__rdivmod__ = _reflected_binary_method(um.divmod, 'divmod')
    # __idivmod__ does not exist
    # TODO: handle the optional third argument for __pow__?
    __pow__, __rpow__, __ipow__ = _numeric_methods(um.power, 'pow')
    __lshift__, __rlshift__, __ilshift__ = _numeric_methods(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\_datasource.py:71** — `# TODO: .zip support, .tar support?`
```
# deferring the import of lzma, bz2 and gzip until needed

# TODO: .zip support, .tar support?
class _FileOpeners:
    """
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\_function_base_impl.py:866** — `# TODO: This preserves the Python int, float, complex manually to get the`
```
raise ValueError("select with an empty condition list is not possible")

    # TODO: This preserves the Python int, float, complex manually to get the
    #       right `result_type` with NEP 50.  Most likely we will grow a better
    #       way to spell this (and this can be replaced).
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\_nanfunctions_impl.py:1689** — `# TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?`
```
See nanpercentile for parameter usage
    """
    # TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?
    arr1d, weights, overwrite_input = _remove_nan_1d(arr1d,
        second_arr1d=weights, overwrite_input=overwrite_input)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\_npyio_impl.py:249** — `# FIXME: This seems like it will copy strings around`
```
bytes.seek(0)
                if magic == format.MAGIC_PREFIX:
                    # FIXME: This seems like it will copy strings around
                    #   more than is strictly necessary.  The zipfile
                    #   will read the string and then
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\tests\test_function_base.py:3816** — `# TODO: Note that times have dubious rounding as of fixing NaTs!`
```
@pytest.mark.parametrize("pos", [0, 23, 10])
    def test_nat_basic(self, dtype, pos):
        # TODO: Note that times have dubious rounding as of fixing NaTs!
        # NaT and NaN should behave the same, do basic tests for NaT:
        a = np.arange(0, 24, dtype=dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\tests\test_io.py:340** — `sup.filter(ResourceWarning)  # TODO: specify exact message`
```
# collector, so we catch the warnings.
            with suppress_warnings() as sup:
                sup.filter(ResourceWarning)  # TODO: specify exact message
                for i in range(1, 1025):
                    try:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\tests\test_recfunctions.py:560** — `# Fixme, this test looks incomplete and broken`
```
z = self.data[-1]

        # Fixme, this test looks incomplete and broken
        #test = merge_arrays((z, np.array([10, 20, 30]).view([('C', int)])))
        #control = np.array([('A', 1., 10), ('B', 2., 20), ('-1', -1, 20)],
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\lib\tests\test_type_check.py:279** — `# Fixme, wrong place, isfinite now ufunc`
```
class TestIsfinite:
    # Fixme, wrong place, isfinite now ufunc

    def test_goodvalues(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\linalg\tests\test_linalg.py:1059** — `# FIXME the 'e' dtype might work in future`
```
noninv = array([[1, 0], [0, 0]])
    stacked = np.block([[[rshft_0]]] * 2)
    # FIXME the 'e' dtype might work in future
    dtnoinv = [object, np.dtype('e'), np.dtype('g'), np.dtype('G')]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\ma\core.py:237** — `# TODO: This is probably a mess, but should best preserve behavior?`
```
# for integer casts, this allows the use of 99999 as a fill value
        # for int8.
        # TODO: This is probably a mess, but should best preserve behavior?
        vals = tuple(
                np.array(_recursive_fill_value(dtype[name], f))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\ma\tests\test_core.py:5617** — `# TODO: Test masked_object, masked_equal, ...`
```
class TestMaskedWhereAliases:

    # TODO: Test masked_object, masked_equal, ...

    def test_masked_values(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\ma\tests\test_old_ma.py:720** — `# TODO FIXME: Find out what the following raises a warning in r8247`
```
def test_testScalarArithmetic(self):
        xm = array(0, mask=1)
        # TODO FIXME: Find out what the following raises a warning in r8247
        with np.errstate(divide='ignore'):
            assert_((1 / array(0)).mask)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\polynomial\chebyshev.py:798** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(chebmul, c1, c2)`
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\polynomial\polynomial.py:405** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = pu.as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    # note: this is more efficient than `pu._div(polymul, c1, c2)`
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\polynomial\polyutils.py:538** — `raise ZeroDivisionError  # FIXME: add message with details to exception`
```
[c1, c2] = as_series([c1, c2])
    if c2[-1] == 0:
        raise ZeroDivisionError  # FIXME: add message with details to exception

    lc1 = len(c1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\polynomial\_polybase.py:432** — `# TODO: we're stuck with disabling math formatting until we handle`
```
@staticmethod
    def _repr_latex_scalar(x, parens=False):
        # TODO: we're stuck with disabling math formatting until we handle
        # exponents in this function
        return fr'\text{{{pu.format_float(x, parens=parens)}}}'
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\random\tests\test_random.py:1069** — `# TODO: Include test for randint once it can broadcast`
```
np.random.seed(self.seed)

    # TODO: Include test for randint once it can broadcast
    # Can steal the test written in PR #6938
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\arrayprint.py:1567** — `# TODO: Custom repr for user DTypes, logic should likely move.`
```
"""
    if type(dtype).__repr__ != np.dtype.__repr__:
        # TODO: Custom repr for user DTypes, logic should likely move.
        return repr(dtype)
    if dtype.names is not None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\fromnumeric.py:44** — `# but this follows what was done before. TODO: revisit this.`
```
conv = _array_converter(obj)
    # As this already tried the method, subok is maybe quite reasonable here
    # but this follows what was done before. TODO: revisit this.
    arr, = conv.as_arrays(subok=False)
    result = getattr(arr, method)(*args, **kwds)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\getlimits.py:374** — `TODO: MachAr should be retired completely ideally.  We currently only`
```
""" Create MachAr instance with found information on float types

    TODO: MachAr should be retired completely ideally.  We currently only
          ever use it system with broken longdouble (valgrind, WSL).
    """
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\numeric.py:545** — `# TODO: this works around .astype(bool) not working properly (gh-9847)`
```
a = asanyarray(a)

    # TODO: this works around .astype(bool) not working properly (gh-9847)
    if np.issubdtype(a.dtype, np.character):
        a_bool = a != a.dtype.type()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\_add_newdocs.py:2276** — `assignment examples; TODO).`
```
Flattened version of the array as an iterator.  The iterator
        allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
        assignment examples; TODO).
    imag : ndarray
        Imaginary part of the array.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\_add_newdocs_scalars.py:129** — `# TODO: These docs probably need an if to highlight the default rather than`
```
""")

# TODO: These docs probably need an if to highlight the default rather than
#       the C-types (and be correct).
add_newdoc_for_scalar_type('int_', [],
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\_dtype.py:174** — `# TODO: this path can never be reached`
```
return native.byteorder
    if byteorder == 'S':
        # TODO: this path can never be reached
        return swapped.byteorder
    elif byteorder == '|':
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\_methods.py:88** — `# TODO: Optimize case when `where` is broadcast along a non-reduction`
```
items = nt.intp(items)
    else:
        # TODO: Optimize case when `where` is broadcast along a non-reduction
        # axis and full sum is more excessive than needed.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_array_coercion.py:452** — `# TODO: This discrepancy _should_ be resolved, either by relaxing the`
```
# case, and traditionally in most cases the behaviour is maintained
        # like this.  (`np.array(scalar, dtype="U6")` would have failed before)
        # TODO: This discrepancy _should_ be resolved, either by relaxing the
        #       cast, or by deprecating the first part.
        scalar = np.datetime64(val, unit)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_casting_unittests.py:781** — `# TODO: While this test is fairly thorough, right now, it does not`
```
def test_structured_view_offsets_parametric(
            self, from_dt, to_dt, expected_off):
        # TODO: While this test is fairly thorough, right now, it does not
        # really test some paths that may have nonzero offsets (they don't
        # really exists).
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_datetime.py:1585** — `# TODO: Allowing unsafe casting by`
```
# should raise between datetime and timedelta
        #
        # TODO: Allowing unsafe casting by
        #       default in ufuncs strikes again... :(
        a = np.array(3, dtype='m8[h]')
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_machar.py:19** — `# Fixme, this needs to raise a 'skip' exception.`
```
MachAr(lambda v: array(v, hiprec))
        except AttributeError:
            # Fixme, this needs to raise a 'skip' exception.
            "Skipping test: no ntypes.float96 available on this platform."
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_multiarray.py:6367** — `# FIXME:`
```
# stats for integer types
        # FIXME:
        # this needs definition as there are lots places along the line
        # where type casting may take place.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_scalarmath.py:103** — `# TODO: It would be nice to resolve this issue.`
```
# array**scalar special case can have different result dtype
        # (Other powers may have issues also, but are not hit here.)
        # TODO: It would be nice to resolve this issue.
        pytest.skip("array**2 can have incorrect/weird result dtype")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_stringdtype.py:1551** — `# TODO: generalize to more ufuncs`
```
# accept more than one string argument and produce a string should
    # behave this way
    # TODO: generalize to more ufuncs
    inp = ["hello", "world"]
    arr = np.array(inp, dtype=StringDType(na_object=None))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_umath.py:1152** — `# FIXME cinf not tested.`
```
one = np.array([1 + 0j])
        cnan = np.array([complex(np.nan, np.nan)])
        # FIXME cinf not tested.
        #cinf = np.array([complex(np.inf, 0)])
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_core\tests\test_umath_complex.py:17** — `# TODO: branch cuts (use Pauli code)`
```
)

# TODO: branch cuts (use Pauli code)
# TODO: conj 'symmetry'
# TODO: FPU exceptions
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_typing\_array_like.py:48** — `# TODO: Wait until mypy supports recursive objects in combination with typevars`
```
# TODO: Wait until mypy supports recursive objects in combination with typevars
_FiniteNestedSequence: TypeAlias = (
    _T
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_typing\_char_codes.py:211** — `# TODO: add `_StringCodes` once it has a scalar type`
```
_TD64Codes,
    _ObjectCodes,
    # TODO: add `_StringCodes` once it has a scalar type
    # _StringCodes,
]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\numpy\_typing\_dtype_like.py:31** — `_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types`
```
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True)

_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\_typing.py:386** — `# TODO(typing#684): add Ellipsis, see`
```
# PositionalIndexerTuple is extends the PositionalIndexer for 2D arrays
# These are used in various __getitem__ overloads
# TODO(typing#684): add Ellipsis, see
# https://github.com/python/typing/issues/684#issuecomment-548203158
# https://bugs.python.org/issue41810
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\api\typing\__init__.py:29** — `# TODO: Can't import Styler without importing jinja2`
```
)

# TODO: Can't import Styler without importing jinja2
# from pandas.io.formats.style import Styler
from pandas.io.json._json import JsonReader
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\algorithms.py:155** — `# e.g. Sparse[bool, False]  # TODO: no test cases get here`
```
return np.asarray(values).view("uint8")
        else:
            # e.g. Sparse[bool, False]  # TODO: no test cases get here
            return np.asarray(values).astype("uint8", copy=False)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\apply.py:922** — `# TODO: Avoid having to change state`
```
axis = self.axis

        # TODO: Avoid having to change state
        self.obj = self.obj if self.axis == 0 else self.obj.T
        self.axis = 0
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arraylike.py:361** — `# TODO: When we support multiple values in __finalize__, this`
```
result, **reconstruct_axes, **reconstruct_kwargs, copy=False
            )
        # TODO: When we support multiple values in __finalize__, this
        # should pass alignable to `__finalize__` instead of self.
        # Then `np.add(a, b)` would consider attrs from both a and b
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\base.py:227** — `# TODO: following GH#45287 can we now use .drop directly without`
```
# equivalent to `self.obj.drop(self.exclusions, axis=1)
            #  but this avoids consolidating and making a copy
            # TODO: following GH#45287 can we now use .drop directly without
            #  making a copy?
            return self.obj._drop_axis(self.exclusions, axis=1, only_slice=True)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\common.py:342** — `# TODO: used only once in indexing; belongs elsewhere?`
```
# TODO: used only once in indexing; belongs elsewhere?
def is_full_slice(obj, line: int) -> bool:
    """
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\config_init.py:426** — `# TODO(3.0): enforcing this deprecation will close GH#52501`
```
def use_inf_as_na_cb(key) -> None:
    # TODO(3.0): enforcing this deprecation will close GH#52501
    from pandas.core.dtypes.missing import _use_inf_as_na
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\construction.py:795** — `# TODO: test cases with arr.dtype.kind in "mM"`
```
elif dtype.kind == "U":
        # TODO: test cases with arr.dtype.kind in "mM"
        if is_ndarray:
            arr = cast(np.ndarray, arr)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\frame.py:896** — `# TODO(EA2D): special case not needed with 2D EAs`
```
# For data is a scalar extension dtype
            if isinstance(dtype, ExtensionDtype):
                # TODO(EA2D): special case not needed with 2D EAs

                values = [
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\generic.py:5587** — `# TODO: Decide if we care about having different examples for different`
```
See the :ref:`user guide <basics.reindexing>` for more.
        """
        # TODO: Decide if we care about having different examples for different
        # kinds
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexing.py:949** — `# FIXME: this assumes only one Ellipsis`
```
#  treat as a single null slice.
                i = tup.index(Ellipsis)
                # FIXME: this assumes only one Ellipsis
                new_key = tup[:i] + (_NS,) + tup[i + 1 :]
                return new_key
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\nanops.py:128** — `# TODO(GH-18976) update all the nanops methods to`
```
# Only applies for the default `min_count` of None
                # since that affects how empty arrays are handled.
                # TODO(GH-18976) update all the nanops methods to
                # correctly handle empty inputs and remove this check.
                # It *may* just be `var`
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\resample.py:448** — `# TODO: test_resample_apply_with_additional_args fails if we go`
```
try:
            if callable(how):
                # TODO: test_resample_apply_with_additional_args fails if we go
                #  through the non-lambda path, not clear that it should.
                func = lambda x: how(x, *args, **kwargs)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\series.py:2271** — `# TODO: integrate bottleneck`
```
# Statistics, overridden ndarray methods

    # TODO: integrate bottleneck
    def count(self) -> int:
        """
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\base.py:2170** — `# TODO(3.0): this can be removed once GH#33302 deprecation is enforced`
```
return result

    # TODO(3.0): this can be removed once GH#33302 deprecation is enforced
    def _fill_mask_inplace(
        self, method: str, limit: int | None, mask: npt.NDArray[np.bool_]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\categorical.py:2147** — `# TODO: GH#15362`
```
# max(np.uint64) as the missing value indicator
        #
        # TODO: GH#15362

        mask = self.isna()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\datetimelike.py:350** — `# TODO: Remove Datetime & DatetimeTZ formatters.`
```
def _formatter(self, boxed: bool = False):
        # TODO: Remove Datetime & DatetimeTZ formatters.
        return "'{}'".format
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\datetimes.py:286** — `# TODO: require any NAs be valid-for-DTA`
```
def _from_scalars(cls, scalars, *, dtype: DtypeObj) -> Self:
        if lib.infer_dtype(scalars, skipna=True) not in ["datetime", "datetime64"]:
            # TODO: require any NAs be valid-for-DTA
            # TODO: if dtype is passed, check for tzawareness compat?
            raise ValueError
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\interval.py:858** — `# TODO: in an IntervalIndex we can reuse the cached`
```
if ascending and kind == "quicksort" and na_position == "last":
            # TODO: in an IntervalIndex we can reuse the cached
            #  IntervalTree.left_sorter
            return np.lexsort((self.right, self.left))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\masked.py:290** — `# TODO: get this all from np_can_hold_element?`
```
"""
        kind = self.dtype.kind
        # TODO: get this all from np_can_hold_element?
        if kind == "b":
            if lib.is_bool(value):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\numeric.py:93** — `# TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed`
```
if isinstance(array, pyarrow.ChunkedArray):
            # TODO this "if" can be removed when requiring pyarrow >= 10.0, which fixed
            # combine_chunks for empty arrays https://github.com/apache/arrow/pull/13757
            if array.num_chunks == 0:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\numpy_.py:301** — `# TODO: assert we have floating dtype?`
```
out_data = self._ndarray.copy()

        # TODO: assert we have floating dtype?
        missing.interpolate_2d_inplace(
            out_data,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\period.py:702** — `# TODO: other cases?`
```
elif diff == 1:
                    dta._freq = self.freq.base
                # TODO: other cases?
            return dta
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\string_.py:198** — `# TODO add more informative repr`
```
return f"{self.name}[{self.storage}]"
        else:
            # TODO add more informative repr
            return self.name
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\string_arrow.py:74** — `# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from`
```
# TODO: Inherit directly from BaseStringArrayMethods. Currently we inherit from
# ObjectStringArrayMixin because we want to have the object-dtype based methods as
# fallback for the ones that pyarrow doesn't yet support
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\_mixins.py:363** — `# TODO: NumpyExtensionArray didn't used to copy, need tests`
```
npvalues = npvalues.T

                # TODO: NumpyExtensionArray didn't used to copy, need tests
                #  for this
                new_values = self._from_backing_data(npvalues)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\arrow\accessors.py:151** — `# TODO: Support negative key but pyarrow does not allow`
```
if isinstance(key, int):
            # TODO: Support negative key but pyarrow does not allow
            # element index to be an array.
            # if key < 0:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\arrow\array.py:133** — `# TODO: Replace with pyarrow floordiv kernel.`
```
right: pa.ChunkedArray | pa.Array | pa.Scalar,
    ) -> pa.ChunkedArray:
        # TODO: Replace with pyarrow floordiv kernel.
        # https://github.com/apache/arrow/issues/39386
        if pa.types.is_integer(left.type) and pa.types.is_integer(right.type):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\arrays\sparse\array.py:384** — `# TODO: make kind=None, and use data.kind?`
```
if dtype is None:
                dtype = data.dtype
            # TODO: make kind=None, and use data.kind?
            data = data.sp_values
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\array_algos\putmask.py:78** — `# TODO: this prob needs some better checking for 2D cases`
```
new = new.astype(values.dtype, copy=False)

    # TODO: this prob needs some better checking for 2D cases
    nlocs = mask.sum()
    if nlocs > 0 and is_list_like(new) and getattr(new, "ndim", 1) == 1:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\array_algos\replace.py:85** — `# TODO: should use missing.mask_missing?`
```
if not regex or not should_use_regex(regex, b):
        # TODO: should use missing.mask_missing?
        op = lambda x: operator.eq(x, b)
    else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\array_algos\take.py:361** — `# FIXME: if we get here with dt64/td64 we need to be sure we have`
```
out = out.view(out_dtype)
        if fill_wrap is not None:
            # FIXME: if we get here with dt64/td64 we need to be sure we have
            #  matching resos
            if fill_value.dtype.kind == "m":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\computation\eval.py:66** — `# TODO: validate this in a more general way (thinking of future engines`
```
)

    # TODO: validate this in a more general way (thinking of future engines
    # that won't necessarily be import-able)
    # Could potentially be done on engine instantiation
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\computation\expr.py:547** — `# TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min`
```
return self.term_type(node.id, self.env, **kwargs)

    # TODO(py314): deprecated since Python 3.8. Remove after Python 3.14 is min
    def visit_NameConstant(self, node, **kwargs) -> Term:
        return self.const_type(node.value, self.env)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\computation\pytables.py:441** — `# TODO: return None might never be reached`
```
elif isinstance(node.op, ast.UAdd):
            raise NotImplementedError("Unary addition not supported")
        # TODO: return None might never be reached
        return None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\dtypes\cast.py:286** — `# TODO: complex?  what if result is already non-object?`
```
else:
                # TODO: complex?  what if result is already non-object?
                dtype = "object"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\dtypes\common.py:1519** — `# TODO: Implement this properly`
```
pass
        if hasattr(dtype, "numpy_dtype"):
            # TODO: Implement this properly
            # https://github.com/pandas-dev/pandas/issues/52576
            return dtype.numpy_dtype.type
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\dtypes\dtypes.py:209** — `# TODO: Document public vs. private API`
```
"""

    # TODO: Document public vs. private API
    name = "category"
    type: type[CategoricalDtypeType] = CategoricalDtypeType
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\dtypes\missing.py:520** — `# TODO: fastpath for pandas' StringDtype`
```
return _array_equivalent_datetimelike(left, right)
        elif is_string_or_object_np_dtype(left.dtype):
            # TODO: fastpath for pandas' StringDtype
            return _array_equivalent_object(left, right, strict_nan)
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\groupby\generic.py:116** — `# TODO(typing) the return value on this callable should be any *scalar*.`
```
from pandas.core.generic import NDFrame

# TODO(typing) the return value on this callable should be any *scalar*.
AggScalar = Union[str, Callable[..., Any]]
# TODO: validate types on ScalarResult and move to _typing
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\groupby\groupby.py:792** — `# TODO: Better repr for GroupBy object`
```
@final
    def __repr__(self) -> str:
        # TODO: Better repr for GroupBy object
        return object.__repr__(self)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\groupby\grouper.py:358** — `# TODO: What are we assuming about subsequent calls?`
```
# Keep self._grouper value before overriding
        if self._grouper is None:
            # TODO: What are we assuming about subsequent calls?
            self._grouper = gpr_index
            self._indexer = self._indexer_deprecated
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\groupby\ops.py:468** — `# TODO: min_count`
```
raise NotImplementedError(f"{self.how} is not implemented")
        else:
            # TODO: min_count
            if self.how != "rank":
                # TODO: should rank take result_mask?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\api.py:145** — `# TODO: handle index names!`
```
Index
    """
    # TODO: handle index names!
    indexes = _get_distinct_objs(indexes)
    if len(indexes) == 0:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\base.py:1465** — `# TODO: why do we need different justify for these cases?`
```
or isinstance(self.dtype, (IntervalDtype, CategoricalDtype))
        ):
            # TODO: why do we need different justify for these cases?
            justify = "all"
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\datetimelike.py:230** — `# TODO: not reached in tests 2023-10-11`
```
self, *, header: list[str], na_rep: str, date_format: str | None = None
    ) -> list[str]:
        # TODO: not reached in tests 2023-10-11
        # matches base class except for whitespace padding and date_format
        return header + list(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\datetimes.py:98** — `# TODO: If we knew what was going in to **d, we might be able to`
```
else:
        with warnings.catch_warnings():
            # TODO: If we knew what was going in to **d, we might be able to
            #  go through _simple_new instead
            warnings.simplefilter("ignore")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\frozen.py:70** — `# TODO: Consider deprecating these in favor of `union` (xref gh-15506)`
```
return type(self)(temp)

    # TODO: Consider deprecating these in favor of `union` (xref gh-15506)
    # error: Incompatible types in assignment (expression has type
    # "Callable[[FrozenList, Any], FrozenList]", base class "list" defined the
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\interval.py:685** — `# TODO: DO this in maybe_booleans_to_slice?`
```
res = lib.maybe_booleans_to_slice(mask.view("u1"))
        if isinstance(res, slice) and res.stop is None:
            # TODO: DO this in maybe_booleans_to_slice?
            res = slice(res.start, len(self), res.step)
        return res
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\multi.py:2996** — `# TODO: need is_valid_na_for_dtype(key, level_index.dtype)`
```
"""
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\period.py:302** — `# TODO: We can do some of these with no-copy / coercion?`
```
if freq and isinstance(data, cls) and data.freq != freq:
                # TODO: We can do some of these with no-copy / coercion?
                # e.g. D -> 2D seems to be OK
                data = data.asfreq(freq)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\indexes\range.py:1108** — `# TODO: if other is a RangeIndex we may have more efficient options`
```
step = op

        # TODO: if other is a RangeIndex we may have more efficient options
        right = extract_array(other, extract_numpy=True, extract_range=True)
        left = self
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\interchange\column.py:115** — `# TODO: chunks are implemented now, probably this should return something`
```
Offset of first element. Always zero.
        """
        # TODO: chunks are implemented now, probably this should return something
        return 0
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\interchange\dataframe_protocol.py:407** — `# TODO: not happy with Optional, but need to flag it may be expensive`
```
@abstractmethod
    def num_rows(self) -> int | None:
        # TODO: not happy with Optional, but need to flag it may be expensive
        #       why include it if it may be None - what do we expect consumers
        #       to do here?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\interchange\from_dataframe.py:470** — `# TODO: No DLPack yet, so need to construct a new ndarray from the data pointer`
```
raise NotImplementedError(f"Conversion for {dtype} is not yet supported.")

    # TODO: No DLPack yet, so need to construct a new ndarray from the data pointer
    # and size in the buffer plus the dtype on the column. Use DLPack as NumPy supports
    # it since https://github.com/numpy/numpy/pull/19083
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\interchange\utils.py:139** — `# TODO(infer_string) this should be LARGE_STRING for pyarrow storage,`
```
if isinstance(dtype, pd.StringDtype):
        # TODO(infer_string) this should be LARGE_STRING for pyarrow storage,
        # but current tests don't cover this distinction
        return ArrowCTypes.STRING
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\array_manager.py:366** — `# TODO what is this used for?`
```
def is_view(self) -> bool:
        """return a boolean if we are a single block and are a view"""
        # TODO what is this used for?
        return False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\base.py:66** — `# TODO share more methods/attributes`
```
class DataManager(PandasObject):
    # TODO share more methods/attributes

    axes: list[Index]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\blocks.py:420** — `# TODO(EA2D): unnecessary with 2D EAs`
```
# See also: split_and_operate
        if result.ndim > 1 and isinstance(result.dtype, ExtensionDtype):
            # TODO(EA2D): unnecessary with 2D EAs
            # if we get a 2D ExtensionArray, we need to split it into 1D pieces
            nbs = []
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\concat.py:114** — `# TODO(ArrayManager) this assumes that all managers are of the same type`
```
needs_copy = copy and concat_axis == 0

    # TODO(ArrayManager) this assumes that all managers are of the same type
    if isinstance(mgrs_indexers[0][0], ArrayManager):
        mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\construction.py:397** — `# TODO: check len(values) == 0?`
```
if len(columns) == 0:
        # TODO: check len(values) == 0?
        block_values = []
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\managers.py:536** — `# FIXME: optimization potential`
```
return self.make_empty()

        # FIXME: optimization potential
        indexer = np.sort(np.concatenate([b.mgr_locs.as_array for b in blocks]))
        inv_indexer = lib.get_reverse_indexer(indexer, self.shape[0])
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\internals\ops.py:120** — `# TODO(EA2D): with 2D EAs only this first clause would be needed`
```
assert rblk.mgr_locs.is_slice_like, rblk.mgr_locs

    # TODO(EA2D): with 2D EAs only this first clause would be needed
    if not (left_ea or right_ea):
        # error: No overload variant of "__getitem__" of "ExtensionArray" matches
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\ops\array_ops.py:234** — `# TODO: can remove this after dropping some future numpy version?`
```
# numpy returned a scalar instead of operating element-wise
        # e.g. numeric array vs str
        # TODO: can remove this after dropping some future numpy version?
        return invalid_comparison(left, right, op)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\concat.py:534** — `# TODO: retain levels?`
```
if isinstance(keys, MultiIndex):
                # TODO: retain levels?
                keys = type(keys).from_tuples(clean_keys, names=keys.names)
            else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\melt.py:477** — `# TODO: anything else to catch?`
```
newdf[j] = to_numeric(newdf[j])
        except (TypeError, ValueError, OverflowError):
            # TODO: anything else to catch?
            pass
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\merge.py:285** — `# TODO, should merge_pieces do this?`
```
# make sure join keys are in the merged
        # TODO, should merge_pieces do this?
        merged[by] = key
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\pivot.py:60** — `# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency`
```
# Note: We need to make sure `frame` is imported before `pivot`, otherwise
# _shared_docs['pivot_table'] will not yet exist.  TODO: Fix this dependency
@Substitution("\ndata : DataFrame")
@Appender(_shared_docs["pivot_table"], indents=1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\reshape.py:229** — `# TODO: in all tests we have mask.any(0).all(); can we rely on that?`
```
new_values, mask = self.get_new_values(dummy_arr, fill_value=-1)
        return new_values, mask.any(0)
        # TODO: in all tests we have mask.any(0).all(); can we rely on that?

    def get_result(self, values, value_columns, fill_value) -> DataFrame:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\reshape\tile.py:503** — `# TODO: handle mismatch between categorical label order and pandas.cut order.`
```
ordered=ordered,
            )
        # TODO: handle mismatch between categorical label order and pandas.cut order.
        np.putmask(ids, na_mask, 0)
        result = algos.take_nd(labels, ids - 1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\strings\accessor.py:186** — `# TODO: Dispatch all the methods`
```
# Note: see the docstring in pandas.core.strings.__init__
    # for an explanation of the implementation.
    # TODO: Dispatch all the methods
    # Currently the following are not dispatched to the array
    # * cat
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\strings\object_array.py:92** — `# FIXME: this should be totally avoidable`
```
if len(err.args) >= 1 and re.search(p_err, err.args[0]):
                # FIXME: this should be totally avoidable
                raise err
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\tools\datetimes.py:370** — `# TODO: Combine with above if DTI/DTA supports Arrow timestamps`
```
elif isinstance(arg_dtype, ArrowDtype) and arg_dtype.type is Timestamp:
        # TODO: Combine with above if DTI/DTA supports Arrow timestamps
        if utc:
            # pyarrow uses UTC, not lowercase utc
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\window\rolling.py:391** — `# TODO: sure we want to overwrite results?`
```
extra_col = Series(self._on, index=self.obj.index, name=name, copy=False)
            if name in result.columns:
                # TODO: sure we want to overwrite results?
                result[name] = extra_col
            elif name in result.index.names:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\_numba\executor.py:125** — `# TODO: Preserve complex dtypes`
```
# TODO: Preserve complex dtypes

float_dtype_mapping: dict[np.dtype, Any] = {
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\core\_numba\extensions.py:66** — `# TODO: Range index support`
```
# TODO: Range index support
# (this currently lowers OK, but does not round-trip)
class IndexType(types.Type):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\common.py:373** — `# TODO: fsspec can also handle HTTP via requests, but leaving this`
```
if isinstance(filepath_or_buffer, str) and is_url(filepath_or_buffer):
        # TODO: fsspec can also handle HTTP via requests, but leaving this
        # unchanged. using fsspec appears to break the ability to infer if the
        # server responded with gzipped data
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\pytables.py:1222** — `#  _table_mod.NoSuchNodeError.  TODO: Catch only these?`
```
except Exception as err:
            # In tests we get here with ClosedFileError, TypeError, and
            #  _table_mod.NoSuchNodeError.  TODO: Catch only these?

            if where is not None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\sql.py:120** — `# TODO: not reached 2023-10-27; needed?`
```
return to_datetime(col, **format)
            except (TypeError, ValueError):
                # TODO: not reached 2023-10-27; needed?
                return col
        return to_datetime(col, errors=error, **format)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\stata.py:339** — `# TODO(non-nano): If/when pandas supports more than datetime64[ns], this`
```
return base + deltas

    # TODO(non-nano): If/when pandas supports more than datetime64[ns], this
    #  should be improved to use correct range, e.g. datetime[Y] for yearly
    bad_locs = np.isnan(dates)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\clipboard\__init__.py:274** — `# TODO: https://github.com/asweigart/pyperclip/issues/43`
```
# Workaround for https://bugs.kde.org/show_bug.cgi?id=342874
        # TODO: https://github.com/asweigart/pyperclip/issues/43
        clipboardContents = stdout.decode(ENCODING)
        # even if blank, Klipper will append a newline at the end
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\excel\_pyxlsb.py:63** — `# TODO: hack in buffer capability`
```
from pyxlsb import open_workbook

        # TODO: hack in buffer capability
        # This might need some modifications to the Pyxlsb library
        # Actual work for opening it is in xlsbpackage.py, line 20-ish
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\excel\_xlsxwriter.py:134** — `# TODO: support other fill patterns`
```
if isinstance(props.get("pattern"), str):
            # TODO: support other fill patterns
            props["pattern"] = 0 if props["pattern"] == "none" else 1
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\formats\css.py:106** — `# TODO: Can we use current color as initial value to comply with CSS standards?`
```
)

        # TODO: Can we use current color as initial value to comply with CSS standards?
        border_declarations = {
            f"border{side}-color": "black",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\formats\excel.py:238** — `# TODO: handle cell width and height: needs support in pandas.io.excel`
```
}

        # TODO: handle cell width and height: needs support in pandas.io.excel

        def remove_none(d: dict[str, str | None]) -> None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\formats\format.py:1227** — `# TODO(3.0): this will be unreachable when use_inf_as_na`
```
return str(NA)
                elif lib.is_float(x) and np.isinf(x):
                    # TODO(3.0): this will be unreachable when use_inf_as_na
                    #  deprecation is enforced
                    return str(x)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\formats\html.py:337** — `# TODO: Refactor to remove code duplication with code`
```
# MultiIndex Columns and Index.
                # Initially fill row with blank cells before column names.
                # TODO: Refactor to remove code duplication with code
                # block below for standard columns index.
                row = [""] * (self.row_levels - 1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\formats\style_render.py:878** — `# TODO try to consolidate the concat visible rows`
```
row_indices: list[int] = []
            _concatenated_visible_rows(obj, 0, row_indices)
            # TODO try to consolidate the concat visible rows
            # methods to a single function / recursion for simplicity
            return row_indices
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\json\_json.py:374** — `# TODO: Do this timedelta properly in objToJSON.c See GH #15137`
```
)

        # TODO: Do this timedelta properly in objToJSON.c See GH #15137
        if (
            (obj.ndim == 1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\json\_normalize.py:466** — `# TODO: handle record value which are lists, at least error`
```
#  {VeryLong: { b: 1,c:2}} -> {VeryLong.b:1 ,VeryLong.c:@}
            #
            # TODO: handle record value which are lists, at least error
            #       reasonably
            data = nested_to_record(data, sep=sep, max_level=max_level)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\parsers\base_parser.py:813** — `# TODO: this is for consistency with`
```
if not is_object_dtype(values.dtype) and not known_cats:
                # TODO: this is for consistency with
                # c-parser which parses all categories
                # as strings
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\parsers\python_parser.py:461** — `# TODO: Use pandas.io.common.dedup_names instead (see #50371)`
```
] + this_unnamed_cols

                    # TODO: Use pandas.io.common.dedup_names instead (see #50371)
                    for i in col_loop_order:
                        col = this_columns[i]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\io\parsers\readers.py:1654** — `# TODO: Refactor this logic, its pretty convoluted`
```
if engine != "c" and value != default:
                    # TODO: Refactor this logic, its pretty convoluted
                    if "python" in engine and argname not in _python_unsupported:
                        pass
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\plotting\_matplotlib\converter.py:823** — `# TODO: Check the following : is it really info['fmt'] ?`
```
quarter_start = (dates_ % 3 == 0).nonzero()
        info_maj[year_start] = True
        # TODO: Check the following : is it really info['fmt'] ?
        #  2023-09-15 this is reached in test_finder_monthly
        info["fmt"][quarter_start] = True
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\plotting\_matplotlib\core.py:182** — `# TODO: Might deprecate `column` argument in future PR (#28373)`
```
# Assign the rest of columns into self.columns if by is explicitly defined
        # while column is not, only need `columns` in hist/box plot when it's DF
        # TODO: Might deprecate `column` argument in future PR (#28373)
        if isinstance(data, DataFrame):
            if column:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\plotting\_matplotlib\misc.py:300** — `# TODO: is the failure mentioned below still relevant?`
```
import matplotlib.pyplot as plt

    # TODO: is the failure mentioned below still relevant?
    # random.sample(ndarray, int) fails on python 3.3, sigh
    data = list(series.values)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\plotting\_matplotlib\timeseries.py:1** — `# TODO: Use the fact that axis can have units to simplify the process`
```
# TODO: Use the fact that axis can have units to simplify the process

from __future__ import annotations
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\test_algos.py:68** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
tm.assert_numpy_array_equal(uniques, expected_uniques)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("sort", [True, False])
    def test_factorize(self, index_or_series_obj, sort):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\test_downstream.py:310** — `# TODO: could check with arraylike of Period objects`
```
# Note: we dont do this for PeriodArray bc _from_sequence won't accept
    #  an array of integers
    # TODO: could check with arraylike of Period objects
    arr, data = array_likes
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\test_multilevel.py:161** — `# TODO groupby with level_values drops names`
```
expected = ymd.groupby([k1, k2]).mean()

        # TODO groupby with level_values drops names
        tm.assert_frame_equal(result, expected, check_names=False)
        assert result.index.names == ymd.index.names[:2]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\apply\test_frame_apply.py:1709** — `# TODO: the result below is wrong, should be fixed (GH53325)`
```
tm.assert_frame_equal(result, expected)

    # TODO: the result below is wrong, should be fixed (GH53325)
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = df.agg({"x": foo1}, 0, 3, c=4)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arithmetic\test_datetime64.py:161** — `# TODO: moved from tests.series.test_operators; needs cleanup`
```
class TestDatetime64SeriesComparison:
    # TODO: moved from tests.series.test_operators; needs cleanup

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arithmetic\test_numeric.py:50** — `# TODO: add more  dtypes here`
```
@pytest.fixture(
    params=[
        # TODO: add more  dtypes here
        Index(np.arange(5, dtype="float64")),
        Index(np.arange(5, dtype="int64")),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arithmetic\test_object.py:96** — `# TODO: parametrize`
```
tm.assert_index_equal(result, expected)

    # TODO: parametrize
    def test_pow_ops_object(self):
        # GH#22922
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arithmetic\test_period.py:208** — `# TODO: parameterize over boxes`
```
class TestPeriodIndexComparisons:
    # TODO: parameterize over boxes

    def test_pi_cmp_period(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arithmetic\test_timedelta64.py:171** — `# TODO: All of these need to be parametrized over box`
```
class TestTimedelta64ArrayComparisons:
    # TODO: All of these need to be parametrized over box

    @pytest.mark.parametrize("dtype", [None, object])
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\test_datetimelike.py:33** — `# TODO: more freq variants`
```
# TODO: more freq variants
@pytest.fixture(params=["D", "B", "W", "ME", "QE", "YE"])
def freqstr(request):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\test_datetimes.py:93** — `# TODO: simplify once we can just .astype to other unit`
```
assert not dta.is_normalized

        # TODO: simplify once we can just .astype to other unit
        exp = np.asarray(dti.normalize()).astype(f"M8[{unit}]")
        expected = DatetimeArray._simple_new(exp, dtype=exp.dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\test_timedeltas.py:106** — `# TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert`
```
assert result.isna().all()

    # TODO: 2022-07-11 this is the only test that gets to DTA.tz_convert
    #  or tz_localize with non-nano; implement tests specific to that.
    def test_add_datetimelike_scalar(self, tda, tz_naive_fixture):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\boolean\test_arithmetic.py:122** — `# TODO(extension) numpy's mul with object array sees booleans as numbers`
```
# invalid array-likes
    if op not in ("__mul__", "__rmul__"):
        # TODO(extension) numpy's mul with object array sees booleans as numbers
        msg = "|".join(
            [
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\boolean\test_construction.py:155** — `# TODO this is currently not public API`
```
def test_coerce_to_array():
    # TODO this is currently not public API
    values = np.array([True, False, True, False], dtype="bool")
    mask = np.array([False, False, False, True], dtype="bool")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\boolean\test_logical.py:123** — `# TODO: test True & False`
```
)
    def test_kleene_or_scalar(self, other, expected):
        # TODO: test True & False
        a = pd.array([True, False, None], dtype="boolean")
        result = a | other
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\categorical\test_analytics.py:47** — `# TODO: raises if we pass axis=0  (on Index and Categorical, not Series)`
```
assert np.minimum.reduce(obj) == "a"
        assert np.maximum.reduce(obj) == "d"
        # TODO: raises if we pass axis=0  (on Index and Categorical, not Series)

        cat = Categorical(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\categorical\test_indexing.py:374** — `# TODO(Categorical): identify other places where this may be`
```
"""

    # TODO(Categorical): identify other places where this may be
    # useful and move to a conftest.py
    def array(self, dtype=None):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\floating\test_arithmetic.py:39** — `# TODO pending NA/NaN discussion`
```
@pytest.mark.parametrize("zero, negative", [(0, False), (0.0, False), (-0.0, True)])
def test_divide_by_zero(dtype, zero, negative):
    # TODO pending NA/NaN discussion
    # https://github.com/pandas-dev/pandas/issues/32265/
    a = pd.array([0, 1, -1, None], dtype=dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\floating\test_construction.py:172** — `# TODO can we specify "floating" in general?`
```
# for integer dtypes, the itemsize is not preserved
    # TODO can we specify "floating" in general?
    result = pd.array(np.array([1, 2], dtype="int32"), dtype="Float64")
    assert result.dtype == Float64Dtype()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\integer\test_arithmetic.py:196** — `# TODO: doing this fillna to keep tests passing as we make`
```
expected = pd.Series(["foo" * x for x in data], index=s.index)
        expected = expected.fillna(np.nan)
        # TODO: doing this fillna to keep tests passing as we make
        #  assert_almost_equal stricter, but the expected with pd.NA seems
        #  more-correct than np.nan here.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\integer\test_function.py:199** — `# TODO(jreback) - these need testing / are broken`
```
# TODO(jreback) - these need testing / are broken

# shift
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\interval\test_overlaps.py:62** — `# TODO: modify this test when implemented`
```
@pytest.mark.parametrize("other_constructor", [IntervalArray, IntervalIndex])
    def test_overlaps_interval_container(self, constructor, other_constructor):
        # TODO: modify this test when implemented
        interval_container = constructor.from_breaks(range(5))
        other_container = other_constructor.from_breaks(range(5))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\masked\test_arithmetic.py:57** — `# TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))`
```
scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)

    # TODO also add len-1 array (np.array([scalar], dtype=data.dtype.numpy_dtype))
    for scalar in [scalar, data.dtype.type(scalar)]:
        if is_bool_not_implemented(data, all_arithmetic_operators):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\masked\test_indexing.py:22** — `# FIXME: don't leave commented-out`
```
arr[[0]] = invalid

        # FIXME: don't leave commented-out
        # with pytest.raises(TypeError):
        #    arr[[0]] = [invalid]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\sparse\test_constructors.py:106** — `# TODO: actionable?`
```
def test_constructor_spindex_dtype(self):
        arr = SparseArray(data=[1, 2], sparse_index=IntIndex(4, [1, 2]))
        # TODO: actionable?
        # XXX: Behavior change: specifying SparseIndex no longer changes the
        # fill_value
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\sparse\test_indexing.py:208** — `# TODO: actionable?`
```
tm.assert_sp_array_equal(result, expected)

        # TODO: actionable?
        # XXX: test change: fill_value=True -> allow_fill=True
        result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\arrays\sparse\test_reductions.py:265** — `# TODO: pin down whether we wrap datetime64("NaT")`
```
result = getattr(arr, func)()
        if expected is NaT:
            # TODO: pin down whether we wrap datetime64("NaT")
            assert result is NaT or np.isnat(result)
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\base\test_misc.py:155** — `# TODO: Should Series cases also raise? Looks like they use numpy`
```
)
    elif obj.dtype.kind == "c" and isinstance(obj, Index):
        # TODO: Should Series cases also raise? Looks like they use numpy
        #  comparison semantics https://github.com/numpy/numpy/issues/15981
        mark = pytest.mark.xfail(reason="complex objects are not comparable")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\base\test_value_counts.py:50** — `# TODO(GH#32514): Order of entries with the same count is inconsistent`
```
expected = expected.astype("Int64")

    # TODO(GH#32514): Order of entries with the same count is inconsistent
    #  on CI (gh-32449)
    if obj.duplicated().any():
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\computation\test_eval.py:98** — `# TODO: using range(5) here is a kludge`
```
# TODO: using range(5) here is a kludge
@pytest.fixture(
    params=list(range(5)),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_astype.py:137** — `# TODO(infer_string) this test can be removed after 3.0 (once str is the default)`
```
def test_astype_str_copy_on_pickle_roundrip():
    # TODO(infer_string) this test can be removed after 3.0 (once str is the default)
    # https://github.com/pandas-dev/pandas/issues/54654
    # ensure_string_array may alter array inplace
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_chained_assignment_deprecation.py:74** — `# TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+`
```
df = df_orig.copy()
    df["a"]  # populate the item_cache
    # TODO(CoW-warn) because of the usage of *args, this doesn't warn on Py3.11+
    if using_copy_on_write:
        with tm.raises_chained_assignment_error(not PY311):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_core_functionalities.py:54** — `# TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100``
```
arr = get_array(df, "a")
    view = None  # noqa: F841
    # TODO(CoW-warn) false positive? -> block gets split because of `df["b"] = 100`
    # which introduces additional refs, even when those of `view` go out of scopes
    with tm.assert_cow_warning(warn_copy_on_write):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_indexing.py:816** — `# TODO add more tests modifying the parent`
```
# TODO add more tests modifying the parent
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_methods.py:148** — `# TODO copy=False without CoW still returns a copy in this case`
```
if request.node.callspec.id.startswith("reindex-"):
        # TODO copy=False without CoW still returns a copy in this case
        if not using_copy_on_write and not using_array_manager and copy is False:
            share_memory = False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\copy_view\test_replace.py:21** — `# TODO: Add these in a further optimization`
```
{"to_replace": {"b": 4}, "value": -1},
        {"to_replace": {"b": {4: 1}}},
        # TODO: Add these in a further optimization
        # We would need to see which columns got replaced in the mask
        # which could be expensive
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\dtypes\cast\test_downcast.py:46** — `# TODO: similar for dt64, dt64tz, Period, Interval?`
```
np.array([1, 2], dtype="m8[D]").astype("m8[ns]"),
        ),
        # TODO: similar for dt64, dt64tz, Period, Interval?
    ],
)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\conftest.py:126** — `TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)`
```
The scalar missing value for this type. Default dtype.na_value.

    TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)
    """
    return dtype.na_value
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_arrow.py:77** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_categorical.py:80** — `# TODO: Is this deliberate?`
```
@pytest.mark.xfail(reason="Memory usage doesn't match")
    def test_memory_usage(self, data):
        # TODO: Is this deliberate?
        super().test_memory_usage(data)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_interval.py:119** — `# TODO: either belongs in tests.arrays.interval or move into base tests.`
```
# TODO: either belongs in tests.arrays.interval or move into base tests.
def test_fillna_non_scalar_raises(data_missing):
    msg = "can only insert Interval objects and NA into an IntervalArray"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_masked.py:267** — `# TODO: patching self is a bad pattern here`
```
def test_combine_le(self, data_repeated):
        # TODO: patching self is a bad pattern here
        orig_data1, orig_data2 = data_repeated(2)
        if orig_data1.dtype.kind == "b":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_numpy.py:219** — `# TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which`
```
@skip_nested
    def test_searchsorted(self, data_for_sorting, as_series):
        # TODO: NumpyExtensionArray.searchsorted calls ndarray.searchsorted which
        #  isn't quite what we want in nested data cases. Instead we need to
        #  adapt something like libindex._bin_search.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_sparse.py:254** — `# TODO: this fails bc we do not pass through data_missing. If we did,`
```
def test_fillna_series(self, data_missing):
        # this one looks doable.
        # TODO: this fails bc we do not pass through data_missing. If we did,
        #  the 0-fill case would xpass
        super().test_fillna_series()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\test_string.py:247** — `# TODO(infer_string)`
```
and (HAS_PYARROW or dtype.storage == "pyarrow")
        ):
            # TODO(infer_string)
            mark = pytest.mark.xfail(
                reason="The pointwise operation result will be inferred to "
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\accumulate.py:39** — `# TODO: require TypeError for things that will _never_ work?`
```
else:
            with pytest.raises((NotImplementedError, TypeError)):
                # TODO: require TypeError for things that will _never_ work?
                getattr(ser, op_name)(skipna=skipna)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\dim2.py:31** — `# TODO: is there a less hacky way of checking this?`
```
test_func = node._obj
            if test_func.__qualname__.startswith("Dim2CompatTests"):
                # TODO: is there a less hacky way of checking this?
                pytest.skip(f"{dtype} does not support 2D.")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\getitem.py:124** — `# TODO: box over scalar, [scalar], (scalar,)?`
```
def test_getitem_invalid(self, data):
        # TODO: box over scalar, [scalar], (scalar,)?

        msg = (
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\methods.py:70** — `# TODO: avoid special-casing`
```
if isinstance(data.dtype, pd.StringDtype) and data.dtype.na_value is np.nan:
            # TODO: avoid special-casing
            expected = expected.astype("float64")
        elif getattr(data.dtype, "storage", "") == "pyarrow" or isinstance(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\missing.py:30** — `# TODO: GH 57739`
```
mask = getattr(result, na_func)()
        if isinstance(mask.dtype, pd.SparseDtype):
            # TODO: GH 57739
            mask = np.array(mask)
            mask.flags.writeable = True
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\reduce.py:86** — `# TODO: the message being checked here isn't actually checking anything`
```
if not self._supports_reduction(ser, op_name):
            # TODO: the message being checked here isn't actually checking anything
            msg = (
                "[Cc]annot perform|Categorical is not ordered for operation|"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\base\setitem.py:220** — `# TODO(xfail) this raises KeyError about labels not found (it tries label-based)`
```
arr = data.copy()

        # TODO(xfail) this raises KeyError about labels not found (it tries label-based)
        # for list of labels with Series
        if box_in_series:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\json\array.py:263** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    return [
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\json\test_json.py:185** — `# TODO (EA.factorize): see if _values_for_factorize allows this.`
```
@unhashable
    def test_sort_values_frame(self):
        # TODO (EA.factorize): see if _values_for_factorize allows this.
        super().test_sort_values_frame()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\extension\list\array.py:130** — `# TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer`
```
def make_data():
    # TODO: Use a regular dict. See _NDFrameIndexer._setitem_with_indexer
    rng = np.random.default_rng(2)
    data = np.empty(100, dtype=object)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_arithmetic.py:304** — `# TODO: test_bool_flex_frame needs a better name`
```
class TestFrameFlexComparisons:
    # TODO: test_bool_flex_frame needs a better name
    @pytest.mark.parametrize("op", ["eq", "ne", "gt", "lt", "ge", "le"])
    def test_bool_flex_frame(self, op):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_block_internals.py:29** — `# TODO(ArrayManager) check which of those tests need to be rewritten to test the`
```
# TODO(ArrayManager) check which of those tests need to be rewritten to test the
# equivalent for ArrayManager
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_constructors.py:317** — `# TODO(CoW-warn) this should warn`
```
if not using_array_manager and not using_copy_on_write:
            should_be_view = DataFrame(df.values, dtype=df[0].dtype)
            # TODO(CoW-warn) this should warn
            # with tm.assert_cow_warning(warn_copy_on_write):
            should_be_view.iloc[0, 0] = 97
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_cumulative.py:31** — `# TODO(wesm): do something with this?`
```
dm = DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=range(5))
        # TODO(wesm): do something with this?
        dm.cumsum()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_logical_ops.py:155** — `_check_unary_op(operator.inv)  # TODO: belongs elsewhere`
```
_check_bin_op(operator.xor)

        _check_unary_op(operator.inv)  # TODO: belongs elsewhere

    @pytest.mark.filterwarnings("ignore:Downcasting object dtype arrays:FutureWarning")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_reductions.py:1774** — `# TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead`
```
df.median()

        # TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead
        #  of expected.values
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_ufunc.py:150** — `# TODO(FloatArray): this will be Float64Dtype.`
```
np.array([[1, 3], [np.nan, np.nan], [3, 4]]),
    )
    # TODO(FloatArray): this will be Float64Dtype.
    expected = pd.DataFrame(expected, index=["a", "b", "c"], columns=["A", "B"])
    tm.assert_frame_equal(result, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\test_unary.py:167** — `# TODO: assert that we have copies?`
```
res_ufunc = np.positive(df)
        expected = df
        # TODO: assert that we have copies?
        tm.assert_frame_equal(result, expected)
        tm.assert_frame_equal(res_ufunc, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\indexing\test_coercion.py:45** — `# TODO: i think this isn't about MultiIndex and could be done with iloc?`
```
assert (A.dtypes == np.float32).all()

        # TODO: i think this isn't about MultiIndex and could be done with iloc?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\indexing\test_indexing.py:644** — `@td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values`
```
assert ix[idx, col] == ts[idx]

    @td.skip_array_manager_invalid_test  # TODO(ArrayManager) rewrite not using .values
    def test_setitem_fancy_scalar(self, float_frame):
        f = float_frame
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\indexing\test_setitem.py:725** — `# TODO(ArrayManager) set column with 2d column array, see #44788`
```
tm.assert_frame_equal(df, expected)

    # TODO(ArrayManager) set column with 2d column array, see #44788
    @td.skip_array_manager_not_yet_implemented
    def test_setitem_npmatrix_2d(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\indexing\test_where.py:727** — `# TODO: ideally we would get Int64 instead of object`
```
mask[1, :] = False

        # TODO: ideally we would get Int64 instead of object
        result = df.where(mask, ser, axis=0)
        expected = DataFrame({"A": [1, np.nan, 3], "B": [4, np.nan, 6]})
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\indexing\test_xs.py:153** — `# TODO: more descriptive name`
```
class TestXSWithMultiIndex:
    def test_xs_doc_example(self):
        # TODO: more descriptive name
        # based on example in advanced.rst
        arrays = [
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_asfreq.py:154** — `# TODO: actually check that this worked.`
```
rule_monthly.asfreq("B", method="pad")
        # TODO: actually check that this worked.

        # don't forget!
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_astype.py:129** — `# TODO(wesm): verification?`
```
tf.astype(np.float32, copy=False)

        # TODO(wesm): verification?
        tf = float_frame.astype(np.float64)
        tf.astype(np.int64, copy=False)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_clip.py:159** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_combine_first.py:212** — `# TODO: this must be int64`
```
tm.assert_frame_equal(res, exp)
        assert res["a"].dtype == "datetime64[ns]"
        # TODO: this must be int64
        assert res["b"].dtype == "int64"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_compare.py:269** — `# GH#18463 TODO: is this really the desired behavior?`
```
)
    if val1 is pd.NA and val2 is pd.NA:
        # GH#18463 TODO: is this really the desired behavior?
        expected.loc[1, ("a", "self")] = np.nan
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_fillna.py:32** — `# TODO(CoW-warn) better warning message`
```
orig = df[:]

        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df.fillna({"A": 2}, inplace=True)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_info.py:535** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_memory_usage_empty_no_warning(using_infer_string):
    # GH#50066
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_interpolate.py:335** — `# TODO: assert something?`
```
)
        df.interpolate(axis=0)
        # TODO: assert something?

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_quantile.py:729** — `# GH#18463 TODO: would we prefer NaTs here?`
```
exp = exp.astype(object)
        if interpolation == "nearest":
            # GH#18463 TODO: would we prefer NaTs here?
            msg = "The 'downcast' keyword in fillna is deprecated"
            with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_rank.py:504** — `# TODO nullable string[python] should also return nullable Int64`
```
)
        if string_dtype_no_object.storage == "python":
            # TODO nullable string[python] should also return nullable Int64
            exp_dtype = "float64"
        expected = Series([1, 2, None, 3], dtype=exp_dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_rename.py:388** — `# TODO: can we construct this without merge?`
```
),
        )
        # TODO: can we construct this without merge?
        k = merge(df4, df5, how="inner", left_index=True, right_index=True)
        result = k.rename(columns={"TClose_x": "TClose", "TClose_y": "QT_Close"})
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_replace.py:751** — `# TODO: what is this even testing?`
```
msg = "DataFrame.fillna with 'method' is deprecated"
        with tm.assert_produces_warning(FutureWarning, match=msg):
            # TODO: what is this even testing?
            result = tsframe.fillna(method="bfill")
            tm.assert_frame_equal(result, tsframe.fillna(method="bfill"))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_shift.py:469** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support`
```
tm.assert_frame_equal(result, expected)

    @td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) axis=1 support
    def test_shift_axis1_multiple_blocks_with_int_fill(self):
        # GH#42719
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_sort_index.py:596** — `# TODO: better name, de-duplicate with test_sort_index_level above`
```
assert result.columns.is_monotonic_increasing

    # TODO: better name, de-duplicate with test_sort_index_level above
    def test_sort_index_level2(self, multiindex_dataframe_random_data):
        frame = multiindex_dataframe_random_data
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_to_csv.py:547** — `# TODO to_csv drops column name`
```
df = self.read_csv(path, index_col=[0, 1], parse_dates=False)

            # TODO to_csv drops column name
            tm.assert_frame_equal(frame, df, check_names=False)
            assert frame.index.names == df.index.names
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_to_dict_of_blocks.py:40** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
def test_to_dict_of_blocks_item_cache(using_copy_on_write, warn_copy_on_write):
    # Calling to_dict_of_blocks should not poison item_cache
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_tz_convert.py:93** — `# TODO: untested`
```
df4 = DataFrame(np.ones(5), MultiIndex.from_arrays([int_idx, l0]))

            # TODO: untested
            getattr(df4, fn)("US/Pacific", level=1)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\frame\methods\test_update.py:186** — `# TODO(CoW-warn) better warning message`
```
df2_orig = df2.copy()
        result_view = df2[:]
        # TODO(CoW-warn) better warning message
        with tm.assert_cow_warning(warn_copy_on_write):
            df2.update(df)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\generic\test_duplicate_labels.py:51** — `# TODO: frame`
```
"other", [pd.Series(0, index=["a", "b", "c"]), pd.Series(0, index=["a", "b"])]
    )
    # TODO: frame
    @not_implemented
    def test_align(self, other):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\generic\test_finalize.py:13** — `# TODO:`
```
import pandas._testing as tm

# TODO:
# * Binary methods (mul, div, etc.)
# * Binary outputs (align, etc.)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_apply.py:461** — `# TODO(GH#34306): Use assert_frame_equal when column name is not np.nan`
```
result = grouped.apply(len)
    expected = grouped.count().rename(columns={"C": np.nan}).drop(columns="D")
    # TODO(GH#34306): Use assert_frame_equal when column name is not np.nan
    tm.assert_index_equal(result.index, expected.index)
    tm.assert_numpy_array_equal(result.values, expected.values)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_categorical.py:86** — `def test_basic(using_infer_string):  # TODO: split this test`
```
def test_basic(using_infer_string):  # TODO: split this test
    cats = Categorical(
        ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_groupby.py:313** — `# TODO: try to get this more consistent?`
```
expected = DataFrame(ex_data).T
    if not as_index:
        # TODO: try to get this more consistent?
        expected.index = Index(range(2))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_groupby_dropna.py:612** — `# TODO: Should this be 3?`
```
na_group = df["x"].nunique(dropna=False) - 1
            else:
                # TODO: Should this be 3?
                na_group = df["x"].nunique(dropna=False) - 1
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_grouping.py:936** — `# TODO: should prob allow a str of Interval work as well`
```
g = d.groupby(pd.cut(d[0], bins), observed=observed)

        # TODO: should prob allow a str of Interval work as well
        # IOW '(0, 5]'
        result = g.get_group(pd.Interval(0, 5))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_numeric_only.py:93** — `# TODO: min, max *should* handle`
```
@pytest.mark.parametrize("method", ["min", "max"])
    def test_extrema(self, df, method):
        # TODO: min, max *should* handle
        # categorical (ordered) dtype
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_raises.py:634** — `# TODO: empty_groups should be true due to unobserved categorical combinations`
```
):
        assert not empty_groups
        # TODO: empty_groups should be true due to unobserved categorical combinations
        empty_groups = True
    if how == "transform":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_reductions.py:747** — `# TODO: For skipna=False, bool(pd.NA) raises; should groupby?`
```
if reduction_func in ["all", "any"]:
        expected_dtype = "bool"
        # TODO: For skipna=False, bool(pd.NA) raises; should groupby?
        expected_value = False if reduction_func == "any" else True
    elif reduction_func in ["count", "nunique", "size"]:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\test_timegrouper.py:78** — `# TODO(infer_string) resample sum introduces 0's`
```
class TestGroupBy:
    # TODO(infer_string) resample sum introduces 0's
    # https://github.com/pandas-dev/pandas/issues/60229
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_aggregate.py:1356** — `# TODO: agg should raise for functions that don't aggregate`
```
def test_nonagg_agg():
    # GH 35490 - Single/Multiple agg of non-agg function give same results
    # TODO: agg should raise for functions that don't aggregate
    df = DataFrame({"a": [1, 1, 2, 2], "b": [1, 2, 2, 1]})
    g = df.groupby("a")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_numba.py:181** — `# FIXME`
```
[
        ({"func": lambda values, index: values.sum()}, "sum"),
        # FIXME
        pytest.param(
            {
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\aggregate\test_other.py:444** — `# FIXME: the original version of this test called `gb.agg(sum)``
```
tm.assert_frame_equal(result, expected)

    # FIXME: the original version of this test called `gb.agg(sum)`
    #  and that raises TypeError if `numeric_only=False` is passed
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\methods\test_quantile.py:65** — `# TODO(non-nano): this should be unnecessary once array_to_datetime`
```
)
    if all_vals.dtype.kind == "M" and expected.dtypes.values[0].kind == "M":
        # TODO(non-nano): this should be unnecessary once array_to_datetime
        #  correctly infers non-nano from Timestamp.unit
        expected = expected.astype(all_vals.dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\methods\test_value_counts.py:427** — `# TODO(nullable) also string[python] should return nullable dtypes`
```
expected["proportion"] /= expected_group_size
        if dtype == "string[pyarrow]":
            # TODO(nullable) also string[python] should return nullable dtypes
            expected["proportion"] = expected["proportion"].convert_dtypes()
    else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\transform\test_numba.py:149** — `# TODO: Test more than just reductions (e.g. actually test transformations once we have`
```
# TODO: Test more than just reductions (e.g. actually test transformations once we have
@pytest.mark.parametrize(
    "agg_func", [["min", "max"], "min", {"B": ["min", "max"], "C": "sum"}]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\groupby\transform\test_transform.py:872** — `# TODO: create xfail condition given other params`
```
{"level": 0},
        {"by": "string"},
        # TODO: create xfail condition given other params
        # {"by": 'string_missing'},
        {"by": ["int", "string"]},
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_any_index.py:50** — `# TODO: could work that into the 'exact="equiv"'?`
```
if index.dtype == object and result.dtype in [bool, "string"]:
        assert (index == result).all()
        # TODO: could work that into the 'exact="equiv"'?
        return  # FIXME: doesn't belong in this file anymore!
    tm.assert_index_equal(result, index, exact="equiv")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_base.py:57** — `# TODO: a bunch of scattered tests check this deprecation is enforced.`
```
@pytest.mark.parametrize("index", ["datetime"], indirect=True)
    def test_new_axis(self, index):
        # TODO: a bunch of scattered tests check this deprecation is enforced.
        #  de-duplicate/centralize them.
        with pytest.raises(ValueError, match="Multi-dimensional indexing"):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_common.py:169** — `# TODO: belongs in series arithmetic tests?`
```
assert second.name == "mario"

        # TODO: belongs in series arithmetic tests?
        s1 = pd.Series(2, index=first)
        s2 = pd.Series(3, index=second[:-1])
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_indexing.py:157** — `return  # TODO: do we want this to raise?`
```
def test_contains_requires_hashable_raises(self, index):
        if isinstance(index, MultiIndex):
            return  # TODO: do we want this to raise?

        msg = "unhashable type: 'list'"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_numpy_compat.py:155** — `# TODO: overlap with tests.series.test_ufunc.test_reductions`
```
@pytest.mark.parametrize("func", [np.maximum, np.minimum])
def test_numpy_ufuncs_reductions(index, func, request):
    # TODO: overlap with tests.series.test_ufunc.test_reductions
    if len(index) == 0:
        pytest.skip("Test doesn't make sense for empty index.")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\test_setops.py:197** — `# TODO: pin down desired dtype; do we want it to be commutative?`
```
# Testing name retention
    # TODO: pin down desired dtype; do we want it to be commutative?
    result = a.intersection(b)
    assert result.name == names[2]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\base_class\test_reshape.py:41** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
def test_insert_missing(self, request, nulls_fixture, using_infer_string):
        if using_infer_string and nulls_fixture is pd.NA:
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH#22295
        # test there is no mangling of NA values
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimelike_\test_equals.py:56** — `# TODO: de-duplicate with other test_equals2 methods`
```
return period_range("2013-01-01", periods=5, freq="D")

    # TODO: de-duplicate with other test_equals2 methods
    @pytest.mark.parametrize("freq", ["D", "M"])
    def test_equals2(self, freq):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_constructors.py:85** — `# TODO: better place for tests shared by DTI/TDI?`
```
DatetimeIndex([pd.NaT, Timestamp("2011-01-01")._value], freq="D")

    # TODO: better place for tests shared by DTI/TDI?
    @pytest.mark.parametrize(
        "index",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_datetime.py:73** — `# TODO: belongs in frame groupby tests?`
```
assert isinstance(next(iter(result.values()))[0], Timestamp)

    # TODO: belongs in frame groupby tests?
    def test_groupby_function_tuple_1677(self):
        df = DataFrame(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_date_range.py:1303** — `#    # TODO give a more useful or informative message?`
```
msg = "Use a lower freq or a higher unit instead"
        with pytest.raises(ValueError, match=msg):
            #    # TODO give a more useful or informative message?
            date_range("2016-01-01", "2016-01-02", freq="ns", unit="ms")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_formats.py:189** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_dti_representation_to_series(self, unit):
        idx1 = DatetimeIndex([], freq="D")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_indexing.py:294** — `# TODO: This method came from test_datetime; de-dup with version above`
```
idx.take(indices, mode="clip")

    # TODO: This method came from test_datetime; de-dup with version above
    @pytest.mark.parametrize("tz", [None, "US/Eastern", "Asia/Tokyo"])
    def test_take2(self, tz):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\test_setops.py:43** — `# TODO: moved from test_datetimelike; dedup with version below`
```
]

    # TODO: moved from test_datetimelike; dedup with version below
    def test_union2(self, sort):
        everything = date_range("2020-01-01", periods=10)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_delete.py:117** — `# TODO: belongs in Series.drop tests?`
```
assert result.freq == expected.freq

    # TODO: belongs in Series.drop tests?
    @pytest.mark.parametrize("tz", [None, "Asia/Tokyo", "US/Pacific"])
    def test_delete_slice2(self, tz, unit):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\datetimes\methods\test_insert.py:180** — `# TODO: also changes DataFrame.__setitem__ with expansion`
```
assert result.freq is None

    # TODO: also changes DataFrame.__setitem__ with expansion
    def test_insert_mismatched_tzawareness(self):
        # see GH#7299
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\interval\test_formats.py:18** — `# TODO: this is a test for DataFrame/Series, not IntervalIndex`
```
class TestIntervalIndexRendering:
    # TODO: this is a test for DataFrame/Series, not IntervalIndex
    @pytest.mark.parametrize(
        "constructor,expected",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\interval\test_indexing.py:369** — `# TODO: with mismatched resolution get_indexer currently raises;`
```
def test_get_indexer_datetime(self):
        ii = IntervalIndex.from_breaks(date_range("2018-01-01", periods=4))
        # TODO: with mismatched resolution get_indexer currently raises;
        #  this should probably coerce?
        target = DatetimeIndex(["2018-01-02"], dtype="M8[ns]")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\interval\test_setops.py:184** — `# TODO: standardize return type of non-union setops type(self vs other)`
```
set_op = getattr(index, op_name)

        # TODO: standardize return type of non-union setops type(self vs other)
        # non-IntervalIndex
        if op_name == "difference":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\multi\test_analytics.py:76** — `# TODO: reshape`
```
# TODO: reshape
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\multi\test_indexing.py:85** — `# TODO: Try creating a UnicodeDecodeError in exception message`
```
with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(timedelta(seconds=30))
        # TODO: Try creating a UnicodeDecodeError in exception message
        with pytest.raises(TypeError, match="^Level type mismatch"):
            idx.slice_locs(df.index[1], (16, "a"))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\multi\test_reshape.py:69** — `# FIXME data types changes to float because`
```
)
    right.set_index(["1st", "2nd"], inplace=True)
    # FIXME data types changes to float because
    # of intermediate nan insertion;
    tm.assert_frame_equal(left, right, check_dtype=False)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\multi\test_setops.py:233** — `# TODO: this is raising in constructing a Categorical when calling`
```
other = MultiIndex.from_product([[3, pd.Timestamp("2000"), 4], ["c", "d"]])

    # TODO: this is raising in constructing a Categorical when calling
    #  algos.safe_sort. Should we catch and re-raise with a better message?
    msg = "'values' is not ordered, please explicitly specify the categories order "
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\numeric\test_numeric.py:535** — `# TODO: we could plausibly try to infer down to int16 here`
```
idx = Index(np.array([1, 2, 3], dtype=np.int8))
    result = idx.map(lambda x: x * 1000)
    # TODO: we could plausibly try to infer down to int16 here
    expected = Index([1000, 2000, 3000], dtype=np.int64)
    tm.assert_index_equal(result, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\period\test_formats.py:115** — `# TODO: These are Series.__repr__ tests`
```
assert result == expected

    # TODO: These are Series.__repr__ tests
    def test_representation_to_series(self):
        # GH#10971
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\period\test_indexing.py:480** — `# TODO: This method came from test_period; de-dup with version above`
```
tm.assert_numpy_array_equal(result[1], expected_missing)

    # TODO: This method came from test_period; de-dup with version above
    def test_get_indexer2(self):
        idx = period_range("2000-01-01", periods=3).asfreq("h", how="start")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\period\test_partial_slicing.py:44** — `# Todo: fix these accessors!`
```
pi = PeriodIndex(["2Q05", "3Q05", "4Q05", "1Q06", "2Q06"], freq="Q")
        ser = Series(np.random.default_rng(2).random(len(pi)), index=pi).cumsum()
        # Todo: fix these accessors!
        assert ser["05Q4"] == ser.iloc[2]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_astype.py:83** — `# TODO: de-duplicate this version (from test_ops) with the one above`
```
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)

    # TODO: de-duplicate this version (from test_ops) with the one above
    # (from test_period)
    def test_astype_object2(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\period\methods\test_to_timestamp.py:30** — `# TODO: can we get the freq to round-trip?`
```
result = pi._data[::2].to_timestamp()
        expected = dti._data[::2]
        # TODO: can we get the freq to round-trip?
        tm.assert_datetime_array_equal(result, expected, check_freq=False)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_formats.py:54** — `# TODO: this is a Series.__repr__ test`
```
assert result == expected

    # TODO: this is a Series.__repr__ test
    def test_representation_to_series(self):
        idx1 = TimedeltaIndex([], freq="D")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexes\timedeltas\test_scalar_compat.py:98** — `# TODO: de-duplicate with test_tdi_round`
```
t1._data.round(freq)

    # TODO: de-duplicate with test_tdi_round
    def test_round(self):
        t1 = timedelta_range("1 days", periods=3, freq="1 min 2 s 3 us")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_at.py:166** — `# TODO: De-duplicate/parametrize`
```
class TestAtErrors:
    # TODO: De-duplicate/parametrize
    #  test_at_series_raises_key_error2, test_at_frame_raises_key_error2
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_chaining_and_caching.py:561** — `# TODO(ArrayManager) fast_xs with array-like scalars is not yet working`
```
tm.assert_frame_equal(df, df_original)

    # TODO(ArrayManager) fast_xs with array-like scalars is not yet working
    @td.skip_array_manager_not_yet_implemented
    def test_chained_getitem_with_lists(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_coercion.py:351** — `# TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"`
```
tm.assert_index_equal(result, expected)

            # TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"
            #  casts that string to Period[M], not clear that is desirable
            if not isinstance(insert, pd.Timestamp):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_iloc.py:550** — `# TODO: GH#27620 this test used to compare iloc against ix; check if this`
```
tm.assert_frame_equal(df, expected)

    # TODO: GH#27620 this test used to compare iloc against ix; check if this
    #  is redundant with another test comparing iloc against loc
    def test_iloc_getitem_frame(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_indexing.py:911** — `# TODO(EA2D): we can make this no-copy in tz-naive case too`
```
if tz is None:
            # TODO(EA2D): we can make this no-copy in tz-naive case too
            assert ser.dtype == dti.dtype
            assert ser._values._ndarray is values._ndarray
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_loc.py:152** — `# TODO: test something?`
```
def test_loc_getitem_label_array_like(self):
        # TODO: test something?
        # array like
        pass
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\test_partial.py:4** — `TODO: these should be split among the indexer tests`
```
test setting *parts* of objects both positionally and label based

TODO: these should be split among the indexer tests
"""
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\interval\test_interval_new.py:171** — `# TODO KeyError is the appropriate error?`
```
if indexer_sl is tm.loc:
            # slices with scalar raise for overlapping intervals
            # TODO KeyError is the appropriate error?
            with pytest.raises(KeyError, match=msg):
                ser.loc[1:4]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_loc.py:828** — `# TODO: standardize return type for MultiIndex.get_loc`
```
loc = mi.append(mi).get_loc("2001-01")
    expected = index.append(index).get_loc("2001-01")
    # TODO: standardize return type for MultiIndex.get_loc
    tm.assert_numpy_array_equal(loc.nonzero()[0], expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_partial.py:121** — `# TODO(ArrayManager) rewrite test to not use .values`
```
df.loc[("a", "foo"), :]

    # TODO(ArrayManager) rewrite test to not use .values
    # exp.loc[2000, 4].values[:] select multiple columns -> .values is not a view
    @td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\indexing\multiindex\test_setitem.py:129** — `# TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in`
```
)

    # TODO(ArrayManager) df.loc["bar"] *= 2 doesn't raise an error but results in
    # all NaNs -> doesn't work in the "split" path (also for BlockManager actually)
    @td.skip_array_manager_not_yet_implemented
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\interchange\test_impl.py:371** — `"TODO: Set ARROW_TIMEZONE_DATABASE environment variable "`
```
raises=pa.ArrowInvalid,
            reason=(
                "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                "on CI to path to the tzdata for pyarrow."
            ),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\interchange\test_utils.py:7** — `# TODO: use ArrowSchema to get reference C-string.`
```
from pandas.core.interchange.utils import dtype_to_arrow_c_fmt

# TODO: use ArrowSchema to get reference C-string.
# At the time, there is no way to access ArrowSchema holding a type format string
# from python. The only way to access it is to export the structure to a C-pointer,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\internals\test_internals.py:48** — `# TODO(ArrayManager) factor out interleave_dtype tests`
```
# this file contains BlockManager specific tests
# TODO(ArrayManager) factor out interleave_dtype tests
pytestmark = td.skip_array_manager_invalid_test
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_clipboard.py:354** — `# TODO avoid this exception?`
```
pa = pytest.importorskip("pyarrow")
            if engine == "c" and string_storage == "pyarrow":
                # TODO avoid this exception?
                string_dtype = pd.ArrowDtype(pa.large_string())
            else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_common.py:316** — `marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),`
```
("io", "data", "legacy_hdf", "datetimetz_object.h5"),
                # cleaned-up in https://github.com/pandas-dev/pandas/pull/57387 on main
                marks=pytest.mark.xfail(reason="TODO(infer_string)", strict=False),
            ),
            (pd.read_stata, "os", ("io", "data", "stata", "stata10_115.dta")),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_fsspec.py:199** — `@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet`
```
@td.skip_array_manager_not_yet_implemented  # TODO(ArrayManager) fastparquet
def test_fastparquet_options(fsspectest):
    """Regression test for writing to a not-yet-existent GCS Parquet file."""
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_http_headers.py:105** — `# TODO(ArrayManager) fastparquet`
```
parquetfastparquet_responder,
            partial(pd.read_parquet, engine="fastparquet"),
            # TODO(ArrayManager) fastparquet
            marks=[
                td.skip_if_no("fastparquet"),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_parquet.py:53** — `# TODO(ArrayManager) fastparquet relies on BlockManager internals`
```
# TODO(ArrayManager) fastparquet relies on BlockManager internals

pytestmark = [
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_spss.py:14** — `# TODO(CoW) - detection of chained assignment in cython`
```
# TODO(CoW) - detection of chained assignment in cython
# https://github.com/pandas-dev/pandas/issues/51315
@pytest.mark.filterwarnings("ignore::pandas.errors.ChainedAssignmentError")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_sql.py:1860** — `# TODO: clean up types_data_frame fixture`
```
)
    if "postgres" in conn_name:
        # TODO: clean up types_data_frame fixture
        result["BoolCol"] = result["BoolCol"].astype(int)
        result["BoolColWithNull"] = result["BoolColWithNull"].astype(float)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\test_stata.py:188** — `# FIXME: don't leave commented-out`
```
with tm.assert_produces_warning(UserWarning):
            parsed_117 = self.read_dta(path3)
            # FIXME: don't leave commented-out
            # 113 is buggy due to limits of date format support in Stata
            # parsed_113 = self.read_dta(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\excel\test_readers.py:248** — `# TODO add index to xls file)`
```
)

        # TODO add index to xls file)
        tm.assert_frame_equal(df1, expected)
        tm.assert_frame_equal(df2, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\excel\test_style.py:29** — `# TODO: should find a better way to check equality`
```
def assert_equal_cell_styles(cell1, cell2):
    # TODO: should find a better way to check equality
    assert cell1.alignment.__dict__ == cell2.alignment.__dict__
    assert cell1.border.__dict__ == cell2.border.__dict__
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\formats\test_format.py:1253** — `# FIXME: don't leave commented-out`
```
assert not has_non_verbose_info_repr(df)

        # FIXME: don't leave commented-out
        # test verbose overrides
        # set_option('display.max_info_columns', 4)  # exceeded
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\formats\test_to_html.py:373** — `# TODO: split this test`
```
@pytest.mark.parametrize("biggie_df_fixture", ["mixed"], indirect=True)
def test_to_html(biggie_df_fixture):
    # TODO: split this test
    df = biggie_df_fixture
    s = df.to_html()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\formats\test_to_string.py:391** — `# TODO: assert that these match??`
```
result = df.to_string()
        expected = "   0\n0  0\n1  0\n2 -0"
        # TODO: assert that these match??

    def test_to_string_complex_float_formatting(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\formats\style\test_style.py:441** — `# test execution added to todo`
```
}

    # test execution added to todo
    result = getattr(df.style, f"{method}_index")(func[method], axis=axis)
    assert len(result._todo) == 1
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\json\test_json_table_schema.py:212** — `# TODO: datedate.date? datetime.time?`
```
)
    def test_as_json_table_type_date_dtypes(self, date_dtype):
        # TODO: datedate.date? datetime.time?
        assert as_json_table_type(date_dtype) == "datetime"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\json\test_pandas.py:177** — `# TODO: a to_epoch method would also solve; see GH 14772`
```
# in milliseconds; these are internally stored in nanosecond,
                # so divide to get where we need
                # TODO: a to_epoch method would also solve; see GH 14772
                expected.isetitem(0, expected.iloc[:, 0].astype(np.int64) // 1000000)
        elif orient == "split":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\parser\test_encoding.py:190** — `# FIXME: this is bad!`
```
if parser.engine == "pyarrow" and pass_encoding is True and utf_value in [16, 32]:
        # FIXME: this is bad!
        pytest.skip("These cases freeze")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\parser\test_na_values.py:686** — `# TODO: this test isn't about the na_values keyword, it is about the empty entries`
```
# TODO: this test isn't about the na_values keyword, it is about the empty entries
#  being returned with NaN entries, whereas the pyarrow engine returns "nan"
@xfail_pyarrow  # mismatched shapes
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\parser\test_network.py:41** — `pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")`
```
# extension inference
    if compression_only == "tar":
        pytest.skip("TODO: Add tar salaraies.csv to pandas/io/parsers/data")

    extension = compression_to_extension[compression_only]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\parser\test_parse_dates.py:1015** — `# TODO: make unit check more specific`
```
result = parser.read_csv(StringIO(data), index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\parser\common\test_common_basic.py:96** — `# TODO: make unit check more specific`
```
fname = prefix + str(os.path.abspath(csv1))
    result = parser.read_csv(fname, index_col=0, parse_dates=True)
    # TODO: make unit check more specific
    if parser.engine == "pyarrow":
        result.index = result.index.as_unit("ns")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_append.py:254** — `# TODO: Test is incorrect when not using_infer_string.`
```
expected = df
            if using_infer_string:
                # TODO: Test is incorrect when not using_infer_string.
                #       Should take the last 4 rows uncondiationally.
                expected = expected[-4:]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_file_handling.py:366** — `# TODO:(3.0): once Categorical replace deprecation is enforced,`
```
retr = read_hdf(store, key)

    # TODO:(3.0): once Categorical replace deprecation is enforced,
    #  we may be able to re-simplify the construction of s_nan
    if dtype == "category":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_put.py:302** — `# TODO(infer_string) make this work for string dtype`
```
with ensure_clean_store(setup_path) as store:
        if using_infer_string:
            # TODO(infer_string) make this work for string dtype
            msg = "Saving a MultiIndex with an extension dtype is not supported."
            with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_read.py:232** — `# TODO(infer_string) make this work for string dtype`
```
path = tmp_path / setup_path
    if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_round_trip.py:438** — `# TODO(infer_string) make this work for string dtype`
```
if using_infer_string:
        # TODO(infer_string) make this work for string dtype
        msg = "Saving a MultiIndex with an extension dtype is not supported."
        with pytest.raises(NotImplementedError, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_select.py:892** — `# FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds

        # multiple (diff selector)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\io\pytables\test_store.py:745** — `# FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None`
```
expected = expected[(expected.A > 0) & (expected.B > 0)]
        tm.assert_frame_equal(result, expected, check_freq=False)
        # FIXME: 2021-01-18 on some (mostly windows) builds we get freq=None
        #  but expect freq="18B"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\libs\test_hashtable.py:264** — `# TODO: moved from test_algos; may be redundancies with other tests`
```
class TestHashTableUnsorted:
    # TODO: moved from test_algos; may be redundancies with other tests
    def test_string_hashtable_set_item_signature(self):
        # GH#30419 fix typing in StringHashTable.set_item to prevent segfault
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\plotting\test_datetimelike.py:775** — `# TODO`
```
def test_mixed_freq_regular_first(self):
        # TODO
        s1 = Series(
            np.arange(20, dtype=np.float64),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\plotting\test_series.py:983** — `# TODO(3.0): this can be removed once Period[B] deprecation is enforced`
```
def test_plot_no_warning(self, ts):
        # GH 55138
        # TODO(3.0): this can be removed once Period[B] deprecation is enforced
        with tm.assert_produces_warning(False):
            _ = ts.plot()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\plotting\frame\test_frame.py:343** — `# TODO add MultiIndex test`
```
# columns.inferred_type == 'mixed'
        # TODO add MultiIndex test

    @pytest.mark.parametrize(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\resample\test_base.py:269** — `# TODO: no tests with len(df.columns) > 0`
```
result = getattr(rs, resample_method)()
    if resample_method == "ohlc":
        # TODO: no tests with len(df.columns) > 0
        mi = MultiIndex.from_product([df.columns, ["open", "high", "low", "close"]])
        expected = DataFrame(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\resample\test_datetime_index.py:2219** — `reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",`
```
marks=pytest.mark.xfail(
                condition=is_platform_windows(),
                reason="TODO: Set ARROW_TIMEZONE_DATABASE env var in CI",
            ),
        ),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\resample\test_period_index.py:316** — `# TODO: should this raise at the resample call instead of at the mean call?`
```
rs = ser.resample("W")
        with pytest.raises(IncompatibleFrequency, match=msg):
            # TODO: should this raise at the resample call instead of at the mean call?
            rs.mean()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\resample\test_resample_api.py:380** — `# TODO(GH#14008): once GH 14008 is fixed, move these tests into`
```
# TODO(GH#14008): once GH 14008 is fixed, move these tests into
# `Base` test class
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\resample\test_time_grouper.py:250** — `expected.index = dti._with_freq(None)  # TODO: is this desired?`
```
unit=dt_df["key"]._values.unit,
    )
    expected.index = dti._with_freq(None)  # TODO: is this desired?
    tm.assert_frame_equal(expected, dt_result)
    assert dt_result.index.name == "key"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\test_cut.py:584** — `# TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating`
```
if unit == "s":
        # TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating
        #  the first entry here raises in array_to_datetime. Should truncate
        #  instead of raising?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\test_melt.py:1205** — `request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))`
```
if using_infer_string and any_string_dtype == "object":
            # triggers object dtype inference warning of dtype=object
            request.applymarker(pytest.mark.xfail(reason="TODO(infer_string)"))
        # GH46044
        df = DataFrame({"id": ["1", "2"], "a-1": [100, 200], "a-2": [300, 400]})
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\test_pivot.py:2625** — `using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"`
```
# while at that point None was converted to NaN
    @pytest.mark.xfail(
        using_string_dtype(), reason="TODO(infer_string) None is cast to NaN"
    )
    def test_pivot_columns_is_none(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\concat\test_append.py:370** — `# TODO: expected used to be `other.astype(object)` which is a more`
```
expected = other.astype(object)
        if isinstance(val, str) and dtype_str != "int64" and not using_array_manager:
            # TODO: expected used to be `other.astype(object)` which is a more
            #  reasonable result.  This was changed when tightening
            #  assert_frame_equal's treatment of mismatched NAs to match the
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\concat\test_concat.py:50** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# test is not written to work with string dtype (checks .base)
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_copy(self, using_array_manager, using_copy_on_write):
        df = DataFrame(np.random.default_rng(2).standard_normal((4, 3)))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\concat\test_datetimes.py:233** — `# TODO: setting nan here is to keep the test passing as we`
```
if item is pd.NaT and not using_array_manager:
                # GH#18463
                # TODO: setting nan here is to keep the test passing as we
                #  make assert_frame_equal stricter, but is nan really the
                #  ideal behavior here?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\concat\test_empty.py:244** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_concat_inner_join_empty(self):
        # GH 15328
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\merge\test_join.py:347** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
# triggers warning about empty entries
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_join_empty_bug(self):
        # generated an exception in 0.4.3
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge.py:569** — `# TODO: should the next loop be un-indented? doing so breaks this test`
```
tm.assert_frame_equal(result, exp)

            # TODO: should the next loop be un-indented? doing so breaks this test
            for kwarg in [
                {"left_index": True, "right_index": True},
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\reshape\merge\test_merge_asof.py:3141** — `# TODO(GH#32306): may be relevant to the expected behavior here.`
```
#  np.array([np.nan, 1]).  Other than that, I (@jbrockmendel)
        #  have NO IDEA what the expected behavior is.
        # TODO(GH#32306): may be relevant to the expected behavior here.

        arr = pd.array([pd.NA, 0, 1], dtype=any_numeric_ea_dtype)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\scalar\period\test_period.py:87** — `# TODO: raise in the future an error when passing lowercase freq`
```
# GH#54105 - Period can be confusingly instantiated with lowercase freq
        # TODO: raise in the future an error when passing lowercase freq
        i1 = Period("2005", freq="Y")
        i2 = Period("2005")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_constructors.py:141** — `# TODO(2.0): the desired output dtype may have non-nano resolution`
```
dtype="m8[ns]",
        )
        # TODO(2.0): the desired output dtype may have non-nano resolution
        msg = f"'{unit}' is deprecated and will be removed in a future version."
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\scalar\timedelta\test_timedelta.py:401** — `# TODO: this is a test of to_timedelta string parsing`
```
assert tup.nanoseconds == 0

    # TODO: this is a test of to_timedelta string parsing
    def test_iso_conversion(self):
        # GH #21877
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\scalar\timestamp\test_constructors.py:313** — `# TODO: if we passed microsecond with a keyword we would mess up`
```
@pytest.mark.parametrize("kwd", ["nanosecond", "microsecond", "second", "minute"])
    def test_constructor_positional_keyword_mixed_with_tzinfo(self, kwd, request):
        # TODO: if we passed microsecond with a keyword we would mess up
        #  xref GH#45307
        if kwd != "nanosecond":
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\test_arithmetic.py:763** — `# TODO: belongs in tests/arithmetic?`
```
ser_utc + ser

    # TODO: belongs in tests/arithmetic?
    def test_datetime_understood(self, unit):
        # Ensures it doesn't fail to create the right series
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\test_constructors.py:571** — `# TODO should this be raising at all?`
```
expected = Series([0, 1, 2], index=index, dtype=int)
        with pytest.raises(AssertionError, match="Series classes are different"):
            # TODO should this be raising at all?
            # https://github.com/pandas-dev/pandas/issues/56131
            tm.assert_series_equal(result, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\test_logical_ops.py:363** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")`
```
tm.assert_series_equal(result, expected)

    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)")
    def test_logical_ops_label_based(self, using_infer_string):
        # GH#4947
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\test_ufunc.py:173** — `@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp`
```
@pytest.mark.parametrize("ufunc", [np.divmod])  # TODO: np.modf, np.frexp
@pytest.mark.parametrize("shuffle", [True, False])
@pytest.mark.filterwarnings("ignore:divide by zero:RuntimeWarning")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\indexing\test_setitem.py:437** — `# TODO: ser.where(~mask, alt) unnecessarily upcasts to int64`
```
tm.assert_series_equal(ser2, expected)

        # TODO: ser.where(~mask, alt) unnecessarily upcasts to int64
        ser3 = orig.copy()
        res = ser3.where(~mask, alt)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\methods\test_align.py:210** — `# TODO: assert something?`
```
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

    # TODO: assert something?
    ts.align(ts[::2], join=join_type)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\methods\test_astype.py:403** — `# TODO: same for EA float/uint dtypes, signed integers?`
```
):
        # GH#45151 We don't cast negative numbers to nonsense values
        # TODO: same for EA float/uint dtypes, signed integers?
        arr = np.arange(5).astype(float_numpy_dtype) - 3  # includes negatives
        ser = Series(arr)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\methods\test_clip.py:73** — `# TODO: avoid this warning here?  seems like we should never be upcasting`
```
# GH#19992
        msg = "Downcasting behavior in Series and DataFrame methods 'where'"
        # TODO: avoid this warning here?  seems like we should never be upcasting
        #  in the first place?
        with tm.assert_produces_warning(FutureWarning, match=msg):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\methods\test_convert_dtypes.py:186** — `@pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)`
```
class TestSeriesConvertDtypes:
    @pytest.mark.xfail(using_string_dtype(), reason="TODO(infer_string)", strict=False)
    @pytest.mark.parametrize("params", product(*[(True, False)] * 5))
    def test_convert_dtypes(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\series\methods\test_diff.py:14** — `# TODO(__array_function__): could make np.diff return a Series`
```
class TestSeriesDiff:
    def test_diff_np(self):
        # TODO(__array_function__): could make np.diff return a Series
        #  matching ser.diff()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\strings\test_cat.py:359** — `# TODO: Strimg option, this should return string dtype`
```
expected = Series([np.nan] * 4, index=s.index, dtype=s.dtype)
    else:  # box == Index
        # TODO: Strimg option, this should return string dtype
        expected = Index([np.nan] * 4, dtype=object)
    result = s.str.cat(t, join="left")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\strings\test_extract.py:19** — `# TODO: should this raise TypeError`
```
def test_extract_expand_kwarg_wrong_type_raises(any_string_dtype):
    # TODO: should this raise TypeError
    values = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)
    with pytest.raises(ValueError, match="expand must be True or False"):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\strings\test_find_replace.py:258** — `# TODO(infer_string)`
```
tm.assert_series_equal(result, expected)

    # TODO(infer_string)
    # this particular combination of events is broken on 2.3
    # would require cherry picking #58483, which in turn requires #57481
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\strings\test_split_partition.py:385** — `# TODO see GH 18463`
```
# check that these are actually np.nan/pd.NA and not None
    # TODO see GH 18463
    # tm.assert_frame_equal does not differentiate
    if is_object_or_nan_string_dtype(any_string_dtype):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\tools\test_to_datetime.py:579** — `# TODO: Timestamp raises ValueError("could not convert string to Timestamp")`
```
def test_to_datetime_overflow(self):
        # we should get an OutOfBoundsDatetime, NOT OverflowError
        # TODO: Timestamp raises ValueError("could not convert string to Timestamp")
        #  can we make these more consistent?
        arg = "08335394550"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\tseries\offsets\test_business_hour.py:986** — `# TODO(GH#55564): as_unit will be unnecessary`
```
tm.assert_index_equal(t1, expected)

        # TODO(GH#55564): as_unit will be unnecessary
        pointwise = DatetimeIndex([x + off for x in idx]).as_unit(exp_unit)
        tm.assert_index_equal(pointwise, expected)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\tseries\offsets\test_offsets.py:573** — `# TODO: belongs in arithmetic tests?`
```
assert hash(off) is not None

    # TODO: belongs in arithmetic tests?
    @pytest.mark.filterwarnings(
        "ignore:Non-vectorized DateOffset being applied to Series or DatetimeIndex"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\tseries\offsets\test_year.py:330** — `# TODO(cython3): "arg: datetime" annotation will impose`
```
result = ts + off
    # TODO(cython3): "arg: datetime" annotation will impose
    # datetime limitations on Timestamp. The fused type below works in cy3
    # ctypedef fused datetimelike:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\tslibs\test_array_to_datetime.py:27** — `# TODO: tests that include tzs, ints`
```
class TestArrayToDatetimeResolutionInference:
    # TODO: tests that include tzs, ints

    def test_infer_all_nat(self):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\util\test_assert_almost_equal.py:341** — `# TODO: to get the same deprecation in assert_numpy_array_equal we need`
```
_assert_almost_equal_both(left, right, check_dtype=False)

        # TODO: to get the same deprecation in assert_numpy_array_equal we need
        #  to change/deprecate the default for strict_nan to become True
        # TODO: to get the same deprecation in assert_index_equal we need to
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\window\test_expanding.py:576** — `# TODO: xref gh-15826`
```
[[5, 6], [2, 1]], index=[0, 2], columns=Index(["X", "Y"], name="foo")
    )
    # TODO: xref gh-15826
    # .loc is not preserving the names
    result1 = df1.expanding().cov(df2, pairwise=True).loc[2]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\tests\window\test_pairwise.py:299** — `# TODO: We're missing a flag somewhere in meson`
```
lambda x, y: x.expanding().corr(y, pairwise=True),
            lambda x, y: x.rolling(window=3).cov(y, pairwise=True),
            # TODO: We're missing a flag somewhere in meson
            pytest.param(
                lambda x, y: x.rolling(window=3).corr(y, pairwise=True),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\_testing\asserters.py:599** — `# TODO(infer_string) this special case could be avoided if we have`
```
left = repr(left)
    elif isinstance(left, StringDtype):
        # TODO(infer_string) this special case could be avoided if we have
        # a more informative repr https://github.com/pandas-dev/pandas/issues/59342
        left = f"StringDtype(storage={left.storage}, na_value={left.na_value})"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\_testing\contexts.py:225** — `# TODO update match`
```
else:
            warning = FutureWarning  # type: ignore[assignment]
            # TODO update match
            match = "ChainedAssignmentError"
        if extra_warnings:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pandas\_testing\__init__.py:226** — `# TODO: Add container like pyarrow types:`
```
BOOL_PYARROW_DTYPES = [pa.bool_()]

    # TODO: Add container like pyarrow types:
    #  https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions
    ALL_PYARROW_DTYPES = (
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\FpxImagePlugin.py:178** — `# FIXME: the fill decoder is not implemented`
```
elif compression == 1:
                # FIXME: the fill decoder is not implemented
                self.tile.append(
                    ImageFile._Tile(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\GifImagePlugin.py:120** — `self._fp = self.fp  # FIXME: hack`
```
self.global_palette = self.palette = p

        self._fp = self.fp  # FIXME: hack
        self.__rewind = self.fp.tell()
        self._n_frames: int | None = None
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\IcoImagePlugin.py:75** — `# TODO: invent a more convenient method for proportional scalings`
```
break
        else:
            # TODO: invent a more convenient method for proportional scalings
            frame = provided_im.copy()
            frame.thumbnail(size, Image.Resampling.LANCZOS, reducing_gap=None)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\Image.py:544** — `# FIXME: take "new" parameters / other image?`
```
def __init__(self) -> None:
        # FIXME: take "new" parameters / other image?
        self._im: core.ImagingCore | DeferredError | None = None
        self._mode = ""
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageCms.py:1103** — `# FIXME: I get different results for the same data w. different`
```
if not isinstance(profile, ImageCmsProfile):
            profile = ImageCmsProfile(profile)
        # FIXME: I get different results for the same data w. different
        # compilers.  Bug in LittleCMS or in the binding?
        if profile.profile.is_intent_supported(intent, direction):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageDraw.py:102** — `# FIXME: fix Fill2 to properly support matte for I+F images`
```
self.ink = self.draw.draw_ink(-1)
        if mode in ("1", "P", "I", "F"):
            # FIXME: fix Fill2 to properly support matte for I+F images
            self.fontmode = "1"
        else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageDraw2.py:54** — `# FIXME: add support for bitmap fonts`
```
self, color: str, file: StrOrBytesPath | BinaryIO, size: float = 12
    ) -> None:
        # FIXME: add support for bitmap fonts
        self.color = ImageColor.getrgb(color)
        self.font = ImageFont.truetype(file, size)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageFile.py:341** — `# FIXME: This is a hack to handle TIFF's JpegTables tag.`
```
self.tile.sort(key=_tilesort)

            # FIXME: This is a hack to handle TIFF's JpegTables tag.
            prefix = getattr(self, "tile_prefix", b"")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageFont.py:19** — `# Todo:`
```
# 2003-09-27 fl   added support for truetype charmap encodings
#
# Todo:
# Adapt to PILFONT2 format (16-bit fonts, compressed, single file)
#
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageOps.py:54** — `# FIXME: apply to lookup table, not image data`
```
def _lut(image: Image.Image, lut: list[int]) -> Image.Image:
    if image.mode == "P":
        # FIXME: apply to lookup table, not image data
        msg = "mode P support coming soon"
        raise NotImplementedError(msg)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImagePalette.py:229** — `raise NotImplementedError(msg)  # FIXME`
```
msg = "unavailable when black is non-zero"
    raise NotImplementedError(msg)  # FIXME
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImageQt.py:140** — `# FIXME - is this really the best way to do this?`
```
# handle filename, if given instead of image name
    if hasattr(im, "toUtf8"):
        # FIXME - is this really the best way to do this?
        im = str(im.toUtf8(), "utf-8")
    if is_path(im):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\ImImagePlugin.py:152** — `# FIXME: this may read whole file if not a text file`
```
break

            # FIXME: this may read whole file if not a text file
            s = s + self.fp.readline()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\JpegImagePlugin.py:110** — `self.info["flashpix"] = s  # FIXME: value will change`
```
elif marker == 0xFFE2 and s.startswith(b"FPXR\0"):
        # extract FlashPix information (incomplete)
        self.info["flashpix"] = s  # FIXME: value will change
    elif marker == 0xFFE2 and s.startswith(b"ICC_PROFILE\0"):
        # Since an ICC profile can be larger than the maximum size of
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\McIdasImagePlugin.py:55** — `# FIXME: add memory map support`
```
mode = rawmode = "I;16B"
        elif w[11] == 4:
            # FIXME: add memory map support
            mode = "I"
            rawmode = "I;32B"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\MpoImagePlugin.py:128** — `self._fp = self.fp  # FIXME: hack`
```
del self.info["mpoffset"]  # no longer needed
        self.is_animated = self.n_frames > 1
        self._fp = self.fp  # FIXME: hack
        self._fp.seek(self.__mpoffsets[0])  # get ready to read first frame
        self.__frame = 0
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\MspImagePlugin.py:184** — `header[12] = checksum  # FIXME: is this the right field?`
```
for h in header:
        checksum = checksum ^ h
    header[12] = checksum  # FIXME: is this the right field?

    # header
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PcdImagePlugin.py:49** — `self._size = 768, 512  # FIXME: not correct for rotated images!`
```
self._mode = "RGB"
        self._size = 768, 512  # FIXME: not correct for rotated images!
        self.tile = [ImageFile._Tile("pcd", (0, 0) + self.size, 96 * 2048)]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PcxImagePlugin.py:96** — `# FIXME: hey, this doesn't work with the incremental loader !!!`
```
elif version == 5 and bits == 8 and planes == 1:
            mode = rawmode = "L"
            # FIXME: hey, this doesn't work with the incremental loader !!!
            self.fp.seek(-769, io.SEEK_END)
            s = self.fp.read(769)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PdfImagePlugin.py:57** — `# FIXME: Should replace ASCIIHexDecode with RunLengthDecode`
```
image_refs: list[PdfParser.IndirectReference],
) -> tuple[PdfParser.IndirectReference, str]:
    # FIXME: Should replace ASCIIHexDecode with RunLengthDecode
    # (packbits) or LZWDecode (tiff/lzw compression).  Note that
    # PDF 1.2 also supports Flatedecode (zip compression).
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PdfParser.py:616** — `# TODO: support reuse of deleted objects`
```
def next_object_id(self, offset: int | None = None) -> IndirectReference:
        try:
            # TODO: support reuse of deleted objects
            reference = IndirectReference(max(self.xref_table.keys()) + 1, 0)
        except ValueError:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PixarImagePlugin.py:61** — `# FIXME: to be continued...`
```
if mode == (14, 2):
            self._mode = "RGB"
        # FIXME: to be continued...

        # create tile descriptor (assuming "dumped")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PngImagePlugin.py:445** — `icc_profile = None  # FIXME`
```
raise
        except zlib.error:
            icc_profile = None  # FIXME
        self.im_info["icc_profile"] = icc_profile
        return s
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PsdImagePlugin.py:40** — `(7, 8): ("L", 1),  # FIXME: multilayer`
```
(3, 8): ("RGB", 3),
    (4, 8): ("CMYK", 4),
    (7, 8): ("L", 1),  # FIXME: multilayer
    (8, 8): ("L", 1),  # duotone
    (9, 8): ("LAB", 3),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\PSDraw.py:44** — `# FIXME: incomplete`
```
def begin_document(self, id: str | None = None) -> None:
        """Set up printing of a document. (Write PostScript DSC header.)"""
        # FIXME: incomplete
        self.fp.write(
            b"%!PS-Adobe-3.0\n"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\SpiderImagePlugin.py:161** — `self._fp = self.fp  # FIXME: hack`
```
self.tile = [ImageFile._Tile("raw", (0, 0) + self.size, offset, self.rawmode)]
        self._fp = self.fp  # FIXME: hack

    @property
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\TiffImagePlugin.py:962** — `# FIXME What about tagdata?`
```
def tobytes(self, offset: int = 0) -> bytes:
        # FIXME What about tagdata?
        result = self._pack("Q" if self._bigtiff else "H", len(self._tags_v2))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\TiffTags.py:209** — `# FIXME add more tags here`
```
33723: ("IptcNaaInfo", UNDEFINED, 1),
    34377: ("PhotoshopInfo", BYTE, 0),
    # FIXME add more tags here
    34665: ("ExifIFD", LONG, 1),
    34675: ("ICCProfile", UNDEFINED, 1),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\PIL\XVThumbImagePlugin.py:17** — `# FIXME: make save work (this requires quantization support)`
```
#
# To do:
# FIXME: make save work (this requires quantization support)
#
from __future__ import annotations
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\build_env.py:200** — `# FIXME: Consider direct URL?`
```
if not req.specifier.contains(dist.version, prereleases=True):
                    conflicting.add((installed_req_str, req_str))
                # FIXME: Consider direct URL?
        return conflicting, missing
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\cache.py:278** — `# TODO: use DirectUrl.equivalent when`
```
)
            else:
                # TODO: use DirectUrl.equivalent when
                # https://github.com/pypa/pip/pull/10564 is merged.
                if origin.url != download_info.url:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\cli\base_command.py:204** — `# TODO: Try to get these passing down from the command?`
```
sys.exit(ERROR)

        # TODO: Try to get these passing down from the command?
        #       without resorting to os.environ to hold these.
        #       This also affects isolated builds and it should.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\commands\inspect.py:60** — `# TODO tags? scheme?`
```
"installed": [self._dist_to_dict(dist) for dist in dists],
            "environment": default_environment(),
            # TODO tags? scheme?
        }
        print_json(data=output)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\index\collector.py:344** — `# TODO: In the future, it would be nice if pip supported PEP 691`
```
if not url.endswith("/"):
            url += "/"
        # TODO: In the future, it would be nice if pip supported PEP 691
        #       style responses in the file:// URLs, however there's no
        #       standard file extension for application/vnd.pypi.simple.v1+json
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\locations\base.py:15** — `# FIXME doesn't account for venv linked to global site-packages`
```
USER_CACHE_DIR = appdirs.user_cache_dir("pip")

# FIXME doesn't account for venv linked to global site-packages
site_packages: str = sysconfig.get_path("purelib")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\metadata\base.py:37** — `from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.`
```
DirectUrlValidationError,
)
from pip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.
from pip._internal.utils.egg_link import egg_link_path_from_sys_path
from pip._internal.utils.misc import is_local, normalize_path
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\models\installation_report.py:50** — `# TODO: currently, the resolver uses the default environment to evaluate`
```
],
            # https://peps.python.org/pep-0508/#environment-markers
            # TODO: currently, the resolver uses the default environment to evaluate
            # environment markers, so that is what we report here. In the future, it
            # should also take into account options such as --python-version or
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\models\selection_prefs.py:6** — `# TODO: This needs Python 3.10's improved slots support for dataclasses`
```
# TODO: This needs Python 3.10's improved slots support for dataclasses
# to be converted into a dataclass.
class SelectionPreferences:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\network\lazy_wheel.py:174** — `# TODO: Get range requests to be correctly cached`
```
headers = base_headers.copy()
        headers["Range"] = f"bytes={start}-{end}"
        # TODO: Get range requests to be correctly cached
        headers["Cache-Control"] = "no-cache"
        return self._session.get(self._url, headers=headers, stream=True)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\operations\prepare.py:557** — `# TODO: separate this part out from RequirementPreparer when the v1`
```
self._prepare_linked_requirement(req, parallel_builds)

        # TODO: separate this part out from RequirementPreparer when the v1
        # resolver can be removed!
        self._complete_partial_requirements(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\req\constructors.py:285** — `# TODO: The is_installable_dir test here might not be necessary`
```
if is_installable_dir(path):
            return path_to_url(path)
        # TODO: The is_installable_dir test here might not be necessary
        #       now that it is done in load_pyproject_toml too.
        raise InstallationError(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\req\req_file.py:107** — `# TODO: replace this with slots=True when dropping Python 3.9 support.`
```
@dataclass(frozen=True)
class ParsedRequirement:
    # TODO: replace this with slots=True when dropping Python 3.9 support.
    __slots__ = (
        "requirement",
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\req\req_install.py:371** — `# FIXME: Is there a better place to create the build_dir? (hg and bzr`
```
dir_name = f"{dir_name}_{uuid.uuid4().hex}"

        # FIXME: Is there a better place to create the build_dir? (hg and bzr
        # need this)
        if not os.path.exists(build_dir):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\req\req_set.py:75** — `TODO remove this property together with the legacy resolver, since the new`
```
"""Return the list of requirements that need to be installed.

        TODO remove this property together with the legacy resolver, since the new
             resolver only returns requirements that need to be installed.
        """
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\req\req_uninstall.py:480** — `# FIXME: need a test for this elif block`
```
for installed_file in installed_files:
                    paths_to_remove.add(os.path.join(dist_location, installed_file))
            # FIXME: need a test for this elif block
            # occurs with --single-version-externally-managed/--record outside
            # of pip
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py:227** — `# TODO performance: this means we iterate the dependencies at least twice,`
```
)
        # check dependencies are valid
        # TODO performance: this means we iterate the dependencies at least twice,
        # we may want to cache parsed Requires-Dist
        try:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\resolution\resolvelib\factory.py:201** — `# TODO: Check already installed candidate, and use it if the link and`
```
version: Optional[Version],
    ) -> Optional[BaseCandidate]:
        # TODO: Check already installed candidate, and use it if the link and
        # editable flag match.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\utils\unpacking.py:326** — `# FIXME: handle?`
```
untar_file(filename, location)
    else:
        # FIXME: handle?
        # FIXME: magic signatures?
        logger.critical(
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_internal\vcs\subversion.py:59** — `# FIXME: should we warn?`
```
entries_fn = os.path.join(base, cls.dirname, "entries")
            if not os.path.exists(entries_fn):
                # FIXME: should we warn?
                continue
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\typing_extensions.py:1020** — `# TODO: Use inspect.VALUE here, and make the annotations lazily evaluated`
```
own_annotations = ns["__annotations__"]
            elif "__annotate__" in ns:
                # TODO: Use inspect.VALUE here, and make the annotations lazily evaluated
                own_annotations = ns["__annotate__"](1)
            else:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\cachecontrol\controller.py:227** — `# TODO: There is an assumption that the result will be a`
```
logger.debug("Current age based on date: %i", current_age)

        # TODO: There is an assumption that the result will be a
        #       urllib3 response object. This may not be best since we
        #       could probably avoid instantiating or constructing the
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\cachecontrol\filewrapper.py:67** — `# TODO: Add some logging here...`
```
# We just don't cache it then.
        # TODO: Add some logging here...
        return False
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\database.py:933** — `# FIXME handle the case where zipfile is not available`
```
requires = parse_requires_path(req_path)
            else:
                # FIXME handle the case where zipfile is not available
                zipf = zipimport.zipimporter(path)
                fileobj = StringIO(zipf.get_data('EGG-INFO/PKG-INFO').decode('utf8'))
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\locators.py:760** — `XXX TODO Note: this cache is never actually cleared. It's assumed that`
```
Get the HTML for an URL, possibly from an in-memory cache.

        XXX TODO Note: this cache is never actually cleared. It's assumed that
        the data won't get stale over the lifetime of a locator instance (not
        necessarily true for the default_locator).
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\metadata.py:239** — `# TODO document the mapping API and UNKNOWN default key`
```
"""

    # TODO document the mapping API and UNKNOWN default key

    def __init__(self, path=None, fileobj=None, mapping=None, scheme='default'):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\resources.py:190** — `todo = [resource]`
```
resource = self.find(resource_name)
        if resource is not None:
            todo = [resource]
            while todo:
                resource = todo.pop(0)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\util.py:401** — `# TODO check k, v for valid values`
```
cp = configparser.ConfigParser()
    for k, v in exports.items():
        # TODO check k, v for valid values
        cp.add_section(k)
        for entry in v.values():
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\version.py:267** — `TODO: fill this out`
```
1.2.3c1
        1.2.3.4
        TODO: fill this out

    Bad:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:839** — `# TODO version verification`
```
# wv = message['Wheel-Version'].split('.', 1)
            # file_version = tuple([int(i) for i in wv])
            # TODO version verification

            records = {}
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\msgpack\fallback.py:499** — `# TODO should we eliminate the recursion?`
```
raise ValueError("Expected map")
            return n
        # TODO should we eliminate the recursion?
        if typ == TYPE_ARRAY:
            if execute == EX_SKIP:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\packaging\metadata.py:204** — `# TODO: The spec doesn't say anything about if the keys should be`
```
parts.extend([""] * (max(0, 2 - len(parts))))  # Ensure 2 items

        # TODO: The spec doesn't say anything about if the keys should be
        #       considered case sensitive or not... logically they should
        #       be case-preserving and case-insensitive, but doing that
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\packaging\requirements.py:29** — `# TODO: Can we test whether something is contained within a requirement?`
```
"""

    # TODO: Can we test whether something is contained within a requirement?
    #       If so how do we do that? Do we need to test against the _name_ of
    #       the thing as well as the version? What about the markers?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\packaging\tags.py:378** — `# TODO: Need to care about 32-bit PPC for ppc64 through 10.2?`
```
elif cpu_arch == "ppc64":
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        if version > (10, 5) or version < (10, 4):
            return []
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\pkg_resources\__init__.py:1** — `# TODO: Add Generic type annotations to initialized collections.`
```
# TODO: Add Generic type annotations to initialized collections.
# For now we'd simply use implicit Any/Unknown which would add redundant annotations
# mypy: disable-error-code="var-annotated"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\pygments\lexer.py:863** — `TODO: clean up the code here.`
```
The result is a combined token stream.

    TODO: clean up the code here.
    """
    insertions = iter(insertions)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\pygments\filters\__init__.py:72** — `highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.`
```
`codetags` : list of strings
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.

    .. versionchanged:: 2.13
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\pygments\lexers\python.py:715** — `# different tokens.  TODO: DelegatingLexer should support this`
```
tblexer = Python2TracebackLexer
        # We have two auxiliary lexers. Use DelegatingLexer twice with
        # different tokens.  TODO: DelegatingLexer should support this
        # directly, by accepting a tuplet of auxiliary lexers and a tuple of
        # distinguishing tokens. Then we wouldn't need this intermediary
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\pygments\lexers\_mapping.py:535** — `'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),`
```
'TlbLexer': ('pip._vendor.pygments.lexers.tlb', 'Tl-b', ('tlb',), ('*.tlb',), ()),
    'TlsLexer': ('pip._vendor.pygments.lexers.tls', 'TLS Presentation Language', ('tls',), (), ()),
    'TodotxtLexer': ('pip._vendor.pygments.lexers.textfmts', 'Todotxt', ('todotxt',), ('todo.txt', '*.todotxt'), ('text/x-todo',)),
    'TransactSqlLexer': ('pip._vendor.pygments.lexers.sql', 'Transact-SQL', ('tsql', 't-sql'), ('*.sql',), ('text/x-tsql',)),
    'TreetopLexer': ('pip._vendor.pygments.lexers.parsers', 'Treetop', ('treetop',), ('*.treetop', '*.tt'), ()),
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\rich\text.py:562** — `# TODO: This is a little inefficient, it is only used by full justify`
```
Style: A Style instance.
        """
        # TODO: This is a little inefficient, it is only used by full justify
        if offset < 0:
            offset = len(self) + offset
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\truststore\_macos.py:558** — `# TODO: Not sure if we need the SecTrustResultType for anything?`
```
)

            # TODO: Not sure if we need the SecTrustResultType for anything?
            # We only care whether or not it's a success or failure for now.
            sec_trust_result_type = Security.SecTrustResultType()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:199** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self.sock = conn
        if self._is_using_tunnel():
            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
            # Mark this connection as not reusable
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\connectionpool.py:522** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, host, port = get_host(url)
        if host is not None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\exceptions.py:289** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\response.py:441** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.")
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\pyopenssl.py:371** — `# FIXME rethrow compatible exceptions should we ever use this`
```
def shutdown(self):
        # FIXME rethrow compatible exceptions should we ever use this
        self.connection.shutdown()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\contrib\securetransport.py:659** — `# TODO: should I do clean shutdown here? Do I have to?`
```
def close(self):
        # TODO: should I do clean shutdown here? Do I have to?
        if self._makefile_refs < 1:
            self._closed = True
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\util\response.py:103** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method = response._method
    if isinstance(method, int):  # Platform-specific: Appengine
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:31** — `# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.`
```
# TODO: In v2 we can remove this sentinel and metaclass with deprecated options.
_Default = object()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:402** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\proto\_package_info.py:40** — `# TODO: Revert to empty string as a package value after protobuf fix.`
```
# A package should be present; get the marshal from there.
    # TODO: Revert to empty string as a package value after protobuf fix.
    # When package is empty, upb based protobuf fails with an
    # "TypeError: Couldn't build proto file into descriptor pool: invalid name: empty part ()' means"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\psycopg2\tz.py:158** — `# TODO: pre-generate some interesting time zones?`
```
LOCAL = LocalTimezone()

# TODO: pre-generate some interesting time zones?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\psycopg2\_range.py:526** — `# TODO: probably won't work with infs, nans and other tricky cases.`
```
# TODO: probably won't work with infs, nans and other tricky cases.
register_adapter(NumericRange, NumberRangeAdapter)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\codec\ber\decoder.py:48** — `raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?`
```
The decoder is allowed to consume as many bytes as necessary.
        """
        raise error.PyAsn1Error('SingleItemDecoder not implemented for %s' % (tagSet,))  # TODO: Seems more like an NotImplementedError?

    def indefLenValueDecoder(self, substrate, asn1Spec,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\codec\ber\encoder.py:189** — `# TODO: try to avoid ASN.1 schema instantiation`
```
def encodeValue(self, value, asn1Spec, encodeFun, **options):
        if asn1Spec is not None:
            # TODO: try to avoid ASN.1 schema instantiation
            value = asn1Spec.clone(value)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\codec\cer\decoder.py:51** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
BitStringPayloadDecoder = decoder.BitStringPayloadDecoder
OctetStringPayloadDecoder = decoder.OctetStringPayloadDecoder
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\codec\der\decoder.py:23** — `# TODO: prohibit non-canonical encoding`
```
# TODO: prohibit non-canonical encoding
RealPayloadDecoder = decoder.RealPayloadDecoder
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\codec\der\encoder.py:34** — `# TODO: move out of sorting key function`
```
return component.getComponent().tagSet
            else:
                # TODO: move out of sorting key function
                names = [namedType.name for namedType in asn1Spec.componentType.namedTypes
                         if namedType.name in component]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\type\constraint.py:85** — `# TODO: fix possible comparison of set vs scalars here`
```
def isSuperTypeOf(self, otherConstraint):
        # TODO: fix possible comparison of set vs scalars here
        return (otherConstraint is self or
                not self._values or
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1\type\univ.py:1724** — `# TODO: remove when Py2.5 support is gone`
```
indices, values = zip(*self._componentValues.items())

        # TODO: remove when Py2.5 support is gone
        values = list(values)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1_modules\rfc2459.py:4** — `# Updated by Russ Housley to resolve the TODO regarding the Certificate`
```
# This file is part of pyasn1-modules software.
#
# Updated by Russ Housley to resolve the TODO regarding the Certificate
#   Policies Certificate Extension.
#
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\pyasn1_modules\rfc2985.py:86** — `# TODO:`
```
# TODO:
# Need a place to import PKCS15Token; it does not yet appear in an RFC
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\graphics\renderPDF.py:72** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\graphics\renderPS.py:772** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\graphics\renderSVG.py:803** — `#pdfgen roundRect function.  TODO`
```
else:
            #cheat and assume ry = rx; better to generalize
            #pdfgen roundRect function.  TODO
            self._canvas.roundRect(
                    rect.x, rect.y,
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\graphics\widgetbase.py:62** — `# TODO when we need it, but not before -`
```
from reportlab.lib.validators import isValidChild

        # TODO when we need it, but not before -
        # expose sequence contents?
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\platypus\paragraph.py:1272** — `#TODO fix this to use binary search for the split points`
```
then push those new words onto words
    '''
    #TODO fix this to use binary search for the split points
    R = []
    aR = R.append
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\reportlab\platypus\xpreformatted.py:209** — `breakLinesCJK = breakLines  #TODO fixme fixme fixme`
```
return lines

    breakLinesCJK = breakLines  #TODO fixme fixme fixme

    # we need this her to get the right splitter
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\requests\adapters.py:686** — `# TODO: Remove this in 3.0.0: see #2811`
```
except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                # TODO: Remove this in 3.0.0: see #2811
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\requests\hooks.py:19** — `# TODO: response is the only one`
```
# TODO: response is the only one
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\cli.py:30** — `# TODO: Add CLI Tests`
```
# TODO: Add CLI Tests
# TODO: Simplify formatter by using argparse `type` arguments
def create_parser():
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\keywords.py:41** — `# FIXME(andi): VALUES shouldn't be listed here`
```
(r'\\\w+', tokens.Command),

    # FIXME(andi): VALUES shouldn't be listed here
    # see https://github.com/andialbrecht/sqlparse/pull/64
    # AS and IN are special, it may be followed by a parenthesis, but
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\sql.py:109** — `# TODO: Add test for regex with is_keyboard = false`
```
if regex:
            # TODO: Add test for regex with is_keyboard = false
            flag = re.IGNORECASE if self.is_keyword else 0
            values = (re.compile(v, flag) for v in values)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\engine\grouping.py:335** — `# TODO: convert this to eidx instead of end token.`
```
else:
            end = tlist.tokens[eidx - 1]
        # TODO: convert this to eidx instead of end token.
        # i think above values are len(tlist) and eidx-1
        eidx = tlist.token_index(end)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\engine\statement_splitter.py:58** — `# FIXME(andi): This makes no sense.  ## this comment neither`
```
self._begin_depth += 1
            if self._is_create:
                # FIXME(andi): This makes no sense.  ## this comment neither
                return 1
            return 0
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\filters\others.py:19** — `# TODO(andi) Comment types should be unified, see related issue38`
```
def _process(tlist):
        def get_next_comment(idx=-1):
            # TODO(andi) Comment types should be unified, see related issue38
            return tlist.token_next_by(i=sql.Comment, t=T.Comment, idx=idx)
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\sqlparse\filters\right_margin.py:13** — `# FIXME: Doesn't work`
```
# FIXME: Doesn't work
class RightMarginFilter:
    keep_together = (
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\connection.py:330** — `# TODO: Fix tunnel so it doesn't depend on self.sock state.`
```
self._has_connected_to_proxy = True

            # TODO: Fix tunnel so it doesn't depend on self.sock state.
            self._tunnel()
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\connectionpool.py:578** — `# TODO: Add optional support for socket.gethostbyname checking.`
```
return True

        # TODO: Add optional support for socket.gethostbyname checking.
        scheme, _, host, port, *_ = parse_url(url)
        scheme = scheme or "http"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\exceptions.py:306** — `# TODO(t-8ch): Stop inheriting from AssertionError in v2.0.`
```
"""ProxyManager does not support the supplied scheme"""

    # TODO(t-8ch): Stop inheriting from AssertionError in v2.0.

    def __init__(self, scheme: str | None) -> None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\response.py:782** — `# FIXME: Ideally we'd like to include the url in the ReadTimeoutError but`
```
except SocketTimeout as e:
                # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
                # there is yet no clean way to get at it from this context.
                raise ReadTimeoutError(self._pool, None, "Read timed out.") from e  # type: ignore[arg-type]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\_base_connection.py:20** — `# TODO: Remove this in favor of a better`
```
class _ResponseOptions(typing.NamedTuple):
    # TODO: Remove this in favor of a better
    # HTTP request/response lifecycle tracking.
    request_method: str
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\http2\connection.py:144** — `# TODO SKIPPABLE_HEADERS from urllib3 are ignored.`
```
def putheader(self, header: str | bytes, *values: str | bytes) -> None:  # type: ignore[override]
        # TODO SKIPPABLE_HEADERS from urllib3 are ignored.
        header = header.encode() if isinstance(header, str) else header
        header = header.lower()  # A lot of upstream code uses capitalized headers.
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\http2\__init__.py:38** — `# TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.`
```
urllib3_connection.HTTPSConnection = HTTP2Connection  # type: ignore[misc]

    # TODO: Offer 'http/1.1' as well, but for testing purposes this is handy.
    urllib3_util.ALPN_PROTOCOLS = ["h2"]
    urllib3_util_ssl.ALPN_PROTOCOLS = ["h2"]
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\util\request.py:229** — `# File-like object, TODO: use seek() and tell() for length?`
```
content_length = len(chunks[0])

    # File-like object, TODO: use seek() and tell() for length?
    elif hasattr(body, "read"):
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\util\response.py:99** — `# FIXME: Can we do this somehow without accessing private httplib _method?`
```
used 'HEAD' as a method.
    """
    # FIXME: Can we do this somehow without accessing private httplib _method?
    method_str = response._method  # type: str  # type: ignore[attr-defined]
    return method_str.upper() == "HEAD"
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\urllib3\util\url.py:454** — `# TODO: Remove this when we break backwards compatibility.`
```
# string values for path if there are any defined values
    # beyond the path in the URL.
    # TODO: Remove this when we break backwards compatibility.
    if not path:
        if query is not None or fragment is not None:
```
---
- **C:\industria\connectit_django\venv\Lib\site-packages\werkzeug\http.py:1343** — `# TODO Remove encoding dance, it seems like clients accept UTF-8 keys`
```
# Send a non-ASCII key as mojibake. Everything else should already be ASCII.
    # TODO Remove encoding dance, it seems like clients accept UTF-8 keys
    buf = [f"{key.encode().decode('latin1')}={value}"]
```
