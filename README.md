<div align="center">

# 🎵 ANorm: Normalize Many Files Easily and Intuitively

## 📁 Project Architecture

```
AudioNormalizer/
├── ⚡ Core System
│   ├── .gitignore                     # 🚫 Git ignore rules
│   ├── main.py                        # 🎯 Main program entry
│   ├── pyproject.toml                 # ⚙️ Project configuration
│   ├── README.md                      # 📝 Project documentation
│
├── 🛠️ GitHub Workflows
│   └── .github/workflows/
│       └── build.yml                  # 🚀 CI/CD build workflow
│
└── 🖥️ App System
    ├── app.py                         # 🏁 App entry point
    ├── utils.py                       # 🧰 General utilities
    ├── core/                          # 🧠 Core logic
    │   ├── app_logic.py               # ⚡ Application logic
    │   └── utils.py                   # 🧮 Core helper functions
    ├── gui/                           # 🎨 Graphical interface
    │   ├── controllers/               # 🎮 GUI controllers
    │   │   └── start_controller.py    # 🖱️ Handles start screen interactions
    │   └── ui/                        # 🖌️ UI layouts
    │       └── start_ui.py            # 📐 Layout for the start screen
    └── resources/                     # 📁 Static resources
        ├── favicon.icns               # 🖼️ App icon (Mac)
        ├── favicon.ico                # 🖼️ App icon (Windows)
        └── favicon.png                # 🖼️ App icon (Other)
```