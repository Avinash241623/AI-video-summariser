import streamlit as st
from transcript import get_youtube_transcript
from summarizer import summarize_text

st.set_page_config(
    page_title="AI Video Intelligence Dashboard",
    page_icon="🧠",
    layout="wide"
)

# ---- Custom Styling ----
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 700;
}
.metric-box {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
.summary-box {
    background-color: #111111;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #333333;
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown('<p class="main-title">🧠 AI Video Intelligence Dashboard</p>', unsafe_allow_html=True)
st.caption("Analyze YouTube videos using AI-powered summarization")

st.divider()

# ---- Input Section ----
url = st.text_input("🔗 Enter YouTube URL")

if st.button("🚀 Analyze Video"):

    if url:

        with st.spinner("📥 Extracting transcript..."):
            transcript = get_youtube_transcript(url)

        with st.spinner("🧠 Generating AI summary..."):
            summary = summarize_text(transcript)

        st.divider()

        # ---- Metrics Row ----
        col1, col2, col3 = st.columns(3)

        col1.metric("Transcript Length", f"{len(transcript)} chars")
        col2.metric("Summary Length", f"{len(summary)} chars")
        col3.metric("Compression Ratio",
                    f"{round((len(summary)/len(transcript))*100, 2)} %")

        st.divider()

        # ---- Summary Section ----
        st.subheader("📌 AI Generated Summary")
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

        # ---- Download Button ----
        st.download_button(
            label="⬇ Download Summary",
            data=summary,
            file_name="video_summary.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter a valid YouTube URL.")