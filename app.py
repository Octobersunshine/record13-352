from flask import Flask, request, jsonify
from converter import s2t, t2s

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    if not data:
        return jsonify({'error': '请求体不能为空'}), 400

    text = data.get('text', '')
    direction = data.get('direction', 's2t')

    if not text:
        return jsonify({'error': 'text 参数不能为空'}), 400

    if direction == 's2t':
        result = s2t(text)
    elif direction == 't2s':
        result = t2s(text)
    else:
        return jsonify({'error': 'direction 参数只能是 s2t 或 t2s'}), 400

    return jsonify({
        'original': text,
        'result': result,
        'direction': direction
    })


@app.route('/s2t', methods=['POST'])
def simple_s2t():
    data = request.get_json()
    if not data:
        return jsonify({'error': '请求体不能为空'}), 400

    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text 参数不能为空'}), 400

    return jsonify({
        'original': text,
        'result': s2t(text)
    })


@app.route('/t2s', methods=['POST'])
def simple_t2s():
    data = request.get_json()
    if not data:
        return jsonify({'error': '请求体不能为空'}), 400

    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text 参数不能为空'}), 400

    return jsonify({
        'original': text,
        'result': t2s(text)
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
