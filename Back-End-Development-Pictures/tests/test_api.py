import pytest
from app import app
from backend.data import data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c: yield c

def test_health(client):
    r=client.get('/health'); assert r.status_code==200; assert r.get_json()=={'status':'OK'}
def test_count(client):
    r=client.get('/count'); assert r.status_code==200; assert 'length' in r.get_json()
def test_data_contains_10_pictures(): assert len(data)>=10
def test_get_picture(client): assert client.get('/picture').status_code==200
def test_get_pictures_check_content_type_equals_json(client): assert client.get('/picture').content_type.startswith('application/json')
def test_get_picture_by_id(client): assert client.get('/picture/1').get_json()['id']==1
def test_pictures_json_is_not_empty(client): assert client.get('/picture').get_json()
def test_post_picture(client):
    p={'id':200,'pic_url':'http://dummyimage.com/230x100.png/dddddd/000000','event_country':'United States','event_state':'California','event_city':'Fremont','event_date':'11/2/2030'}
    data[:] = [x for x in data if x['id']!=200]
    r=client.post('/picture',json=p); assert r.status_code==201; assert r.get_json()==p
def test_post_picture_duplicate(client):
    p={'id':200,'pic_url':'http://dummyimage.com/230x100.png/dddddd/000000','event_country':'United States','event_state':'California','event_city':'Fremont','event_date':'11/2/2030'}
    if not any(x['id']==200 for x in data): data.append(p.copy())
    r=client.post('/picture',json=p); assert r.status_code==302
def test_update_picture_by_id(client):
    p={'id':1,'pic_url':'https://example.com/updated.jpg','event_country':'United States','event_state':'Texas','event_city':'Austin','event_date':'1/1/2031'}
    r=client.put('/picture/1',json=p); assert r.status_code in (200,201); assert r.get_json()['event_city']=='Austin'
def test_delete_picture_by_id(client):
    if not any(x['id']==201 for x in data): data.append({'id':201,'pic_url':'x','event_country':'x','event_state':'x','event_city':'x','event_date':'x'})
    r=client.delete('/picture/201'); assert r.status_code==204
