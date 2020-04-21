from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))
jsondata = os.path.join(here, "data.json")

def test_basic():

    prj = MicroappProject()
    data = '\'["foo", {"bar": ["baz", null, 1.0, 2]}]\''
    cmd = "dict2json %s -o %s" % (data, jsondata)

    ret = prj.main(cmd)

    assert ret == 0
    assert os.path.exists(jsondata)

    os.remove(jsondata)
