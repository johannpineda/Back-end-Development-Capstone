from flask import Blueprint, jsonify, request
from http import HTTPStatus
from .data import data

bp = Blueprint("pictures", __name__)

@bp.route('/health', methods=['GET'])
def health():
    return jsonify(status='OK'), HTTPStatus.OK

@bp.route('/count', methods=['GET'])
def count():
    return jsonify(length=len(data)), HTTPStatus.OK

@bp.route('/picture', methods=['GET'])
def get_pictures():
    return jsonify(data), HTTPStatus.OK

@bp.route('/picture/<int:id>', methods=['GET'])
def get_picture_by_id(id):
    picture = next((p for p in data if p['id'] == id), None)
    if picture is None:
        return jsonify(message='picture not found'), HTTPStatus.NOT_FOUND
    return jsonify(picture), HTTPStatus.OK

@bp.route('/picture', methods=['POST'])
def create_picture():
    picture = request.get_json()
    if not picture:
        return jsonify(message='request body required'), HTTPStatus.BAD_REQUEST
    if any(p['id'] == picture.get('id') for p in data):
        return jsonify(Message=f"picture with id {picture['id']} already present"), HTTPStatus.FOUND
    data.append(picture)
    return jsonify(picture), HTTPStatus.CREATED

@bp.route('/picture/<int:id>', methods=['PUT'])
def update_picture(id):
    picture = next((p for p in data if p['id'] == id), None)
    if picture is None:
        return jsonify(message='picture not found'), HTTPStatus.NOT_FOUND
    incoming = request.get_json() or {}
    picture.clear(); picture.update(incoming); picture['id'] = id
    return jsonify(picture), HTTPStatus.CREATED

@bp.route('/picture/<int:id>', methods=['DELETE'])
def delete_picture(id):
    picture = next((p for p in data if p['id'] == id), None)
    if picture is None:
        return jsonify(message='picture not found'), HTTPStatus.NOT_FOUND
    data.remove(picture)
    return '', HTTPStatus.NO_CONTENT
