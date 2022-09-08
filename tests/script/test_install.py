# This test covers script installation, version, shared library install

import cmind as cm

r = cm.access({'action':'run', 'automation':'script', 'tags': 'python,src,install,_shared', 'version': '3.9.10', 'quiet': 'true'})
if 'return' not in r:
    raise Exception('CM access function should always return key \'return\'!')
if 'error' in r:
    raise Exception(r['error'])

r = cm.access({'action':'search', 'automation':'cache', 'tags': 'python,src,install,_shared,version-3.9.10'})
if 'return' not in r:
    raise Exception('CM access function should always return key \'return\'!')
if 'error' in r:
    raise Exception(r['error'])
if 'list' not in r:
    raise Exception('CM access function should always return a list for search action!')
if len(r['list']) < 1:
    raise Exception('CM search failed for the cached installation!')