from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-advice', methods=['POST'])
def get_advice():
    data = request.json
    mood = data.get('mood')
    
    advice = {
        'happy': "Great to hear you're happy! Keep up the positive habits and stay connected with loved ones.",
        'neutral': "It's okay to feel neutral. Consider doing something you enjoy to boost your mood.",
        'sad': "It's important to acknowledge sadness. Try talking to a friend or doing something relaxing."
    }
    
    return jsonify({'advice': advice.get(mood, "No advice available.")})

if __name__ == '__main__':
    app.run(debug=True)
