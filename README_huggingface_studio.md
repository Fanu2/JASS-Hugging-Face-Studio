# Jass Hugging Face Studio

A single-file PySide6 desktop application for building a personal **Hugging Face Hub library**.

The Hugging Face Hub is much broader than a simple channel platform: it hosts models, datasets and Spaces, with millions of public repositories. citeturn0search2turn0search3turn0search0

## Included

- `huggingface_studio.py` — single-file PySide6 application
- `index.html` — directory of 100 Hugging Face creators/organizations
- `huggingface_channels_100.csv` — seed directory
- `README.md` — documentation

## Features

- 🤗 100 preloaded Hugging Face creators/organizations
- ➕ Add Hugging Face profiles manually
- ⭐ Favorites
- 🏷️ Categories
- 🔎 Search
- 📝 Notes
- 🌐 Open directly on Hugging Face
- 📊 Dashboard statistics
- 💾 Local SQLite database
- 🖥️ Single Python file

## Run

```powershell
py -m pip install PySide6
py huggingface_studio.py
```

The local database is:

```text
C:\Users\<username>\.jass_huggingface_studio.db
```

## Why "channels"?

Hugging Face does not use YouTube-style channels as its primary organizational unit. This Studio therefore treats **Hugging Face user profiles and organizations as channels** for the purpose of creating a personal discovery library.

The Hub currently includes models, datasets and Spaces. citeturn0search2

## Roadmap

### V0.1
- [x] 100 curated Hub profiles
- [x] Dashboard
- [x] Search
- [x] Favorites
- [x] Categories
- [x] Notes
- [x] Local SQLite

### V0.2
- [ ] Live Hub API search
- [ ] Creator profile metadata
- [ ] Avatar/thumbnail support
- [ ] Model counts
- [ ] Dataset counts
- [ ] Space counts

### V0.3 — Hugging Face Intelligence
- [ ] Search models from the application
- [ ] Search datasets
- [ ] Browse Spaces
- [ ] Trending models
- [ ] Model task filters
- [ ] Library filters
- [ ] Parameter-size filters

The official Hub model browser exposes task, library, language, license and parameter filters, making these natural future features. citeturn0search8

### V0.4 — Local AI Workspace
- [ ] Favorite models
- [ ] Download manager
- [ ] GGUF/quantized model tracker
- [ ] Ollama compatibility notes
- [ ] LM Studio compatibility notes
- [ ] Local model inventory
- [ ] Model comparison

## Design Goal

Jass Hugging Face Studio is intended to be a **personal AI discovery and model-library manager**, not a replacement for the Hugging Face website.

The Studio provides a personal layer for discovering, organizing and tracking the Hub.

## Official Hub

urlHugging Face Hubhttps://huggingface.co/

