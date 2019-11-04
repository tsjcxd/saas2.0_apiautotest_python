import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base.rest_client import Rest_Client
from public.get_token import get_token


class CoachLevel:
    """教练等级所有API的封装"""
    def __init__(self,token):
        self.rest = Rest_Client(token)

    def coach_level_list(self,data=None,**kwargs):
        """教练等级列表（分页）"""
        resp = self.rest.get('/v1/setting/coach',data=data,**kwargs)
        return resp

    def coach_level_create(self,data=None, json=None, **kwargs):
        """新增教练等级"""
        resp = self.rest.post('/v1/setting/coach', data=data, json=None, **kwargs)
        return resp
    
    def coach_level_delete(self, coach_id,**kwargs):
        resp = self.rest.delete('/v1/setting/coach/{}'.format(coach_id), **kwargs)
        return resp
        

if __name__ == "__main__":
    from public.get_token import get_token
    token = get_token("st6527031128", "CUEw6057")
    print(token)
    c = CoachLevel(token)
    r = c.coach_level_list()
    print(r)