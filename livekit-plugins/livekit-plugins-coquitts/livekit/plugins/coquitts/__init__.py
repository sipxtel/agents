import typing  # noqa: I001


def __getattr__(name: str) -> typing.Any:
    if name == "realtime":
        try:
            from .experimental import realtime
        except ImportError as e:
            raise ImportError("The 'realtime' module not supported and/or implemented.") from e

        return realtime

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


from .tts import TTS, ChunkedStream  # noqa: E402
from .version import __version__  # noqa: E402

__all__ = ["TTS", "ChunkedStream", "__version__"]

from livekit.agents import Plugin  # noqa: E402

from .log import logger  # noqa: E402


class CoquiPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(CoquiPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
