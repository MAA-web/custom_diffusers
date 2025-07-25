from ...models.controlnets.multicontrolnet import MultiControlNetModel
from ...utils import deprecate, logging


logger = logging.get_logger(__name__)


class MultiControlNetModel(MultiControlNetModel):
    def __init__(self, *args, **kwargs):
        deprecation_message = "Importing `MultiControlNetModel` from `custom_diffusers.pipelines.controlnet.multicontrolnet` is deprecated and this will be removed in a future version. Please use `from custom_diffusers.models.controlnets.multicontrolnet import MultiControlNetModel`, instead."
        deprecate("custom_diffusers.pipelines.controlnet.multicontrolnet.MultiControlNetModel", "0.34", deprecation_message)
        super().__init__(*args, **kwargs)
