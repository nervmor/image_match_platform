import phash
from .. import intfc
from ..conf import configure
from ..defn.define import *

class checker:
    def __init__(self, category, pic_url):
        self._category = category
        self._pic_url = pic_url
        self._phash_interface = intfc.phash.pash_interface(
            configure.engine_srv_url,
            configure.feature_srv_url)
        self._img_interface = intfc.img.img_interface()

    def run(self):
        ret = res_fail
        result = {}
        while (True):
            ret, info = self._img_interface.fetch(self._pic_url)
            if ret <> res_succs:
                break
            phash_task = phash.pash_check_task(self._phash_interface, self._img_interface, self._category, info)
            ret, result = phash_task.run()
            if ret <> res_succs:
                break
            print result
            break



