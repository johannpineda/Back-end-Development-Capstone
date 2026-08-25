from flask import Blueprint, jsonify, request
from bson import ObjectId
from .db import collection
bp=Blueprint('songs',__name__)

def clean(doc):
    if not doc: return None
    doc=dict(doc); doc['_id']=str(doc['_id']); return doc

@bp.get('/health')
def health(): return jsonify(status='OK'),200

@bp.get('/song')
def get_songs(): return jsonify([clean(x) for x in collection().find()]),200

@bp.get('/song/<id>')
def get_song(id):
    try: doc=collection().find_one({'_id':ObjectId(id)})
    except Exception: doc=collection().find_one({'id':id})
    if not doc: return jsonify(message='song not found'),404
    return jsonify(clean(doc)),200

@bp.post('/song')
def create_song():
    payload=request.get_json() or {}
    result=collection().insert_one(payload)
    return jsonify(clean(collection().find_one({'_id':result.inserted_id}))),201

@bp.put('/song/<id>')
def update_song(id):
    payload=request.get_json() or {}; payload.pop('_id',None)
    try: q={'_id':ObjectId(id)}
    except Exception: q={'id':id}
    result=collection().update_one(q,{'$set':payload})
    if not result.matched_count: return jsonify(message='song not found'),404
    return jsonify(clean(collection().find_one(q))),200

@bp.delete('/song/<id>')
def delete_song(id):
    try: q={'_id':ObjectId(id)}
    except Exception: q={'id':id}
    result=collection().delete_one(q)
    if not result.deleted_count: return jsonify(message='song not found'),404
    return '',204
