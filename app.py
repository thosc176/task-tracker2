import streamlit as st
import pandas as pd

st.set_page_config(page_title="Theo dõi công việc", layout="wide")

st.title("📋 Theo dõi công việc cá nhân & nhóm nhỏ")

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

with st.form("task_form"):
    st.subheader("➕ Thêm công việc mới")
    title = st.text_input("Tên công việc")
    deadline = st.date_input("Hạn hoàn thành")
    status = st.selectbox("Trạng thái", ["Chưa làm", "Đang làm", "Hoàn thành"])
    note = st.text_area("Ghi chú")
    submitted = st.form_submit_button("Thêm công việc")

    if submitted and title:
        st.session_state["tasks"].append({
            "Tên": title,
            "Hạn": deadline.strftime("%d/%m/%Y"),
            "Trạng thái": status,
            "Ghi chú": note
        })
        st.success("✅ Đã thêm công việc!")

st.subheader("📌 Danh sách công việc")
df = pd.DataFrame(st.session_state["tasks"])
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("Chưa có công việc nào.")
