for f in ./services/gitignore/*.gitignore; do (cat "${f}"; echo) >> ./services/.gitignore; done
