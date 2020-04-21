from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))
app = os.path.join(here, "..", "dict2json.py")
jsondata = os.path.join(here, "data.json")

def test_basic():

    prj = MicroappProject()
    data = '\'["foo", {"bar": ["baz", null, 1.0, 2]}]\''
    cmd = "%s %s -o %s" % (app, data, jsondata)

    ret = prj.main(cmd)

    assert ret == 0
    assert os.path.exists(jsondata)

    os.remove(jsondata)
