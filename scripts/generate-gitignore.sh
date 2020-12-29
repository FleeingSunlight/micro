for f in ./gitignore/*.gitignore; do (cat "${f}"; echo) >> ./services/.gitignore; done
