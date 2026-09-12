import sys
import sqlite3
import webbrowser
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QComboBox, QMainWindow,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget, QAbstractItemView, QHeaderView
)

APP_NAME = "Jass Hugging Face Studio"
DB_PATH = Path.home() / ".jass_huggingface_studio.db"

SEED_CHANNELS = [('Hugging Face', 'https://huggingface.co/huggingface', 'AI Platform'), ('OpenAI Community', 'https://huggingface.co/openai-community', 'AI Models'), ('Google', 'https://huggingface.co/google', 'AI Models'), ('Meta Llama', 'https://huggingface.co/meta-llama', 'LLMs'), ('Microsoft', 'https://huggingface.co/microsoft', 'AI Models'), ('Qwen', 'https://huggingface.co/Qwen', 'LLMs'), ('Mistral AI', 'https://huggingface.co/mistralai', 'LLMs'), ('DeepSeek AI', 'https://huggingface.co/deepseek-ai', 'LLMs'), ('NVIDIA', 'https://huggingface.co/nvidia', 'AI Hardware'), ('IBM Granite', 'https://huggingface.co/ibm-granite', 'LLMs'), ('Intel', 'https://huggingface.co/Intel', 'AI Hardware'), ('AMD', 'https://huggingface.co/amd', 'AI Hardware'), ('Apple', 'https://huggingface.co/apple', 'AI Research'), ('Facebook AI', 'https://huggingface.co/facebook', 'AI Research'), ('Stability AI', 'https://huggingface.co/stabilityai', 'Generative AI'), ('Black Forest Labs', 'https://huggingface.co/black-forest-labs', 'Image Generation'), ('Cohere', 'https://huggingface.co/CohereForAI', 'LLMs'), ('Allen AI', 'https://huggingface.co/allenai', 'AI Research'), ('BAAI', 'https://huggingface.co/BAAI', 'AI Research'), ('01 AI', 'https://huggingface.co/01-ai', 'LLMs'), ('THUDM', 'https://huggingface.co/THUDM', 'LLMs'), ('InternLM', 'https://huggingface.co/internlm', 'LLMs'), ('OpenBMB', 'https://huggingface.co/openbmb', 'LLMs'), ('MiniMax', 'https://huggingface.co/MiniMaxAI', 'LLMs'), ('Zhipu AI', 'https://huggingface.co/zai-org', 'LLMs'), ('Moonshot AI', 'https://huggingface.co/moonshotai', 'LLMs'), ('ByteDance', 'https://huggingface.co/ByteDance', 'AI Research'), ('Tencent', 'https://huggingface.co/tencent', 'AI Research'), ('Alibaba DAMO', 'https://huggingface.co/damo', 'AI Research'), ('Baidu', 'https://huggingface.co/baidu', 'AI Research'), ('SenseTime', 'https://huggingface.co/SenseTime', 'Computer Vision'), ('Salesforce AI', 'https://huggingface.co/Salesforce', 'AI Research'), ('Adobe', 'https://huggingface.co/adobe', 'AI Research'), ('Nokia', 'https://huggingface.co/Nokia', 'AI Research'), ('ServiceNow AI', 'https://huggingface.co/ServiceNow-AI', 'Enterprise AI'), ('Databricks', 'https://huggingface.co/databricks', 'AI Data'), ('Snowflake', 'https://huggingface.co/snowflake', 'AI Data'), ('MongoDB', 'https://huggingface.co/mongodb', 'AI Data'), ('Nomic AI', 'https://huggingface.co/nomic-ai', 'Embeddings'), ('Unsloth', 'https://huggingface.co/unsloth', 'LLM Tools'), ('Lightricks', 'https://huggingface.co/Lightricks', 'Generative AI'), ('Runway', 'https://huggingface.co/runwayml', 'Video AI'), ('ElevenLabs', 'https://huggingface.co/elevenlabs', 'Speech AI'), ('Kyutai', 'https://huggingface.co/kyutai', 'Speech AI'), ('Hume AI', 'https://huggingface.co/humeai', 'Speech AI'), ('NVIDIA NeMo', 'https://huggingface.co/nvidia', 'AI Models'), ('Black Forest Labs', 'https://huggingface.co/black-forest-labs', 'Image Generation'), ('Krea AI', 'https://huggingface.co/krea', 'Image Generation'), ('Ideogram', 'https://huggingface.co/ideogram', 'Image Generation'), ('LAION', 'https://huggingface.co/laion', 'Datasets'), ('EleutherAI', 'https://huggingface.co/EleutherAI', 'AI Research'), ('Together AI', 'https://huggingface.co/togethercomputer', 'AI Infrastructure'), ('Nous Research', 'https://huggingface.co/NousResearch', 'LLMs'), ('Teknium', 'https://huggingface.co/teknium', 'LLMs'), ('TheBloke', 'https://huggingface.co/TheBloke', 'GGUF'), ('bartowski', 'https://huggingface.co/bartowski', 'GGUF'), ('lmstudio-community', 'https://huggingface.co/lmstudio-community', 'Local AI'), ('TheBloke Archive', 'https://huggingface.co/TheBloke', 'Local AI'), ('MaziyarPanahi', 'https://huggingface.co/MaziyarPanahi', 'LLMs'), ('bartowski Archive', 'https://huggingface.co/bartowski', 'Local AI'), ('QuantFactory', 'https://huggingface.co/QuantFactory', 'Quantization'), ('ggml-org', 'https://huggingface.co/ggml-org', 'Local AI'), ('Mozilla', 'https://huggingface.co/mozilla', 'AI Research'), ('Mozilla AI', 'https://huggingface.co/Mozilla', 'AI Research'), ('NVIDIA AI', 'https://huggingface.co/nvidia', 'AI Models'), ('H2O AI', 'https://huggingface.co/h2oai', 'LLMs'), ('Together Computer', 'https://huggingface.co/togethercomputer', 'LLMs'), ('Upstage', 'https://huggingface.co/upstage', 'LLMs'), ('Cerebras', 'https://huggingface.co/cerebras', 'AI Hardware'), ('Groq', 'https://huggingface.co/Groq', 'AI Hardware'), ('Sakana AI', 'https://huggingface.co/SakanaAI', 'AI Research'), ('Arcee AI', 'https://huggingface.co/arcee-ai', 'LLMs'), ('AI2', 'https://huggingface.co/allenai', 'AI Research'), ('NousResearch', 'https://huggingface.co/NousResearch', 'LLMs'), ('OpenGVLab', 'https://huggingface.co/OpenGVLab', 'Computer Vision'), ('IDEA-Research', 'https://huggingface.co/IDEA-Research', 'Computer Vision'), ('ByteDance Research', 'https://huggingface.co/ByteDance', 'AI Research'), ('Hugging Face H4', 'https://huggingface.co/h4', 'AI Research'), ('Hugging Face SmolLab', 'https://huggingface.co/HuggingFaceTB', 'Small Models'), ('Hugging Face TB', 'https://huggingface.co/HuggingFaceTB', 'Small Models'), ('Hugging Face Sentence Transformers', 'https://huggingface.co/sentence-transformers', 'Embeddings'), ('Sentence Transformers', 'https://huggingface.co/sentence-transformers', 'Embeddings'), ('Microsoft Research', 'https://huggingface.co/microsoft', 'AI Research'), ('Google Research', 'https://huggingface.co/google', 'AI Research'), ('Meta AI', 'https://huggingface.co/facebook', 'AI Research'), ('Mistral Research', 'https://huggingface.co/mistralai', 'AI Research'), ('Qwen Research', 'https://huggingface.co/Qwen', 'AI Research'), ('DeepSeek Research', 'https://huggingface.co/deepseek-ai', 'AI Research'), ('IBM Research', 'https://huggingface.co/ibm-granite', 'AI Research'), ('Stanford NLP', 'https://huggingface.co/stanfordnlp', 'NLP'), ('Berkeley AI Research', 'https://huggingface.co/berkeley-nest', 'AI Research'), ('Cornell AI', 'https://huggingface.co/cornellius-gat', 'AI Research'), ('Salesforce AI Research', 'https://huggingface.co/Salesforce', 'AI Research'), ('Mila', 'https://huggingface.co/mila-iqia', 'AI Research'), ('NYU', 'https://huggingface.co/nyu-mll', 'NLP'), ('BigScience', 'https://huggingface.co/bigscience', 'AI Research'), ('Helsinki-NLP', 'https://huggingface.co/Helsinki-NLP', 'NLP'), ('UKPLab', 'https://huggingface.co/UKPLab', 'NLP'), ('DeepMind', 'https://huggingface.co/deepmind', 'AI Research'), ('Anthropic Research', 'https://huggingface.co/Anthropic', 'AI Research')]


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()
        self.seed()

    def create_tables(self):
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS channels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            category TEXT DEFAULT 'Other',
            favorite INTEGER DEFAULT 0,
            notes TEXT DEFAULT '',
            created_at TEXT NOT NULL
        );
        """)
        self.conn.commit()

    def seed(self):
        count = self.conn.execute("SELECT COUNT(*) FROM channels").fetchone()[0]
        if count:
            return
        now = datetime.now().isoformat(timespec="seconds")
        self.conn.executemany(
            """INSERT OR IGNORE INTO channels
               (name,url,category,created_at) VALUES(?,?,?,?)""",
            [(n, u, c, now) for n, u, c in SEED_CHANNELS]
        )
        self.conn.commit()


class ChannelDialog(QDialog):
    def __init__(self, parent=None, row=None):
        super().__init__(parent)
        self.setWindowTitle("Add Hugging Face Channel" if row is None else "Edit Channel")
        self.resize(520, 300)

        self.name = QLineEdit()
        self.url = QLineEdit()
        self.url.setPlaceholderText("https://huggingface.co/username-or-org")
        self.category = QComboBox()
        self.category.addItems([
            "AI Platform", "LLMs", "AI Research", "Computer Vision",
            "Image Generation", "Video AI", "Speech AI", "Embeddings",
            "Datasets", "Local AI", "GGUF", "Quantization", "MLOps",
            "NLP", "Diffusion", "RLHF", "AI Hardware", "Other"
        ])
        self.notes = QTextEdit()

        if row:
            self.name.setText(row["name"])
            self.url.setText(row["url"])
            self.category.setCurrentText(row["category"])
            self.notes.setPlainText(row["notes"] or "")

        form = QFormLayout()
        form.addRow("Name:", self.name)
        form.addRow("Hugging Face URL:", self.url)
        form.addRow("Category:", self.category)
        form.addRow("Notes:", self.notes)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def values(self):
        return (
            self.name.text().strip(),
            self.url.text().strip(),
            self.category.currentText(),
            self.notes.toPlainText().strip()
        )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle(APP_NAME)
        self.resize(1200, 760)
        self.setStyleSheet("""
        QMainWindow, QWidget { background:#111827; color:#e5e7eb; }
        QLabel { color:#e5e7eb; }
        QPushButton { background:#f97316; color:white; border:none;
                      border-radius:7px; padding:9px 14px; }
        QPushButton:hover { background:#fb923c; }
        QLineEdit,QTextEdit,QComboBox { background:#1f2937; color:#f9fafb;
                      border:1px solid #374151; border-radius:6px; padding:7px; }
        QListWidget { background:#0f172a; border:none; padding:8px; }
        QListWidget::item { padding:12px 10px; border-radius:6px; }
        QListWidget::item:selected { background:#ea580c; }
        QTableWidget { background:#172033; alternate-background-color:#1f2937;
                      gridline-color:#374151; border:1px solid #374151; }
        QHeaderView::section { background:#1f2937; color:#cbd5e1;
                      padding:9px; border:none; }
        """)

        self.build_ui()
        self.refresh_all()

    def build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)
        main = QHBoxLayout(root)
        main.setContentsMargins(0,0,0,0)
        main.setSpacing(0)

        sidebar = QWidget()
        sidebar.setFixedWidth(230)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(15,20,15,15)

        title = QLabel("JASS\nHUGGING FACE\nSTUDIO")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        side.addWidget(title)
        side.addSpacing(25)

        self.nav = QListWidget()
        for x in ["🏠  Dashboard", "🤗  Channels", "🔥  Trending",
                  "⭐  Favorites", "🧠  Models", "📊  Categories"]:
            self.nav.addItem(x)
        self.nav.currentRowChanged.connect(self.change_page)
        side.addWidget(self.nav)
        side.addStretch()

        info = QLabel("Local-first Hugging Face\ncreator & organization library")
        info.setWordWrap(True)
        info.setStyleSheet("color:#64748b;font-size:10px;")
        side.addWidget(info)

        content = QWidget()
        cv = QVBoxLayout(content)
        cv.setContentsMargins(25,20,25,20)

        header = QHBoxLayout()
        self.page_title = QLabel("Dashboard")
        self.page_title.setFont(QFont("Segoe UI",22,QFont.Weight.Bold))
        header.addWidget(self.page_title)
        header.addStretch()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search creators, organizations, categories…")
        self.search.setFixedWidth(340)
        self.search.textChanged.connect(self.refresh_current_page)
        header.addWidget(self.search)
        cv.addLayout(header)

        self.pages = QStackedWidget()
        cv.addWidget(self.pages)

        self.dashboard = self.make_dashboard()
        self.channels_page = self.make_channels()
        self.trending = self.make_simple_page("Trending models and repositories")
        self.favorites = self.make_simple_page("Favorite Hugging Face channels")
        self.models = self.make_simple_page("Model Hub")
        self.categories = self.make_categories()

        for p in [self.dashboard,self.channels_page,self.trending,
                  self.favorites,self.models,self.categories]:
            self.pages.addWidget(p)

        main.addWidget(sidebar)
        main.addWidget(content,1)
        self.nav.setCurrentRow(0)

    def make_dashboard(self):
        page = QWidget()
        l = QVBoxLayout(page)
        self.stats = QLabel()
        self.stats.setStyleSheet("font-size:18px;padding:18px;background:#172033;border-radius:10px;")
        l.addWidget(self.stats)
        h = QLabel("Featured Hugging Face Channels")
        h.setFont(QFont("Segoe UI",16,QFont.Weight.Bold))
        l.addWidget(h)
        self.dashboard_table = self.table(["Name","Category","Favorite"])
        self.dashboard_table.doubleClicked.connect(self.open_dashboard_channel)
        self.dashboard_table.setCursor(Qt.PointingHandCursor)
        l.addWidget(self.dashboard_table)
        return page

    def make_channels(self):
        page = QWidget()
        l = QVBoxLayout(page)
        buttons = QHBoxLayout()
        for text, fn in [
            ("＋ Add from Hugging Face", self.add_channel),
            ("Edit", self.edit_channel),
            ("Delete", self.delete_channel),
            ("★ Favorite", self.toggle_favorite),
            ("Open Hub", self.open_channel)
        ]:
            b = QPushButton(text)
            b.clicked.connect(fn)
            buttons.addWidget(b)
        buttons.addStretch()
        l.addLayout(buttons)
        self.channel_table = self.table(["Name","Category","Favorite","Notes"])
        self.channel_table.doubleClicked.connect(self.open_channel)
        l.addWidget(self.channel_table)
        return page

    def make_simple_page(self, heading):
        page = QWidget()
        l = QVBoxLayout(page)
        l.setSpacing(14)

        label = QLabel(heading)
        label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        l.addWidget(label)

        subtitle = QLabel("Click any item to open the corresponding Hugging Face Hub section.")
        subtitle.setStyleSheet("color:#94a3b8;")
        l.addWidget(subtitle)

        destinations = {
            "Trending models and repositories": [
                ("🔥 Trending Models", "Discover currently popular models on the Hub."),
                ("🚀 Trending Spaces", "Explore popular interactive AI demos and apps."),
                ("📚 Trending Datasets", "Explore datasets gaining attention."),
                ("🆕 Recently Updated Models", "Browse recently updated models."),
            ],
            "Favorite Hugging Face channels": [
                ("⭐ My Favorite Channels", "Open your local favorites in the Channels section."),
                ("🤗 Hugging Face Hub", "Open the main Hugging Face Hub."),
            ],
            "Model Hub": [
                ("🧠 All Models", "Browse the complete model catalog."),
                ("💬 Text Generation", "Find language and text-generation models."),
                ("👁️ Computer Vision", "Find image and vision models."),
                ("🎨 Text-to-Image", "Find image-generation models."),
                ("🎙️ Speech Recognition", "Find automatic speech-recognition models."),
                ("🔊 Text-to-Speech", "Find speech synthesis models."),
                ("🔤 Embeddings", "Find embedding and feature-extraction models."),
                ("📦 GGUF / Quantized", "Search for quantized and local-LLM models."),
            ],
        }

        urls = {
            "🔥 Trending Models": "https://huggingface.co/models?sort=trending",
            "🚀 Trending Spaces": "https://huggingface.co/spaces?sort=trending",
            "📚 Trending Datasets": "https://huggingface.co/datasets?sort=trending",
            "🆕 Recently Updated Models": "https://huggingface.co/models?sort=modified",
            "⭐ My Favorite Channels": None,
            "🤗 Hugging Face Hub": "https://huggingface.co/",
            "🧠 All Models": "https://huggingface.co/models",
            "💬 Text Generation": "https://huggingface.co/models?pipeline_tag=text-generation",
            "👁️ Computer Vision": "https://huggingface.co/models?pipeline_tag=image-classification",
            "🎨 Text-to-Image": "https://huggingface.co/models?pipeline_tag=text-to-image",
            "🎙️ Speech Recognition": "https://huggingface.co/models?pipeline_tag=automatic-speech-recognition",
            "🔊 Text-to-Speech": "https://huggingface.co/models?pipeline_tag=text-to-speech",
            "🔤 Embeddings": "https://huggingface.co/models?pipeline_tag=feature-extraction",
            "📦 GGUF / Quantized": "https://huggingface.co/models?search=GGUF",
        }

        grid = QVBoxLayout()
        for text, description in destinations.get(heading, []):
            button = QPushButton()
            button.setMinimumHeight(68)
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px 18px;
                    background: #172033;
                    border: 1px solid #374151;
                    border-radius: 9px;
                    font-size: 15px;
                }
                QPushButton:hover {
                    background: #26344d;
                    border: 1px solid #f97316;
                }
                QPushButton:pressed { background: #334155; }
            """)
            button.setText(f"{text}\n    {description}")
            url = urls[text]
            if text == "⭐ My Favorite Channels":
                button.clicked.connect(lambda: self.nav.setCurrentRow(1))
            else:
                button.clicked.connect(lambda checked=False, u=url: QDesktopServices.openUrl(QUrl(u)))
            grid.addWidget(button)

        l.addLayout(grid)
        l.addStretch()
        return page

    def make_categories(self):
        page = QWidget()
        l = QVBoxLayout(page)
        h = QLabel("Hugging Face categories")
        h.setFont(QFont("Segoe UI",16,QFont.Weight.Bold))
        l.addWidget(h)
        self.category_list = QListWidget()
        self.category_list.itemDoubleClicked.connect(self.open_category)
        self.category_list.setCursor(Qt.PointingHandCursor)
        l.addWidget(self.category_list)
        return page

    def table(self, headers):
        t = QTableWidget()
        t.setColumnCount(len(headers))
        t.setHorizontalHeaderLabels(headers)
        t.setSelectionBehavior(QAbstractItemView.SelectRows)
        t.setSelectionMode(QAbstractItemView.SingleSelection)
        t.setEditTriggers(QAbstractItemView.NoEditTriggers)
        t.setAlternatingRowColors(True)
        t.verticalHeader().setVisible(False)
        t.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        return t

    def change_page(self, row):
        titles = ["Dashboard","Channels","Trending","Favorites","Models","Categories"]
        self.pages.setCurrentIndex(row)
        self.page_title.setText(titles[row])
        self.search.clear()
        self.refresh_current_page()

    def refresh_current_page(self):
        idx = self.pages.currentIndex()
        if idx == 0: self.refresh_dashboard()
        elif idx == 1: self.refresh_channels()
        elif idx == 2: self.refresh_filtered(self.trending, favorite_only=False)
        elif idx == 3: self.refresh_filtered(self.favorites, favorite_only=True)
        elif idx == 4: self.refresh_models()
        elif idx == 5: self.refresh_categories()

    def refresh_all(self):
        self.refresh_dashboard()
        self.refresh_channels()
        self.refresh_filtered(self.trending, False)
        self.refresh_filtered(self.favorites, True)
        self.refresh_models()
        self.refresh_categories()

    def refresh_dashboard(self):
        total = self.db.conn.execute("SELECT COUNT(*) FROM channels").fetchone()[0]
        fav = self.db.conn.execute("SELECT COUNT(*) FROM channels WHERE favorite=1").fetchone()[0]
        cats = self.db.conn.execute("SELECT COUNT(DISTINCT category) FROM channels").fetchone()[0]
        self.stats.setText(f"🤗  {total} Channels     •     ⭐  {fav} Favorites     •     🏷️  {cats} Categories")
        rows = self.db.conn.execute(
            "SELECT id,name,category,favorite FROM channels ORDER BY favorite DESC,name LIMIT 12"
        ).fetchall()
        self.fill(self.dashboard_table, rows, ["name","category","favorite"])

    def refresh_channels(self):
        q = self.search.text().lower()
        rows = self.db.conn.execute("SELECT * FROM channels ORDER BY name").fetchall()
        rows = [r for r in rows if not q or q in r["name"].lower() or q in r["category"].lower()]
        self.fill(self.channel_table, rows, ["name","category","favorite","notes"])

    def refresh_filtered(self, page, favorite_only):
        # Trending, Favorites and Models now use dedicated clickable Hub
        # action buttons rather than a table. Only refresh a table if the
        # page actually provides one.
        table = page.property("table")
        if table is None:
            return

        q = self.search.text().lower()
        sql = "SELECT * FROM channels"
        if favorite_only:
            sql += " WHERE favorite=1"
        rows = self.db.conn.execute(sql + " ORDER BY name").fetchall()
        rows = [
            r for r in rows
            if not q or q in r["name"].lower() or q in r["category"].lower()
        ]
        self.fill(table, rows, ["name","category","favorite"])

    def refresh_models(self):
        self.refresh_filtered(self.models, False)

    def refresh_categories(self):
        rows = self.db.conn.execute(
            "SELECT category,COUNT(*) n FROM channels GROUP BY category ORDER BY category"
        ).fetchall()
        self.category_list.clear()
        for r in rows:
            item = QListWidgetItem(f"🏷️  {r['category']} — {r['n']} channels   →  double-click to explore")
            item.setData(Qt.UserRole, r["category"])
            self.category_list.addItem(item)

    def fill(self, table, rows, keys):
        table.setRowCount(len(rows))
        for i,row in enumerate(rows):
            for j,key in enumerate(keys):
                value = row[key]
                if key == "favorite":
                    value = "★" if value else ""
                item = QTableWidgetItem(str(value or ""))
                if "id" in row.keys():
                    item.setData(Qt.UserRole,row["id"])
                table.setItem(i,j,item)
        table.resizeRowsToContents()

    def open_category(self, item):
        category = item.data(Qt.UserRole)
        # Use Hugging Face's model search and preserve the category as a query.
        url = "https://huggingface.co/models?search=" + QUrl.toPercentEncoding(category).data().decode()
        QDesktopServices.openUrl(QUrl(url))

    def open_dashboard_channel(self, index):
        item = self.dashboard_table.item(index.row(), 0)
        if not item:
            return
        cid = item.data(Qt.UserRole)
        if cid is None:
            return
        row = self.db.conn.execute("SELECT url FROM channels WHERE id=?", (cid,)).fetchone()
        if row:
            QDesktopServices.openUrl(QUrl(row["url"]))

    def selected_id(self):
        row = self.channel_table.currentRow()
        if row < 0: return None
        return self.channel_table.item(row,0).data(Qt.UserRole)

    def add_channel(self):
        dlg = ChannelDialog(self)
        if dlg.exec() == QDialog.Accepted:
            name,url,cat,notes = dlg.values()
            if not name or not url:
                QMessageBox.warning(self,"Missing information","Name and Hugging Face URL are required.")
                return
            if not url.startswith("https://huggingface.co/"):
                QMessageBox.warning(self,"Invalid URL","Please enter a Hugging Face Hub profile or organization URL.")
                return
            try:
                self.db.conn.execute(
                    "INSERT INTO channels(name,url,category,notes,created_at) VALUES(?,?,?,?,?)",
                    (name,url,cat,notes,datetime.now().isoformat(timespec="seconds"))
                )
                self.db.conn.commit()
            except sqlite3.IntegrityError:
                QMessageBox.information(self,"Already added","This Hugging Face channel is already in your library.")
            self.refresh_all()

    def edit_channel(self):
        cid = self.selected_id()
        if cid is None: return
        row = self.db.conn.execute("SELECT * FROM channels WHERE id=?",(cid,)).fetchone()
        dlg = ChannelDialog(self,row)
        if dlg.exec() == QDialog.Accepted:
            name,url,cat,notes = dlg.values()
            self.db.conn.execute(
                "UPDATE channels SET name=?,url=?,category=?,notes=? WHERE id=?",
                (name,url,cat,notes,cid)
            )
            self.db.conn.commit()
            self.refresh_all()

    def delete_channel(self):
        cid = self.selected_id()
        if cid is None: return
        if QMessageBox.question(self,"Delete channel","Delete the selected channel?") == QMessageBox.Yes:
            self.db.conn.execute("DELETE FROM channels WHERE id=?",(cid,))
            self.db.conn.commit()
            self.refresh_all()

    def toggle_favorite(self):
        cid = self.selected_id()
        if cid is None: return
        self.db.conn.execute("UPDATE channels SET favorite=1-favorite WHERE id=?",(cid,))
        self.db.conn.commit()
        self.refresh_all()

    def open_channel(self):
        cid = self.selected_id()
        if cid is None: return
        row = self.db.conn.execute("SELECT url FROM channels WHERE id=?",(cid,)).fetchone()
        webbrowser.open(row["url"])


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
