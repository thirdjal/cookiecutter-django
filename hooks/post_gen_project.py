from __future__ import print_function

import os

PROJECT_SLUG = "{{ cookiecutter.slug }}"
NODE_DIR = "node_modules"
STATIC_DIR = os.path.join(PROJECT_SLUG, "static")

WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "
TERMINATOR = "\x1b[0m"


def install_node_dependencies():
    print(INFO + "Installing external dependancies" + TERMINATOR)
    os.system("npm install --silent --no-fund --omit=optional")


def link_bootstrap():
    print(INFO + "Linking Bootstrap" + TERMINATOR)
    SOURCE_DIR = os.path.join(NODE_DIR, "bootstrap", "dist")
    files = [
        os.path.join("css", "bootstrap.min.css"),
        os.path.join("css", "bootstrap.min.css.map"),
        os.path.join("js", "bootstrap.bundle.min.js"),
        os.path.join("js", "bootstrap.bundle.min.js.map"),
    ]

    for file in files:
        os.symlink(
            os.path.abspath(os.path.join(SOURCE_DIR, file)),
            os.path.join(STATIC_DIR, file),
        )


def link_bootstrap_icons():
    print(INFO + "Linking Bootstrap Icons" + TERMINATOR)
    SOURCE_DIR = os.path.join(NODE_DIR, "bootstrap-icons", "font")
    os.mkdir(os.path.join(STATIC_DIR, "fonts", "fonts"))
    files = [
        {"src": "", "dst": "fonts", "filename": "bootstrap-icons.css"},
        {
            "src": "fonts",
            "dst": os.path.join("fonts", "fonts"),
            "filename": "bootstrap-icons.woff",
        },
        {
            "src": "fonts",
            "dst": os.path.join("fonts", "fonts"),
            "filename": "bootstrap-icons.woff2",
        },
    ]

    for file in files:
        os.symlink(
            os.path.abspath(os.path.join(SOURCE_DIR, file["src"], file["filename"])),
            os.path.join(STATIC_DIR, file["dst"], file["filename"]),
        )


def main():
    install_node_dependencies()
    link_bootstrap()
    link_bootstrap_icons()
    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
