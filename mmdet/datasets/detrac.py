from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class DETRACDataset(CocoDataset):

    CLASSES = ('car', 'van', 'others', 'bus')
