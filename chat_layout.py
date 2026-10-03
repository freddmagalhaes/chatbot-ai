import streamlit as st


def apply_stile_chat():
    st.markdown(
        """
        <style>
            :root {
                --bg-dark: #0b1020;
                --bg-panel: #121a2b;
                --bg-panel-strong: #1b2438;
                --user-bubble: #1d4ed8;
                --assistant-bubble: #1f2937;
                --border: rgba(148, 163, 184, 0.2);
                --text: #e5eefb;
                --muted: #9fb3d1;
                --accent: #7dd3fc;
                --success: #22c55e;
            }

            .stApp {
                background: radial-gradient(circle at top, #13233d 0%, var(--bg-dark) 42%, #090d16 100%);
                color: var(--text);
            }

            .block-container {
                padding-top: 1.2rem;
                padding-bottom: 1.2rem;
                max-width: 1200px;
            }

            h1 {
                color: #f8fafc;
                font-weight: 800;
                letter-spacing: -0.04em;
            }

            [data-testid="stSidebar"] {
                background: rgba(11, 16, 32, 0.96);
                border-right: 1px solid var(--border);
            }

            .stSidebar .block-container {
                padding-top: 1rem;
            }

            [data-testid="stChatMessage"] {
                border: 1px solid var(--border);
                border-radius: 18px;
                padding: 0.9rem 1rem;
                margin: 0.55rem 0;
                box-shadow: 0 4px 16px rgba(2, 6, 23, 0.28);
            }

            [data-testid="stChatMessage"] p {
                margin: 0;
                line-height: 1.6;
                color: var(--text);
            }

            [data-testid="stChatMessage"]:has(> div > p) {
                background: transparent;
            }

            div[data-testid="stChatMessage"] {
                background: rgba(15, 23, 42, 0.65);
            }

            div[data-testid="stChatMessage"][data-icon="user"] {
                background: linear-gradient(135deg, rgba(29, 78, 216, 0.92), rgba(30, 64, 175, 0.82));
                border: 1px solid rgba(96, 165, 250, 0.45);
            }

            div[data-testid="stChatMessage"][data-icon="assistant"] {
                background: linear-gradient(135deg, rgba(31, 41, 55, 0.94), rgba(17, 24, 39, 0.9));
                border: 1px solid rgba(148, 163, 184, 0.18);
            }

            .stInfo {
                background: rgba(59, 130, 246, 0.12);
                border: 1px solid rgba(96, 165, 250, 0.5);
                color: #dbeafe;
                border-radius: 12px;
            }

            .stError {
                border-radius: 12px;
                border: 1px solid rgba(248, 113, 113, 0.35);
            }

            .stChatInput {
                border-radius: 16px;
                border: 1px solid rgba(148, 163, 184, 0.2);
                background: rgba(15, 23, 42, 0.9);
                box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.4);
            }

            .stChatInput textarea {
                color: var(--text) !important;
                background: transparent !important;
            }

            .stButton > button {
                border-radius: 12px;
                background: linear-gradient(135deg, #2563eb, #3b82f6);
                color: white;
                border: none;
                font-weight: 600;
                padding: 0.6rem 1rem;
            }

            .stButton > button:hover {
                background: linear-gradient(135deg, #1d4ed8, #2563eb);
            }

            .stMarkdown {
                color: var(--text);
            }

            .stMarkdown code {
                background: rgba(15, 23, 42, 0.8);
                color: #bfdbfe;
                padding: 0.15rem 0.35rem;
                border-radius: 6px;
            }

            .stMarkdown pre {
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(148, 163, 184, 0.14);
                border-radius: 12px;
                padding: 0.8rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
