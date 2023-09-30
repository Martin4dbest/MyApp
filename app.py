from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Define the directory where video uploads will be stored in the diorectory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No video file provided"

    video = request.files['video']

    if video.filename == '':
        return "No video file selected"

    if video:
        # Save the video to the UPLOAD_FOLDER
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)
        return f"Video '{video.filename}' has been uploaded successfully!"

@app.route('/')
def home():
    return "Welcome to the Video Upload and Playback App"

@app.route('/play/<filename>')
def play_video(filename):
    # Render a page to play the video
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return render_template('play.html', video_path=video_path)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
