from flask import Flask, request, jsonify
from converter import convert, s2t, s2hk, t2s, VALID_LOCALES

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    if not data:
        return jsonify({'error': '请求体不能为空'}), 400

    text = data.get('text', '')
    locale = data.get('locale', 'zh-tw')

    if not text:
        return jsonify({'error': 'text 参数不能为空'}), 400

    if locale not in VALID_LOCALES:
        return jsonify({'error': f'locale 参数只能是: {", ".join(sorted(VALID_LOCALES))}'}), 400

    try:
        result = convert(text, locale)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({
        'original': text,
        'result': result,
        'locale': locale
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
        'result': s2t(text),
        'locale': 'zh-tw'
    })


@app.route('/s2hk', methods=['POST'])
def simple_s2hk():
    data = request.get_json()
    if not data:
        return jsonify({'error': '请求体不能为空'}), 400

    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text 参数不能为空'}), 400

    return jsonify({
        'original': text,
        'result': s2hk(text),
        'locale': 'zh-hk'
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
        'result': t2s(text),
        'locale': 'zh-cn'
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
