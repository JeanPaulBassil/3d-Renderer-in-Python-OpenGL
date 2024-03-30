# 3D Renderer Project

This project is a simple 3D renderer implemented in Python using the OpenGL library.

## Setup

Follow these steps to set up the project:

1. Clone the repository:

```bash
git clone https://github.com/JeanPaulBassil/3d-Renderer-in-Python-OpenGL.git
cd 3d-Renderer-in-Python-OpenGL
```
2. Create a virtual environment

```bash
python3 -m venv venv
```
3. Activate the virtual environment:

On Linux or MacOS
```bash
source venv/bin/activate
```

On Windows
```bash
.\venv\Scripts\activate
```
You might want to install the GLUT library to be able to open the window on your local machine.

On Linux:
```bash
sudo apt-get install freeglut3-dev
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

### Running the project

After setting up, you can run the project with 
```bash
python main.py
```

This will open a window displaying a 3D object rendered with OpenGL
 